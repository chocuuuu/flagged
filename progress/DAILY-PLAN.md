# Flagged — Outcome-Based Milestone Guide

## How to use this guide

The milestones are ordered learning outcomes, not weeks, days, or deadlines. Work blocks are small pieces of study and implementation; combine or split them to fit the time you have. Stop between blocks whenever needed.

The project remains the full 12-milestone learning plan. Milestone 5 is an early, useful local end-to-end system, not a scope cut. The remaining milestones build on it. GCP concepts are explored locally with emulators, adapters, and Terraform validation by default; live provisioning is optional and requires the approval gate in `COST-BOUNDARY.md`.

For each meaningful change, first discuss the concept, purpose, alternatives, assumptions, files, and tests. At the end, record what you learned, what failed, what evidence proves the behavior, and what remains uncertain.

## Milestone 1 — Domain and local foundation

**Outcome:** Explain the product and its control/data-plane boundary, and reproduce the starting local environment.

Work blocks:

- Define the feature-flag problem, glossary, deployment-versus-release distinction, and project scope.
- Study feature-flag concepts and OpenFeature/commercial reference models; record what is in and out of scope.
- Sketch the initial control-plane/data-plane architecture and explain why evaluation is local.
- Bootstrap the repository structure and local Python/frontend/SDK tooling.
- Create the Docker Compose foundation and verify that the local database can be started, stopped, and recreated.

Evidence: architecture sketch, clean setup instructions, and a successful local environment recreation.

## Milestone 2 — API and relational data foundation

**Outcome:** Build a tested FastAPI and PostgreSQL foundation with repeatable schema changes.

Work blocks:

- Create the FastAPI application shell and health/readiness endpoints.
- Define request validation and a consistent API error contract.
- Connect SQLAlchemy and establish a clear database-session lifecycle.
- Add Alembic migrations and test applying them to a clean database.
- Define the initial project/environment/flag schema, constraints, and indexes.

Evidence: automated API/database tests and a clean migration run.

## Milestone 3 — Flag control plane and admin access

**Outcome:** Manage flags through a protected API and retain an auditable history of changes.

Work blocks:

- Implement project, environment, and feature-flag CRUD.
- Add flag edit-version checks to prevent lost updates.
- Record audit events with before/after state in the same transaction as mutations.
- Implement the single-operator admin authentication in ADR-018.
- Test authorized, unauthorized, invalid, conflicting, and failure cases.

Evidence: API tests show successful changes are audited atomically and stale edits are rejected.

## Milestone 4 — Admin dashboard

**Outcome:** Operate the local control plane through a usable browser dashboard.

Work blocks:

- Create the Astro/React application shell and navigation.
- Build project and environment views with loading, empty, and error states.
- Build flag list/create/edit/toggle workflows.
- Display audit history and before/after values.
- Harden forms, input validation, accessibility, and browser error behavior.

Evidence: a browser walkthrough of the admin workflows and relevant component/API tests.

## Milestone 5 — SDK and first local end-to-end behavior

**Outcome:** Change a flag in the control plane and observe the demo app respond without rebuilding it.

Work blocks:

- Define the public TypeScript SDK contract before implementation.
- Fetch and validate configuration during SDK bootstrap.
- Store an immutable in-memory configuration snapshot.
- Implement boolean evaluation and caller-provided fallback behavior.
- Integrate the SDK into the demo store and demonstrate a live flag change.

Evidence: end-to-end local demonstration, unit/integration tests, and a documented unavailable-API fallback.

## Milestone 6 — Isolation, rollout, and targeting

**Outcome:** Deliver the correct environment configuration and evaluate deterministic user assignment.

Work blocks:

- Design environment-scoped, read-only SDK client keys and their revocation flow.
- Enforce project/environment isolation at the API boundary.
- Implement and test deterministic percentage bucketing.
- Define and implement the intentionally small targeting-rule set.
- Document precedence and exercise a table-driven evaluation matrix.

Evidence: tests for revoked keys, environment separation, stable user assignment, and rule precedence.

