# PROGRESS.md

# Flagged — 60-Day Progress Tracker

## How to use

Each day is one focused learning/engineering session. A day does not mean "finish all code"; it means complete the learning target, record evidence, and commit progress.

Suggested session structure:

```text
20–30 min  Learn/read
60–120 min Implement
20–45 min  Test/debug
10 min     Notes/commit
```

## Daily tracker

- [ ] Day 01 — Project charter, terminology, environment setup
- [ ] Day 02 — Read/annotate feature-flag concepts and LaunchDarkly/OpenFeature models
- [ ] Day 03 — Define control plane vs data plane; draw first architecture
- [ ] Day 04 — Repository bootstrap; GitHub branch/commit conventions
- [ ] Day 05 — Local Docker Compose skeleton
- [ ] Day 06 — FastAPI app shell and health endpoint
- [ ] Day 07 — Pydantic models and API conventions
- [ ] Day 08 — SQLAlchemy setup and database connection
- [ ] Day 09 — Alembic migrations
- [ ] Day 10 — Project/environment schema
- [ ] Day 11 — Flag schema
- [ ] Day 12 — CRUD API for projects/environments
- [ ] Day 13 — CRUD API for flags
- [ ] Day 14 — Validation/error handling
- [ ] Day 15 — API integration tests
- [ ] Day 16 — Admin authentication
- [ ] Day 17 — Authorization boundaries
- [ ] Day 18 — Audit event model
- [ ] Day 19 — Audit trail implementation
- [ ] Day 20 — Admin API cleanup and docs
- [ ] Day 21 — Astro + React dashboard shell
- [ ] Day 22 — Project/environment screens
- [ ] Day 23 — Flag list/create/edit UI
- [ ] Day 24 — Flag enable/disable workflow
- [ ] Day 25 — Dashboard tests
- [ ] Day 26 — SDK package skeleton
- [ ] Day 27 — SDK bootstrap endpoint
- [ ] Day 28 — Immutable in-memory config
- [ ] Day 29 — Boolean evaluation
- [ ] Day 30 — Demo Store integration
- [ ] Day 31 — Environment/client-key model
- [ ] Day 32 — Percentage rollout design
- [ ] Day 33 — Deterministic hashing implementation
- [ ] Day 34 — Targeting rules v1
- [ ] Day 35 — Evaluation precedence and test matrix
- [ ] Day 36 — Polling implementation
- [ ] Day 37 — ETag/version optimization
- [ ] Day 38 — Stale configuration and fallback
- [ ] Day 39 — Redis cache experiment
- [ ] Day 40 — Multi-instance cache behavior
- [ ] Day 41 — SSE endpoint
- [ ] Day 42 — SDK SSE client
- [ ] Day 43 — Reconnect/backoff behavior
- [ ] Day 44 — Out-of-order/duplicate update handling
- [ ] Day 45 — Propagation-latency benchmark
- [ ] Day 46 — Structured logging
- [ ] Day 47 — Metrics and traces
- [ ] Day 48 — Failure injection
- [ ] Day 49 — Load testing
- [ ] Day 50 — Performance tuning and report
- [ ] Day 51 — GCP project cost guardrails
- [ ] Day 52 — Terraform foundation
- [ ] Day 53 — Cloud Run deployment
- [ ] Day 54 — Firestore adapter
- [ ] Day 55 — Pub/Sub integration
- [ ] Day 56 — GCP IAM hardening
- [ ] Day 57 — GitHub Actions CI
- [ ] Day 58 — CD/deploy workflow
- [ ] Day 59 — End-to-end cloud validation
- [ ] Day 60 — Final demo, ADR review, documentation, retrospective

## Sprint tracker

- [ ] Sprint 1 — Domain, repo, local environment
- [ ] Sprint 2 — Python API + database foundation
- [ ] Sprint 3 — Core flag management + audit
- [ ] Sprint 4 — Admin dashboard
- [ ] Sprint 5 — SDK + local evaluation
- [ ] Sprint 6 — Environments + rollouts + targeting
- [ ] Sprint 7 — Polling + caching
- [ ] Sprint 8 — SSE + consistency
- [ ] Sprint 9 — Observability + resilience + load testing
- [ ] Sprint 10 — Terraform + GCP foundation
- [ ] Sprint 11 — Firestore + Pub/Sub + IAM
- [ ] Sprint 12 — CI/CD + cloud validation + final documentation

## ADR tracker

- [ ] ADR-001 — Local-first development and cloud-later migration
- [ ] ADR-002 — Modular monolith before microservices
- [ ] ADR-003 — Python + FastAPI for the control plane
- [ ] ADR-004 — Astro + React for dashboard and demo app
- [ ] ADR-005 — PostgreSQL as local source of truth
- [ ] ADR-006 — Firestore as default GCP persistence path
- [ ] ADR-007 — Persistence repository boundary
- [ ] ADR-008 — Evaluate feature flags in the SDK
- [ ] ADR-009 — Polling before SSE before Pub/Sub
- [ ] ADR-010 — Monotonic configuration versions
- [ ] ADR-011 — Deterministic hashing for percentage rollouts
- [ ] ADR-012 — Scoped read-only client keys
- [ ] ADR-013 — Do not require managed Redis
- [ ] ADR-014 — Cloud Run for stateless application hosting
- [ ] ADR-015 — Terraform for infrastructure
- [ ] ADR-016 — GitHub Actions for CI/CD
- [ ] ADR-017 — Observability is a core requirement

## Cost safety checklist

- [ ] Budget/alert configured before cloud provisioning
- [ ] No always-on paid cache created
- [ ] No unnecessary Cloud SQL instance created
- [ ] Cloud Run min instances = 0 unless deliberately testing otherwise
- [ ] Logs are bounded
- [ ] Artifact images are cleaned up
- [ ] Firestore free-tier database is the default path
- [ ] Pub/Sub usage monitored
- [ ] GCP resources deleted after experiments

## Evidence to record

For each major milestone, record:

```text
What I built:
What I learned:
What broke:
Why it broke:
How I fixed it:
What test proves it:
What trade-off I made:
What I would change at 10x scale:
Commit:
```
