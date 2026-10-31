# Flagged - 60-Session Execution Plan

**Canonical plan:** 60 working sessions over 12 weeks; 12 sprints x 5 sessions. These are suggested work sessions, not calendar dates or a deadline.

Each numbered session has one goal, one verification line, and a proposed focused commit message. Run the smallest relevant local check; for design/documentation sessions, record the consistency review or other repeatable evidence instead. Never claim a test passed unless it was run.

## Sprint/session map

| Sprint | Sessions | Focus |
|---:|---:|---|
| 1 | 1-5 | — Domain and local foundation |
| 2 | 6-10 | — API and relational data foundation |
| 3 | 11-15 | — Flag control plane and admin access |
| 4 | 16-20 | — Admin dashboard |
| 5 | 21-25 | — SDK and first local end-to-end behavior |
| 6 | 26-30 | — Isolation, rollout, and targeting |
| 7 | 31-35 | — Refresh, cache, and stale behavior |
| 8 | 36-40 | — Streaming and consistency |
| 9 | 41-45 | — Observability, resilience, and measurement |
| 10 | 46-50 | — GCP and Terraform foundations |
| 11 | 51-55 | — Document data, events, and IAM |
| 12 | 56-60 | — CI/CD design and final engineering package |

## Sprint 1 - Domain and local foundation

**Outcome:** Explain the product and its control/data-plane boundary, and reproduce the starting local environment.

### Session 01 - Define the feature-flag problem, glossary, deployment-versus-release distinction, and project scope.

**Goal:** Define the feature-flag problem, glossary, deployment-versus-release distinction, and project scope.
**Test:** `S01-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** architecture sketch, clean setup instructions, and a successful local environment recreation.
**Commit:** `docs(sprint-1): define-the-feature-flag-problem-glossary`

### Session 02 - Study feature-flag concepts and OpenFeature/commercial reference models; record what is in and out of scope.

**Goal:** Study feature-flag concepts and OpenFeature/commercial reference models; record what is in and out of scope.
**Test:** `S01-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** architecture sketch, clean setup instructions, and a successful local environment recreation.
**Commit:** `docs(sprint-1): study-feature-flag-concepts-and`

### Session 03 - Sketch the initial control-plane/data-plane architecture and explain why evaluation is local.

**Goal:** Sketch the initial control-plane/data-plane architecture and explain why evaluation is local.
**Test:** `S01-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** architecture sketch, clean setup instructions, and a successful local environment recreation.
**Commit:** `docs(sprint-1): sketch-the-initial-control-plane-data`

### Session 04 - Bootstrap the repository structure and local Python/frontend/SDK tooling.

**Goal:** Bootstrap the repository structure and local Python/frontend/SDK tooling.
**Test:** `S01-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** architecture sketch, clean setup instructions, and a successful local environment recreation.
**Commit:** `feat(sprint-1): bootstrap-the-repository-structure-and`

### Session 05 - Create the Docker Compose foundation and verify that the local database can be started, stopped, and recreated.

**Goal:** Create the Docker Compose foundation and verify that the local database can be started, stopped, and recreated.
**Test:** `S01-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** architecture sketch, clean setup instructions, and a successful local environment recreation.
**Commit:** `test(sprint-1): create-the-docker-compose-foundation-and`


## Sprint 2 - API and relational data foundation

**Outcome:** Build a tested FastAPI and PostgreSQL foundation with repeatable schema changes.

### Session 06 - Create the FastAPI application shell and health/readiness endpoints.

**Goal:** Create the FastAPI application shell and health/readiness endpoints.
**Test:** `S02-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** automated API/database tests and a clean migration run.
**Commit:** `feat(sprint-2): create-the-fastapi-application-shell-and`

### Session 07 - Implement request validation and the shared error contract from `docs/API-CONTRACT.md`.

