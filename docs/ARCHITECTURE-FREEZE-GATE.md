# Architecture freeze gate

## Purpose and status vocabulary

A freeze-gate review is a scoped pre-milestone check. It looks for contradictions, decisions that are costly to reverse, security and failure gaps, missing evidence, and cost exposure before implementation starts. It answers two separate questions:

1. Is the project ready to begin this specific milestone?
2. Is the architecture frozen across all planned milestones?

A **Go** for one milestone does not mean the whole architecture is frozen.

ADR status records implementation evidence, not planning approval:

- **Proposed** — decision is under consideration, planned, or being implemented; verification is incomplete.
- **Accepted** — implementation was delivered and relevant behavior was tested and verified in the milestone. Link the evidence.
- **Superseded by ADR-XXX** — a later verified decision replaced it; preserve the original record.

Do not mark a decision Accepted merely because its prose was reviewed, its alternatives were discussed, or a proposed algorithm's standalone examples passed.

## Repeatable checklist

Run this checklist before the first implementation task in a milestone that crosses a persistence, evaluation, propagation, authentication, SDK/API, deployment, or repository boundary. Record **Pass**, **Block**, or **Defer** for each item and link evidence.

### A. Scope and decision ownership

- [ ] Name the milestone and the exact implementation scope.
- [ ] Identify applicable PRD requirements, backlog stories, ADRs, and owners of each contract.
- [ ] Confirm every Tier 1 decision touched by this milestone has one clear source of truth.
- [ ] Confirm Proposed decisions are not described elsewhere as implemented or Accepted.
- [ ] List decisions intentionally deferred to later milestones and explain why the current work does not depend on them.

### B. Consistency and contract

- [ ] Compare README, PRD, DATA, ARCHITECTURE, SYSTEM-DESIGN, SECURITY, API contract, ADRs, and milestone plan for conflicting terms, fields, routes, defaults, and version semantics.
- [ ] Confirm persistence models, request/response shapes, and public SDK behavior agree.
- [ ] For distributed behavior, document ordering, concurrency, retries, duplicate delivery, outage, recovery, and last-known-good behavior.
- [ ] Ensure each breaking public API/SDK change has a versioning and compatibility plan.
- [ ] Define measurable acceptance tests for the exact behavior, not just a proxy or document review.

### C. Security and privacy

- [ ] Identify trust boundaries, credentials, authorization scope, and public/browser-visible data.
- [ ] Confirm secrets and personal/sensitive data are excluded from client payloads, logs, and source control.
- [ ] Define failure behavior for invalid, expired, revoked, cross-scope, and malformed credentials.
- [ ] Identify abuse controls appropriate to the milestone, including request limits and oversized input/payload behavior.

### D. Data and concurrency

- [ ] Identify the source of truth and all derived caches/projections.
- [ ] Define atomic write boundaries, revision/version semantics, uniqueness, deletion/recreation behavior, and consistent reads.
- [ ] Confirm adapters can provide the required transaction and query semantics; document adapter-specific limits.
- [ ] Define migration, rollback, and recovery behavior where applicable.

### E. Cost and operational safety

- [ ] Confirm the default development/test path is local and does not provision cloud resources or incur cloud-service charges.
- [ ] For optional live services, identify every resource, database/location, billable operation, workload assumption, quota, and cleanup path.
- [ ] Verify current official pricing, eligibility, and billing prerequisites immediately before live use; quotas and budgets are not spending caps.
- [ ] Obtain explicit user approval before any live provisioning or paid hosted workflow.
- [ ] Define observable signals and a failure/runbook path for new distributed behavior.

### F. Evidence and readiness decision

- [ ] Run focused tests, format/lint/type checks, and documentation/contract checks appropriate to the change.
- [ ] Record measurements for capacity, propagation, or read/write-cost claims that affect the decision.
- [ ] Keep ADR status Proposed until implementation verification exists; link test/build/deployment evidence when accepting it.
- [ ] Record the result as **Go**, **Go with explicit deferrals**, or **No-Go**, with blockers and scope.

## Current review

**Review date:** 2026-10-30

**Repository state reviewed:** planning/documentation baseline; no application, SDK, infrastructure, or test implementation directories are present.

**Overall architecture freeze:** **No-Go**

**Milestone 1 planning/local foundation:** **Go with deferrals**

**API/backend implementation:** **No-Go pending contract and data-model reconciliation**

**Live cloud implementation:** **No-Go; optional and requires a separate cost review and explicit approval**

### Results

