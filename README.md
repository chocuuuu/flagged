# Flagged — Project Plan Package

## Distributed Feature Flag & Configuration Platform

This is a learning project with 60 working sessions over 12 weeks, organized as
12 five-session sprints. These are working-session labels, not calendar dates or a
completion deadline.

The project is designed to be:

- local-first;
- cloud-later;
- system-design heavy;
- test and debugging driven;
- AI-assisted but not AI-dependent;
- GitHub-centered;
- Terraform-managed;
- designed to add no cloud-service charges on its default path.

## Start here

1. Read `PRD.md`.
2. Read `ARCHITECTURE.md`.
3. Read `SYSTEM-DESIGN.md`.
4. Read `SKILLS.md`.
5. Read `AGENTS.md`.
6. Start Sprint 1 when ready; pause and resume between sessions.
7. Track demonstrated outcomes in `progress/PROGRESS.md`.
8. Use `progress/DAILY-PLAN.md` as the canonical 60-session plan.
9. Use `progress/PROGRESS.md` as its derived checklist; Jira stories are the backlog.
10. Run the scoped [architecture freeze gate](docs/ARCHITECTURE-FREEZE-GATE.md) before implementation work that crosses a system boundary.
11. Review the [technical design draft](docs/TECHNICAL-DESIGN.md) for the initial product, architecture, data, and sequence diagrams.

## Project stack

```text
Frontend      Astro + React + TypeScript
Backend       Python + FastAPI
Local DB      PostgreSQL
Cache lab     Redis (optional local experiment)
SDK           TypeScript
Containers    Docker / Docker Compose
IaC           Terraform
CI/CD         GitHub Actions
Cloud learning GCP (local emulators and Terraform review by default)
Cloud DB      Firestore (deferred; no adapter selected)
Events        Pub/Sub (emulator or local adapter by default)
Runtime       Cloud Run (design/validation by default)
Observability local-first; cloud services only by explicit opt-in
```

## Important database decision

PostgreSQL is the selected local source-of-truth baseline. The project does **not**
require two production databases.

- PostgreSQL = selected local relational source-of-truth baseline.
- Firestore = deferred optional GCP learning experiment; no adapter/read model is
  selected for implementation.
- Repository boundary = makes the persistence decision explicit and testable.

Read ADR-005, ADR-006, and ADR-007 together.

## Cost boundary

The default path is **$0 in cloud-service charges**: develop locally, and use emulators or local adapters for cloud concepts where practical. No GCP provisioning or hosted CI is required to complete the learning milestones.

Free tiers are quotas, not a zero-cost guarantee. Live GCP resources and hosted services are optional experiments and must not be created without explicit approval after checking current pricing, billing prerequisites, expected usage, and cleanup steps. See `COST-BOUNDARY.md`.

## Files

- `CLAUDE.md`
- `AGENTS.md`
- `PRD.md`
- `DATA.md`
- `ARCHITECTURE.md`
- `SECURITY.md`
- `SYSTEM-DESIGN.md`
- `SKILLS.md`
- `COST-BOUNDARY.md`
- `DEPENDENCIES.md`
- `docs/SPRINT-CALENDAR.md`
- `progress/PROGRESS.md`
- `progress/DAILY-PLAN.md`
- `jira/JIRA-BACKLOG.md`
- `jira/IMPORT-ID-MAP.csv` (stable mapping from backlog keys to existing Jira IDs)
- `jira/FLAGGED-JIRA-IMPORT.csv` (generated in the existing numeric-ID format)
- `AUDIT-REPORT.md`
- `CHANGELOG-AUDIT.md`
- `docs/DECISIONS-PENDING.md`
- `docs/adrs/`
- `docs/ARCHITECTURE-FREEZE-GATE.md` (repeatable pre-milestone gate and current review)
- `docs/TECHNICAL-DESIGN.md` (planning draft: use cases, architecture, data, and sequence diagrams)
- `docs/API-CONTRACT.md` (draft; proposed v1 HTTP contract)

Generate `jira/FLAGGED-JIRA-IMPORT.csv` from the canonical Markdown backlog and
stable ID map with `python scripts/generate_jira_csv.py`; do not hand-edit the
generated CSV or reassign IDs that already exist in Jira. The legacy
`jira/JIRA-BACKLOG.csv` export is not the active import source; its tracked deletion
was already present when this audit began and was left untouched.

## Suggested repo layout

```text
Flagged/
├── docs/
│   ├── adrs/
│   ├── benchmarks/
│   └── runbooks/
├── jira/
│   ├── JIRA-BACKLOG.md
│   ├── IMPORT-ID-MAP.csv
│   └── FLAGGED-JIRA-IMPORT.csv
├── progress/
├── scripts/
├── PRD.md
├── DATA.md
├── ARCHITECTURE.md
├── SECURITY.md
├── SYSTEM-DESIGN.md
├── SKILLS.md
├── AGENTS.md
└── CLAUDE.md
```