**Goal:** Implement request validation and the shared error contract from `docs/API-CONTRACT.md`.
**Test:** `S02-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** automated API/database tests and a clean migration run.
**Commit:** `docs(sprint-2): define-request-validation-and-a-consistent`

### Session 08 - Connect SQLAlchemy and establish a clear database-session lifecycle.

**Goal:** Connect SQLAlchemy and establish a clear database-session lifecycle.
**Test:** `S02-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** automated API/database tests and a clean migration run.
**Commit:** `feat(sprint-2): connect-sqlalchemy-and-establish-a-clear`

### Session 09 - Add Alembic migrations and test applying them to a clean database.

**Goal:** Add Alembic migrations and test applying them to a clean database.
**Test:** `S02-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** automated API/database tests and a clean migration run.
**Commit:** `test(sprint-2): add-alembic-migrations-and-test-applying`

### Session 10 - Define the initial project/environment/flag schema, constraints, and indexes.

**Goal:** Define the initial project/environment/flag schema, constraints, and indexes.
**Test:** `S02-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** automated API/database tests and a clean migration run.
**Commit:** `docs(sprint-2): define-the-initial-project-environment`


## Sprint 3 - Flag control plane and admin access

**Outcome:** Manage flags through a protected API and retain an auditable history of changes.

### Session 11 - Implement project, environment, and feature-flag CRUD.

**Goal:** Implement project, environment, and feature-flag CRUD.
**Test:** `S03-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** API tests show successful changes are audited atomically and stale edits are rejected.
**Commit:** `feat(sprint-3): implement-project-environment-and-feature`

### Session 12 - Add flag edit-version checks to prevent lost updates.

**Goal:** Add flag edit-version checks to prevent lost updates.
**Test:** `S03-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** API tests show successful changes are audited atomically and stale edits are rejected.
**Commit:** `feat(sprint-3): add-flag-edit-version-checks-to-prevent`

### Session 13 - Record audit events with before/after state in the same transaction as mutations.

**Goal:** Record audit events with before/after state in the same transaction as mutations.
**Test:** `S03-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** API tests show successful changes are audited atomically and stale edits are rejected.
**Commit:** `docs(sprint-3): record-audit-events-with-before-after`

### Session 14 - Implement the single-operator admin authentication in ADR-018.

**Goal:** Implement the single-operator admin authentication in ADR-018.
**Test:** `S03-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** API tests show successful changes are audited atomically and stale edits are rejected.
**Commit:** `feat(sprint-3): implement-the-single-operator-admin`

### Session 15 - Test authorized, unauthorized, invalid, conflicting, and failure cases.

**Goal:** Test authorized, unauthorized, invalid, conflicting, and failure cases.
**Test:** `S03-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** API tests show successful changes are audited atomically and stale edits are rejected.
**Commit:** `test(sprint-3): test-authorized-unauthorized-invalid`


## Sprint 4 - Admin dashboard

**Outcome:** Operate the local control plane through a usable browser dashboard.

### Session 16 - Create the Astro/React application shell and navigation.

**Goal:** Create the Astro/React application shell and navigation.
**Test:** `S04-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a browser walkthrough of the admin workflows and relevant component/API tests.
**Commit:** `feat(sprint-4): create-the-astro-react-application-shell`

### Session 17 - Build project and environment views with loading, empty, and error states.

**Goal:** Build project and environment views with loading, empty, and error states.
**Test:** `S04-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a browser walkthrough of the admin workflows and relevant component/API tests.
**Commit:** `feat(sprint-4): build-project-and-environment-views-with`

### Session 18 - Build flag list/create/edit/toggle workflows.

**Goal:** Build flag list/create/edit/toggle workflows.
**Test:** `S04-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a browser walkthrough of the admin workflows and relevant component/API tests.
**Commit:** `feat(sprint-4): build-flag-list-create-edit-toggle`

### Session 19 - Display audit history and before/after values.

**Goal:** Display audit history and before/after values.
**Test:** `S04-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a browser walkthrough of the admin workflows and relevant component/API tests.
**Commit:** `feat(sprint-4): display-audit-history-and-before-after`

### Session 20 - Harden forms, input validation, accessibility, and browser error behavior.

**Goal:** Harden forms, input validation, accessibility, and browser error behavior.
**Test:** `S04-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a browser walkthrough of the admin workflows and relevant component/API tests.
**Commit:** `feat(sprint-4): harden-forms-input-validation`


