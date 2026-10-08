# ARCHITECTURE.md

# Flagged — Architecture

## 1. Architectural goal

Build a centralized control plane with decentralized, low-latency evaluation.

The central service answers:

> What configuration should exist?

The SDK answers:

> Given the locally cached configuration and this user's context, what should the application do?

---

# 2. High-level architecture

```text
                       CONTROL PLANE

                ┌─────────────────────┐
                │     Admin UI        │
                │   Astro + React     │
                └──────────┬──────────┘
                           │ HTTPS
                           ▼
                ┌─────────────────────┐
                │ Feature Flag API    │
                │ Python / FastAPI    │
                └───────┬───────┬─────┘
                        │       │
                        │       └───────── Audit
                        ▼
                 ┌───────────────┐
                 │ Source of     │
                 │ truth         │
                 └───────────────┘
                        │
                 update event
                        ▼
                 ┌───────────────┐
                 │ Event layer   │
                 │ SSE / PubSub  │
                 └───────┬───────┘
                         │

                    DATA PLANE

             ┌───────────┼───────────┐
             ▼           ▼           ▼
          SDK A        SDK B       SDK C
             │           │           │
        memory cache memory cache memory cache
             │           │           │
             ▼           ▼           ▼
        local eval   local eval   local eval
             │           │           │
             ▼           ▼           ▼
          App A        App B       Demo App
```

---

# 3. Control plane

Components:

- Admin UI
- Admin API
- persistence
- audit log
- configuration versioning
- update publishing

The control plane is allowed to be relatively slower because humans use it infrequently compared with flag evaluations.

---

# 4. Data plane

The client SDK is the data plane.

It should:

1. bootstrap configuration;
2. keep the latest valid configuration in memory;
3. evaluate flags locally;
4. periodically or continuously receive updates;
5. reconnect after failures;
6. fall back to safe defaults.

The normal evaluation path should not depend on the database.

---

# 5. Demo application flow

```text
Browser
  │
  ▼
Astro/React Demo Store
  │
  ▼
@Flagged/sdk
  │
  ├── memory snapshot
  │
  ▼
Evaluator
  │
  ├── flag state
  ├── target rules
  ├── rollout
  └── default
  │
  ▼
true / false / variant
```

---

# 6. Configuration lifecycle

## Bootstrap

```text
SDK starts
   ↓
GET /sdk/config
   ↓
validate response
   ↓
set local version
   ↓
ready
```

## Polling

```text
timer
  ↓
GET /sdk/config?afterVersion=42
  ↓
new version?
  ├── no → keep snapshot
  └── yes → atomically replace
```

## Streaming

```text
SDK
 │
 │ SSE connection
 ▼
/sdk/stream
 │
 └── CONFIG_UPDATED(version=43)
         ↓
    fetch/validate config
         ↓
    compare version
         ↓
    replace snapshot
```

---

# 7. Why versioning exists

Suppose:

```text
Update 42
Update 43
```

arrive in this order:

```text
43 arrives
42 arrives
```

The SDK must never move backward.

Rule:

```text
if incoming.version <= current.version:
    ignore
```

This is a simple but powerful consistency guard.

---

# 8. Percentage rollout

Use a stable hash:

```text
bucket = hash(flagKey + subjectKey) % 100
```

Then:

```text
bucket < percentage
```

means the user is included.

This creates stable assignment without server-side session storage.

---

# 9. Local Redis role

Redis is used to study shared caching and invalidation.

Development topology:

```text
API replica A ─┐
               ├── Redis
API replica B ─┘
```

The SDK still evaluates locally.

Redis is not intended to be in the SDK's normal evaluation path.

---

# 10. GCP architecture

```text
                GitHub
                   │
              GitHub Actions
                   │
                   ▼
            Artifact Registry
                   │
                   ▼
                Cloud Run
           ┌───────┴────────┐
           ▼                ▼
       Admin/API       SSE endpoint
           │                │
           ▼                │
        Firestore            │
           │                 │
           └───────┬─────────┘
                   ▼
                Pub/Sub
                   │
                   ▼
          configuration events
```

A simplified final cloud deployment may keep SSE and API in one Cloud Run service to avoid unnecessary service proliferation.

---

# 11. Why not create separate microservices?

The first version should be a modular monolith.

Reasons:

- lower operational complexity
- easier debugging
- fewer network boundaries
- easier local development
- enough complexity already exists in distributed configuration delivery

A later experiment may split the stream/update component if there is a measured reason.

---

# 12. Cloud Run principles

Services should be stateless.

Do not depend on:

- local filesystem for durable data
- process memory as global truth
- one specific instance

Each instance must be disposable.

---

# 13. Deployment path

```text
Developer
   ↓
Git branch
   ↓
Pull Request
   ↓
GitHub Actions
   ↓
tests
   ↓
build
   ↓
container
   ↓
Artifact Registry
   ↓
Cloud Run
```

Terraform manages the infrastructure.

Application configuration is injected at deployment time.

---

# 14. Local → cloud migration strategy

### Local

```text
PostgreSQL
Redis
FastAPI
Astro
SSE
Docker
```

### Cloud learning stage

```text
Cloud Run
Firestore
Pub/Sub
Artifact Registry
IAM
Cloud Logging
Terraform
```

The application domain layer should not have to be rewritten to understand cloud networking.

---

# 15. Architecture evolution

### Version 0

In-process flag dictionary.

### Version 1

FastAPI + PostgreSQL.

### Version 2

SDK + demo store.

### Version 3

Local cache + polling.

### Version 4

SSE updates.

### Version 5

Multiple API instances + Redis experiment.

### Version 6

GCP Cloud Run + Firestore.

### Version 7

Pub/Sub configuration propagation.

### Version 8

Observability, resilience, load testing.

---

# 16. Main trade-offs

## Central evaluation vs local evaluation

Local evaluation:

- faster
- resilient
- lower network cost
- more complex synchronization

Central evaluation:

- always current
- simpler client
- adds network latency
- creates a dependency on platform availability

Chosen: **local evaluation**.

## Polling vs SSE

Polling:

- simple
- resilient
- less infrastructure complexity
- slower propagation

SSE:

- near-real-time
- efficient updates
- connection/reconnect complexity

Chosen: **both, progressively**.

## PostgreSQL vs Firestore

PostgreSQL:

- stronger relational model
- familiar SQL
- excellent local learning environment

Firestore:

- managed
- serverless
- free-tier-compatible for small usage
- different query/data model

Chosen: **both, behind a repository boundary**.

## Redis vs in-memory cache

In-memory:

- fastest
- simplest
- per-instance only

Redis:

- shared
- introduces network latency and another failure mode
- useful for distributed caching experiments

Chosen: **memory first, Redis experiment second**.

