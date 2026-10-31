# Flagged API contract (draft)

**Status:** Draft for review; not approved for implementation

**API version:** `v1`

This document is the single draft HTTP contract for the control plane and SDK. It is
not yet approved for implementation: related ADRs remain Proposed and endpoints are
not implemented or verified. Both the API and SDK implementation must reference this
contract; do not duplicate route or payload definitions in implementation notes.
Review together with ADR-012, ADR-018, ADR-019, ADR-020, ADR-021, and ADR-022.

## 1. Contract principles

- Every endpoint is under `/v1`. A future incompatible contract uses a new major path such as `/v2`; additive optional response fields may be introduced in `v1`.
- JSON request and response bodies use UTF-8. Timestamps are UTC RFC 3339 strings. Resource IDs are opaque UUIDs; resource keys are stable, URL-encoded path segments.
- Admin routes use the session and CSRF model from ADR-018. SDK routes use an environment-scoped client key as described in ADR-012.
- SDK configuration responses are complete snapshots, not deltas. The environment `revision` orders snapshots; a flag's `version` is only an optimistic-concurrency token.
- Variant evaluation is not supported in the first implementation milestone. The v1 flag write API accepts `type: "boolean"` only.
- Lists use cursor pagination: `?limit=50&cursor=<opaque>`. `limit` defaults to 50 and must be from 1 through 100. List responses have the shape `{"items":[...],"nextCursor":"..."}`; `nextCursor` is `null` at the end.

## 2. Authentication and request protections

### Admin

- Admin endpoints are under `/v1/admin`.
- After login, the server authenticates the `HttpOnly`, `SameSite=Lax` signed session cookie defined by ADR-018. Set `Secure` on HTTPS.
- `POST /v1/admin/session` checks the request `Origin` and the configured admin password, sets the cookie, and returns a CSRF token. `GET /v1/admin/session` returns the current authentication state and a CSRF token for an authenticated session. `DELETE /v1/admin/session` logs out and clears the cookie.
- Every state-changing admin request made within an authenticated session must include `X-CSRF-Token` and pass the ADR-018 origin check. Session creation has no pre-auth session token; it must pass the strict `Origin` check to prevent login CSRF.
- Admin session responses, errors, and resource responses use `Cache-Control: no-store`.

### SDK

- SDK routes are under `/v1/sdk/projects/{projectKey}/environments/{environmentKey}`.
- Send the client key using the HTTP `Authorization` header with the `Bearer` scheme. Never send it in a URL, query string, or log.
- A client key can read configuration and open its environment's stream only. It cannot call admin endpoints or mutate data.
- Resolve and authenticate the key before evaluating conditional request headers. Invalid or revoked keys receive `401`. A valid key scoped to a different project/environment receives `404`, without revealing the key's actual scope.
- Because browser keys are observable, key scope does not make the SDK payload confidential. Payload contents follow ADR-022.

### Request IDs

The server returns an opaque `X-Request-ID` for each request. When supplied by a trusted caller, a bounded `X-Request-ID` may be echoed after validation. Request IDs are for support and tracing; they must not contain credentials or personal data.

## 3. Shared resource shapes

### Project

```json
{
  "id": "uuid",
  "key": "storefront",
  "name": "Storefront",
  "description": "Optional description",
  "createdAt": "2026-10-30T00:00:00Z",
  "updatedAt": "2026-10-30T00:00:00Z"
}
```

Create request:

```json
{ "key": "storefront", "name": "Storefront", "description": "Optional description" }
```

Update request:

```json
{ "name": "Customer storefront", "description": "Updated description" }
```

Create and get return the Project object directly. Project keys are globally unique and immutable after creation.

### Environment

```json
{
  "id": "uuid",
  "projectKey": "storefront",
  "key": "production",
  "name": "Production",
  "revision": 42,
  "createdAt": "2026-10-30T00:00:00Z",
  "updatedAt": "2026-10-30T00:00:00Z"
}
```

Create request is `{ "key": "production", "name": "Production" }`; update request is `{ "name": "Production (primary)" }`. Create, get, and update return the Environment object directly. The `revision` is the current client-visible configuration revision. Environment keys are unique within a project, immutable, and never reusable after deletion. Environment deletion is not exposed in v1 until the key tombstone/retention behavior is implemented.

### Flag

