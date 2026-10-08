# JIRA-BACKLOG.md

# Flagged — Jira-Style Sprint Board

**Cadence:** 12 sprints × 5 working sessions = 60 sessions  
**Workflow:** Backlog → Ready → In Progress → Code Review → QA → Done

## Board conventions

### Issue hierarchy

```text
Epic
 └── Story
      └── Task
           └── Subtask
```

### Recommended Jira fields

- Issue Type
- Summary
- Description
- Epic Link
- Parent
- Sprint
- Priority
- Story Points
- Acceptance Criteria
- Learning Objective
- Dependencies
- GitHub Branch
- Status

- EPIC-1 — Foundation
- EPIC-2 — Backend & Data
- EPIC-3 — Flag Management
- EPIC-4 — Dashboard
- EPIC-5 — SDK
- EPIC-6 — Evaluation & Targeting
- EPIC-7 — Caching & Polling
- EPIC-8 — Streaming & Consistency
- EPIC-9 — Observability & Resilience
- EPIC-10 — GCP Infrastructure
- EPIC-11 — Cloud Data & Events
- EPIC-12 — CI/CD & Finalization

---

# Sprint 1 — Foundation & Domain

**Duration:** 5 working sessions

## FF-101 — Project charter and glossary

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 1  
**Epic:** EPIC-1

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-101-1** — Write problem statement
- [ ] **FF-101-2** — Define control/data plane terms
- [ ] **FF-101-3** — Write first architecture sketch

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-102 — Repository bootstrap

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 1  
**Epic:** EPIC-1

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-102-1** — Create monorepo structure
- [ ] **FF-102-2** — Configure Python tooling
- [ ] **FF-102-3** — Configure frontend/SDK workspace

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-103 — Local infrastructure

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 1  
**Epic:** EPIC-1

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-103-1** — Create Docker Compose
- [ ] **FF-103-2** — Run PostgreSQL locally
- [ ] **FF-103-3** — Add health checks and startup documentation

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-104 — Engineering workflow

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 1  
**Epic:** EPIC-1

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-104-1** — Set branch strategy
- [ ] **FF-104-2** — Add commit conventions
- [ ] **FF-104-3** — Create issue/PR templates

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 2 — Python API & Database

**Duration:** 5 working sessions

## FF-201 — FastAPI foundation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 2  
**Epic:** EPIC-2

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-201-1** — Create app factory
- [ ] **FF-201-2** — Add health/readiness endpoints
- [ ] **FF-201-3** — Configure structured error handling

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-202 — Database layer

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 2  
**Epic:** EPIC-2

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-202-1** — Configure SQLAlchemy
- [ ] **FF-202-2** — Create Alembic baseline
- [ ] **FF-202-3** — Implement DB session lifecycle

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-203 — Core schema

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 2  
**Epic:** EPIC-2

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-203-1** — Create projects/environments tables
- [ ] **FF-203-2** — Create feature_flags table
- [ ] **FF-203-3** — Add uniqueness/index constraints

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-204 — API tests

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 2  
**Epic:** EPIC-2

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-204-1** — Create pytest fixtures
- [ ] **FF-204-2** — Write CRUD integration tests
- [ ] **FF-204-3** — Add invalid-input tests

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 3 — Flag Management & Audit

**Duration:** 5 working sessions

## FF-301 — Project/environment CRUD

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 3  
**Epic:** EPIC-3

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-301-1** — Build create/list/update/delete endpoints
- [ ] **FF-301-2** — Validate environment keys
- [ ] **FF-301-3** — Document endpoint behavior

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-302 — Feature flag CRUD

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 3  
**Epic:** EPIC-3

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-302-1** — Build create/list/update/delete
- [ ] **FF-302-2** — Add version incrementing
- [ ] **FF-302-3** — Add optimistic update protection

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-303 — Audit trail

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 3  
**Epic:** EPIC-3

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-303-1** — Create audit_events table
- [ ] **FF-303-2** — Record mutations
- [ ] **FF-303-3** — Add audit read endpoint

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-304 — Admin authentication

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 3  
**Epic:** EPIC-3

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-304-1** — Implement login
- [ ] **FF-304-2** — Protect admin routes
- [ ] **FF-304-3** — Add authorization tests

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 4 — Dashboard

**Duration:** 5 working sessions

## FF-401 — Astro/React shell

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 4  
**Epic:** EPIC-4

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-401-1** — Create dashboard layout
- [ ] **FF-401-2** — Add routing/navigation
- [ ] **FF-401-3** — Configure API client

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-402 — Project/environment UI

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 4  
**Epic:** EPIC-4

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-402-1** — Project list
- [ ] **FF-402-2** — Environment selector
- [ ] **FF-402-3** — Environment state/loading/error UI

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-403 — Flag management UI

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 4  
**Epic:** EPIC-4

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-403-1** — Flag table
- [ ] **FF-403-2** — Create/edit form
- [ ] **FF-403-3** — Enable/disable control

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-404 — Audit UX

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 4  
**Epic:** EPIC-4

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-404-1** — Audit history page
- [ ] **FF-404-2** — Before/after display
- [ ] **FF-404-3** — Error and empty states

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 5 — SDK & Local Evaluation

