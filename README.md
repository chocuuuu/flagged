# Flagged — Project Plan Package

## Distributed Feature Flag & Configuration Platform

This package is the planning baseline for a 12-week / 60-session learning project.

The project is designed to be:

- local-first;
- cloud-later;
- system-design heavy;
- test and debugging driven;
- AI-assisted but not AI-dependent;
- GitHub-centered;
- Terraform-managed;
- as close to zero-cost as practical.

## Start here

1. Read `PRD.md`.
2. Read `ARCHITECTURE.md`.
3. Read `SYSTEM-DESIGN.md`.
4. Read `SKILLS.md`.
5. Read `AGENTS.md`.
6. Start Sprint 1.
7. Track progress in `progress/PROGRESS.md`.
8. Manage execution in `jira/JIRA-BACKLOG.md`.

## Project stack

```text
Frontend      Astro + React + TypeScript
Backend       Python + FastAPI
Local DB      PostgreSQL
Cache lab     Redis
SDK           TypeScript
Containers    Docker / Docker Compose
IaC           Terraform
CI/CD         GitHub Actions
Cloud         GCP
Cloud DB      Firestore
Events        Pub/Sub
Runtime       Cloud Run
Observability Cloud Logging/Monitoring
```

## Important database decision

PostgreSQL and Firestore are used for different stages intentionally.

The project does **not** require two production databases.

- PostgreSQL = rich local relational learning environment.
- Firestore = low-ops GCP deployment experiment with free-tier-compatible usage.
- Repository boundary = makes the persistence decision explicit and testable.

Read ADR-005, ADR-006, and ADR-007 together.

## Cost warning

Do not provision paid managed Redis/Memorystore as part of the standard plan.

Do not provision Cloud SQL unless an explicit cost-approved experiment is being performed.

Cloud free tiers are quotas, not guarantees of zero spend. Re-check official pricing immediately before cloud provisioning.

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
- `jira/JIRA-BACKLOG.csv`
- `docs/adrs/`

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
