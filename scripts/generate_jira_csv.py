#!/usr/bin/env python3
"""Generate the Jira import CSV from the canonical Markdown backlog."""

from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKLOG = ROOT / "jira" / "JIRA-BACKLOG.md"
OUTPUT = ROOT / "jira" / "FLAGGED-JIRA-IMPORT.csv"
ID_MAP = ROOT / "jira" / "IMPORT-ID-MAP.csv"
SKILLS = ROOT / "SKILLS.md"
CALENDAR = ROOT / "docs" / "SPRINT-CALENDAR.md"
EM_DASH = "\u2014"
EN_DASH = "\u2013"
FIELDS = [
    "Work item ID",
    "Work type",
    "Summary",
    "Description",
    "Parent",
    "Priority",
    "Story Points",
]
ISSUE_RE = re.compile(r"^## (FLAG-\d+) " + EM_DASH + r" (.+)$", re.MULTILINE)
SUBTASK_RE = re.compile(
    r"^- \[ \] \*\*(FLAG-\d+)\*\* " + EM_DASH + r" (.+)$", re.MULTILINE
)
ID_MAP_FIELDS = ["Source Key", "Work item ID"]


def field(block: str, name: str) -> str:
    match = re.search(r"^\*\*" + re.escape(name) + r":\*\* (.+?)\s*$", block, re.MULTILINE)
    if not match:
        raise ValueError(f"Missing `{name}` field in Jira story.")
    return match.group(1).replace("<br>", "").strip()


def load_id_map(source_keys: set[str]) -> dict[str, str]:
    with ID_MAP.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ID_MAP_FIELDS:
            raise ValueError(f"{ID_MAP.relative_to(ROOT)} must have columns {ID_MAP_FIELDS}.")
        identifiers: dict[str, str] = {}
        used_ids: set[str] = set()
        for row in reader:
            source_key = row["Source Key"].strip()
            work_item_id = row["Work item ID"].strip()
            if not re.fullmatch(r"FLAG-\d+", source_key) or not re.fullmatch(
                r"\d+", work_item_id
            ):
                raise ValueError(f"Invalid source key or numeric work item ID: {row}.")
            if source_key in identifiers:
                raise ValueError(f"Duplicate source key in ID map: {source_key}")
            if work_item_id in used_ids:
                raise ValueError(f"Duplicate work item ID in ID map: {work_item_id}")
            identifiers[source_key] = work_item_id
            used_ids.add(work_item_id)

    missing = sorted(source_keys - identifiers.keys())
    unexpected = sorted(identifiers.keys() - source_keys)
    if missing or unexpected:
        details = []
        if missing:
            details.append(f"missing mappings: {', '.join(missing)}")
        if unexpected:
            details.append(f"unused mappings: {', '.join(unexpected)}")
        raise ValueError(f"{ID_MAP.relative_to(ROOT)} does not match the backlog ({'; '.join(details)}).")
    return identifiers


