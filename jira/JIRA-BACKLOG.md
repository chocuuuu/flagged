# JIRA-BACKLOG.md

# Flagged - Jira Backlog

`JIRA-BACKLOG.md` is the canonical issue source. Generate the CSV import with
`python scripts/generate_jira_csv.py`; do not hand-edit the CSV. `IMPORT-ID-MAP.csv`
maps the `FLAG-*` Jira keys shown in the workspace to the numeric work item IDs
required by the existing import format. Preserve existing mappings. For a new
issue, use the next key issued by the Jira workspace and add a unique numeric
work item ID to the map. The generated import keeps the existing seven-column
format and numeric parent IDs.

**Execution model:** 12 ordered sprints x 5 working sessions; 60 working sessions over 12 weeks, with no fixed calendar dates or deadline

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
- Milestone
- Priority
- Story Points
- Sprint
- Epic
- Test Evidence
- Acceptance Criteria
- Learning Objective
- Dependencies
- GitHub Branch
- Status

- FLAG-1 — Foundation
- FLAG-2 — Backend & Data
- FLAG-3 — Flag Management
- FLAG-4 — Dashboard
- FLAG-5 — SDK
- FLAG-6 — Evaluation & Targeting
- FLAG-7 — Caching & Polling
- FLAG-8 — Streaming & Consistency
- FLAG-9 — Observability & Resilience
- FLAG-10 — GCP Infrastructure
- FLAG-11 — Cloud Data & Events
- FLAG-12 — CI/CD & Finalization

---

# Sprint 1 — Domain & local foundation

**Timing:** Outcome-based; no fixed duration

## FLAG-13 — Project charter and glossary

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 1<br>
**Epic:** FLAG-1
**Learning Objective:** Domain & local foundation

**Test Evidence:** `FLAG-13-T1` (success path) and `FLAG-13-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-61** — Write problem statement
- [ ] **FLAG-62** — Define control/data plane terms
- [ ] **FLAG-63** — Write first architecture sketch

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-14 — Repository bootstrap

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 1<br>
**Epic:** FLAG-1
**Learning Objective:** Domain & local foundation

**Test Evidence:** `FLAG-14-T1` (success path) and `FLAG-14-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-64** — Create monorepo structure
- [ ] **FLAG-65** — Configure Python tooling
- [ ] **FLAG-66** — Configure frontend/SDK workspace

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-15 — Local infrastructure

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 1<br>
**Epic:** FLAG-1
**Learning Objective:** Domain & local foundation

**Test Evidence:** `FLAG-15-T1` (success path) and `FLAG-15-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-67** — Create Docker Compose
- [ ] **FLAG-68** — Run PostgreSQL locally
- [ ] **FLAG-69** — Add health checks and startup documentation

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-16 — Engineering workflow

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 1<br>
**Epic:** FLAG-1
**Learning Objective:** Domain & local foundation

**Test Evidence:** `FLAG-16-T1` (success path) and `FLAG-16-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-70** — Set branch strategy
- [ ] **FLAG-71** — Add commit conventions
- [ ] **FLAG-72** — Create issue/PR templates

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 2 — Python API & relational data

**Timing:** Outcome-based; no fixed duration

## FLAG-17 — FastAPI foundation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 2<br>
**Epic:** FLAG-2
**Learning Objective:** Python API & relational data

**Test Evidence:** `FLAG-17-T1` (success path) and `FLAG-17-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-73** — Create app factory
- [ ] **FLAG-74** — Add unauthenticated `/v1/health` and `/v1/ready` endpoints with bounded status responses
- [ ] **FLAG-75** — Implement the shared error shape from `docs/API-CONTRACT.md` and test validation/server failures

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-18 — Database layer

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 2<br>
**Epic:** FLAG-2
**Learning Objective:** Python API & relational data

**Test Evidence:** `FLAG-18-T1` (success path) and `FLAG-18-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-76** — Configure SQLAlchemy
- [ ] **FLAG-77** — Create Alembic baseline
- [ ] **FLAG-78** — Implement DB session lifecycle

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-19 — Core schema

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 2<br>
**Epic:** FLAG-2
**Learning Objective:** Python API & relational data