## Sprint 5 - SDK and first local end-to-end behavior

**Outcome:** Change a flag in the control plane and observe the demo app respond without rebuilding it.

### Session 21 - Define the public TypeScript SDK contract before implementation.

**Goal:** Define the public TypeScript SDK contract before implementation.
**Test:** `S05-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** end-to-end local demonstration, unit/integration tests, and a documented unavailable-API fallback.
**Commit:** `docs(sprint-5): define-the-public-typescript-sdk-contract`

### Session 22 - Fetch and validate configuration during SDK bootstrap.

**Goal:** Fetch and validate configuration during SDK bootstrap.
**Test:** `S05-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** end-to-end local demonstration, unit/integration tests, and a documented unavailable-API fallback.
**Commit:** `test(sprint-5): fetch-and-validate-configuration-during`

### Session 23 - Store an immutable in-memory configuration snapshot.

**Goal:** Store an immutable in-memory configuration snapshot.
**Test:** `S05-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** end-to-end local demonstration, unit/integration tests, and a documented unavailable-API fallback.
**Commit:** `feat(sprint-5): store-an-immutable-in-memory-configuration`

### Session 24 - Implement boolean evaluation and caller-provided fallback behavior.

**Goal:** Implement boolean evaluation and caller-provided fallback behavior.
**Test:** `S05-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** end-to-end local demonstration, unit/integration tests, and a documented unavailable-API fallback.
**Commit:** `feat(sprint-5): implement-boolean-evaluation-and-caller`

### Session 25 - Integrate the SDK at `apps/demo-store/src/components/FlaggedDemo.tsx` and demonstrate a live flag change.

**Goal:** Integrate the SDK at `apps/demo-store/src/components/FlaggedDemo.tsx` and demonstrate a live flag change.
**Test:** `S05-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** end-to-end local demonstration, unit/integration tests, and a documented unavailable-API fallback.
**Commit:** `feat(sprint-5): integrate-the-sdk-at-apps-demo-store-src`


## Sprint 6 - Isolation, rollout, and targeting

**Outcome:** Deliver the correct environment configuration and evaluate deterministic user assignment.

### Session 26 - Design environment-scoped, read-only SDK client keys and their revocation flow.

**Goal:** Design environment-scoped, read-only SDK client keys and their revocation flow.
**Test:** `S06-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** tests for revoked keys, environment separation, stable user assignment, and rule precedence.
**Commit:** `feat(sprint-6): design-environment-scoped-read-only-sdk`

### Session 27 - Enforce project/environment isolation at the API boundary.

**Goal:** Enforce project/environment isolation at the API boundary.
**Test:** `S06-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** tests for revoked keys, environment separation, stable user assignment, and rule precedence.
**Commit:** `feat(sprint-6): enforce-project-environment-isolation-at`

### Session 28 - Implement and test deterministic percentage bucketing.

**Goal:** Implement and test deterministic percentage bucketing.
**Test:** `S06-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** tests for revoked keys, environment separation, stable user assignment, and rule precedence.
**Commit:** `test(sprint-6): implement-and-test-deterministic`

### Session 29 - Define and implement the intentionally small targeting-rule set.

**Goal:** Define and implement the intentionally small targeting-rule set.
**Test:** `S06-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** tests for revoked keys, environment separation, stable user assignment, and rule precedence.
**Commit:** `docs(sprint-6): define-and-implement-the-intentionally`

### Session 30 - Document precedence and exercise a table-driven evaluation matrix.

**Goal:** Document precedence and exercise a table-driven evaluation matrix.
**Test:** `S06-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** tests for revoked keys, environment separation, stable user assignment, and rule precedence.
**Commit:** `test(sprint-6): document-precedence-and-exercise-a-table`


## Sprint 7 - Refresh, cache, and stale behavior