```json
{
  "id": "uuid",
  "key": "new_checkout",
  "name": "New checkout",
  "description": "Optional description",
  "type": "boolean",
  "enabled": true,
  "rolloutBasisPoints": 1000,
  "version": 3,
  "createdAt": "2026-10-30T00:00:00Z",
  "updatedAt": "2026-10-30T00:00:00Z"
}
```

Create request:

```json
{
  "key": "new_checkout",
  "name": "New checkout",
  "description": "Optional description",
  "type": "boolean",
  "enabled": false,
  "rolloutBasisPoints": 0
}
```

`description`, `enabled`, and `rolloutBasisPoints` are optional; defaults are `null`, `false`, and `0`. Server-created flags start at `version: 1`. Update requests include `expectedVersion` and only the fields to change, for example `{ "expectedVersion": 3, "enabled": true }`. Delete sends `{ "expectedVersion": 3 }`. A successful mutation returns/increments the flag's new version. Rule mutations use the parent flag's expected version, preventing lost updates across a flag and its rules.

`rolloutBasisPoints` is an integer from 0 through 10000, inclusive. Fractions and decimal percentage values are invalid. The response omits internal targeting-rule IDs; rule ordering and evaluation follow ADR-020.

Flag create and update responses use:

```json
{
  "flag": {
    "id": "uuid",
    "key": "new_checkout",
    "name": "New checkout",
    "description": "Optional description",
    "type": "boolean",
    "enabled": true,
    "rolloutBasisPoints": 1000,
    "version": 4,
    "createdAt": "2026-10-30T00:00:00Z",
    "updatedAt": "2026-10-30T00:00:00Z"
  },
  "revision": 43
}
```

The flag detail response has a `flag` object using the Flag shape above, a `rules` array using the Rule shape below, and the current environment `revision`.

### Rule

```json
{
  "id": "uuid",
  "attribute": "plan",
  "operator": "equals",
  "value": "pro",
  "priority": 10,
  "enabled": true
}
```

Create request:

```json
{
  "expectedFlagVersion": 3,
  "attribute": "plan",
  "operator": "equals",
  "value": "pro",
  "priority": 10,
  "enabled": true
}
```

`enabled` defaults to `true`. Update requests include `expectedFlagVersion` and only changed rule fields. Delete sends `{ "expectedFlagVersion": 3 }`. Rule mutation responses have this shape:

```json
{
  "rule": {
    "id": "uuid",
    "attribute": "plan",
    "operator": "equals",
    "value": "pro",
    "priority": 10,
    "enabled": true
  },
  "flagVersion": 4,
  "revision": 43
}
```

Delete returns `204` with `X-Flag-Version` and `X-Environment-Revision` headers. Equal priorities are allowed. The SDK snapshot excludes disabled rules and contains enabled rules in the server's deterministic order; the SDK does not re-sort them.

### Client key

List responses contain metadata only:

```json
{
  "id": "uuid",
  "keyPrefix": "ff_client_ab12",
  "status": "active",
  "createdAt": "2026-10-30T00:00:00Z",
  "revokedAt": null
}
```

The create request is `{}`. Its response is `{ "id": "...", "keyPrefix": "...", "status": "active", "createdAt": "...", "revokedAt": null, "key": "<full client key>" }`; the generated full key is returned exactly once. It is never returned by list routes, stored in plaintext, or included in logs. Revocation is permanent; it changes no SDK configuration revision.

## 4. Admin routes

All resource routes in this section require an authenticated admin session. The
session-creation route is the login entry point; session read and deletion follow the
session behavior above. State-changing routes additionally require CSRF validation.