**Test Evidence:** `FLAG-19-T1` (success path) and `FLAG-19-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-79** — Create projects/environments tables
- [ ] **FLAG-80** — Create feature_flags table
- [ ] **FLAG-81** — Add uniqueness/index constraints

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-20 — API tests

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 2<br>
**Epic:** FLAG-2
**Learning Objective:** Python API & relational data

**Test Evidence:** `FLAG-20-T1` (success path) and `FLAG-20-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-82** — Create pytest fixtures
- [ ] **FLAG-83** — Write CRUD integration tests
- [ ] **FLAG-84** — Test invalid-input responses against the shared API error contract

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 3 — Flag management & admin access

**Timing:** Outcome-based; no fixed duration

## FLAG-21 — Project/environment CRUD

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 3<br>
**Epic:** FLAG-3
**Learning Objective:** Flag management & admin access

**Test Evidence:** `FLAG-21-T1` (success path) and `FLAG-21-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-85** — Build create/list/update/delete endpoints
- [ ] **FLAG-86** — Validate environment keys
- [ ] **FLAG-87** — Document endpoint behavior

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-22 — Feature flag CRUD

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 3<br>
**Epic:** FLAG-3
**Learning Objective:** Flag management & admin access

**Test Evidence:** `FLAG-22-T1` (success path) and `FLAG-22-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-88** — Build create/list/update/delete
- [ ] **FLAG-89** — Add version incrementing
- [ ] **FLAG-90** — Add optimistic update protection

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-23 — Audit trail

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 3<br>
**Epic:** FLAG-3
**Learning Objective:** Flag management & admin access

**Test Evidence:** `FLAG-23-T1` (success path) and `FLAG-23-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-91** — Create audit_events table
- [ ] **FLAG-92** — Record mutations
- [ ] **FLAG-93** — Add audit read endpoint

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-24 — Admin authentication

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 3<br>
**Epic:** FLAG-3
**Learning Objective:** Flag management & admin access

**Test Evidence:** `FLAG-24-T1` (success path) and `FLAG-24-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-94** — Verify configured admin password and issue signed HttpOnly session cookie (ADR-018)
- [ ] **FLAG-95** — Enforce session, Origin, and CSRF checks on admin mutations
- [ ] **FLAG-96** — Test invalid password, expired session, CSRF failure, and authorized access

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 4 — Dashboard

**Timing:** Outcome-based; no fixed duration

## FLAG-25 — Astro/React shell

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 4<br>
**Epic:** FLAG-4
**Learning Objective:** Dashboard

**Test Evidence:** `FLAG-25-T1` (success path) and `FLAG-25-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-97** — Create dashboard layout
- [ ] **FLAG-98** — Add routing/navigation
- [ ] **FLAG-99** — Configure API client

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-26 — Project/environment UI

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 4<br>
**Epic:** FLAG-4
**Learning Objective:** Dashboard

**Test Evidence:** `FLAG-26-T1` (success path) and `FLAG-26-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-100** — Project list
- [ ] **FLAG-101** — Environment selector
- [ ] **FLAG-102** — Environment state/loading/error UI

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-27 — Flag management UI

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 4<br>
**Epic:** FLAG-4
**Learning Objective:** Dashboard

**Test Evidence:** `FLAG-27-T1` (success path) and `FLAG-27-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-103** — Flag table
- [ ] **FLAG-104** — Create/edit form
- [ ] **FLAG-105** — Enable/disable control

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-28 — Audit UX

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 4<br>
**Epic:** FLAG-4
**Learning Objective:** Dashboard

**Test Evidence:** `FLAG-28-T1` (success path) and `FLAG-28-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-106** — Audit history page
- [ ] **FLAG-107** — Before/after display
- [ ] **FLAG-108** — Error and empty states

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 5 — SDK & local evaluation

**Timing:** Outcome-based; no fixed duration

## FLAG-29 — SDK package

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 5<br>
**Epic:** FLAG-5
**Learning Objective:** SDK & local evaluation

**Test Evidence:** `FLAG-29-T1` (success path) and `FLAG-29-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-109** — Create package structure
- [ ] **FLAG-110** — Define the public SDK API against `docs/API-CONTRACT.md`
- [ ] **FLAG-111** — Add SDK contract tests for response parsing, API errors, and fallback

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-30 — Configuration bootstrap

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 5<br>
**Epic:** FLAG-5
**Learning Objective:** SDK & local evaluation

**Test Evidence:** `FLAG-30-T1` (success path) and `FLAG-30-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-112** — Implement config fetch
- [ ] **FLAG-113** — Validate config schema
- [ ] **FLAG-114** — Store immutable snapshot

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-31 — Evaluation engine

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 5<br>
**Epic:** FLAG-5
**Learning Objective:** SDK & local evaluation