**Outcome:** Refresh SDK configuration efficiently while continuing to use the last valid snapshot during failures.

### Session 31 - Expose SDK configuration revision/age diagnostics.

**Goal:** Expose SDK configuration revision/age diagnostics.
**Test:** `S07-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** measured request reduction, stale-window observations, and tests proving a failed refresh does not erase good state.
**Commit:** `feat(sprint-7): expose-sdk-configuration-revision-age`

### Session 32 - Implement configurable polling and test timeout/server-error behavior.

**Goal:** Implement configurable polling and test timeout/server-error behavior.
**Test:** `S07-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** measured request reduction, stale-window observations, and tests proving a failed refresh does not erase good state.
**Commit:** `test(sprint-7): implement-configurable-polling-and-test`

### Session 33 - Add conditional HTTP requests using ETags or revision hints.

**Goal:** Add conditional HTTP requests using ETags or revision hints.
**Test:** `S07-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** measured request reduction, stale-window observations, and tests proving a failed refresh does not erase good state.
**Commit:** `feat(sprint-7): add-conditional-http-requests-using-etags`

### Session 34 - Define and test last-known-good fallback behavior.

**Goal:** Define and test last-known-good fallback behavior.
**Test:** `S07-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** measured request reduction, stale-window observations, and tests proving a failed refresh does not erase good state.
**Commit:** `test(sprint-7): define-and-test-last-known-good-fallback`

### Session 35 - Run an optional local Redis experiment comparing per-process and shared caching; document whether it helps.

**Goal:** Run an optional local Redis experiment comparing per-process and shared caching; document whether it helps.
**Test:** `S07-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** measured request reduction, stale-window observations, and tests proving a failed refresh does not erase good state.
**Commit:** `test(sprint-7): run-an-optional-local-redis-experiment`


## Sprint 8 - Streaming and consistency

**Outcome:** Deliver updates over SSE and converge after disconnects, duplicates, or reordered notifications.

### Session 36 - Learn SSE's long-lived HTTP connection model and build a minimal local proof of concept.

**Goal:** Learn SSE's long-lived HTTP connection model and build a minimal local proof of concept.
**Test:** `S08-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** interruption/restart experiment and automated ordering/idempotency tests.
**Commit:** `feat(sprint-8): learn-sse-s-long-lived-http-connection`

### Session 37 - Implement an update stream with a documented event schema and disconnect handling.

**Goal:** Implement an update stream with a documented event schema and disconnect handling.
**Test:** `S08-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** interruption/restart experiment and automated ordering/idempotency tests.
**Commit:** `docs(sprint-8): implement-an-update-stream-with-a`

### Session 38 - Consume stream events from the SDK and expose connection diagnostics.

**Goal:** Consume stream events from the SDK and expose connection diagnostics.
**Test:** `S08-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** interruption/restart experiment and automated ordering/idempotency tests.
**Commit:** `feat(sprint-8): consume-stream-events-from-the-sdk-and`

### Session 39 - Add bounded reconnect/backoff and a catch-up fetch after reconnect.

**Goal:** Add bounded reconnect/backoff and a catch-up fetch after reconnect.
**Test:** `S08-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** interruption/restart experiment and automated ordering/idempotency tests.
**Commit:** `feat(sprint-8): add-bounded-reconnect-backoff-and-a-catch`

### Session 40 - Test duplicate and out-of-order revisions and prove the SDK never moves backward.

**Goal:** Test duplicate and out-of-order revisions and prove the SDK never moves backward.
**Test:** `S08-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** interruption/restart experiment and automated ordering/idempotency tests.
**Commit:** `test(sprint-8): test-duplicate-and-out-of-order-revisions`


## Sprint 9 - Observability, resilience, and measurement

**Outcome:** Explain system behavior using evidence from logs, metrics, failure tests, and bounded load tests.

### Session 41 - Add structured logs without credentials or other sensitive values.

