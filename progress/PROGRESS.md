# Flagged - 60-Session Progress Tracker

This checklist is derived from the canonical `progress/DAILY-PLAN.md`. Mark a session complete only after its goal, test evidence, and actual commit/reference are recorded. These are working sessions, not calendar days.

## Sessions

### Sprint 1 - Domain and local foundation
- [ ] **Session 01** - Define the feature-flag problem, glossary, deployment-versus-release distinction, and project scope
- [ ] **Session 02** - Study feature-flag concepts and OpenFeature/commercial reference models; record what is in and out of scope
- [ ] **Session 03** - Sketch the initial control-plane/data-plane architecture and explain why evaluation is local
- [ ] **Session 04** - Bootstrap the repository structure and local Python/frontend/SDK tooling
- [ ] **Session 05** - Create the Docker Compose foundation and verify that the local database can be started, stopped, and recreated

### Sprint 2 - API and relational data foundation
- [ ] **Session 06** - Create the FastAPI application shell and health/readiness endpoints
- [ ] **Session 07** - Define request validation and a consistent API error contract
- [ ] **Session 08** - Connect SQLAlchemy and establish a clear database-session lifecycle
- [ ] **Session 09** - Add Alembic migrations and test applying them to a clean database
- [ ] **Session 10** - Define the initial project/environment/flag schema, constraints, and indexes

### Sprint 3 - Flag control plane and admin access
- [ ] **Session 11** - Implement project, environment, and feature-flag CRUD
- [ ] **Session 12** - Add flag edit-version checks to prevent lost updates
- [ ] **Session 13** - Record audit events with before/after state in the same transaction as mutations
- [ ] **Session 14** - Implement the single-operator admin authentication in ADR-018
- [ ] **Session 15** - Test authorized, unauthorized, invalid, conflicting, and failure cases

### Sprint 4 - Admin dashboard
- [ ] **Session 16** - Create the Astro/React application shell and navigation
- [ ] **Session 17** - Build project and environment views with loading, empty, and error states
- [ ] **Session 18** - Build flag list/create/edit/toggle workflows
- [ ] **Session 19** - Display audit history and before/after values
- [ ] **Session 20** - Harden forms, input validation, accessibility, and browser error behavior

### Sprint 5 - SDK and first local end-to-end behavior
- [ ] **Session 21** - Define the public TypeScript SDK contract before implementation
- [ ] **Session 22** - Fetch and validate configuration during SDK bootstrap
- [ ] **Session 23** - Store an immutable in-memory configuration snapshot
- [ ] **Session 24** - Implement boolean evaluation and caller-provided fallback behavior
- [ ] **Session 25** - Integrate the SDK at `apps/demo-store/src/components/FlaggedDemo.tsx` and demonstrate a live flag change

### Sprint 6 - Isolation, rollout, and targeting
- [ ] **Session 26** - Design environment-scoped, read-only SDK client keys and their revocation flow
- [ ] **Session 27** - Enforce project/environment isolation at the API boundary
- [ ] **Session 28** - Implement and test deterministic percentage bucketing
- [ ] **Session 29** - Define and implement the intentionally small targeting-rule set
- [ ] **Session 30** - Document precedence and exercise a table-driven evaluation matrix

### Sprint 7 - Refresh, cache, and stale behavior
- [ ] **Session 31** - Expose SDK configuration revision/age diagnostics
- [ ] **Session 32** - Implement configurable polling and test timeout/server-error behavior
- [ ] **Session 33** - Add conditional HTTP requests using ETags or revision hints
- [ ] **Session 34** - Define and test last-known-good fallback behavior
- [ ] **Session 35** - Run an optional local Redis experiment comparing per-process and shared caching; document whether it helps

### Sprint 8 - Streaming and consistency
- [ ] **Session 36** - Learn SSE's long-lived HTTP connection model and build a minimal local proof of concept
- [ ] **Session 37** - Implement an update stream with a documented event schema and disconnect handling
- [ ] **Session 38** - Consume stream events from the SDK and expose connection diagnostics
- [ ] **Session 39** - Add bounded reconnect/backoff and a catch-up fetch after reconnect
- [ ] **Session 40** - Test duplicate and out-of-order revisions and prove the SDK never moves backward

