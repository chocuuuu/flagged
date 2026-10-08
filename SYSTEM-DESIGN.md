# SYSTEM-DESIGN.md

# Flagged — System Design Learning Guide

## 1. Core system-design question

> How can a centralized platform distribute configuration to many application instances while allowing low-latency local evaluation and graceful behavior during outages?

Everything in this project should connect back to this question.

---

# 2. Capacity assumptions

This is a personal learning system, not a production SaaS.

Initial target:

```text
Projects: < 10
Environments/project: 3
Flags/environment: < 500
SDK clients: < 20 demo instances
Flag evaluations: up to 1,000/sec in synthetic tests
Configuration updates: < 10/sec in tests
```

These are test targets used for architecture experiments, not claims of production capacity.

---

# 3. Latency model

Central evaluation:

```text
app
 ↓
network
 ↓
flag service
 ↓
possibly database/cache
 ↓
network
 ↓
app
```

Local evaluation:

```text
app
 ↓
SDK
 ↓
memory
 ↓
result
```

Expected:

```text
local evaluation << network evaluation
```

Measure it instead of relying on intuition.

---

# 4. Consistency model

Configuration source of truth:

```text
database
```

Client state:

```text
eventually consistent snapshot
```

Desired property:

> After a successful configuration change, healthy clients converge to the new version within the target propagation window.

Not required:

> Every client changes at exactly the same instant.

---

# 5. Failure scenarios

## Database unavailable

Admin changes fail.

Existing SDK clients should continue evaluating their last configuration.

## Feature API unavailable

Existing clients use cached configuration.

New clients may use a default/fail-safe behavior.

## SSE connection lost

SDK:

```text
detect
↓
close/reconnect
↓
exponential backoff
↓
bootstrap/poll to catch up
```

## Duplicate update

Ignore based on version.

## Out-of-order update

Ignore older version.

## Corrupt payload

Reject and preserve previous snapshot.

## Redis unavailable

Fall back to in-memory behavior where safe.

## Pub/Sub duplicate

Consumer handles event idempotently.

---

# 6. Backpressure

The control plane can generate updates.

Consumers may process slower than producers.

Potential strategies:

- version coalescing
- latest-version fetch
- bounded in-memory queues
- reconnect bootstrap

For flag configuration, receiving every historical state is often less valuable than reaching the latest valid state quickly.

This is a key design insight to test.

---

# 7. Caching strategy

## SDK cache

Use:

```text
immutable snapshot
```

Benefits:

- lock-free-ish reads in normal usage
- easy reasoning
- simple rollback
- clear version semantics

## Redis

Used to explore:

```text
cache-aside
TTL
shared state
invalidation
```

Don't add Redis to every request merely because it exists.

---

# 8. Polling design

Baseline:

```text
pollInterval = 30s
```

Use ETag or version hints where practical.

Experiment with:

```text
5s
15s
30s
60s
```

Measure:

- propagation latency
- request volume
- stale window

---

# 9. SSE design

A stream event can be:

```json
{
  "type": "config.updated",
  "version": 43
}
```

The client can then:

```text
receive event
  ↓
fetch latest config
  ↓
validate
  ↓
compare version
  ↓
replace snapshot
```

Sending only "version changed" instead of the full config teaches an important concept:

> notifications and state transfer are different concerns.

---

# 10. Pub/Sub design

GCP path:

```text
Flag API
   ↓
publish config.updated
   ↓
Pub/Sub topic
   ↓
subscriber
   ↓
notify/update stream service
```

Assume at-least-once delivery.

Therefore:

```text
consumer = idempotent
```

Use:

- event ID
- version
- deterministic state update

---

# 11. Hot path vs cold path

## Hot path

```text
application
→ SDK
→ memory
→ evaluate
```

Must be extremely cheap.

## Cold/control path

```text
admin
→ API
→ database
→ publish
```

Can tolerate higher latency.

This is one of the core architectural choices.

---

# 12. Load-testing experiments

Experiment A:

```text
local evaluation
1k/sec
5k/sec
10k/sec
```

Experiment B:

```text
central evaluation
1k/sec
```

Experiment C:

```text
polling clients
10 / 100 / 1,000
```

Experiment D:

```text
SSE clients
10 / 100 / 1,000 synthetic connections
```

Measure:

- p50
- p95
- p99
- throughput
- errors
- CPU
- memory
- update propagation latency

---

# 13. Architecture questions to answer in the final report

1. Why is the database not in the evaluation path?
2. Why does the SDK keep configuration in memory?
3. Why use deterministic hashing for rollouts?
4. What consistency model does the system provide?
5. What happens when the control plane is down?
6. Why choose polling before SSE?
7. Why add Pub/Sub after SSE?
8. When is Redis useful?
9. Why is the service a modular monolith?
10. Why does local PostgreSQL differ from GCP Firestore?
11. What would break at 10x traffic?
12. What would change at 100x traffic?
13. Which components would you shard?
14. What would you make multi-region?
15. What would you keep eventually consistent?

---

# 14. Future architecture, not current scope

Possible future evolution:

```text
                    Global control plane
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
              Region A            Region B
                 │                   │
               edge                edge
                 │                   │
               SDKs                SDKs
```

Only discuss this until the core system is stable.

