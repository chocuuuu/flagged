# DAILY-PLAN.md

# Flagged — 60-Working-Session Execution Plan

## Working assumption

- 5 sessions/week
- 12 weeks
- 2–4 focused hours/session
- Longer sessions may compress the schedule; shorter sessions may extend it
- The goal is learning evidence, not speed

## Session template

```text
1. Learn        20–45 min
2. Design       15–30 min
3. Implement    60–120 min
4. Test/debug   20–45 min
5. Document     10–20 min
6. Commit       5–10 min
```

## Phase 1 — Understand and bootstrap

### Day 1 — Project charter
Goal: understand exactly what a feature flag service solves.
Tools: GitHub, VS Code, Claude Code, Gemini.
Deliverable: problem statement + glossary.
Test: explain deployment vs release, control plane vs data plane without notes.
Commit: `docs: add project charter and glossary`

### Day 2 — Study reference architectures
Goal: inspect LaunchDarkly/OpenFeature concepts.
Deliverable: one-page comparison of commercial/reference concepts.
Experiment: identify which concepts are in/out of scope.
Commit: `docs: document feature flag domain concepts`

### Day 3 — First architecture
Goal: draw control/data-plane architecture.
Tools: Mermaid, draw.io/Excalidraw.
Deliverable: architecture v0.
Checkpoint: explain why database is not in the evaluation hot path.
Commit: `docs: add initial system architecture`

### Day 4 — Monorepo
Goal: create repository structure and boundaries.
Tools: Git, GitHub, pnpm, uv.
Deliverable: apps/services/packages/docs directories.
Test: clean clone setup.
Commit: `chore: bootstrap monorepo`

### Day 5 — Docker Compose
Goal: create local reproducible infrastructure.
Tools: Docker, PostgreSQL.
Deliverable: compose file + health checks.
Test: destroy/recreate environment successfully.
Commit: `infra: add local database compose setup`

## Phase 2 — Python/API/database

### Day 6 — FastAPI shell
Goal: create backend application and health endpoints.
Tools: FastAPI, pytest.
Test: unit + HTTP health check.
Commit: `feat(api): add fastapi service shell`

### Day 7 — Validation
Goal: learn Pydantic request/response validation.
Deliverable: API error contract.
Test: malformed payload cases.
Commit: `feat(api): add request validation`

### Day 8 — SQLAlchemy
Goal: connect service layer to PostgreSQL.
Deliverable: DB session dependency.
Test: connection test + transaction rollback fixture.
Commit: `feat(db): add sqlalchemy integration`

### Day 9 — Alembic
Goal: learn schema migrations.
Deliverable: first migration.
Experiment: migrate up/down in a clean database.
Commit: `infra(db): add alembic migrations`

### Day 10 — Core schema
Goal: implement projects/environments.
Deliverable: tables, constraints, indexes.
Test: duplicate environment rejection.
Commit: `feat(db): add project and environment models`

## Phase 3 — Flag management

### Day 11 — Flag model
Goal: model feature flags and version field.
Test: unique key per environment.
Commit: `feat(flag): add feature flag model`

### Day 12 — Flag CRUD
Goal: build create/list/update/delete.
Test: API integration suite.
Commit: `feat(flag): add flag crud endpoints`

### Day 13 — Versioning
Goal: prevent lost updates.
Experiment: simulate two clients updating the same flag.
Commit: `feat(flag): add optimistic version checks`

### Day 14 — Audit events
Goal: make changes observable.
Test: each mutation creates an audit record.
Commit: `feat(audit): record configuration changes`

### Day 15 — Admin authentication
Goal: protect control-plane endpoints.
Test: unauthorized/forbidden/success cases.
Commit: `feat(auth): protect admin endpoints`

## Phase 4 — Dashboard

### Day 16 — Astro/React shell
Goal: build dashboard skeleton.
Tools: Astro, React, TypeScript, Tailwind.
Commit: `feat(dashboard): add application shell`