**Duration:** 5 working sessions

## FF-501 — SDK package

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 5  
**Epic:** EPIC-5

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-501-1** — Create package structure
- [ ] **FF-501-2** — Define public SDK API
- [ ] **FF-501-3** — Add build/test pipeline

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-502 — Configuration bootstrap

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 5  
**Epic:** EPIC-5

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-502-1** — Implement config fetch
- [ ] **FF-502-2** — Validate config schema
- [ ] **FF-502-3** — Store immutable snapshot

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-503 — Evaluation engine

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 5  
**Epic:** EPIC-5

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-503-1** — Boolean evaluation
- [ ] **FF-503-2** — Default/fallback evaluation
- [ ] **FF-503-3** — Evaluation unit-test matrix

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-504 — Demo Store integration

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 5  
**Epic:** EPIC-5

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-504-1** — Integrate SDK
- [ ] **FF-504-2** — Add new checkout flag
- [ ] **FF-504-3** — Demonstrate live switch without rebuild

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 6 — Environments, Rollouts & Targeting

**Duration:** 5 working sessions

## FF-601 — Client keys

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 6  
**Epic:** EPIC-6

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-601-1** — Generate scoped keys
- [ ] **FF-601-2** — Hash stored secrets
- [ ] **FF-601-3** — Build revoke flow

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-602 — Environment isolation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 6  
**Epic:** EPIC-6

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-602-1** — Prevent cross-environment reads
- [ ] **FF-602-2** — Test staging/production separation
- [ ] **FF-602-3** — Add SDK environment configuration

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-603 — Percentage rollout

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 6  
**Epic:** EPIC-6

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-603-1** — Implement stable hashing
- [ ] **FF-603-2** — Build 0/50/100% cases
- [ ] **FF-603-3** — Test deterministic user assignment

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-604 — Targeting rules

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 6  
**Epic:** EPIC-6

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-604-1** — Define v1 rule model
- [ ] **FF-604-2** — Implement equals/contains
- [ ] **FF-604-3** — Test rule precedence

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 7 — Caching & Polling

**Duration:** 5 working sessions

## FF-701 — In-memory configuration cache

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 7  
**Epic:** EPIC-7

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-701-1** — Atomic snapshot replacement
- [ ] **FF-701-2** — Track version/age
- [ ] **FF-701-3** — Expose cache diagnostics

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-702 — Polling

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 7  
**Epic:** EPIC-7

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-702-1** — Add polling scheduler
- [ ] **FF-702-2** — Handle timeouts/errors
- [ ] **FF-702-3** — Measure stale window

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-703 — HTTP cache optimization

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 7  
**Epic:** EPIC-7

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-703-1** — Implement ETag/version conditional requests
- [ ] **FF-703-2** — Test 304 behavior
- [ ] **FF-703-3** — Benchmark request reduction

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-704 — Redis experiment

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 7  
**Epic:** EPIC-7

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-704-1** — Run Redis locally
- [ ] **FF-704-2** — Implement shared cache adapter
- [ ] **FF-704-3** — Document when Redis helps

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 8 — SSE & Consistency

**Duration:** 5 working sessions

## FF-801 — SSE stream

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 8  
**Epic:** EPIC-8

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-801-1** — Create stream endpoint
- [ ] **FF-801-2** — Define event schema
- [ ] **FF-801-3** — Handle client disconnects

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-802 — SDK stream client

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 8  
**Epic:** EPIC-8

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-802-1** — Connect to SSE
- [ ] **FF-802-2** — Update snapshot from events
- [ ] **FF-802-3** — Add stream status diagnostics

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-803 — Reconnect behavior

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 8  
**Epic:** EPIC-8

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-803-1** — Exponential backoff
- [ ] **FF-803-2** — Catch-up bootstrap
- [ ] **FF-803-3** — Test connection interruption

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-804 — Consistency controls

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 8  
**Epic:** EPIC-8

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-804-1** — Reject stale versions
- [ ] **FF-804-2** — Handle duplicates
- [ ] **FF-804-3** — Test out-of-order events

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 9 — Observability, Resilience & Load

**Duration:** 5 working sessions

## FF-901 — Structured observability

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 9  
**Epic:** EPIC-9

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-901-1** — Add request logs
- [ ] **FF-901-2** — Add evaluation telemetry
- [ ] **FF-901-3** — Add propagation metrics

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-902 — Tracing/metrics

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 9  
**Epic:** EPIC-9

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-902-1** — Instrument service boundaries
- [ ] **FF-902-2** — Expose latency metrics
- [ ] **FF-902-3** — Measure propagation delay

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-903 — Failure injection

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 9  
**Epic:** EPIC-9

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-903-1** — Break database
- [ ] **FF-903-2** — Break stream connection
- [ ] **FF-903-3** — Test stale-cache fallback

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-904 — Load testing

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 9  
**Epic:** EPIC-9

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-904-1** — Create Locust scenarios
- [ ] **FF-904-2** — Measure p50/p95/p99
- [ ] **FF-904-3** — Write performance report

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 10 — Terraform & GCP Foundation

