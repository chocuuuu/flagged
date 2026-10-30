# Flagged — Project Plan Package

## Distributed Feature Flag & Configuration Platform

This is an outcome-based learning project. Its 12 milestones are an ordered guide, not a calendar or deadline.

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
6. Start Milestone 1 when ready; pause and resume between milestones or work blocks.
7. Track demonstrated outcomes in `progress/PROGRESS.md`.
8. Use `progress/DAILY-PLAN.md` as the detailed, non-calendar work guide.
9. Treat the Jira sprint groupings as backlog organization, not deadlines.
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
Cloud DB      Firestore (emulator by default)
Events        Pub/Sub (emulator or local adapter by default)
Runtime       Cloud Run (design/validation by default)
Observability local-first; cloud services only by explicit opt-in
```

## Important database decision

PostgreSQL and Firestore are used for different stages intentionally.

The project does **not** require two production databases.

- PostgreSQL = rich local relational learning environment.
- Firestore = optional GCP learning experiment; use its emulator by default.
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
- `SPRINT-CALENDAR.md`
- `progress/PROGRESS.md`
- `progress/DAILY-PLAN.md`
- `jira/JIRA-BACKLOG.md`
- `docs/adrs/`
- `docs/ARCHITECTURE-FREEZE-GATE.md` (repeatable pre-milestone gate and current review)
- `docs/TECHNICAL-DESIGN.md` (planning draft: use cases, architecture, data, and sequence diagrams)
- `docs/API-CONTRACT.md` (draft; proposed v1 HTTP contract)

`jira/JIRA-BACKLOG.csv` is an older export and is not an authoritative planning source. Use `jira/FLAGGED-JIRA-IMPORT.csv` for the supplied Jira import data.

## Suggested repo layout

```text
Flagged/
├── apps/
│   ├── dashboard/
│   └── demo-store/
├── services/
│   └── flag-api/
├── packages/
│   ├── sdk/
│   └── evaluator/
├── infrastructure/
│   └── terraform/
├── tests/
├── docs/
│   ├── adrs/
│   ├── benchmarks/
│   └── runbooks/
├── docker-compose.yml
├── PRD.md
├── DATA.md
├── ARCHITECTURE.md
├── SECURITY.md
├── SYSTEM-DESIGN.md
├── SKILLS.md
├── AGENTS.md
└── CLAUDE.md
```
