# ADR-022: SDK payload and client-visible configuration

**Status:** Proposed

**Related decisions:** [ADR-010](./ADR-010-versioned-config.md), [ADR-012](./ADR-012-api-key-scoping.md), [ADR-019](./ADR-019-configuration-version-semantics.md), [ADR-020](./ADR-020-rule-precedence-and-rollout-bucketing.md)

## Context

The browser SDK evaluates flags locally, so it must receive the configuration needed to make the same evaluation decisions as the control plane intends. A browser is an untrusted client: any configuration sent to it can be inspected, copied, and retained by its user. Calling a payload "SDK-safe" does not make its contents confidential.

The revision rules in ADR-019 need a stable inventory of the persisted fields that affect the SDK snapshot. The current model defines basic flag and targeting-rule fields, but mentions variants without yet defining their data schema.

## Decision

- The SDK configuration endpoint returns one complete snapshot for a single environment, authenticated by that environment's read-only client key. The key permits configuration reads only; it does not grant admin access.
- The client-visible configuration consists of:
  - The environment's stable key and environment-wide `revision`.
  - For each SDK-evaluable flag: `key`, `type`, `enabled`, and `rollout.basisPoints` (an integer from `0` through `10000`, inclusive).
  - For each enabled targeting rule: `attribute`, `operator`, `value`, and `priority`. Disabled rules are excluded. The server orders included rules as specified by ADR-020; the SDK evaluates them in the received order and does not re-sort them.
  - For variant flags, the variant keys, values, and allocation data required by the SDK evaluator. The exact persisted and wire representation must be defined alongside the variant data model before variant payload implementation.
- There are no client-visible environment settings in the initial model. If an environment-level setting is added to the SDK payload later, its effect on revision increments must be documented in an ADR and the payload contract.
- `generatedAt` may be returned as response metadata, but it is not part of the persisted configuration and does not itself advance the environment revision. The revision is the sole ordering value for snapshots.
- Revision `0` with an empty `flags` list is a valid snapshot. A snapshot contains the complete current set of SDK-evaluable flags for the environment, so removing a flag is reflected by its absence in the next higher-revision snapshot.
- An environment may contain at most 500 flags. A serialized SDK snapshot, including response metadata, may not exceed 900 KiB (921,600 bytes). The lower application limit leaves headroom beneath Firestore's 1 MiB per-document limit for the materialized snapshot document's field names and metadata. Before committing a mutation, the server validates the resulting flag count and serialized snapshot size. If either limit would be exceeded, reject the mutation with a validation error and commit neither the mutation nor a revision. Never truncate a snapshot. If stored data nevertheless exceeds the limit, fail the SDK response explicitly and leave SDK clients on their last-known-good snapshot.
- The SDK evaluation context is supplied by the calling application at evaluation time; it is not part of the configuration snapshot. It contains a stable subject key for percentage rollouts and caller-provided string attributes for targeting. Missing, null, or non-string targeting attributes do not match a rule.
- Rollout values are represented as integer basis points in the persisted configuration and wire payload; the snapshot does not contain a floating-point percentage.
- Do not include admin-only fields: database or internal entity IDs, flag names/descriptions, audit data, client-key material or hashes, admin credentials, or other control-plane metadata.
- All fields in the payload, including targeting attributes, rule values, and variant data, are public to anyone able to use or inspect the browser client. Do not put secrets, personal data, or sensitive business logic in them. A targeting rule evaluated with browser-supplied attributes is not an authorization control; sensitive operations must be authorized by a trusted server.
- Client keys are environment-scoped and revocable, but a key embedded in a browser application must be treated as observable and potentially scrapeable. Scoping and rate limiting constrain abuse; they do not make the payload confidential.

## Alternatives considered

### Evaluate flags only on the server

Rejected for the initial product because local SDK evaluation is a core product requirement and avoids a network request on each evaluation. Server evaluation remains an option for future use cases that require keeping rule inputs or configuration confidential, and would require a separate API and ADR.

### Return only evaluated flag values to the browser

Rejected for the initial SDK because it would require server-side evaluation or additional evaluation requests and would no longer support deterministic local evaluation from a cached snapshot.

### Treat client-key authentication as configuration confidentiality

Rejected because a browser client cannot keep its key secret. The key scopes access and supports revocation; it is not a confidentiality boundary.

## Consequences

The payload is sufficient for local evaluation but intentionally discloses its evaluation rules and values to browser users. Teams must make browser exposure part of their configuration authoring and threat-model decisions. Any configuration that cannot safely be disclosed must not be sent through this endpoint.

The payload field list is the source of truth for ADR-019's client-visible change classification: changing any listed persisted evaluation field advances the environment revision; changing only excluded admin metadata does not. `revision` itself changes atomically with those mutations. `generatedAt` is response metadata, not a configuration mutation.

Variant flags are part of the product requirements, but the current data model does not define their persisted representation. Before implementing variant snapshots, define that schema and the corresponding wire format without exposing internal IDs or administrative metadata.

Variant flag evaluation and variant payload delivery are out of scope for the first implementation milestone. The first milestone must not imply variant support merely because the type is reserved in the payload contract.

## Verification

Tests for the API, persistence adapters, and SDK should establish that:

- an environment-scoped client key can read only its own SDK configuration and cannot call admin operations;
- the response includes the enumerated evaluation fields and excludes internal IDs, descriptions, audit records, key material, and admin credentials;
- each targeting rule is serialized in deterministic evaluation order;
- disabled targeting rules are omitted, and enabling or disabling a rule changes the payload and advances the revision;
- mutations that would exceed 500 flags or a 900 KiB serialized snapshot are rejected without committing configuration or a revision, and oversized stored snapshots are never truncated;
- missing, null, or non-string context attributes do not match targeting rules;
- changing any persisted client-visible evaluation field advances the environment revision, while changing excluded admin metadata does not;
- rollout basis points are serialized and evaluated as integers without floating-point percentage conversion;
- the response's revision and configuration are read from the same committed state, and an empty revision-`0` snapshot is valid;
- removing a flag is reflected in the next complete snapshot;
- browser evaluation does not treat targeting results as authorization for protected operations;
- variant payload tests are added when the variant schema and wire representation are defined; variant evaluation remains out of scope for the first implementation milestone.