**Test Evidence:** `FLAG-31-T1` (success path) and `FLAG-31-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-115** — Boolean evaluation
- [ ] **FLAG-116** — Default/fallback evaluation
- [ ] **FLAG-117** — Evaluation unit-test matrix

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-32 — Demo Store integration

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 5<br>
**Epic:** FLAG-5
**Learning Objective:** SDK & local evaluation

**Test Evidence:** `FLAG-32-T1` (success path) and `FLAG-32-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-118** — Integrate SDK in `apps/demo-store/src/components/FlaggedDemo.tsx`
- [ ] **FLAG-119** — Add `new_checkout` to the checkout page
- [ ] **FLAG-120** — Demonstrate a live switch without rebuilding the demo store
- [ ] **FLAG-205** — Use `new_product_card` on the product-list page
- [ ] **FLAG-206** — Use `holiday_banner` on the home page
- [ ] **FLAG-207** — Build Product detail and Cart pages and verify their navigation

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 6 — Isolation, rollouts & targeting

**Timing:** Outcome-based; no fixed duration

## FLAG-33 — Client keys

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 6<br>
**Epic:** FLAG-6
**Learning Objective:** Isolation, rollouts & targeting

**Test Evidence:** `FLAG-33-T1` (success path) and `FLAG-33-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-121** — Generate environment-scoped keys with `ff_client_` prefix and one-time display
- [ ] **FLAG-122** — Hash stored secrets
- [ ] **FLAG-123** — Build revoke flow

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-34 — Environment isolation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 6<br>
**Epic:** FLAG-6
**Learning Objective:** Isolation, rollouts & targeting

**Test Evidence:** `FLAG-34-T1` (success path) and `FLAG-34-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-124** — Prevent cross-environment reads
- [ ] **FLAG-125** — Test staging/production separation
- [ ] **FLAG-126** — Add SDK environment configuration

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-35 — Percentage rollout

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 6<br>
**Epic:** FLAG-6
**Learning Objective:** Isolation, rollouts & targeting

**Test Evidence:** `FLAG-35-T1` (success path) and `FLAG-35-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-127** — Implement stable hashing
- [ ] **FLAG-128** — Build 0/50/100% cases
- [ ] **FLAG-129** — Test deterministic user assignment

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-36 — Targeting rules

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 6<br>
**Epic:** FLAG-6
**Learning Objective:** Isolation, rollouts & targeting

**Test Evidence:** `FLAG-36-T1` (success path) and `FLAG-36-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-130** — Define v1 rule model
- [ ] **FLAG-131** — Implement equals/contains
- [ ] **FLAG-132** — Test rule precedence

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 7 — Refresh, caching & fallback

**Timing:** Outcome-based; no fixed duration

## FLAG-37 — In-memory configuration cache

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 7<br>
**Epic:** FLAG-7
**Learning Objective:** Refresh, caching & fallback

**Test Evidence:** `FLAG-37-T1` (success path) and `FLAG-37-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-133** — Atomic snapshot replacement
- [ ] **FLAG-134** — Track version/age
- [ ] **FLAG-135** — Expose cache diagnostics

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-38 — Polling

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 7<br>
**Epic:** FLAG-7
**Learning Objective:** Refresh, caching & fallback

**Test Evidence:** `FLAG-38-T1` (success path) and `FLAG-38-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-136** — Add polling scheduler
- [ ] **FLAG-137** — Handle timeouts/errors
- [ ] **FLAG-138** — Measure stale window

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-39 — HTTP cache optimization

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 7<br>
**Epic:** FLAG-7
**Learning Objective:** Refresh, caching & fallback

**Test Evidence:** `FLAG-39-T1` (success path) and `FLAG-39-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-139** — Implement ETag/version conditional requests
- [ ] **FLAG-140** — Test 304 behavior
- [ ] **FLAG-141** — Benchmark request reduction

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-40 — Redis experiment

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 7<br>
**Epic:** FLAG-7
**Learning Objective:** Refresh, caching & fallback

**Test Evidence:** `FLAG-40-T1` (success path) and `FLAG-40-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-142** — Run the optional Redis experiment with a local-only container; do not use managed Memorystore
- [ ] **FLAG-143** — Implement the shared-cache adapter for the local experiment only; the default evaluation path remains the SDK memory snapshot
- [ ] **FLAG-144** — Compare local Redis with in-process caching and document when it helps

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 8 — SSE & consistency