| Method and path | Auth | Request | Success |
|---|---|---|---|
| `POST /v1/admin/session` | Strict Origin check; pre-auth | `{"password":"..."}` | `200`, session cookie and `{"csrfToken":"..."}` |
| `GET /v1/admin/session` | Admin session, if present | None | `200`, authenticated state and CSRF token, or `401` |
| `DELETE /v1/admin/session` | Admin session + CSRF | CSRF header | `204`, cleared cookie |
| `GET /v1/admin/projects` | Admin session | Pagination query | `200`, paginated projects |
| `POST /v1/admin/projects` | Admin session + CSRF | Project create shape | `201`, project |
| `GET /v1/admin/projects/{projectKey}` | Admin session | None | `200`, project |
| `PATCH /v1/admin/projects/{projectKey}` | Admin session + CSRF | Project update shape | `200`, project |
| `GET /v1/admin/projects/{projectKey}/environments` | Admin session | Pagination query | `200`, paginated environments |
| `POST /v1/admin/projects/{projectKey}/environments` | Admin session + CSRF | Environment create shape | `201`, environment |
| `GET /v1/admin/projects/{projectKey}/environments/{environmentKey}` | Admin session | None | `200`, environment |
| `PATCH /v1/admin/projects/{projectKey}/environments/{environmentKey}` | Admin session + CSRF | Environment update shape | `200`, environment |
| `GET /v1/admin/projects/{projectKey}/environments/{environmentKey}/flags` | Admin session | Pagination query | `200`, paginated flags and `X-Environment-Revision` |
| `POST /v1/admin/projects/{projectKey}/environments/{environmentKey}/flags` | Admin session + CSRF | Flag create shape | `201`, FlagMutationResponse |
| `GET /v1/admin/projects/{projectKey}/environments/{environmentKey}/flags/{flagKey}` | Admin session | None | `200`, FlagDetailResponse |
| `PATCH /v1/admin/projects/{projectKey}/environments/{environmentKey}/flags/{flagKey}` | Admin session + CSRF | Changed fields plus `expectedVersion` | `200`, FlagMutationResponse |
| `DELETE /v1/admin/projects/{projectKey}/environments/{environmentKey}/flags/{flagKey}` | Admin session + CSRF | `{"expectedVersion":3}` | `204`; advances revision in `X-Environment-Revision` |
| `POST /v1/admin/projects/{projectKey}/environments/{environmentKey}/flags/{flagKey}/rules` | Admin session + CSRF | Rule create shape | `201`, rule, flag version, and environment revision |
| `PATCH /v1/admin/projects/{projectKey}/environments/{environmentKey}/flags/{flagKey}/rules/{ruleId}` | Admin session + CSRF | Changed fields plus `expectedFlagVersion` | `200`, rule, flag version, and environment revision |
| `DELETE /v1/admin/projects/{projectKey}/environments/{environmentKey}/flags/{flagKey}/rules/{ruleId}` | Admin session + CSRF | `{"expectedFlagVersion":3}` | `204`; tokens in `X-Flag-Version` and `X-Environment-Revision` |
| `GET /v1/admin/projects/{projectKey}/environments/{environmentKey}/client-keys` | Admin session | Pagination query | `200`, paginated key metadata |
| `POST /v1/admin/projects/{projectKey}/environments/{environmentKey}/client-keys` | Admin session + CSRF | `{}` | `201`, metadata plus one-time full `key` |
| `DELETE /v1/admin/projects/{projectKey}/environments/{environmentKey}/client-keys/{clientKeyId}` | Admin session + CSRF | None | `204`; revokes key |
| `GET /v1/admin/projects/{projectKey}/audit-events` | Admin session | Pagination query; optional `environmentKey` | `200`, paginated redacted audit events |
| `GET /v1/health` | None | None | `200`, `{"status":"ok"}` when process is alive |
| `GET /v1/ready` | None | None | `200`, `{"status":"ready"}` or `503 DEPENDENCY_UNAVAILABLE` when required dependencies are unavailable |
| `GET /v1/sdk/projects/{projectKey}/environments/{environmentKey}/config` | Bearer client key | Optional `If-None-Match` | `200` with the section 5 snapshot, `304` when unchanged |
| `GET /v1/sdk/projects/{projectKey}/environments/{environmentKey}/stream` | Bearer client key | Optional `Last-Event-ID` | `200` SSE stream using the section 6 event schema |

Every non-success response uses the shared error shape in section 7, except
bodyless `204` and conditional `304` responses. Health responses disclose only
service status.

Project and environment deletion are not part of v1. Flag and rule delete requests carry concurrency tokens in their JSON bodies because deletion conflicts must be reported with the shared JSON error shape; clients must send `Content-Type: application/json`.

Admin mutation responses that change client-visible configuration include the resulting environment `revision`. A mutation that changes only admin metadata leaves it unchanged. The configuration, audit event, and revision commit atomically. The flag delete route returns its resulting revision in `X-Environment-Revision` because a `204` response has no body.

### Audit history