## Milestone 7 — Refresh, cache, and stale behavior

**Outcome:** Refresh SDK configuration efficiently while continuing to use the last valid snapshot during failures.

Work blocks:

- Expose SDK configuration revision/age diagnostics.
- Implement configurable polling and test timeout/server-error behavior.
- Add conditional HTTP requests using ETags or revision hints.
- Define and test last-known-good fallback behavior.
- Run an optional local Redis experiment comparing per-process and shared caching; document whether it helps.

Evidence: measured request reduction, stale-window observations, and tests proving a failed refresh does not erase good state.

## Milestone 8 — Streaming and consistency

**Outcome:** Deliver updates over SSE and converge after disconnects, duplicates, or reordered notifications.

Work blocks:

- Learn SSE's long-lived HTTP connection model and build a minimal local proof of concept.
- Implement an update stream with a documented event schema and disconnect handling.
- Consume stream events from the SDK and expose connection diagnostics.
- Add bounded reconnect/backoff and a catch-up fetch after reconnect.
- Test duplicate and out-of-order revisions and prove the SDK never moves backward.

Evidence: interruption/restart experiment and automated ordering/idempotency tests.

## Milestone 9 — Observability, resilience, and measurement

**Outcome:** Explain system behavior using evidence from logs, metrics, failure tests, and bounded load tests.

Work blocks:

- Add structured logs without credentials or other sensitive values.
- Instrument refresh/evaluation boundaries and expose useful local metrics.
- Measure configuration-change-to-client-update propagation.
- Inject local database/API/stream failures and record the actual fallback behavior.
- Run a resource-bounded load test and report percentiles, throughput, and errors.

Evidence: a failure matrix and benchmark report with environment and limitations recorded.

## Milestone 10 — GCP and Terraform foundations

**Outcome:** Understand the intended GCP deployment and validate infrastructure configuration without provisioning resources.

Work blocks:

- Review the cost boundary, billing requirements, resource ownership, and teardown plan.
- Create Terraform configuration and run formatting, initialization as appropriate, validation, and static checks without applying it.
- Build and run the container locally; document Artifact Registry image lifecycle.
- Configure and validate a Cloud Run deployment plan with scale-to-zero intent, without deploying it.
- Study Cloud Run logs and operations through local equivalents; document what remains cloud-specific.

Evidence: reviewed Terraform plan/configuration and a resource inventory/cleanup runbook. Do not run `terraform apply` on the default path.

## Milestone 11 — Document data, events, and IAM

**Outcome:** Model the cloud data/event path and test its core semantics locally.

Work blocks:

- Map the relational domain to Firestore documents and explain query/transaction trade-offs.
- Test the repository contract against a Firestore emulator or local adapter.
- Publish configuration-change events through a Pub/Sub emulator or local event-bus adapter.
- Consume duplicate events idempotently and connect event revision to the SDK catch-up path.
- Design least-privilege IAM policies and cloud observability without creating live resources.

Evidence: adapter/event tests, documented emulator limitations, and an IAM permission matrix.

## Milestone 12 — CI/CD design and final engineering package

**Outcome:** Demonstrate reproducible local checks, a safe release design, and the complete system's trade-offs.

Work blocks:

- Run lint, unit/integration tests, and builds locally; design optional hosted CI without enabling it by default.
- Document a controlled deployment and rollback workflow; do not deploy without explicit approval.
- Validate the end-to-end local path from dashboard through API and SDK, including propagation and failure fallback.
- Compare benchmark results with the earlier baseline and update the architecture evolution record.
- Present the demo, security/cost walkthrough, ADR review, and learning retrospective.

Evidence: repeatable local validation, final report, and a list of known gaps and next experiments.

## Completion standard

A milestone is complete when you can:

- explain the central concept in your own words;
- demonstrate the intended behavior;
- point to a test or other repeatable evidence;
- describe a relevant failure mode and its behavior;
- explain the trade-off and what remains imperfect.

There is no penalty for taking longer, changing the order after documenting a dependency, or pausing to learn a prerequisite.
