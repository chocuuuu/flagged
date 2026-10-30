# Flagged — Milestone Roadmap

These are 12 ordered outcome milestones, not sprints with fixed dates, weeks, or session counts. Work at a sustainable pace and update progress when the evidence exists. Use `progress/DAILY-PLAN.md` for suggested work blocks and `progress/PROGRESS.md` to record completion.

| Milestone | Focus | Outcome |
|---:|---|---|
| 1 | Domain & local foundation | Clear scope, architecture, and reproducible local workspace |
| 2 | Python API & relational data | Tested FastAPI and PostgreSQL foundation |
| 3 | Flag management & admin access | CRUD, audit trail, version-checked edits, and single-admin auth |
| 4 | Dashboard | Browser workflows for projects, environments, flags, and audit history |
| 5 | SDK & local evaluation | Working local end-to-end flag change in the demo app |
| 6 | Isolation, rollouts & targeting | Scoped keys, environment separation, deterministic evaluation |
| 7 | Refresh, caching & fallback | Polling, conditional requests, last-known-good state, optional local Redis |
| 8 | SSE & consistency | Streaming, reconnect, and monotonic environment revisions |
| 9 | Observability & resilience | Failure evidence, telemetry, propagation and performance measurements |
| 10 | GCP & Terraform foundations | Cost-reviewed, locally validated infrastructure design; no apply by default |
| 11 | Cloud data, events & IAM | Firestore/Pub/Sub concepts tested with local emulators or adapters |
| 12 | CI/CD & finalization | Reproducible local checks, deployment design, final report and retrospective |

## Scheduling guidance

- There is no prescribed number of sessions or hours per milestone.
- A milestone may be split into several work periods or combined with a small adjacent item when its prerequisites are understood.
- Do not mark work complete because time elapsed; use the evidence in the milestone guide.
- The first five milestones provide a useful local system. Completing them does not require dropping the remaining learning objectives.
- Live cloud provisioning and hosted CI/CD are optional experiments, not completion requirements. Follow `COST-BOUNDARY.md` before considering them.

## Jira relationship

The existing Jira issue hierarchy is a backlog of work. Its groupings help organize related issues; they do not impose a calendar commitment. The currently maintained Jira import source is `jira/FLAGGED-JIRA-IMPORT.csv`; `jira/JIRA-BACKLOG.csv` is an older export and should not be used.