def generate() -> str:
    text = BACKLOG.read_text(encoding="utf-8")
    sprint_matches = list(
        re.finditer(r"^# Sprint (\d+) " + EM_DASH + r" (.+)$", text, re.MULTILINE)
    )
    if len(sprint_matches) != 12:
        raise ValueError(f"Expected 12 sprint headings, found {len(sprint_matches)}.")
    backlog_focus = {
        int(match.group(1)): match.group(2).strip() for match in sprint_matches
    }

    skills_text = SKILLS.read_text(encoding="utf-8")
    skills_section = re.search(
        r"^## Sprint focus\s*\n(.*?)(?=^## Stage 1|\Z)",
        skills_text,
        re.MULTILINE | re.DOTALL,
    )
    if not skills_section:
        raise ValueError("SKILLS.md has no Sprint focus table.")
    skills_focus = {
        int(number): title.strip()
        for number, title in re.findall(
            r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|$",
            skills_section.group(1),
            re.MULTILINE,
        )
    }
    if skills_focus != backlog_focus:
        raise ValueError("Jira sprint names do not match SKILLS.md sprint objectives.")

    calendar_text = CALENDAR.read_text(encoding="utf-8")
    calendar_focus = {
        int(number): title.strip()
        for number, title in re.findall(
            rf"^\|\s*(\d+)\s*\|\s*\d+[{EN_DASH}-]\d+\s*\|\s*(.+?)\s*\|",
            calendar_text,
            re.MULTILINE,
        )
    }
    if calendar_focus != backlog_focus:
        raise ValueError("Jira sprint names do not match docs/SPRINT-CALENDAR.md.")

    epic_matches = list(
        re.finditer(r"^- (FLAG-\d+) " + EM_DASH + r" (.+)$", text, re.MULTILINE)
    )
    if len(epic_matches) != 12:
        raise ValueError(f"Expected 12 epic definitions, found {len(epic_matches)}.")
    epics = {match.group(1): match.group(2).strip() for match in epic_matches}

    rows: list[dict[str, str]] = []
    sprint_names = {
        int(match.group(1)): match.group(2).strip() for match in sprint_matches
    }
    for sprint_number, sprint_name in sprint_names.items():
        epic_key = f"FLAG-{sprint_number}"
        if epic_key not in epics:
            raise ValueError(f"Missing {epic_key} definition.")
        rows.append(
            {
                "Source Key": epic_key,
                "Work type": "Epic",
                "Summary": epics[epic_key],
                "Description": (
                    f"Flagged epic {epics[epic_key]}.\n\n"
                    f"Learning Objective:\n{epics[epic_key]}"
                ),
                "Parent": "",
                "Priority": "High",
                "Story Points": "",
            }
        )

    issues = list(ISSUE_RE.finditer(text))
    if len(issues) != 48:
        raise ValueError(f"Expected 48 Jira stories, found {len(issues)}.")
    story_keys: set[str] = set()
    subtask_keys: set[str] = set()
    story_counts = {number: 0 for number in sprint_names}

    for index, match in enumerate(issues):
        key, summary = match.group(1), match.group(2).strip()
        start = match.start()
        end = issues[index + 1].start() if index + 1 < len(issues) else len(text)
        next_sprint = re.search(r"^# Sprint \d+ " + EM_DASH, text[start:end], re.MULTILINE)
        if next_sprint:
            end = start + next_sprint.start()
        block = text[start:end]

        sprint_value = field(block, "Sprint")
        sprint_match = re.fullmatch(r"Sprint (\d+)", sprint_value)
        if not sprint_match:
            raise ValueError(f"Invalid Sprint field in {key}: {sprint_value}")
        sprint_number = int(sprint_match.group(1))
        epic = field(block, "Epic")
        objective = field(block, "Learning Objective")
        priority = field(block, "Priority")
        points = field(block, "Story Points")
        test_evidence = field(block, "Test Evidence")
        if sprint_number not in sprint_names or epic != f"FLAG-{sprint_number}":
            raise ValueError(f"Sprint/Epic mismatch in {key}.")
        if objective != skills_focus[sprint_number]:
            raise ValueError(f"Learning Objective mismatch in {key}.")
        if priority != "High" or points != "3":
            raise ValueError(f"Expected High priority and 3 points in {key}.")
        if key in story_keys:
            raise ValueError(f"Duplicate story key: {key}")
        story_keys.add(key)
        story_counts[sprint_number] += 1

        subtasks = SUBTASK_RE.findall(block)
        if not subtasks:
            raise ValueError(f"{key} must list its planned subtasks.")
        if not re.search(rf"`{re.escape(key)}-T1`.*`{re.escape(key)}-T2`", test_evidence):
            raise ValueError(f"{key} must name success and failure test IDs.")
        for subtask_key, subtask_summary in subtasks:
            if subtask_key in subtask_keys or subtask_key in story_keys or subtask_key in epics:
                raise ValueError(f"Duplicate subtask key: {subtask_key}")
            subtask_keys.add(subtask_key)

        rows.append(
            {
                "Source Key": key,
                "Work type": "Story",
                "Summary": summary,
                "Description": (
                    f"Sprint: {sprint_value}\n"
                    f"Learning Objective: {objective}\n"
                    f"Test Evidence: {test_evidence}\n"
                    "Definition of Done: local behavior; success and failure tests; "
                    "documented design; no accidental secrets or paid infrastructure; "
                    "focused commit/PR."
                ),
                "Parent": epic,
                "Priority": priority,
                "Story Points": points,
            }
        )
        for subtask_key, subtask_summary in subtasks:
            rows.append(
                {
                    "Source Key": subtask_key,
                    "Work type": "Sub-task",
                    "Summary": subtask_summary.strip(),
                    "Description": f"Parent story: {key}. See the parent story's test evidence and acceptance criteria.",
                    "Parent": key,
                    "Priority": priority,
                    "Story Points": "1",
                }
            )

    wrong_counts = {number: count for number, count in story_counts.items() if count != 4}
    if wrong_counts:
        raise ValueError(f"Each sprint must have four stories: {wrong_counts}")
    identifiers = load_id_map({row["Source Key"] for row in rows})
    for row in rows:
        source_key = row.pop("Source Key")
        parent_key = row["Parent"]
        row["Work item ID"] = identifiers[source_key]
        row["Parent"] = identifiers[parent_key] if parent_key else ""

    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if the generated CSV differs from the checked-in import file.",
    )
    args = parser.parse_args()
    try:
        generated = generate()
    except (OSError, ValueError) as error:
        print(f"Jira generation failed: {error}", file=sys.stderr)
        return 1
    counts: dict[str, int] = {}
    for row in csv.DictReader(io.StringIO(generated)):
        kind = row["Work type"]
        counts[kind] = counts.get(kind, 0) + 1

    if args.check:
        current = OUTPUT.read_text(encoding="utf-8-sig") if OUTPUT.exists() else ""
        if current != generated:
            print(f"{OUTPUT.relative_to(ROOT)} is stale; run this script to regenerate it.", file=sys.stderr)
            return 1
        print(
            "Jira CSV matches the Markdown source "
            f"({counts.get('Epic', 0)} epics, {counts.get('Story', 0)} stories, "
            f"{counts.get('Sub-task', 0)} subtasks)."
        )
        return 0

    with OUTPUT.open("w", encoding="utf-8", newline="") as stream:
        stream.write(generated)
    print(
        f"Generated {OUTPUT.relative_to(ROOT)} "
        f"({counts.get('Epic', 0)} epics, {counts.get('Story', 0)} stories, "
        f"{counts.get('Sub-task', 0)} subtasks)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
