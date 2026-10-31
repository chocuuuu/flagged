# ADR-023: Repository structure

**Status:** Proposed

## Context

The project is a learning-first modular monolith. Its documentation, ADRs, Jira
backlog, progress plans, and local validation scripts currently live in distinct
top-level directories. Application packages have not yet been implemented.

## Decision

Keep the current repository layout as the planning baseline:

- project-level product, architecture, security, cost, and operating documents stay
  at the repository root;
- ADRs, API/operations guidance, and learning references live under `docs/`;
- Jira planning artifacts live under `jira/`;
- canonical sessions and their derived checklist live under `progress/`;
- local repository checks and generators live under `scripts/`.

Introduce application directories only when their implementation milestone begins.
Do not create premature service boundaries or move the planning sources to simulate
an application structure that does not exist yet.

## Consequences

- The planning sources remain easy to find and validate locally.
- Future application/package boundaries require a reviewed change when that work
  begins; this ADR does not prescribe names or introduce services.
- No directory move or application implementation is part of this decision.

## Verification

The repository layout is recorded in `README.md`; the local consistency check
verifies paths listed in the README and is run before implementation work.
