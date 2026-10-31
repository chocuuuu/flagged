#!/usr/bin/env python3
"""Check repository planning documents for known cross-document drift."""

from __future__ import annotations

import csv
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "progress" / "DAILY-PLAN.md"
CALENDAR = ROOT / "docs" / "SPRINT-CALENDAR.md"
BACKLOG = ROOT / "jira" / "JIRA-BACKLOG.md"
CSV_PATH = ROOT / "jira" / "FLAGGED-JIRA-IMPORT.csv"
README = ROOT / "README.md"
GENERATOR = ROOT / "scripts" / "generate_jira_csv.py"
EM_DASH = "\u2014"
EN_DASH = "\u2013"


class CheckFailure(Exception):
    """Raised when a required consistency check fails."""


def fail(message: str) -> None:
    raise CheckFailure(message)


def check_adr_references() -> int:
    adr_files = list((ROOT / "docs" / "adrs").glob("ADR-*.md"))
    adr_by_number = {
        int(match.group(1)): path
        for path in adr_files
        if (match := re.match(r"ADR-(\d+)", path.name))
    }
    existing = set(adr_by_number)
    markdown_files = list(ROOT.rglob("*.md"))
    references: set[int] = set()
    for path in markdown_files:
        if ".git" in path.parts:
            continue
        references.update(int(number) for number in re.findall(r"\bADR-(\d{3})\b", path.read_text(encoding="utf-8", errors="replace")))
    missing = sorted(references - existing)
    if missing:
        fail(f"Dangling ADR references: {', '.join(f'ADR-{number:03d}' for number in missing)}")
    for path in adr_files:
        adr_text = path.read_text(encoding="utf-8")
        if not re.search(r"^\*\*Status:\*\*", adr_text, re.MULTILINE):
            fail(f"{path.relative_to(ROOT)} has no Status line.")

    tracker_text = (ROOT / "progress" / "PROGRESS.md").read_text(encoding="utf-8")
    tracker = {
        int(number): (title.strip(), status.strip())
        for number, title, status in re.findall(
            r"^- \[ \] ADR-(\d{3}): (.+?) - (Proposed|Accepted)$",
            tracker_text,
            re.MULTILINE,
        )
    }
    if set(tracker) != existing:
        fail("PROGRESS.md ADR tracker does not list exactly the existing ADR files.")
    for number, path in adr_by_number.items():
        adr_text = path.read_text(encoding="utf-8")
        title_match = re.search(r"^# ADR-\d{3}: (.+)$", adr_text, re.MULTILINE)
        status_match = re.search(r"^\*\*Status:\*\* (.+)$", adr_text, re.MULTILINE)
        if not title_match or not status_match:
            fail(f"{path.relative_to(ROOT)} needs a parseable title and status.")
        expected_status = status_match.group(1).strip().split()[0]
        if tracker[number] != (title_match.group(1).strip(), expected_status):
            fail(f"PROGRESS.md ADR-{number:03d} title/status differs from its ADR file.")
    return len(references)


def check_sprint_map() -> tuple[int, int]:
    calendar_text = CALENDAR.read_text(encoding="utf-8")
    rows = re.findall(
        rf"^\|\s*(\d+)\s*\|\s*(\d+)[{EN_DASH}-](\d+)\s*\|",
        calendar_text,
        re.MULTILINE,
    )
    if len(rows) != 12:
        fail(f"Sprint calendar must contain 12 sprint ranges; found {len(rows)}.")
    expected_start = 1
    for index, (sprint, start, end) in enumerate(rows, start=1):
        sprint_num, first, last = int(sprint), int(start), int(end)
        if sprint_num != index or first != expected_start or last - first != 4:
            fail(
                f"Invalid sprint range at row {index}: sprint {sprint_num}, "
                f"sessions {first}-{last}."
            )
        expected_start = last + 1
    if expected_start != 61:
        fail(f"Sprint ranges must cover sessions 1-60; ended at {expected_start - 1}.")

    plan_text = PLAN.read_text(encoding="utf-8")
    session_blocks = list(
        re.finditer(r"^### Session (\d{2}) - (.+)$", plan_text, re.MULTILINE)
    )
    session_numbers = [int(match.group(1)) for match in session_blocks]
    if session_numbers != list(range(1, 61)):
        fail("Daily plan must contain each session 01 through 60 exactly once.")
    for index, match in enumerate(session_blocks):
        end = session_blocks[index + 1].start() if index + 1 < len(session_blocks) else len(plan_text)
        block = plan_text[match.start() : end]
        for label in ("**Goal:**", "**Test:**", "**Commit:**"):
            if label not in block:
                fail(f"Session {int(match.group(1)):02d} has no {label.strip('*')}.")
    if len(re.findall(r"^## Sprint \d+ - ", plan_text, re.MULTILINE)) != 12:
        fail("Daily plan must contain 12 sprint sections.")
    return 12, len(session_numbers)