**Duration:** 5 working sessions

## FF-1001 — Cost guardrails

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 10  
**Epic:** EPIC-10

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1001-1** — Create budget/alert
- [ ] **FF-1001-2** — Document free-tier assumptions
- [ ] **FF-1001-3** — Write cleanup checklist

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1002 — Terraform foundation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 10  
**Epic:** EPIC-10

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1002-1** — Create provider/module layout
- [ ] **FF-1002-2** — Create state configuration
- [ ] **FF-1002-3** — Add variables/outputs

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1003 — Artifact Registry

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 10  
**Epic:** EPIC-10

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1003-1** — Create repository
- [ ] **FF-1003-2** — Build container locally
- [ ] **FF-1003-3** — Push versioned image

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1004 — Cloud Run foundation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 10  
**Epic:** EPIC-10

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1004-1** — Deploy stateless API
- [ ] **FF-1004-2** — Configure environment variables
- [ ] **FF-1004-3** — Validate scale-to-zero behavior

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 11 — Firestore, Pub/Sub & IAM

**Duration:** 5 working sessions

## FF-1101 — Firestore adapter

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 11  
**Epic:** EPIC-11

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1101-1** — Map local domain to documents
- [ ] **FF-1101-2** — Implement repository methods
- [ ] **FF-1101-3** — Run parity tests vs PostgreSQL

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1102 — Pub/Sub propagation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 11  
**Epic:** EPIC-11

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1102-1** — Create topic/subscription
- [ ] **FF-1102-2** — Publish configuration events
- [ ] **FF-1102-3** — Consume and handle duplicates

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1103 — GCP IAM

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 11  
**Epic:** EPIC-11

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1103-1** — Create least-privilege runtime identity
- [ ] **FF-1103-2** — Limit Firestore permissions
- [ ] **FF-1103-3** — Limit Pub/Sub permissions

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1104 — Cloud observability

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 11  
**Epic:** EPIC-11

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1104-1** — Configure useful logs
- [ ] **FF-1104-2** — Validate log volume
- [ ] **FF-1104-3** — Create basic operational dashboard/queries

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 12 — CI/CD, Cloud Validation & Finalization

**Duration:** 5 working sessions

## FF-1201 — GitHub Actions CI

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 12  
**Epic:** EPIC-12

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1201-1** — Lint workflow
- [ ] **FF-1201-2** — Unit/integration test workflow
- [ ] **FF-1201-3** — Build artifact workflow

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1202 — Deployment workflow

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 12  
**Epic:** EPIC-12

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1202-1** — Deploy Cloud Run from trusted branch
- [ ] **FF-1202-2** — Use environment configuration
- [ ] **FF-1202-3** — Add rollback procedure

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1203 — End-to-end validation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 12  
**Epic:** EPIC-12

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1203-1** — Test cloud SDK bootstrap
- [ ] **FF-1203-2** — Test Pub/Sub/SSE propagation
- [ ] **FF-1203-3** — Test failure fallback

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1204 — Final engineering package

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 12  
**Epic:** EPIC-12

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1204-1** — Review ADRs
- [ ] **FF-1204-2** — Write architecture/benchmark report
- [ ] **FF-1204-3** — Record final demo and retrospective

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Cross-cutting Tasks

## Documentation

- [ ] Keep `PRD.md` aligned with scope changes.
- [ ] Keep `ARCHITECTURE.md` aligned with real implementation.
- [ ] Add an ADR for material architecture changes.
- [ ] Maintain `SYSTEM-DESIGN.md` with measured evidence.
- [ ] Maintain `SECURITY.md` as security controls evolve.

## GitHub

- [ ] Protect `main`.
- [ ] Require CI checks before merge.
- [ ] Link PRs to Jira issues.
- [ ] Keep commits focused.
- [ ] Tag milestone releases.

## AI collaboration

- [ ] Use concept checkpoint before unfamiliar implementation.
- [ ] Ask AI to explain failing tests rather than patch blindly.
- [ ] Keep an AI/dev journal of notable lessons.
- [ ] Review AI-generated code for correctness and security.

## Final demo checklist

- [ ] Create a feature flag.
- [ ] Toggle it from the dashboard.
- [ ] See the demo app change without rebuilding.
- [ ] Configure a 10% rollout.
- [ ] Demonstrate deterministic assignment.
- [ ] Disconnect the service and demonstrate cached behavior.
- [ ] Show a configuration update reaching clients.
- [ ] Show metrics/logs.
- [ ] Show Terraform deployment.
- [ ] Explain at least three trade-offs.