### Day 17 — Project/environment UI
Goal: browse configuration scope.
Test: loading/error/empty states.
Commit: `feat(dashboard): add project environment views`

### Day 18 — Flag management UI
Goal: create/edit/toggle flags.
Test: API integration from browser.
Commit: `feat(dashboard): add flag management`

### Day 19 — Audit UI
Goal: inspect who changed configuration.
Commit: `feat(dashboard): add audit history`

### Day 20 — Dashboard hardening
Goal: validation, accessibility, error UX.
Test: browser smoke tests.
Commit: `fix(dashboard): harden admin workflows`

## Phase 5 — SDK and evaluation

### Day 21 — SDK contract
Goal: design public SDK API before implementation.
Deliverable: README examples + type definitions.
Commit: `docs(sdk): define client contract`

### Day 22 — Bootstrap
Goal: fetch environment configuration.
Test: malformed/timeout/401 responses.
Commit: `feat(sdk): add configuration bootstrap`

### Day 23 — Immutable cache
Goal: safely store configuration in memory.
Test: atomic replacement and snapshot reads.
Commit: `feat(sdk): add in memory config store`

### Day 24 — Evaluation
Goal: implement boolean evaluation.
Test: deterministic unit matrix.
Commit: `feat(sdk): add boolean evaluation`

### Day 25 — Demo store integration
Goal: integrate SDK into the demo application.
Demo: toggle a checkout UI without rebuilding.
Commit: `feat(demo): integrate feature flag sdk`

## Phase 6 — Rollouts and targeting

### Day 26 — Client keys
Goal: scope read-only SDK credentials.
Test: admin key rejected by SDK endpoint.
Commit: `feat(auth): add scoped client keys`

### Day 27 — Environment isolation
Goal: prevent cross-environment access.
Test: production client cannot read staging.
Commit: `feat(auth): enforce environment isolation`

### Day 28 — Percentage rollout
Goal: deterministic hashing.
Experiment: same user remains in same bucket.
Commit: `feat(eval): add deterministic percentage rollout`

### Day 29 — Targeting rules
Goal: support equals/contains.
Test: rule order and fallback cases.
Commit: `feat(eval): add targeting rules`

### Day 30 — Evaluation matrix
Goal: document precedence.
Deliverable: decision table.
Test: comprehensive rules + rollout matrix.
Commit: `test(eval): expand evaluation behavior matrix`

## Phase 7 — Caching and polling

### Day 31 — SDK age/version diagnostics
Goal: track snapshot age/version.
Commit: `feat(sdk): expose configuration diagnostics`

### Day 32 — Polling
Goal: periodically refresh configuration.
Test: server unavailable while polling.
Commit: `feat(sdk): add configuration polling`

### Day 33 — ETag/version optimization
Goal: reduce unnecessary payloads.
Test: 304/no-change path.
Commit: `feat(api): add conditional configuration fetch`

### Day 34 — Stale fallback
Goal: define last-known-good behavior.
Experiment: shut down API and keep demo running.
Commit: `feat(sdk): add stale configuration fallback`

### Day 35 — Redis lab
Goal: compare in-memory and shared cache.
Tools: Redis, Docker.
Deliverable: benchmark + trade-off notes.
Commit: `docs(cache): document redis experiment`

## Phase 8 — SSE and consistency

### Day 36 — SSE fundamentals
Goal: understand long-lived HTTP connections.
Deliverable: minimal SSE proof of concept.
Commit: `feat(stream): add sse proof of concept`

### Day 37 — Production-ish stream endpoint
Goal: stream version/update events.
Test: multiple clients.
Commit: `feat(stream): add configuration update stream`

### Day 38 — SDK stream
Goal: consume update events.
Commit: `feat(sdk): consume sse updates`