def check_jira() -> tuple[int, int, int]:
    result = subprocess.run(
        [sys.executable, str(GENERATOR), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode:
        fail(result.stderr.strip() or "Jira Markdown and CSV differ.")

    with CSV_PATH.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    expected_fields = [
        "Work item ID",
        "Work type",
        "Summary",
        "Description",
        "Parent",
        "Priority",
        "Story Points",
    ]
    if not rows or list(rows[0]) != expected_fields:
        fail(f"Jira CSV columns must match the existing import format: {expected_fields}.")
    kinds = {kind: sum(row["Work type"] == kind for row in rows) for kind in ("Epic", "Story", "Sub-task")}
    if kinds != {"Epic": 12, "Story": 48, "Sub-task": 149}:
        fail(f"Jira requires 12 epics, 48 stories, and 149 subtasks; found {kinds}.")
    work_item_ids = [row["Work item ID"] for row in rows]
    if any(not re.fullmatch(r"\d+", value) for value in work_item_ids):
        fail("Jira CSV work item IDs must be numeric.")
    if len(work_item_ids) != len(set(work_item_ids)):
        fail("Jira CSV contains duplicate work item IDs.")
    rows_by_id = {row["Work item ID"]: row for row in rows}
    for row in rows:
        item_id = row["Work item ID"]
        if not row["Priority"]:
            fail(f"Jira row {item_id} lacks Priority.")
        if row["Work type"] == "Epic":
            if row["Parent"]:
                fail(f"Jira epic {item_id} must not have a parent.")
        elif row["Work type"] in ("Story", "Sub-task"):
            parent = rows_by_id.get(row["Parent"])
            expected_parent_type = "Epic" if row["Work type"] == "Story" else "Story"
            if not parent or parent["Work type"] != expected_parent_type:
                fail(f"Jira row {item_id} has an invalid {expected_parent_type} parent.")
        else:
            fail(f"Jira row {item_id} has unsupported work type {row['Work type']}.")
        if row["Work type"] == "Story":
            if row["Story Points"] != "3":
                fail(f"Jira story {item_id} does not have the canonical 3 points.")
            description = row["Description"].replace("\r\n", "\n").replace("\r", "\n")
            if not re.search(r"^Sprint: Sprint \d+$", description, re.MULTILINE):
                fail(f"Jira story {item_id} has no sprint in its description.")
        if row["Work type"] == "Sub-task" and row["Story Points"] != "1":
            fail(f"Jira subtask {item_id} does not have the canonical 1 point.")
    return kinds["Epic"], kinds["Story"], kinds["Sub-task"]


def check_cloud_cost_gate() -> tuple[int, int]:
    text = BACKLOG.read_text(encoding="utf-8")
    gate = re.search(r"^- \[ \] \*\*FLAG-169\*\* .+$", text, re.MULTILINE)
    if not gate:
        fail("Jira backlog is missing the FLAG-169 budget/alert gate.")
    if "budget/alert" not in gate.group(0).lower() or "spend caps" not in gate.group(0).lower():
        fail("FLAG-169 must configure a budget/alert and state that alerts are not spend caps.")
    provisioning = re.compile(
        r"\b(?:terraform apply|provision (?:a )?(?:live )?(?:cloud|gcp)|"
        r"deploy (?:to )?cloud run|cloud run deployment|enable (?:cloud )?apis|"
        r"create (?:a )?(?:live )?(?:gcp|cloud|firestore|pub/sub|"
        r"artifact registry|gcs)(?:\s|$))",
        re.IGNORECASE,
    )
    provisioning_matches = []
    for match in re.finditer(r"^- \[ \] \*\*(FLAG-\d+)\*\* .+$", text, re.MULTILINE):
        if match.group(1) == "FLAG-169":
            continue
        line = match.group(0)
        if provisioning.search(line):
            provisioning_matches.append(match)
            if match.start() < gate.start():
                fail(f"{match.group(1)} appears before the FLAG-169 cost gate.")

    cloud_run_tasks = [
        line
        for line in text.splitlines()
        if "Cloud Run" in line and "Terraform" in line
    ]
    for line in cloud_run_tasks:
        if not re.search(
            r"(?:minimum instances\s*(?:=|to)\s*0|scale-to-zero)",
            line,
            re.IGNORECASE,
        ):
            fail("A Jira Cloud Run Terraform task does not require minimum instances = 0.")
    return len(provisioning_matches), len(cloud_run_tasks)


def check_readme_paths() -> int:
    text = README.read_text(encoding="utf-8")
    start_section = re.search(
        r"^## Start here\s*\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    files_section = re.search(r"^## Files\s*\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    layout_section = re.search(
        r"^## Suggested repo layout\s*\n```text\s*\n(.*?)\n```",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not start_section or not files_section or not layout_section:
        fail("README must contain Start here, Files, and Suggested repo layout sections.")

    paths = {
        item.rstrip("/")
        for item in re.findall(r"^- `([^`]+)`", files_section.group(1), re.MULTILINE)
    }
    for link, inline_path in re.findall(
        r"\[[^\]]+\]\(([^)]+\.md)\)|`([^`]+\.md)`",
        start_section.group(1),
    ):
        paths.add((link or inline_path).rstrip("/"))
    stack: list[str] = []
    for line in layout_section.group(1).splitlines():
        match = re.match(r"^([│ ]*)(?:├──|└──)\s+([^ ]+)", line)
        if not match:
            continue
        depth = len(match.group(1)) // 4
        name = match.group(2)
        stack = stack[:depth]
        stack.append(name)
        paths.add("/".join(part.rstrip("/") for part in stack))

    missing = sorted(path for path in paths if not (ROOT / Path(path)).exists())
    if missing:
        fail(f"README lists missing paths: {', '.join(missing)}")
    return len(paths)


def tracked_and_local_files() -> list[Path]:
    paths: set[Path] = set()
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        capture_output=True,
        check=True,
    )
    for raw in result.stdout.split(b"\0"):
        if raw:
            path = ROOT / Path(raw.decode("utf-8"))
            if path.is_file():
                paths.add(path)
    ignored = {".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"}
    for path in ROOT.rglob("*"):
        if path.is_file() and not any(part in ignored for part in path.parts):
            paths.add(path)
    return sorted(paths)


def check_secrets() -> str:
    patterns = [
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        re.compile(r"\b(?:ghp|gho|ghu|ghs|github_pat)_[A-Za-z0-9_]{20,}\b"),
        re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
        re.compile(r"(?i)\b(?:api[_-]?key|client[_-]?secret|password|token)\s*[:=]\s*(['\"])([^'\"\s]{12,})\1"),
    ]
    placeholders = ("<", "${", "...", "change-me", "replace-me", "your-", "example")
    findings: list[str] = []
    files = tracked_and_local_files()
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in patterns:
            for match in pattern.finditer(text):
                value = match.group(0).lower()
                if any(placeholder in value for placeholder in placeholders):
                    continue
                findings.append(f"{path.relative_to(ROOT)}:{text.count(chr(10), 0, match.start()) + 1}")
    if findings:
        fail("Secret-like patterns found: " + ", ".join(sorted(set(findings))))

    gitleaks = shutil.which("gitleaks")
    if gitleaks:
        result = subprocess.run(
            [gitleaks, "detect", "--no-git", "--source", str(ROOT), "--redact", "--exit-code", "1"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode:
            fail("Gitleaks reported a finding or failed to scan; inspect its redacted output.")
        return "heuristics + Gitleaks"
    return "heuristics (Gitleaks not installed)"


def check_stale_terms() -> int:
    stale_patterns = [
        re.compile(r"\bCONFIG_UPDATED\b"),
        re.compile(r'"type"\s*:\s*"config\.updated"'),
        re.compile(r"config\.updated\s*\(\s*revision\s*="),
        re.compile(r"\b60-Day\b", re.IGNORECASE),
        re.compile(r"\b60-Working-Session\b", re.IGNORECASE),
        re.compile(r"\b" + "F" * 2 + r"-\d+(?:-\d+)?\b"),
    ]
    findings = []
    for path in ROOT.rglob("*"):
        if path.suffix.lower() not in {".md", ".csv", ".py"}:
            continue
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in stale_patterns:
            if pattern.search(text):
                findings.append(f"{path.relative_to(ROOT)} ({pattern.pattern})")
    if findings:
        fail("Retired terminology or SSE event name remains: " + "; ".join(findings))
    return len(stale_patterns)


def main() -> int:
    try:
        adr_count = check_adr_references()
        sprint_count, session_count = check_sprint_map()
        epic_count, story_count, subtask_count = check_jira()
        provisioning_tasks, cloud_run_tasks = check_cloud_cost_gate()
        readme_paths = check_readme_paths()
        secret_result = check_secrets()
        stale_count = check_stale_terms()
    except (CheckFailure, OSError, subprocess.SubprocessError) as error:
        print(f"CONSISTENCY CHECK FAILED: {error}", file=sys.stderr)
        return 1

    print("CONSISTENCY CHECK PASSED")
    print(f"- ADR references resolve; every ADR has a Status line ({adr_count} referenced IDs).")
    print(f"- Sprint/session map: {sprint_count} sprints, {session_count} sessions, contiguous 1-60.")
    print(f"- Jira CSV matches Markdown: {epic_count} epics, {story_count} stories, {subtask_count} subtasks.")
    print(f"- Budget/alert gate and scale-to-zero checks: {provisioning_tasks} planned provisioning tasks found; {cloud_run_tasks} Cloud Run/Terraform tasks checked.")
    print(f"- README Files/layout paths exist ({readme_paths} paths).")
    print(f"- Secret scan: {secret_result}.")
    print(f"- Retired term/event-name patterns clear ({stale_count} patterns).")
    print("GitHub Actions is not required to run this local check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
