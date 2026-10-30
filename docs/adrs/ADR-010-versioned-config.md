# ADR-010: Environment-wide configuration revisions

**Status:** Accepted

## Decision

Each environment owns one monotonically increasing configuration revision. The server increments it atomically with every successful transaction that changes client-visible configuration. A snapshot carries that environment revision. Each SDK instance retains its latest valid snapshot and accepts an incoming snapshot only when its revision is strictly greater than the current one.

## Context

distributed update events can be duplicated or reordered, and concurrent writers must not publish distinct states under the same revision.

## Transaction and failure requirements

- Commit the configuration mutation, environment revision increment, and audit event in one transaction.
- Serialize concurrent revision allocation: use an atomic row update or row lock in PostgreSQL and a transaction in Firestore.
- A failed transaction must not publish a new revision.
- SDK clients keep the last-known-good snapshot when fetching or validating a newer one fails.

## Consequences

This provides simple idempotency/staleness protection with a small state model. A flag's per-record version may separately protect edits to that flag; it is not the version of the environment snapshot. The environment becomes the serialization point for client-visible configuration changes. This makes revision semantics straightforward and prevents ambiguity when several flags change, but concurrent updates to the same environment may contend on its revision record. The project should measure this only if it becomes a practical bottleneck; correctness takes priority at the intended personal-project scale.
