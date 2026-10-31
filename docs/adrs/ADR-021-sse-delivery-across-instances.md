# ADR-021: SSE delivery across stateless instances

**Status:** Proposed

**Supplements:** [ADR-009](./ADR-009-progressive-propagation.md), [ADR-014](./ADR-014-gcp-cloud-run.md)

**Related decisions:** [ADR-010](./ADR-010-versioned-config.md), [ADR-019](./ADR-019-configuration-version-semantics.md), [ADR-020](./ADR-020-rule-precedence-and-rollout-bucketing.md), [ADR-022](./ADR-022-sdk-payload-and-client-visible-fields.md)

## Context

An SSE connection is bound to the application instance that accepted it, while an admin write may be handled by another instance. Process-local notifications alone cannot deliver that update to the connected client. The application must remain stateless and the local-first path must not depend on a paid managed service.

Configuration state and its monotonically increasing environment revision are committed together in the database. SDK snapshots are complete and versioned; stream events can therefore notify clients that a newer snapshot may be available without carrying configuration themselves.

ADR-010's use of the word “version” for snapshot ordering means the environment-wide `revision` defined by ADR-019.

## Decision

- The database remains the source of truth for stream change detection. In the local development and emulator path, each active stream checks its environment's current revision every 5 seconds. A 60-second interval is proposed for a future, explicitly approved Firestore deployment; it is not an active default while the Firestore adapter is deferred. Re-measure the interval and review current cost/read volume under the cloud cost gate before any live use.
- The stream checks the database revision only; it does not load or transmit the full configuration while polling. An update made through any application instance is observed by every instance's streams through the shared database.
- On connection, the SDK may supply the revision of its currently installed snapshot. A supplied value is valid only if it is a non-negative integer no greater than the current database revision. If it is absent, malformed, negative, or greater than the current revision, treat the baseline as unknown and immediately send a `config.updated` event with the current database revision. Otherwise, send the event immediately only when the current database revision is greater than the supplied baseline. This prevents a malformed or client-inflated baseline from suppressing updates.
- SSE events are invalidation hints, not configuration transfer. The SDK fetches the complete snapshot through the SDK configuration endpoint, validates it, and installs it only if its revision is strictly newer than its current snapshot.
- Intermediate revisions may be coalesced. The contract is convergence to the latest committed state, not delivery of every historical configuration. A duplicate notification is harmless.
- On every `config.updated` event, reconnect, or stream close due to its lifetime limit, the SDK performs a full snapshot fetch, validates it, and installs it only when its revision is strictly greater than its current snapshot. It does not merely check a revision or fetch a delta. This also covers changes missed during disconnects.
- Send an SSE comment heartbeat every 20 seconds, including while database reads are failing, so intermediaries do not treat an otherwise healthy connection as idle. A heartbeat is not evidence that the database is healthy or that the stream is current.
- A database read failure is logged and counted as a stream polling failure; it is not represented as a successful revision or configuration update. The connection may remain open with heartbeats while the SDK retains its last-known-good snapshot and continues its normal polling fallback. When reads recover, the next successful check reports the latest revision.
- The maximum stream lifetime defaults to 5 minutes. The stream must close before the hosting request timeout; configure the hosting timeout to exceed the stream lifetime by at least 30 seconds. For Cloud Run, verify the service's configured request timeout and the platform-supported maximum during deployment configuration. If the configured timeout is too short, reduce the stream lifetime so the stream closes at least 30 seconds before it.
- The local database-backed polling path is the default and is suitable for the project's small test target. The local emulator/test adapter must exercise the same cross-instance semantics.
- For read-volume planning, use the formula `active streams × 86400 / polling interval in seconds`. At 20 continuously connected clients, this is 345,600 revision checks/day at 5 seconds or 28,800/day at 60 seconds, before bootstrap, snapshot, reconnect, or other reads. These are workload calculations, not price or quota guarantees. A prior pricing/quota note checked on 2026-10-30 is historical and must not be treated as current. Verify current official pricing, quota eligibility, billing prerequisites, data layout, and total workload before any live deployment; require explicit approval under ADR-006 and the cloud cost gate. If expected charges are not acceptable, keep the deployment local or do not enable live SSE.
- Pub/Sub or another shared notification bus is not required for the initial implementation. It may be evaluated only if measured database-read load or propagation latency justifies it; live managed-service use remains optional and subject to the cloud cost approval gate. Any such change requires a new ADR.
- Stream authentication uses the environment-scoped, read-only client-key authorization from ADR-012. Stream events contain no flag values, rules, secrets, or admin data.

## Alternatives considered

### Process-local publish/subscribe only

Rejected because it misses writes handled by a different service instance and does not preserve the stateless deployment model.

### Require Pub/Sub for initial SSE

Rejected because it adds a managed dependency and operational/cost considerations before the project's small local-first workload demonstrates a need. Pub/Sub remains a future experiment, not the default path.

### Send the full configuration in each SSE event

Rejected because it duplicates the bootstrap contract, increases stream bandwidth, complicates event recovery, and couples notification delivery to snapshot transfer. Revision hints plus a normal snapshot fetch preserve one validation and ordering path.

### Rely only on SSE without polling or reconnect reconciliation

Rejected because stream connections can fail, be terminated by hosting timeouts, or miss notifications. Polling and reconnect bootstrap provide recovery.

## Consequences

Every active stream performs periodic database reads, so database load grows with active connections and the polling frequency. Local development uses a five-second interval; a 60-second interval is proposed for a future Firestore adapter and would give a nominal change-detection delay of up to one interval plus database and dispatch latency. At 20 continuously connected clients, this corresponds to 28,800 revision checks/day, excluding snapshot refreshes and all other reads. No current price or free quota is asserted here. Verify current official pricing, quota eligibility, and billing requirements before live use; explicit approval remains required.

During database outages, SSE cannot announce changes. Existing SDKs continue using their last-known-good snapshots, and reconnect or regular configuration polling converges them after recovery. SSE is a latency optimization, not a correctness or availability dependency.

Streams remain open for at most five minutes by default, send heartbeats every 20 seconds, and close before the configured hosting request timeout. Application instances need no shared in-memory state, sticky-session routing, or managed messaging service. A future push bus could reduce polling reads but would add delivery, subscription, and duplicate-handling behavior that must be specified and measured.

## Verification

Tests for the API, SDK, and local multi-instance setup should establish that:

- an update written through instance A is detected by a stream connected to instance B through the shared database revision;
- a stream connection immediately reports the current revision when its baseline is absent, malformed, negative, or ahead of the database; a newer valid baseline receives the current revision only when it is stale;
- duplicate and coalesced events cause the SDK to fetch and install only a complete, strictly newer snapshot;
- a database outage does not emit a false success, does not erase the client's last-known-good snapshot, and recovery reports the latest revision;
- every event, reconnect, and lifetime close triggers a full snapshot fetch, not only a revision check or delta; tests cover an event missed while disconnected;
- streams send 20-second heartbeats, close within the five-minute lifetime, and respect a hosting request timeout at least 30 seconds longer;
- stream events contain only the event type and revision, never configuration or secrets;
- read-volume calculations match 345,600 reads/day for 20 streams at 5 seconds and 28,800 reads/day at 60 seconds; active-stream revision polling frequency and update-detection latency are measurable at the documented local test scale.
- revision-check calculations match the active-stream count and interval; total reads, pricing, quota eligibility, and billing prerequisites are re-verified before live use without relying on historical quota notes.
