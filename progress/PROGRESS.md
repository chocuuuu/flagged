# Flagged — Milestone Progress Tracker

## How to use

Progress is measured by outcomes and evidence, not elapsed calendar time. Check a milestone only when its completion evidence is available and you can explain the learning objective. Use `progress/DAILY-PLAN.md` for suggested work blocks; pause or resume whenever your other responsibilities require it.

The full project contains 12 milestones. Milestone 5 is the first useful local end-to-end system, not the end of scope. Live GCP provisioning is not needed to complete any milestone.

## Milestones

- [ ] **M1 — Domain and local foundation:** scope, glossary, architecture sketch, repository/tooling, reproducible local database.
- [ ] **M2 — API and relational data foundation:** FastAPI, validation, SQLAlchemy, migrations, schema, tests.
- [ ] **M3 — Flag control plane and admin access:** CRUD, optimistic flag edits, atomic audit, single-admin authentication, security tests.
- [ ] **M4 — Admin dashboard:** project/environment/flag/audit workflows with loading, error, and accessibility behavior.
- [ ] **M5 — SDK and first local end-to-end behavior:** bootstrap, immutable snapshot, evaluation/fallback, demo-store live update.
- [ ] **M6 — Isolation, rollout, and targeting:** scoped client keys, environment isolation, deterministic bucketing, targeting precedence.
- [ ] **M7 — Refresh, cache, and stale behavior:** polling, conditional HTTP, last-known-good state, optional local Redis experiment.
- [ ] **M8 — Streaming and consistency:** SSE, reconnect/catch-up, environment revisions, duplicate/out-of-order update tests.
- [ ] **M9 — Observability, resilience, and measurement:** structured logs, metrics, failure matrix, bounded load and propagation evidence.
- [ ] **M10 — GCP and Terraform foundations:** cost review, local Terraform validation, container/Cloud Run plan, cleanup documentation; no apply by default.
- [ ] **M11 — Document data, events, and IAM:** Firestore emulator/adapter, Pub/Sub emulator/local adapter, idempotency, least-privilege design.
- [ ] **M12 — CI/CD design and final engineering package:** local checks, deployment/rollback design, final end-to-end evidence, report and retrospective.

## ADR tracker

- [ ] ADR-001 — Local-first development and cloud-later migration
- [ ] ADR-002 — Modular monolith before microservices
- [ ] ADR-003 — Python + FastAPI for the control plane
- [ ] ADR-004 — Astro + React for dashboard and demo app
- [ ] ADR-005 — PostgreSQL as local source of truth
- [ ] ADR-006 — Firestore emulator by default; live use is optional
- [ ] ADR-007 — Persistence repository boundary
- [ ] ADR-008 — Evaluate feature flags in the SDK
- [ ] ADR-009 — Polling before SSE before Pub/Sub
- [ ] ADR-010 — Environment-wide monotonic configuration revisions
- [ ] ADR-011 — Deterministic hashing for percentage rollouts
- [ ] ADR-012 — Scoped read-only client keys
- [ ] ADR-013 — Do not require managed Redis
- [ ] ADR-014 — Cloud Run as an optional stateless deployment target
- [ ] ADR-015 — Terraform for infrastructure
- [ ] ADR-016 — GitHub Actions as optional hosted CI/CD
- [ ] ADR-017 — Observability is a core requirement
- [ ] ADR-018 — Single-operator admin authentication

## Cost safety checklist

- [ ] Default development, testing, and cloud-learning path uses local services, emulators, or adapters.
- [ ] No live GCP resource is required for milestone completion.
- [ ] `terraform apply` and paid hosted workflows remain disabled unless explicitly approved.
- [ ] Before an approved live experiment, current pricing/billing prerequisites, resource limits, and cleanup steps are documented.
- [ ] Free quotas, budgets, and alerts are not treated as spending caps.
- [ ] Resources and data from any explicitly approved experiment are cleaned up and deletion is verified.

## Evidence to record for each milestone

```text
What I built or investigated:
What I learned:
What confused me:
What broke and why:
What test or repeatable evidence proves the behavior:
What trade-off I chose and why:
What I would change at 10x scale:
What remains incomplete:
Commit or reference:
```
