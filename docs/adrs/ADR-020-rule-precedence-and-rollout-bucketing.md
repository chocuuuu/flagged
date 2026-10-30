# ADR-020: Rule precedence and deterministic rollout bucketing

**Status:** Proposed

**Supplements:** [ADR-011](./ADR-011-deterministic-rollout.md)

**Related decisions:** [ADR-019](./ADR-019-configuration-version-semantics.md), [ADR-022](./ADR-022-sdk-payload-and-client-visible-fields.md)

## Context

Flagged evaluates configuration locally in TypeScript SDKs, while the control plane persists it in Python-backed adapters. Rule ordering and percentage rollout bucketing must therefore have identical, testable behavior across implementations. The current schema supports a base flag state, percentage rollout, and targeting predicates but does not define precedence, missing-context behavior, or a cross-language hash specification.

## Decision

### Evaluation context and rule matching

- The calling application supplies an evaluation context with an `attributes` map of string keys to string values for targeting. It may also supply a stable, non-empty string `subjectKey` for percentage rollouts; when absent or empty, partial rollouts fail closed.
- Attribute names are matched exactly and case-sensitively. `equals` is exact, case-sensitive string equality. `contains` is a case-sensitive literal substring comparison.
- A missing attribute, null value, or non-string value never matches a rule. The evaluator does not coerce values to strings.
- Context values are runtime inputs and are not included in the SDK configuration snapshot.

### Precedence

Evaluate a flag in this order:

1. If the flag's `enabled` field is false, return false without evaluating rules or rollout.
2. Evaluate enabled targeting rules in their received order. The first matching rule returns true and takes precedence over percentage rollout.
3. If no rule matches, evaluate the integer `basisPoints`. `0` returns false and `10000` returns true without needing a subject key. For `basisPoints` from `1` through `9999`, a missing or empty `subjectKey` returns false; otherwise use the deterministic bucket below.

The initial rule model contains allow rules only: a match enables the flag. Deny rules and rule-specific return values are not part of this decision.

### Rule order and disabled rules

- Equal rule priorities are allowed. The server includes enabled rules only, sorted by ascending numeric `priority`, then by the canonical lowercase UUID string for the rule ID in ascending ordinal/bytewise string order as a stable tiebreaker. Implementations compare the canonical string form, not a database-specific UUID binary representation.
- Rule IDs are used only for server-side ordering and are not serialized into the SDK payload.
- The SDK evaluates rules in array order exactly as received. It does not sort or otherwise reorder them.
- A rule that is disabled is omitted from the SDK payload. Enabling or disabling a rule changes the client-visible snapshot and advances the environment revision when the payload changes. Editing an already-disabled rule does not advance the revision unless another client-visible field changes.

### Rollout bucketing

- Use synchronous 32-bit FNV-1a over this exact byte sequence:
  1. ASCII bytes for `flagged-rollout-v1`, then one zero byte.
  2. The flag key encoded as UTF-8, preceded by its byte length as an unsigned 32-bit big-endian integer.
  3. The subject key encoded as UTF-8, preceded by its byte length as an unsigned 32-bit big-endian integer.
- Initialize the hash to `2166136261`. For each byte, update `hash = ((hash XOR byte) * 16777619) mod 2^32`.
- Implementations must preserve exact 32-bit multiplication. In JavaScript, use `Math.imul((hash ^ byte), 16777619) >>> 0` (or an equivalent exact operation); ordinary `Number` multiplication can lose precision.
- Convert the unsigned hash to a bucket in `[0, 9999]` as `floor(hash * 10000 / 4294967296)`.
- The canonical rollout value is an integer `basisPoints` from `0` through `10000`, stored and transmitted as an integer in the database model and SDK payload. Admin API writes use the same integer representation. A UI may display a percentage, but must convert it to an exact integer basis-point value before submitting; values with more than two percentage decimal places are invalid.
- The subject is in the rollout when `bucket < basisPoints`. This rule gives explicit outcomes at the endpoints: zero basis points includes nobody, and 10000 basis points includes everybody regardless of subject key. For a partial rollout (1 through 9999 basis points), a missing or empty `subjectKey` fails closed and returns false.
- This is a deterministic distribution mechanism, not a cryptographic primitive. It must not be used for authentication, authorization, secret generation, or adversarial security decisions.

Test vectors:

| Flag key | Subject key | Unsigned FNV-1a hash | Bucket |
|---|---|---:|---:|
| `checkout` | `user-123` | `2698349097` | `6282` |
| `new_search` | `alice` | `1847041651` | `4300` |

For example, `user-123` is excluded from `checkout` at 6282 basis points because bucket `6282` is not less than `6282`; at 6283 basis points, it is included. This strict-boundary example is normative.

## Alternatives considered

### Random assignment per evaluation

Rejected because a subject could switch results between evaluations and across SDK instances.

### Cryptographic hashing

Rejected for the initial synchronous evaluation path. Rollout bucketing needs repeatability and adequate distribution, not secrecy or collision resistance. A standard, small 32-bit hash avoids asynchronous browser crypto APIs and added dependencies. It is explicitly not a security boundary.

### Use rule priority without a tiebreaker

Rejected because equal-priority rules could be returned in database-dependent order, producing different results across reads or adapters.

### Include disabled rules in the SDK payload

Rejected because disabled targeting logic is not needed for evaluation and should not be disclosed to browser clients.

## Consequences

Evaluation is deterministic and synchronous in both browser and server-side SDK implementations. The server is responsible for stable rule ordering; the SDK consumes that order as part of the snapshot contract. The 32-bit non-cryptographic hash is inexpensive but does not protect against a caller deliberately choosing subject keys to land in a desired bucket.

Changing the algorithm, byte encoding, bucketing conversion, rule precedence, or ordering is a behavioral SDK contract change and requires a new ADR and compatibility plan. The test vectors above must be shared by every implementation.

## Verification

Tests for the control plane and SDK implementations should establish that:

- both implementations produce the exact test-vector hashes and buckets;
- rollout results are stable across repeated evaluations and independent implementations;
- `enabled: false` always returns false; a matching enabled rule returns true before rollout; and no matching rule falls through to rollout;
- database, admin API, and SDK payload use integer basis points in the inclusive range 0–10000, and reject fractional, out-of-range, or non-integer values;
- rollout boundaries at 0, 10000, and one-basis-point increments behave as specified without floating-point percentage conversion;
- missing, null, and non-string attributes do not match; string `equals` and `contains` behavior is exact and case-sensitive;
- equal rule priorities are accepted; the server orders rules by priority and canonical lowercase UUID string tiebreaker, omits disabled rules, and the SDK preserves received order;
- missing or empty subject keys fail closed for partial rollouts but do not prevent an explicit matching rule or a `0`/`10000` basis-point rollout result.