**Timing:** Outcome-based; no fixed duration

## FLAG-41 — SSE stream

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 8<br>
**Epic:** FLAG-8
**Learning Objective:** SSE & consistency

**Test Evidence:** `FLAG-41-T1` (success path) and `FLAG-41-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-145** — Create stream endpoint
- [ ] **FLAG-146** — Define event schema
- [ ] **FLAG-147** — Handle client disconnects

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-42 — SDK stream client

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 8<br>
**Epic:** FLAG-8
**Learning Objective:** SSE & consistency

**Test Evidence:** `FLAG-42-T1` (success path) and `FLAG-42-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-148** — Connect to SSE
- [ ] **FLAG-149** — Update snapshot from events
- [ ] **FLAG-150** — Add stream status diagnostics

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-43 — Reconnect behavior

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 8<br>
**Epic:** FLAG-8
**Learning Objective:** SSE & consistency

**Test Evidence:** `FLAG-43-T1` (success path) and `FLAG-43-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-151** — Exponential backoff
- [ ] **FLAG-152** — Catch-up bootstrap
- [ ] **FLAG-153** — Test connection interruption

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-44 — Consistency controls

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 8<br>
**Epic:** FLAG-8
**Learning Objective:** SSE & consistency

**Test Evidence:** `FLAG-44-T1` (success path) and `FLAG-44-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-154** — Reject stale versions
- [ ] **FLAG-155** — Handle duplicates
- [ ] **FLAG-156** — Test out-of-order events

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 9 — Observability & resilience

**Timing:** Outcome-based; no fixed duration

## FLAG-45 — Structured observability

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 9<br>
**Epic:** FLAG-9
**Learning Objective:** Observability & resilience

**Test Evidence:** `FLAG-45-T1` (success path) and `FLAG-45-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-157** — Add request logs
- [ ] **FLAG-158** — Add evaluation telemetry
- [ ] **FLAG-159** — Add propagation metrics

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-46 — Tracing/metrics

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 9<br>
**Epic:** FLAG-9
**Learning Objective:** Observability & resilience

**Test Evidence:** `FLAG-46-T1` (success path) and `FLAG-46-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-160** — Instrument service boundaries
- [ ] **FLAG-161** — Expose latency metrics
- [ ] **FLAG-162** — Measure propagation delay

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-47 — Failure injection

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 9<br>
**Epic:** FLAG-9
**Learning Objective:** Observability & resilience

**Test Evidence:** `FLAG-47-T1` (success path) and `FLAG-47-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-163** — Break database
- [ ] **FLAG-164** — Break stream connection
- [ ] **FLAG-165** — Test stale-cache fallback

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-48 — Load testing

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 9<br>
**Epic:** FLAG-9
**Learning Objective:** Observability & resilience

**Test Evidence:** `FLAG-48-T1` (success path) and `FLAG-48-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-166** — Create Locust scenarios
- [ ] **FLAG-167** — Measure p50/p95/p99
- [ ] **FLAG-168** — Write performance report

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 10 — GCP & Terraform foundations

**Timing:** Outcome-based; no fixed duration

## FLAG-49 — Cost guardrails

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 10<br>
**Epic:** FLAG-10
**Learning Objective:** GCP & Terraform foundations

**Test Evidence:** `FLAG-49-T1` (success path) and `FLAG-49-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-169** — Review current pricing and billing, then configure a budget/alert before any optional provisioning; document that alerts are not spend caps
- [ ] **FLAG-170** — Record quotas as unverified until re-checked; do not rely on free-tier assumptions
- [ ] **FLAG-171** — Write and validate the resource cleanup checklist before any approved provisioning

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-50 — Terraform foundation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 10<br>
**Epic:** FLAG-10
**Learning Objective:** GCP & Terraform foundations

**Test Evidence:** `FLAG-50-T1` (success path) and `FLAG-50-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-172** — Create provider/module layout
- [ ] **FLAG-173** — Document local state by default and optional GCS state cost, locking, access, and cleanup
- [ ] **FLAG-174** — Add variables/outputs
- [ ] **FLAG-208** — Set Cloud Run minimum instances to 0 in the Terraform default

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-51 — Artifact Registry

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 10<br>
**Epic:** FLAG-10
**Learning Objective:** GCP & Terraform foundations