| Area | Result | Evidence / next action |
|---|---|---|
| Mission, technology direction, local-first and cloud cost gate | Pass for planning | See [AGENTS.md](../AGENTS.md), [README.md](../README.md), and [COST-BOUNDARY.md](../COST-BOUNDARY.md). No live resources are required. |
| ADR lifecycle | Corrected; no implementation accepted | ADR-001 through ADR-022 are Proposed. The earlier Accepted labels on ADR-001–018 described decisions but had no implementation evidence in this repository; they were changed to Proposed without changing their decision text. |
| Environment revision vs. per-flag edit version | Proposed; contract drafted | ADR-019 covers atomic revision changes, consistent bootstrap reads, deletion, and key reuse. API request/response behavior is in draft [API-CONTRACT.md](API-CONTRACT.md). Needs implementation tests during its milestone. |
| Rule precedence and rollout | Proposed; standalone vectors verified | ADR-020 defines deterministic behavior and integer basis points. Python and TypeScript reference checks matched its listed vectors, but there is no SDK or backend implementation. |
| Browser payload/security boundary | Proposed | ADR-022 lists public fields, omits disabled rules/admin data, defines snapshot limits, and excludes variant payloads from the first implementation milestone. Confirm this against the approved API and actual evaluator before implementation. |
| API contract | Block for backend/API implementation | [API-CONTRACT.md](API-CONTRACT.md) is a draft. Review route completeness, concurrency/error behavior, login/CSRF flow, pagination consistency, and OpenAPI shape before implementation. |
| PostgreSQL local persistence | Defer implementation details to local-data milestone | DATA.md describes relational entities, but the API contract and implementation must settle constraints, migrations, audit atomicity, and consistent reads. |
| Firestore SDK snapshot read model | Block for Firestore milestone; defer now | API-CONTRACT proposes a materialized snapshot document but this is not accepted. Validate its atomic projection maintenance, document-size accounting, key-revocation lookup, and actual read/write costs before implementing a Firestore adapter. |
| Firestore quota/cost | Pass for planning only; no live approval | COST-BOUNDARY records the official pricing-page check on 2026-10-30 and requires re-verification. The API-contract example workload can exceed the nominal daily free read quota. Do not treat free quotas as guarantees. |
| Cross-instance SSE | Proposed; no implementation evidence | ADR-021 defines database-backed revision polling, reconnect/full snapshot refresh, 5-minute lifetime, and 20-second heartbeat. Its local interval and live Firestore interval are different; measure behavior and reads when the milestone is built. |
| Diagrams, dependency/license register, runbooks, benchmarks | Partial | [TECHNICAL-DESIGN.md](TECHNICAL-DESIGN.md) now provides planning-draft diagrams. They are not verified implementation views; dependency/license records, runbooks, and benchmarks should be added with the milestones they describe rather than guessed in advance. |
| Freeze-gate automation and test evidence | Not ready globally | No application, SDK, infrastructure, or test tree exists in the current repository. Add focused tests and CI as implementation arrives. |

### Explicitly deferred decisions

- **Firestore materialized snapshot:** decide at the Firestore adapter milestone. The proposed single-document projection would make endpoint reads predictable but adds a derived write model and consistency work.
- **Live Firestore polling interval and budget:** 60 seconds is only a planning default for a separately approved experiment. Recalculate from measured active streams, snapshots, key validation/revocation needs, and all other database activity.
- **Variant payload/schema:** outside the first implementation milestone. Define its persisted and wire format before exposing variant evaluation.
- **OpenAPI generation and contract tests:** establish when the local API contract is reviewed and backend work starts; keep the API draft non-normative until then.
- **Production capacity and deployment settings:** the documented figures are learning/test targets, not production guarantees.

### Immediate next-gate conditions

Before Milestone 2 API/backend implementation:

1. Review and resolve the API contract's proposed Firestore projection without making it a dependency of local PostgreSQL.
2. Align API routes/resource shapes, authentication flows, error codes, optimistic concurrency, and conditional requests with the PRD, DATA, SECURITY, ADRs, and sprint stories.
3. Decide the local persistence transaction boundaries and test plan for project/environment/flag/rule changes, audit records, per-flag versions, and environment revisions.
4. Generate or maintain an OpenAPI 3.1 contract and validate example requests/responses against it.

Before the Firestore/cloud-data milestone, run a separate gate with current official pricing, exact resource inventory, measured read/write pattern, transaction/document-size constraints, rollback/cleanup steps, and explicit user approval. Until then, use PostgreSQL locally and Firestore emulator/local adapters only.