**Goal:** Add structured logs without credentials or other sensitive values.
**Test:** `S09-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a failure matrix and benchmark report with environment and limitations recorded.
**Commit:** `feat(sprint-9): add-structured-logs-without-credentials-or`

### Session 42 - Instrument refresh/evaluation boundaries and expose useful local metrics.

**Goal:** Instrument refresh/evaluation boundaries and expose useful local metrics.
**Test:** `S09-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a failure matrix and benchmark report with environment and limitations recorded.
**Commit:** `test(sprint-9): instrument-refresh-evaluation-boundaries`

### Session 43 - Measure configuration-change-to-client-update propagation.

**Goal:** Measure configuration-change-to-client-update propagation.
**Test:** `S09-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a failure matrix and benchmark report with environment and limitations recorded.
**Commit:** `test(sprint-9): measure-configuration-change-to-client`

### Session 44 - Inject local database/API/stream failures and record the actual fallback behavior.

**Goal:** Inject local database/API/stream failures and record the actual fallback behavior.
**Test:** `S09-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a failure matrix and benchmark report with environment and limitations recorded.
**Commit:** `test(sprint-9): inject-local-database-api-stream-failures`

### Session 45 - Run a resource-bounded load test and report percentiles, throughput, and errors.

**Goal:** Run a resource-bounded load test and report percentiles, throughput, and errors.
**Test:** `S09-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** a failure matrix and benchmark report with environment and limitations recorded.
**Commit:** `test(sprint-9): run-a-resource-bounded-load-test-and`


## Sprint 10 - GCP and Terraform foundations

**Outcome:** Understand the intended GCP deployment and validate infrastructure configuration without provisioning resources.

### Session 46 - Review the cost boundary, billing requirements, resource ownership, and teardown plan.

**Goal:** Review the cost boundary, billing requirements, resource ownership, and teardown plan.
**Test:** `S10-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** reviewed Terraform plan/configuration and a resource inventory/cleanup runbook. Do not run `terraform apply` on the default path.
**Commit:** `docs(sprint-10): review-the-cost-boundary-billing`

### Session 47 - Create Terraform configuration and run formatting, initialization as appropriate, validation, and static checks without applying it.

**Goal:** Create Terraform configuration and run formatting, initialization as appropriate, validation, and static checks without applying it.
**Test:** `S10-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** reviewed Terraform plan/configuration and a resource inventory/cleanup runbook. Do not run `terraform apply` on the default path.
**Commit:** `test(sprint-10): create-terraform-configuration-and-run`

### Session 48 - Build and run the container locally; document Artifact Registry image lifecycle.

**Goal:** Build and run the container locally; document Artifact Registry image lifecycle.
**Test:** `S10-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** reviewed Terraform plan/configuration and a resource inventory/cleanup runbook. Do not run `terraform apply` on the default path.
**Commit:** `test(sprint-10): build-and-run-the-container-locally`

### Session 49 - Configure and validate a Cloud Run deployment plan with scale-to-zero intent, without deploying it.

**Goal:** Configure and validate a Cloud Run deployment plan with scale-to-zero intent, without deploying it.
**Test:** `S10-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** reviewed Terraform plan/configuration and a resource inventory/cleanup runbook. Do not run `terraform apply` on the default path.
**Commit:** `test(sprint-10): configure-and-validate-a-cloud-run`

### Session 50 - Study Cloud Run logs and operations through local equivalents; document what remains cloud-specific.

**Goal:** Study Cloud Run logs and operations through local equivalents; document what remains cloud-specific.
**Test:** `S10-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** reviewed Terraform plan/configuration and a resource inventory/cleanup runbook. Do not run `terraform apply` on the default path.
**Commit:** `test(sprint-10): study-cloud-run-logs-and-operations`


## Sprint 11 - Document data, events, and IAM

**Outcome:** Model the cloud data/event path and test its core semantics locally.

### Session 51 - Map the relational domain to Firestore documents and explain query/transaction trade-offs.