**Test Evidence:** `FLAG-51-T1` (success path) and `FLAG-51-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-175** — Define optional Artifact Registry resource; do not apply by default
- [ ] **FLAG-176** — Build container locally
- [ ] **FLAG-177** — Document image push and cleanup; execute only after explicit cloud approval

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-52 — Cloud Run foundation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 10<br>
**Epic:** FLAG-10
**Learning Objective:** GCP & Terraform foundations

**Test Evidence:** `FLAG-52-T1` (success path) and `FLAG-52-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-178** — Validate a stateless API plan without applying; set Cloud Run minimum instances to 0
- [ ] **FLAG-179** — Configure environment variables
- [ ] **FLAG-180** — Verify Cloud Run minimum instances = 0 and scale-to-zero configuration in Terraform

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 11 — Cloud data, events & IAM

**Timing:** Outcome-based; no fixed duration

## FLAG-53 — Firestore adapter

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 11<br>
**Epic:** FLAG-11
**Learning Objective:** Cloud data, events & IAM

**Test Evidence:** `FLAG-53-T1` (success path) and `FLAG-53-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-181** — Map local domain to documents
- [ ] **FLAG-182** — Implement repository methods
- [ ] **FLAG-183** — Run parity tests vs PostgreSQL

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-54 — Pub/Sub propagation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 11<br>
**Epic:** FLAG-11
**Learning Objective:** Cloud data, events & IAM

**Test Evidence:** `FLAG-54-T1` (success path) and `FLAG-54-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-184** — Create topic/subscription
- [ ] **FLAG-185** — Publish configuration events
- [ ] **FLAG-186** — Consume and handle duplicates

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-55 — GCP IAM

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 11<br>
**Epic:** FLAG-11
**Learning Objective:** Cloud data, events & IAM

**Test Evidence:** `FLAG-55-T1` (success path) and `FLAG-55-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-187** — Create least-privilege runtime identity
- [ ] **FLAG-188** — Limit Firestore permissions
- [ ] **FLAG-189** — Limit Pub/Sub permissions

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-56 — Cloud observability

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 11<br>
**Epic:** FLAG-11
**Learning Objective:** Cloud data, events & IAM

**Test Evidence:** `FLAG-56-T1` (success path) and `FLAG-56-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-190** — Configure useful logs
- [ ] **FLAG-191** — Validate log volume
- [ ] **FLAG-192** — Create basic operational dashboard/queries

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 12 — CI/CD & finalization

**Timing:** Outcome-based; no fixed duration

## FLAG-57 — GitHub Actions CI

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 12<br>
**Epic:** FLAG-12
**Learning Objective:** CI/CD & finalization

**Test Evidence:** `FLAG-57-T1` (success path) and `FLAG-57-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-193** — Lint and type-check workflow
- [ ] **FLAG-194** — Unit and integration test workflow
- [ ] **FLAG-195** — Build artifact workflow
- [ ] **FLAG-209** — Run the consistency checker locally and in the optional hosted CI gate

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-58 — Deployment workflow

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 12<br>
**Epic:** FLAG-12
**Learning Objective:** CI/CD & finalization

**Test Evidence:** `FLAG-58-T1` (success path) and `FLAG-58-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-196** — Document optional Cloud Run deployment from a trusted branch; deploy only after explicit approval and the cost gate
- [ ] **FLAG-197** — Use environment configuration
- [ ] **FLAG-198** — Add rollback procedure

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-59 — End-to-end validation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 12<br>
**Epic:** FLAG-12
**Learning Objective:** CI/CD & finalization

**Test Evidence:** `FLAG-59-T1` (success path) and `FLAG-59-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-199** — Test cloud SDK bootstrap
- [ ] **FLAG-200** — Test Pub/Sub/SSE propagation
- [ ] **FLAG-201** — Test failure fallback

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FLAG-60 — Final engineering package

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3<br>
**Sprint:** Sprint 12<br>
**Epic:** FLAG-12
**Learning Objective:** CI/CD & finalization

**Test Evidence:** `FLAG-60-T1` (success path) and `FLAG-60-T2` (failure path); name the implemented test file when the test is added.

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FLAG-202** — Review ADRs
- [ ] **FLAG-203** — Write architecture/benchmark report
- [ ] **FLAG-204** — Record final demo and retrospective

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
