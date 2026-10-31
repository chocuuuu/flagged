# Flagged — 60-Session Sprint Calendar

The learning plan is **60 working sessions over 12 weeks**, organized as 12
sprints of five sessions. These are working-session labels, not calendar dates or a
completion deadline. The canonical session goals, tests, and proposed commit messages
are in `progress/DAILY-PLAN.md`; `progress/PROGRESS.md` is the derived checklist.

| Sprint | Sessions | Focus | Outcome |
|---:|---:|---|---|
| 1 | 1–5 | Domain & local foundation | Clear scope, architecture, and reproducible local workspace |
| 2 | 6–10 | Python API & relational data | Tested FastAPI and PostgreSQL foundation |
| 3 | 11–15 | Flag management & admin access | CRUD, audit trail, version-checked edits, and single-admin auth |
| 4 | 16–20 | Dashboard | Browser workflows for projects, environments, flags, and audit history |
| 5 | 21–25 | SDK & local evaluation | Working local end-to-end flag change in the demo app |
| 6 | 26–30 | Isolation, rollouts & targeting | Scoped keys, environment separation, deterministic evaluation |
| 7 | 31–35 | Refresh, caching & fallback | Polling, conditional requests, last-known-good state, optional local Redis |
| 8 | 36–40 | SSE & consistency | Streaming, reconnect, and monotonic environment revisions |
| 9 | 41–45 | Observability & resilience | Failure evidence, telemetry, propagation and performance measurements |
| 10 | 46–50 | GCP & Terraform foundations | Cost-reviewed, locally validated infrastructure design; no apply by default |
| 11 | 51–55 | Cloud data, events & IAM | Firestore/Pub/Sub concepts tested with local emulators or adapters |
| 12 | 56–60 | CI/CD & finalization | Reproducible local checks, deployment design, final report and retrospective |

## Scheduling and cost guardrails

- Session numbers define the suggested sequence; they do not represent dates,
  deadlines, or required daily cadence.
- Each sprint is exactly five consecutive sessions. There are no gaps or overlaps.
- A session is complete only when its goal and evidence are recorded, not because
  time elapsed.
- The default development and validation path remains local. Live cloud provisioning
  and hosted CI/CD are optional and require the approval gate in `COST-BOUNDARY.md`.
- The Jira backlog organizes tasks under these sprint themes; the session plan is
  the canonical day-by-day learning sequence.
