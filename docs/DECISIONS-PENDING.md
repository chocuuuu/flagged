# Decisions pending

These items affect architecture, persistence behavior, or the public HTTP/SDK
contract. Do not implement the affected contract until the owner records a choice.

## DP-001 — SDK stream cursor and event contract

**Evidence:** `docs/API-CONTRACT.md` and ADR-021 specify an SSE `config.updated`
event with `{"revision": N}` data and use `Last-Event-ID` for the installed revision
and reconnect cursor. `ARCHITECTURE.md` illustrates the same event name and revision
but does not define the wire-level cursor. No `afterVersion` query parameter is
currently defined.

**Options**

1. Keep the existing contract: `event: config.updated`, `data: {"revision": N}`,
   SSE `id: N`, and `Last-Event-ID` for the cursor.
2. Add `afterVersion` as the initial cursor query parameter while retaining
   `Last-Event-ID` for reconnects. Define precedence when both are supplied.
3. Replace the existing cursor convention with `afterVersion` for both initial
   connection and reconnects.

**Recommendation:** Option 1. It is already specified in ADR-021 and the draft API
contract; it avoids putting client state in a URL and does not add conflicting cursor
sources. If `afterVersion` is required, record its precedence and URL logging/privacy
implications before changing the contract.

**Status:** Resolved 2026-10-31 — option 1 selected. Keep the existing contract:
`config.updated`, `{"revision": N}`, SSE `id: N`, and `Last-Event-ID`. Do not add an
`afterVersion` query parameter.

## DP-002 — Admin audit-history route

**Evidence:** `SECURITY.md` gives admins permission to view audit history and PRD
FR-12 requires an audit log, but `docs/API-CONTRACT.md` explicitly leaves audit
retrieval unshaped. The endpoint inventory therefore has no audit read route.

**Options**

1. Add `GET /v1/admin/projects/{projectKey}/audit-events`, with optional
   `environmentKey`, cursor pagination, and redacted before/after values.
2. Add `GET /v1/admin/projects/{projectKey}/environments/{environmentKey}/audit-events`
   for environment-scoped reads, plus a separate project-level route only if needed.
3. Defer audit retrieval from v1 and amend the product/security requirements first.

**Recommendation:** Option 1, provided pagination, filters, and secret redaction are
specified in the contract before implementation. This supports project and
environment history with one route while keeping authorization in the admin API.

**Status:** Resolved 2026-10-31 — option 1 selected. Add the project-scoped route with
an optional environment filter. The exact filters, pagination, response shape, and
redaction rules must be defined in the API contract before implementation.

## DP-003 — Firestore SDK snapshot read model

**Evidence:** ADR-006 makes Firestore optional cloud persistence, while
`docs/API-CONTRACT.md` proposes a materialized `sdk_snapshots/{environmentId}`
document written atomically with source configuration and revision. The contract
labels this design as requiring review. No implementation evidence exists.

**Options**

1. Keep the proposed single-document projection as derived data, with atomic
   mutation/revision/audit/projection writes and explicit size limits.
2. Read the source documents to build snapshots on demand and measure the resulting
   read and latency behavior.
3. Defer the Firestore adapter; keep PostgreSQL as the only implemented datastore
   and revisit the cloud read model at the Firestore milestone.

**Recommendation:** Option 3 for the local-first project baseline. Before any
Firestore implementation, compare options 1 and 2 against transaction limits,
snapshot size, read volume, and current cost. This keeps the database source of truth
clear and avoids treating an unverified proposal as an accepted architecture.

**Status:** Resolved 2026-10-31 — option 3 selected. Defer the Firestore adapter; keep
PostgreSQL as the implemented source-of-truth baseline. Do not treat the
materialized-projection proposal as an accepted design. Re-evaluate the read model
before the Firestore milestone.

## Audit constraints and disposition

- The existing ADR files are all `Proposed`. `AGENTS.md` says an ADR becomes
  `Accepted` only in the milestone that implements and verifies its decision.
  Therefore the request to mark ADR-001–ADR-017 `Accepted` cannot be followed before
  implementation evidence exists; the tracker reflects the current status of all
  23 ADRs, including ADR-023.
- The existing worktree already has a deletion of tracked `jira/JIRA-BACKLOG.csv`.
  It is preserved. No file was restored or deleted by this audit.

All three owner choices above are resolved. DP-003 is a recorded deferral, not an
approval to implement Firestore. No open owner decision blocks the local-first
planning baseline; the final readiness report separately identifies items that
cannot be certified before implementation or a clean-clone run.

## Validation evidence and remaining gates (not owner decisions)

- Gitleaks 8.30.1 was installed for this local scan. Both
  `gitleaks detect --source . --no-git --redact --exit-code 1` and
  `gitleaks git . --redact --exit-code 1` passed with no findings; the history
  scan covered 28 local commits. Re-run before the first push if repository
  content changes afterward.
- Run `python scripts/generate_jira_csv.py --check` and
  `python scripts/check_consistency.py` in a clean clone after the audit changes
  are preserved. This dirty worktree also contains a pre-existing deletion of
  `jira/JIRA-BACKLOG.csv`, which this audit intentionally did not restore.
- Live cloud pricing review/provisioning is not required for Sprint 1 or the
  local-first baseline. Before any future live experiment, re-verify current
  official pricing, billing prerequisites, and cleanup, then obtain explicit
  approval as required by `COST-BOUNDARY.md`.