### Day 39 — Reconnect
Goal: exponential backoff and catch-up.
Test: terminate/restart server.
Commit: `feat(sdk): add stream reconnect handling`

### Day 40 — Ordering/idempotency
Goal: reject duplicates/out-of-order messages.
Test: versions 10, 12, 11.
Commit: `test(sdk): add update ordering guarantees`

## Phase 9 — Observability/resilience/performance

### Day 41 — Structured logging
Goal: logs with request IDs, environment, flag/config version.
Commit: `feat(obs): add structured logging`

### Day 42 — Metrics
Goal: measure evaluation latency and refresh failures.
Commit: `feat(obs): add evaluation metrics`

### Day 43 — Propagation measurement
Goal: measure admin change → client update.
Experiment: 100 update events.
Commit: `test(obs): measure configuration propagation`

### Day 44 — Failure injection
Goal: break DB, API, and stream intentionally.
Deliverable: failure matrix.
Commit: `test(resilience): add failure scenarios`

### Day 45 — Load testing
Goal: establish baseline with Locust.
Measure: p50/p95/p99, throughput, errors.
Commit: `test(perf): add load test scenarios`

## Phase 10 — GCP foundation

### Day 46 — Cost guardrails
Goal: configure budget/alerts and cleanup procedures.
Deliverable: cost checklist.
Commit: `docs(cost): add gcp cost guardrails`

### Day 47 — Terraform structure
Goal: provider, variables, outputs, state.
Test: plan with no changes.
Commit: `infra: bootstrap terraform`

### Day 48 — Artifact Registry
Goal: build/push versioned image.
Test: pull and run image locally.
Commit: `infra: add artifact registry`

### Day 49 — Cloud Run
Goal: deploy stateless API.
Test: scale-to-zero and cold start behavior.
Commit: `infra: deploy api to cloud run`

### Day 50 — Cloud logging/operations
Goal: inspect cloud logs and runtime behavior.
Commit: `ops: document cloud run operations`

## Phase 11 — Firestore/Pub/Sub/IAM

### Day 51 — Firestore model
Goal: map relational domain to documents.
Deliverable: mapping document and ADR.
Commit: `docs(data): document firestore mapping`

### Day 52 — Firestore adapter
Goal: implement repository adapter.
Test: domain-level parity suite.
Commit: `feat(db): add firestore repository`

### Day 53 — Pub/Sub topic
Goal: publish configuration-change events.
Test: event payload and version.
Commit: `feat(events): publish config updates`

### Day 54 — Pub/Sub consumer
Goal: consume events idempotently.
Test: duplicate delivery.
Commit: `feat(events): consume config updates`

### Day 55 — IAM hardening
Goal: least-privilege runtime identity.
Test: denied permission outside required resources.
Commit: `infra(security): tighten gcp iam`

## Phase 12 — CI/CD and finalization

### Day 56 — CI
Goal: lint + tests + build on pull request.
Commit: `ci: add github actions checks`

### Day 57 — CD
Goal: controlled deployment to Cloud Run.
Test: rollback procedure.
Commit: `ci: add cloud deployment workflow`

### Day 58 — Cloud E2E
Goal: test dashboard → API → Firestore → Pub/Sub → SDK/SSE.
Commit: `test(e2e): validate cloud architecture`

### Day 59 — Final benchmark and docs
Goal: compare baseline vs final system.
Deliverable: benchmark report and architecture evolution diagram.
Commit: `docs: add final benchmark report`

### Day 60 — Final capstone
Goal: perform complete demo and retrospective.
Deliverables:
- demo recording
- architecture walkthrough
- security walkthrough
- cost review
- ADR review
- "what I learned" retrospective
Commit: `docs: finalize project documentation`

## Completion standard

Do not mark a day complete because the code "exists."

Mark it complete when the learner can:

- explain the concept;
- demonstrate the behavior;
- show a test;
- describe a failure mode;
- point to the Git commit;
- state what remains imperfect.