`GET /v1/admin/projects/{projectKey}/audit-events` requires an authenticated admin
session. It accepts the standard `limit` and opaque `cursor` pagination parameters
and an optional `environmentKey` filter. Results are ordered newest first, with a
stable event-ID tiebreaker. The response is
`{"items":[...],"nextCursor":null}`. Each event contains `id`, `projectKey`,
`environmentKey` (nullable), `actor`, `action`, `resourceType`, `resourceId`,
`before`, `after`, and `timestamp`. Values that could reveal credentials, key
material, or other secrets are redacted; full client keys are never included.
Project-scope mismatch and unknown projects return the shared `404` error shape.
Invalid cursors use `400 INVALID_CURSOR`.

Example item:

```json
{
  "id": "uuid",
  "projectKey": "storefront",
  "environmentKey": "production",
  "actor": "configured-admin",
  "action": "flag.updated",
  "resourceType": "flag",
  "resourceId": "uuid",
  "before": {"enabled": false},
  "after": {"enabled": true},
  "timestamp": "2026-10-30T00:00:00Z"
}
```

## 5. SDK configuration snapshot

### Route and response

`GET /v1/sdk/projects/{projectKey}/environments/{environmentKey}/config`

Authentication is the SDK bearer client key. A `200` response is the complete snapshot:

```json
{
  "environment": "production",
  "revision": 42,
  "flags": [
    {
      "key": "new_checkout",
      "type": "boolean",
      "enabled": true,
      "rollout": { "basisPoints": 1000 },
      "rules": [
        {
          "attribute": "plan",
          "operator": "equals",
          "value": "pro",
          "priority": 10
        }
      ]
    }
  ]
}
```

The body follows ADR-022: complete environment snapshot, no internal IDs, descriptions, disabled rules, audit data, client-key material, or admin fields. Rules follow ADR-020 order. Variant flags are not supported in the first milestone. An empty environment at revision 0 returns `200` with `"flags":[]`.

The v1 snapshot omits `generatedAt`; the revision and ETag are stable for an unchanged client-visible configuration.

### Conditional requests

- The response includes `ETag: "config-r42"` and `Cache-Control: private, no-cache, must-revalidate`.
- Send `If-None-Match: "config-r42"` to check whether the snapshot changed. If the current representation has the same revision, return `304 Not Modified`, an empty body, and the current `ETag`.
- Authentication and environment scope checks happen before the conditional check; a matching ETag never bypasses authorization.
- `304` is only a network/body optimization. It does not imply a free database read.
- `revision` in the JSON body is the authoritative value. `ETag` is an opaque HTTP validator; clients must not parse it as a revision.

### Read pattern and cost boundary

- PostgreSQL reads the environment revision, flags, and enabled rules in one consistent database transaction/snapshot and constructs the response from that committed state.
- Firestore persistence and its SDK snapshot read model are deferred by owner decision
  DP-003 in `docs/DECISIONS-PENDING.md`. Revisit and measure the read model before
  implementing a Firestore adapter.
- ADR-022's proposed 500-flag and 900 KiB snapshot bounds remain subject to the
  implementation review; do not attribute them to an active Firestore projection.
- Do not estimate live Firestore usage or cost from an unselected read model. Any
  future estimate must use a measured request pattern, current official pricing, and
  the explicit cloud approval gate.

## 6. SSE stream

`GET /v1/sdk/projects/{projectKey}/environments/{environmentKey}/stream`

- Authenticate with the same SDK bearer client key as configuration reads.
- The SDK uses a streaming `fetch` request so it can set `Authorization` and `Last-Event-ID` headers without putting credentials in a URL.
- On initial connection, send `Last-Event-ID` with the SDK's installed revision when known. On reconnect, send the last event ID received. The server validates it as a non-negative integer no greater than the current revision; absent, malformed, negative, or ahead-of-current values mean “unknown.”
- Send `Content-Type: text/event-stream`, `Cache-Control: no-cache, no-transform`, and disable proxy buffering where supported.
- When the baseline is unknown or behind, emit an immediate event. Subsequent change events may coalesce revisions:

```text
id: 43
event: config.updated
data: {"revision":43}

```

- Event data contains only the `revision`; the SSE `id` is the same revision for reconnect tracking. The SDK fetches and validates the full snapshot after each event, reconnect, or stream close; it installs only a strictly newer revision.
- The cursor is carried in the `Last-Event-ID` header; there is no `afterVersion`
  query parameter (owner decision DP-001).