### Sprint 9 - Observability, resilience, and measurement
- [ ] **Session 41** - Add structured logs without credentials or other sensitive values
- [ ] **Session 42** - Instrument refresh/evaluation boundaries and expose useful local metrics
- [ ] **Session 43** - Measure configuration-change-to-client-update propagation
- [ ] **Session 44** - Inject local database/API/stream failures and record the actual fallback behavior
- [ ] **Session 45** - Run a resource-bounded load test and report percentiles, throughput, and errors

### Sprint 10 - GCP and Terraform foundations
- [ ] **Session 46** - Review the cost boundary, billing requirements, resource ownership, and teardown plan
- [ ] **Session 47** - Create Terraform configuration and run formatting, initialization as appropriate, validation, and static checks without applying it
- [ ] **Session 48** - Build and run the container locally; document Artifact Registry image lifecycle
- [ ] **Session 49** - Configure and validate a Cloud Run deployment plan with scale-to-zero intent, without deploying it
- [ ] **Session 50** - Study Cloud Run logs and operations through local equivalents; document what remains cloud-specific

### Sprint 11 - Document data, events, and IAM
- [ ] **Session 51** - Map the relational domain to Firestore documents and explain query/transaction trade-offs
- [ ] **Session 52** - Test the repository contract against a Firestore emulator or local adapter
- [ ] **Session 53** - Publish configuration-change events through a Pub/Sub emulator or local event-bus adapter
- [ ] **Session 54** - Consume duplicate events idempotently and connect event revision to the SDK catch-up path
- [ ] **Session 55** - Design least-privilege IAM policies and cloud observability without creating live resources

### Sprint 12 - CI/CD design and final engineering package
- [ ] **Session 56** - Run lint, unit/integration tests, and builds locally; design optional hosted CI without enabling it by default
- [ ] **Session 57** - Document a controlled deployment and rollback workflow; do not deploy without explicit approval
- [ ] **Session 58** - Validate the end-to-end local path from dashboard through API and SDK, including propagation and failure fallback
- [ ] **Session 59** - Compare benchmark results with the earlier baseline and update the architecture evolution record
- [ ] **Session 60** - Present the demo, security/cost walkthrough, ADR review, and learning retrospective

## ADR tracker

ADR status remains Proposed until the decision is implemented and verified as required by `AGENTS.md`.
- [ ] ADR-001: Local-first development and cloud-later migration - Proposed
- [ ] ADR-002: Modular monolith before microservices - Proposed
- [ ] ADR-003: Python + FastAPI for the control plane - Proposed
- [ ] ADR-004: Astro + React for dashboard and demo app - Proposed
- [ ] ADR-005: PostgreSQL as local source of truth - Proposed
- [ ] ADR-006: Firestore as an optional cloud persistence experiment - Proposed
- [ ] ADR-007: Persistence repository boundary - Proposed
- [ ] ADR-008: Evaluate feature flags in the SDK - Proposed
- [ ] ADR-009: Polling before SSE before Pub/Sub - Proposed
- [ ] ADR-010: Environment-wide configuration revisions - Proposed
- [ ] ADR-011: Deterministic hashing for percentage rollouts - Proposed
- [ ] ADR-012: Scoped read-only client keys - Proposed
- [ ] ADR-013: Do not require managed Redis - Proposed
- [ ] ADR-014: Cloud Run for stateless application hosting - Proposed
- [ ] ADR-015: Terraform for infrastructure - Proposed
- [ ] ADR-016: GitHub Actions for CI/CD - Proposed
- [ ] ADR-017: Observability is a core requirement - Proposed
- [ ] ADR-018: Single-operator admin authentication - Proposed
- [ ] ADR-019: Configuration revision and flag edit-version semantics - Proposed
- [ ] ADR-020: Rule precedence and deterministic rollout bucketing - Proposed
- [ ] ADR-021: SSE delivery across stateless instances - Proposed
- [ ] ADR-022: SDK payload and client-visible configuration - Proposed
- [ ] ADR-023: Repository structure - Proposed

## Cost safety checklist

- [ ] Default development, testing, and cloud-learning path uses local services, emulators, or adapters.
- [ ] No live cloud resource is required for sprint completion.
- [ ] `terraform apply` and paid hosted workflows remain disabled unless explicitly approved.
- [ ] Before an approved live experiment, current pricing/billing prerequisites, resource limits, and cleanup steps are documented.
- [ ] Free quotas, budgets, and alerts are not treated as spending caps.
- [ ] Resources and data from any explicitly approved experiment are cleaned up and deletion is verified.

## Sprint evidence

For each sprint, record the outcome, what was learned, failures and their causes, verification evidence, remaining risks, and the actual commit or reference.