**Goal:** Map the relational domain to Firestore documents and explain query/transaction trade-offs.
**Test:** `S11-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** adapter/event tests, documented emulator limitations, and an IAM permission matrix.
**Commit:** `docs(sprint-11): map-the-relational-domain-to-firestore`

### Session 52 - Test the repository contract against a Firestore emulator or local adapter.

**Goal:** Test the repository contract against a Firestore emulator or local adapter.
**Test:** `S11-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** adapter/event tests, documented emulator limitations, and an IAM permission matrix.
**Commit:** `test(sprint-11): test-the-repository-contract-against-a`

### Session 53 - Publish configuration-change events through a Pub/Sub emulator or local event-bus adapter.

**Goal:** Publish configuration-change events through a Pub/Sub emulator or local event-bus adapter.
**Test:** `S11-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** adapter/event tests, documented emulator limitations, and an IAM permission matrix.
**Commit:** `feat(sprint-11): publish-configuration-change-events`

### Session 54 - Consume duplicate events idempotently and connect event revision to the SDK catch-up path.

**Goal:** Consume duplicate events idempotently and connect event revision to the SDK catch-up path.
**Test:** `S11-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** adapter/event tests, documented emulator limitations, and an IAM permission matrix.
**Commit:** `feat(sprint-11): consume-duplicate-events-idempotently-and`

### Session 55 - Design least-privilege IAM policies and cloud observability without creating live resources.

**Goal:** Design least-privilege IAM policies and cloud observability without creating live resources.
**Test:** `S11-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** adapter/event tests, documented emulator limitations, and an IAM permission matrix.
**Commit:** `feat(sprint-11): design-least-privilege-iam-policies-and`


## Sprint 12 - CI/CD design and final engineering package

**Outcome:** Demonstrate reproducible local checks, a safe release design, and the complete system's trade-offs.

### Session 56 - Run lint, unit/integration tests, and builds locally; design optional hosted CI without enabling it by default.

**Goal:** Run lint, unit/integration tests, and builds locally; design optional hosted CI without enabling it by default.
**Test:** `S12-T1` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** repeatable local validation, final report, and a list of known gaps and next experiments.
**Commit:** `test(sprint-12): run-lint-unit-integration-tests-and-builds`

### Session 57 - Document a controlled deployment and rollback workflow; do not deploy without explicit approval.

**Goal:** Document a controlled deployment and rollback workflow; do not deploy without explicit approval.
**Test:** `S12-T2` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** repeatable local validation, final report, and a list of known gaps and next experiments.
**Commit:** `docs(sprint-12): document-a-controlled-deployment-and`

### Session 58 - Validate the end-to-end local path from dashboard through API and SDK, including propagation and failure fallback.

**Goal:** Validate the end-to-end local path from dashboard through API and SDK, including propagation and failure fallback.
**Test:** `S12-T3` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** repeatable local validation, final report, and a list of known gaps and next experiments.
**Commit:** `test(sprint-12): validate-the-end-to-end-local-path-from`

### Session 59 - Compare benchmark results with the earlier baseline and update the architecture evolution record.

**Goal:** Compare benchmark results with the earlier baseline and update the architecture evolution record.
**Test:** `S12-T4` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** repeatable local validation, final report, and a list of known gaps and next experiments.
**Commit:** `test(sprint-12): compare-benchmark-results-with-the-earlier`

### Session 60 - Present the demo, security/cost walkthrough, ADR review, and learning retrospective.

**Goal:** Present the demo, security/cost walkthrough, ADR review, and learning retrospective.
**Test:** `S12-T5` - verify the stated deliverable against the sprint outcome; run a focused automated check or record a repeatable review. For implementation work, include a failure case.
**Evidence:** repeatable local validation, final report, and a list of known gaps and next experiments.
**Commit:** `docs(sprint-12): present-the-demo-security-cost-walkthrough`

## Completion standard

A session is complete only when its goal, verification result, and commit/reference are recorded. Do not record a commit as completed before creating it. A sprint is complete when its five sessions have evidence and its outcome can be explained.

Live cloud provisioning and hosted CI/CD remain optional. Follow `COST-BOUNDARY.md`; do not provision resources as part of these sessions without explicit approval.