- Send an SSE comment heartbeat (`: keep-alive`) every 20 seconds. A heartbeat does not indicate database health or configuration freshness.
- Maximum connection lifetime is 5 minutes by default. The stream closes at that limit; the SDK reconnects with bounded exponential backoff and jitter and performs a full snapshot fetch. Configure the hosting request timeout at least 30 seconds longer than the stream lifetime.
- Revoking a key immediately rejects subsequent configuration and stream requests. An already-open stream carries revision hints only and may stay open until the server detects closure or its five-minute lifetime ends; the SDK's next snapshot fetch is rejected after revocation.
- Pre-stream failures use the shared JSON error format and HTTP status codes. After streaming headers are sent, failures are logged and counted, the server closes the stream, and the SDK reconnects; do not emit a success-shaped application error event.

## 7. Error format and status mapping

Every non-`304`, non-`204` API error uses:

```json
{
  "error": {
    "code": "VERSION_CONFLICT",
    "message": "The flag changed since it was read.",
    "details": [
      { "field": "expectedVersion", "issue": "Expected 3; current version is 4." }
    ],
    "requestId": "opaque-id"
  }
}
```

`details` may be an empty array. Messages are for people; clients branch only on stable `code` values.

| HTTP | Stable codes | Use |
|---|---|---|
| `400` | `MALFORMED_REQUEST`, `INVALID_CURSOR`, `INVALID_CONDITIONAL_HEADER` | Invalid JSON or malformed protocol/header values |
| `401` | `AUTHENTICATION_REQUIRED`, `INVALID_CREDENTIALS`, `INVALID_CLIENT_KEY`, `CLIENT_KEY_REVOKED`, `SESSION_EXPIRED` | Missing/invalid/expired credential |
| `403` | `FORBIDDEN`, `CSRF_FAILED` | Authenticated credential lacks route permission, or admin CSRF/origin validation failed |
| `404` | `NOT_FOUND`, `ENVIRONMENT_SCOPE_MISMATCH` | Missing resource or a valid SDK key used against a different project/environment |
| `409` | `VERSION_CONFLICT`, `KEY_ALREADY_EXISTS`, `RESOURCE_CONFLICT` | Stale expected flag version, duplicate immutable key, or other state conflict |
| `413` | `REQUEST_TOO_LARGE`, `SNAPSHOT_TOO_LARGE` | Request or resulting configuration exceeds documented size limit |
| `422` | `VALIDATION_ERROR`, `UNSUPPORTED_FLAG_TYPE`, `UNSUPPORTED_RULE_OPERATOR` | Well-formed request with invalid fields or unsupported v1 feature |
| `428` | `VERSION_REQUIRED` | Mutation omitted the required optimistic-concurrency token |
| `429` | `RATE_LIMITED` | Request limit exceeded; include `Retry-After` |
| `500` | `INTERNAL_ERROR` | Unexpected server failure; do not include stack traces or secrets |
| `503` | `DEPENDENCY_UNAVAILABLE` | Required database/dependency unavailable; existing SDK snapshot remains usable |

Missing `expectedVersion` or `expectedFlagVersion` returns `428 VERSION_REQUIRED`. A malformed token returns `422 VALIDATION_ERROR`. A stale token returns `409 VERSION_CONFLICT` with the current version when the resource exists. Malformed JSON is `400`. A client key presented to an admin endpoint is `403`, not `401`, because it is valid but has the wrong permission.

## 8. Endpoint inventory

The complete route inventory is the method/path/auth/request/success table in
section 4. Request and response schemas are defined in sections 2–7. Keep this
table as the single route inventory; implementation notes should link here rather
than duplicate it.

## 9. Review gates before implementation

- Firestore persistence and its SDK snapshot read model are deferred by owner decision
  DP-003 in `docs/DECISIONS-PENDING.md`. Revisit before a Firestore adapter is
  implemented; this draft does not select a projection or read-on-demand strategy.
- Confirm whether admin project/environment deletion remains excluded from v1 and how retained audit history interacts with any later deletion endpoint.
- Confirm that browser SDKs use `fetch`-based SSE rather than native `EventSource` so credentials remain in headers.
- Ensure all ADR-dependent field names, rule order, revision semantics, and client-key scope remain consistent with ADR-012, ADR-018, ADR-019, ADR-020, ADR-021, and ADR-022.
- Generate or maintain an OpenAPI 3.1 description from the approved contract when implementation begins; test request/response and error examples against it.
