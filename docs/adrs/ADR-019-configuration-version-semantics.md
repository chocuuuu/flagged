# ADR-019: Configuration revision and flag edit-version semantics

**Status:** Proposed

**Supplements:** [ADR-010](./ADR-010-versioned-config.md)

**Related decision:** ADR-022 will define the SDK payload and enumerate its client-visible fields.

## Context

Flagged has two different version values with different jobs:

- An environment-wide configuration revision identifies an ordered client-visible snapshot.
- A feature flag's `version` supports optimistic concurrency when editing that flag.

Both values are useful, but treating them as interchangeable can cause stale snapshots to be accepted, unrelated flag updates to conflict, or SDK payloads to expose an implementation detail as their ordering mechanism. The distinction must remain consistent across the API, persistence adapters, and SDK.

The revision rule also depends on a precise boundary between client-visible configuration and admin-only metadata. ADR-022 owns the SDK payload contract and its field inventory; this ADR uses that inventory to determine when the environment revision advances.

## Decision

- `environments.config_revision` is the authoritative version of client-visible configuration for an environment. It starts at `0`; revision `0` is a valid, empty configuration snapshot that an SDK may bootstrap and accept.
- A successful transaction increments the environment revision exactly once when it creates, changes, or deletes a flag, or changes any other client-visible configuration defined by ADR-022. This includes changes to active targeting rules and their evaluation order. Deleting a flag advances the revision; the next complete snapshot represents deletion by omitting that flag.
- A transaction that changes only admin-only metadata, changes a disabled rule without changing the client-visible payload, or makes no effective client-visible change does not increment the revision.
- The configuration mutation, revision increment, and corresponding audit event commit atomically. Failed or rolled-back transactions do not publish a revision.
- Revision allocation is serialized per environment. PostgreSQL uses an atomic environment-row update or row lock in the transaction; Firestore performs the equivalent operation in a transaction.
- A bootstrap response's revision and configuration data must come from the same committed database state. Read them in one transaction or consistent database snapshot; do not combine a revision and flags read from different states.
- `feature_flags.version` is an optimistic-concurrency token for that flag only. It is not a snapshot version, is not compared across flags, and does not determine SDK snapshot freshness.
- SDK configuration responses carry the environment `revision`. SDKs install a validated snapshot only when its revision is strictly greater than the currently installed revision. Equal or lower revisions are ignored; a failed fetch or validation leaves the last-known-good snapshot in place.
- The server-side API contract defines how flag edits supply and receive the optimistic-concurrency token. The SDK snapshot contract uses only the environment revision for ordering.
- An environment key is never reused within its project, including after deletion. A recreated environment must use a new key, so a client cannot mistake its newly initialized revision for a stale snapshot of the deleted environment.
- The client-visible field inventory in ADR-022 defines which persisted changes require a revision increment. Fields outside that payload are admin-only and do not advance the revision unless ADR-022 changes the payload contract.

## Alternatives considered

### Use each flag's version to order SDK configuration

Rejected because there is no single ordering value for a snapshot containing multiple flags. A change to one flag also cannot identify the freshness of the complete environment configuration.

### Increment the environment revision for every persisted write

Rejected because admin-only metadata and no-op writes do not change the client-visible snapshot. Advancing its revision for those writes creates unnecessary propagation and cache replacement.

### Use the environment revision for flag-edit concurrency

Rejected because a change to any flag would make edits to every other flag appear stale, coupling independent edits unnecessarily.

## Consequences

The environment row is the serialization point for client-visible changes, while per-flag optimistic concurrency remains scoped to a flag. This keeps SDK freshness checks simple and lets independent flag edits avoid conflicts unless they change the same flag or environment-level client-visible configuration concurrently.

The serialization point can contend under concurrent writes to one environment. Correctness takes priority at the project's intended scale; measure contention before considering a different design. Both persistence adapters must preserve the same atomicity and monotonicity semantics.

## Verification

Tests for the API, persistence adapters, and SDK should establish that:

- two concurrent client-visible changes receive distinct, increasing environment revisions;
- one transaction that changes multiple client-visible fields increments the environment revision once;
- creating, changing, and deleting flags advance the revision; deleting a flag makes it absent from the next complete snapshot;
- creating, changing, deleting, enabling, or disabling an active rule advances the revision when the emitted SDK payload changes;
- admin-only changes and no-op writes leave the environment revision unchanged;
- a failed or rolled-back mutation leaves configuration, revision, and audit event consistent;
- a bootstrap read concurrent with a write returns a revision and configuration from the same committed state;
- revision `0` can be bootstrapped as a valid empty configuration;
- deleting an environment does not make its key available for reuse within the project;
- a stale flag-edit token cannot overwrite a newer edit to that flag;
- SDKs ignore equal and lower snapshot revisions, accept a higher valid revision, and retain the last-known-good snapshot on refresh failure.
