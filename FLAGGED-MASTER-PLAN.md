# Flagged — Project Plan Package

## Distributed Feature Flag & Configuration Platform

This package is the planning baseline for a 12-week / 60-session learning project.

The project is designed to be:

- local-first;
- cloud-later;
- system-design heavy;
- test and debugging driven;
- AI-assisted but not AI-dependent;
- GitHub-centered;
- Terraform-managed;
- as close to zero-cost as practical.

## Start here

1. Read `PRD.md`.
2. Read `ARCHITECTURE.md`.
3. Read `SYSTEM-DESIGN.md`.
4. Read `SKILLS.md`.
5. Read `AGENTS.md`.
6. Start Sprint 1.
7. Track progress in `progress/PROGRESS.md`.
8. Manage execution in `jira/JIRA-BACKLOG.md`.

## Project stack

```text
Frontend      Astro + React + TypeScript
Backend       Python + FastAPI
Local DB      PostgreSQL
Cache lab     Redis
SDK           TypeScript
Containers    Docker / Docker Compose
IaC           Terraform
CI/CD         GitHub Actions
Cloud         GCP
Cloud DB      Firestore
Events        Pub/Sub
Runtime       Cloud Run
Observability Cloud Logging/Monitoring
```

## Important database decision

PostgreSQL and Firestore are used for different stages intentionally.

The project does **not** require two production databases.

- PostgreSQL = rich local relational learning environment.
- Firestore = low-ops GCP deployment experiment with free-tier-compatible usage.
- Repository boundary = makes the persistence decision explicit and testable.

Read ADR-005, ADR-006, and ADR-007 together.

## Cost warning

Do not provision paid managed Redis/Memorystore as part of the standard plan.

Do not provision Cloud SQL unless an explicit cost-approved experiment is being performed.

Cloud free tiers are quotas, not guarantees of zero spend. Re-check official pricing immediately before cloud provisioning.

## Files

- `CLAUDE.md`
- `AGENTS.md`
- `PRD.md`
- `DATA.md`
- `ARCHITECTURE.md`
- `SECURITY.md`
- `SYSTEM-DESIGN.md`
- `SKILLS.md`
- `COST-BOUNDARY.md`
- `SPRINT-CALENDAR.md`
- `progress/PROGRESS.md`
- `progress/DAILY-PLAN.md`
- `jira/JIRA-BACKLOG.md`
- `jira/JIRA-BACKLOG.csv`
- `docs/adrs/`

## Suggested repo layout

```text
Flagged/
├── apps/
│   ├── dashboard/
│   └── demo-store/
├── services/
│   └── flag-api/
├── packages/
│   ├── sdk/
│   └── evaluator/
├── infrastructure/
│   └── terraform/
├── tests/
├── docs/
│   ├── adrs/
│   ├── benchmarks/
│   └── runbooks/
├── docker-compose.yml
├── PRD.md
├── DATA.md
├── ARCHITECTURE.md
├── SECURITY.md
├── SYSTEM-DESIGN.md
├── SKILLS.md
├── AGENTS.md
└── CLAUDE.md
```


---

# FILE: CLAUDE.md

# CLAUDE.md

> Project: **Flagged — Distributed Feature Flag & Configuration Platform**
> Canonical agent instructions live in `AGENTS.md`. This file contains Claude Code-specific workflow guidance.

## 1. Project mission

The goal is not to generate a feature-flag platform as quickly as possible. The goal is to **learn cloud engineering and distributed-system design through deliberate implementation, testing, debugging, and iteration**.

AI is an engineering assistant, not the author of the learning process.

## 2. Non-negotiable AI behavior

Before modifying code for a non-trivial task, the agent should:

1. Explain the architectural purpose of the change.
2. Identify assumptions and dependencies.
3. State what files/components it expects to touch.
4. State what tests should prove the change.
5. Implement the smallest useful increment.
6. Run or specify the relevant tests.
7. Explain failures instead of hiding them.
8. Never remove a test simply because it fails.
9. Never introduce a dependency without explaining why it is needed.
10. Never create secrets, credentials, real API keys, or personal data.
11. Never silently change architecture, storage semantics, or public SDK behavior.

## 3. Learning-first rule

When a task introduces a new concept, the agent must first provide a short "Concept checkpoint":

- What problem does this concept solve?
- Why is it needed here?
- What simpler approach did we have before?
- What trade-off are we introducing?
- How can the user verify it experimentally?

Examples:

- Redis: explain cache-aside and invalidation before implementing it.
- SSE: explain long-lived HTTP connections before adding the stream.
- Pub/Sub: explain at-least-once delivery and idempotency before wiring events.
- Firestore: explain document semantics and free-tier constraints before migrating.
- Cloud Run: explain stateless deployment and scale-to-zero behavior before deployment.

## 4. Preferred AI loop

Use:

```text
Understand → Design → Implement → Test → Debug → Measure → Document
```

Do not use:

```text
Prompt → Generate entire application → Hope it works
```

## 5. Debugging protocol

When a test or runtime behavior fails:

1. Reproduce it.
2. Isolate the boundary where behavior diverges.
3. Form one or more hypotheses.
4. Add the smallest useful diagnostic.
5. Fix the root cause.
6. Add/regress a test.
7. Document the lesson when architectural.

## 6. Code-generation limits

Avoid:

- giant one-shot implementations
- unrelated refactors
- "cleanup" during feature work
- framework replacement without an ADR
- speculative abstractions
- premature microservices

Prefer:

- small commits
- narrow pull requests
- explicit interfaces
- typed request/response models
- tests next to the behavior they protect
- boring infrastructure that is easy to destroy and recreate

## 7. Dependency policy

Every new dependency needs:

- purpose
- alternatives considered
- maintenance/complexity impact
- cost impact, if any
- whether standard-library functionality could reasonably solve the need

## 8. Security policy

Never:

- commit `.env`
- hard-code API keys
- place admin credentials in the client SDK
- expose admin API credentials to the demo application
- log access tokens or secrets
- disable TLS verification in normal code
- broaden IAM permissions "temporarily" without documenting and reverting them

## 9. Git workflow

Use:

```text
main
└── feature/<short-name>
```

For meaningful changes:

- issue-linked branch
- focused commit
- tests included
- PR description
- review/checks
- merge
- delete branch

Commit style:

```text
feat(scope): ...
fix(scope): ...
test(scope): ...
refactor(scope): ...
docs(scope): ...
infra(scope): ...
chore(scope): ...
```

## 10. Agent autonomy

The agent may autonomously:

- read the repository
- propose implementation steps
- create tests
- run local tools
- make small code changes within the approved task
- update documentation

The agent should pause and ask for user direction only when:

- a requirement is genuinely ambiguous and materially changes architecture;
- an external paid service may be created;
- a destructive cloud action could create cost/data loss;
- credentials or permissions are required that the user has not explicitly provided.

For ordinary implementation ambiguity, choose the smallest reversible option and document the decision.

## 11. Cloud cost gate

Before introducing any managed GCP resource that can incur charges:

```text
1. Identify the service.
2. Check its current pricing/free tier.
3. Estimate this project's expected usage.
4. Tell the user whether the step is optional or required.
5. Prefer a local/emulated alternative when the learning objective is unchanged.
6. Add deletion/cleanup commands.
```

Never create an always-on paid resource merely because a reference architecture commonly uses it.

## 12. Definition of done for AI-assisted work

A task is not done merely because code was written.

It is done when:

- behavior matches acceptance criteria;
- relevant tests pass;
- failure behavior is understood;
- documentation is updated when necessary;
- no secrets are introduced;
- the user can explain the key design decision;
- the change has a focused commit.



---

# FILE: AGENTS.md

# AGENTS.md

# Flagged — Agent Operating Contract

## Mission

Build **Distributed Feature Flag & Configuration Platform** as a 12-week, learning-first cloud engineering project.

The repository must remain understandable to a developer who did not watch the implementation happen.

## Architecture principles

1. **Local-first, cloud-later.**
2. **Control plane and data plane are explicitly separated.**
3. **Feature evaluation is local whenever practical.**
4. **The database is the source of truth; SDK memory is a distributed cache.**
5. **Configuration propagation must be observable and versioned.**
6. **Stateless services are preferred.**
7. **External managed services are introduced only when they teach a useful cloud concept.**
8. **Every distributed behavior must have a failure story.**
9. **Public SDK behavior is treated as an API contract.**
10. **Infrastructure is reproducible with Terraform.**

## Technology choices

### Backend
- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- PostgreSQL for local development
- Redis locally for caching experiments
- pytest + httpx
- Ruff
- mypy where practical

### Frontend
- Astro
- React
- TypeScript
- Tailwind CSS
- browser-focused feature-flag SDK

### SDK
- TypeScript
- local in-memory configuration
- REST configuration bootstrap
- polling
- SSE streaming
- deterministic evaluation
- safe default/fallback behavior

### Cloud
- Google Cloud Run
- Firestore (cloud deployment path)
- Pub/Sub
- Artifact Registry
- IAM
- Cloud Logging / Monitoring
- Terraform
- GitHub Actions

### Local infrastructure
- Docker
- Docker Compose
- PostgreSQL
- Redis
- optional Pub/Sub emulator or local event-bus adapter

## Rules for architecture changes

Changes to the following require an ADR:

- primary datastore
- evaluation location
- propagation mechanism
- authentication model
- SDK API contract
- cloud provider/service selection
- caching model
- deployment topology
- repository structure

## Required engineering artifacts

The repository should maintain:

```text
README.md
PRD.md
DATA.md
ARCHITECTURE.md
SECURITY.md
SYSTEM-DESIGN.md
SKILLS.md
CLAUDE.md
AGENTS.md
docs/adrs/
docs/runbooks/
docs/benchmarks/
```

## AI collaboration protocol

For each meaningful task:

```text
Context
→ Concept checkpoint
→ Small design
→ Implementation
→ Tests
→ Failure/edge cases
→ Measurement
→ Documentation
```

The agent must not hide complexity from the learner.

## No-shotgun coding

Do not generate the entire platform in one request. Work in the Jira sequence and preserve the ability to understand, test, and debug each layer.

## Cloud cost safety

Before any cloud provisioning:

- state the services that will be created;
- state whether each can incur charges;
- use the smallest configuration;
- add cleanup commands;
- prefer free-tier-compatible usage;
- verify the current price page when pricing could have changed.



---

# FILE: SKILLS.md

# SKILLS.md

# Flagged — Learning & Skills Roadmap

## Learning objective

By the end of the project, the learner should be able to explain, build, test, deploy, and troubleshoot a small production-style feature-flag platform.

The project is intentionally organized as a progression from **single-process software → distributed application → cloud deployment**.

---

# Skill matrix

| Area | Target | Why it matters |
|---|---|---|
| Python/FastAPI | Intermediate | Core backend implementation |
| SQL/PostgreSQL | Intermediate | Source-of-truth data modeling |
| TypeScript | Intermediate | SDK and frontend |
| Astro/React | Intermediate | Admin dashboard + demo app |
| HTTP | Intermediate | APIs, caching, SSE |
| SDK design | Intermediate | Client integration boundary |
| Caching | Intermediate | Low-latency local reads |
| Consistency | Intermediate | Configuration propagation |
| Event-driven architecture | Intermediate | Pub/Sub update distribution |
| Distributed systems | Intermediate | Failure, retries, ordering, stale data |
| Observability | Intermediate | Measure real behavior |
| Security | Intermediate | API keys, roles, least privilege |
| Docker | Intermediate | Reproducible local infrastructure |
| Terraform | Intermediate | Infrastructure as Code |
| GitHub Actions | Intermediate | CI/CD |
| GCP | Intermediate | Cloud deployment and operations |
| Load testing | Intermediate | Performance validation |

---

# Learning sequence

## Stage 1 — Domain and HTTP
Learn:

- what a feature flag is
- deployment vs release
- environments
- flag evaluation
- control plane vs data plane
- REST
- HTTP status codes
- ETags / If-None-Match concept

Deliverable: a written explanation of the system in your own words.

## Stage 2 — Python backend
Learn:

- FastAPI routing
- Pydantic validation
- dependency injection
- SQLAlchemy
- Alembic migrations
- service/repository boundaries
- transaction boundaries
- exception handling

Deliverable: working CRUD API with tests.

## Stage 3 — Data modeling
Learn:

- relational schema
- primary/foreign keys
- uniqueness
- indexes
- audit/event tables
- optimistic versioning

Deliverable: reproducible local database.

## Stage 4 — SDK design
Learn:

- package APIs
- configuration bootstrap
- in-memory state
- evaluation purity
- timeout behavior
- fallback behavior

Deliverable: usable TypeScript SDK.

## Stage 5 — Caching
Learn:

- cache-aside
- TTL
- stale data
- invalidation
- cache stampede
- memory vs Redis

Deliverable: benchmark before/after caching.

## Stage 6 — Configuration propagation
Learn:

- polling
- SSE
- reconnect
- event versioning
- eventual consistency
- idempotent update handling

Deliverable: measurable propagation latency.

## Stage 7 — Event-driven cloud
Learn:

- Pub/Sub
- publisher/subscriber model
- at-least-once delivery
- retries
- duplicate messages
- dead-letter concepts

Deliverable: cloud propagation path.

## Stage 8 — Cloud operations
Learn:

- Cloud Run
- stateless services
- IAM
- Artifact Registry
- Terraform state
- deployment variables
- logging
- monitoring

Deliverable: reproducible GCP deployment.

## Stage 9 — Security
Learn:

- admin authentication
- scoped SDK keys
- authorization
- threat modeling
- secret handling
- rate limiting
- auditability

## Stage 10 — Performance and resilience
Learn:

- latency percentiles
- throughput
- concurrency
- load generation
- failure injection
- graceful degradation

Deliverable: benchmark and failure report.

---

# Recommended study references

Use official documentation first:

- Python documentation
- FastAPI documentation
- SQLAlchemy documentation
- PostgreSQL documentation
- Astro documentation
- React documentation
- TypeScript documentation
- Redis documentation
- Docker documentation
- Terraform documentation
- Google Cloud documentation
- OpenTelemetry documentation
- OpenFeature documentation
- GitHub Actions documentation

Use commercial feature-flag documentation such as LaunchDarkly as a **reference implementation model**, not as an instruction manual.



---

# FILE: PRD.md

# PRD.md

# Flagged
## Distributed Feature Flag & Configuration Platform

**Status:** Approved planning baseline  
**Duration:** 12 weeks / 60 working sessions  
**Primary goal:** Learn cloud and system design by building, testing, breaking, and improving a real distributed platform.

---

# 1. Problem statement

Software teams often want to deploy code without immediately releasing a new behavior to every user.

Traditional deployment-only release flow couples:

```text
code deployment
      +
user exposure
```

This creates operational pressure when:

- a feature is incomplete;
- a feature needs a gradual rollout;
- only internal/beta users should receive it;
- production behavior must be disabled quickly;
- a team wants to separate deployment from release.

A feature-flag platform separates these concerns.

The central platform stores and manages configuration, while consuming applications evaluate flags locally from configuration distributed by the platform.

---

# 2. Product vision

Build a small-scale alternative to the core capabilities of a commercial feature-management platform.

The product should let a developer:

1. Create a project.
2. Create environments.
3. Create feature flags.
4. Enable/disable a flag.
5. Configure a percentage rollout.
6. Define simple targeting rules.
7. Issue a client SDK key for an environment.
8. Allow a demo application to retrieve configuration.
9. Evaluate flags locally in the SDK.
10. Propagate updates without requiring application redeployment.
11. Observe configuration propagation and evaluation behavior.

---

# 3. Real-world analogy

A production application contains the new behavior, but a runtime decision determines whether users enter that code path.

Example:

```text
new_checkout = OFF

Application:
if flag("new_checkout"):
    new_checkout()
else:
    old_checkout()
```

Turning the flag off does not necessarily roll back the deployment. It changes runtime behavior.

Commercial products such as LaunchDarkly and standards/projects such as OpenFeature provide related concepts. This project implements a learning-focused subset.

---

# 4. Target user

Primary user:

**Developer / small engineering team**

They need to:

- safely introduce a feature;
- test new behavior with a limited population;
- disable behavior quickly;
- manage different environments;
- integrate an application through an SDK.

Secondary user:

**Platform administrator**

They manage projects, environments, flags, rules, and audit information.

---

# 5. Demo application

Only one demo application is required:

## Flagged Demo Store

An intentionally small Astro + React storefront.

Pages/features:

- Home
- Product list
- Product detail
- Cart
- Checkout

The storefront exists to demonstrate the platform. It is not intended to become a complete e-commerce product.

Demo flags:

```text
new_checkout
new_product_card
holiday_banner
```

---

# 6. Functional requirements

## FR-01 Projects

Users can create and view projects.

## FR-02 Environments

Each project supports:

- development
- staging
- production

## FR-03 Feature flags

A flag has:

- stable key
- display name
- description
- type
- enabled state
- environment
- version
- timestamps

## FR-04 Boolean evaluation

The SDK must support:

```text
isEnabled(flagKey, context)
```

## FR-05 Percentage rollout

Support deterministic user bucketing.

## FR-06 Targeting

Initial targeting should support a deliberately small rule set:

```text
attribute equals value
attribute contains value
```

Stretch:

- AND/OR groups
- multiple rules
- variants

## FR-07 Configuration bootstrap

SDK can fetch an environment configuration.

## FR-08 Local evaluation

After configuration is loaded, normal flag evaluations should not require a network request.

## FR-09 Polling

SDK can periodically refresh configuration.

## FR-10 Streaming

SDK can optionally maintain an SSE connection for update events.

## FR-11 Versioning

Every configuration update has a monotonically increasing version.

The SDK must ignore an older configuration received after a newer one.

## FR-12 Audit log

Record:

- who changed a flag
- what changed
- previous value
- new value
- timestamp

## FR-13 Safe fallback

When the platform cannot be reached, the SDK uses:

1. last known good configuration;
2. otherwise caller-specified default.

## FR-14 API keys

SDK/client keys must be scoped to a project/environment and must not have administrative privileges.

---

# 7. Non-functional requirements

## NFR-01 Low evaluation latency

Local evaluation should be orders of magnitude cheaper/faster than a network round trip.

Exact target will be benchmarked rather than assumed.

## NFR-02 Propagation target

Target configuration propagation:

**< 5 seconds under normal demo conditions**

This is an engineering target, not a correctness guarantee.

## NFR-03 Availability

A temporary flag service outage should not automatically break the demo application.

## NFR-04 Idempotency

Repeated update events must not corrupt SDK state.

## NFR-05 Observability

The system should expose enough telemetry to answer:

- How long does evaluation take?
- How quickly do updates propagate?
- How many updates fail?
- How often is stale configuration used?

## NFR-06 Reproducibility

A new developer should be able to run the core system locally using documented commands.

## NFR-07 Cost

Core development target: **$0**.

Cloud deployment target: **near $0 and designed around free-tier-compatible usage**.

---

# 8. Scope by phase

## MVP

- Python/FastAPI API
- PostgreSQL
- admin authentication
- project/environment/flag CRUD
- boolean evaluation
- TypeScript SDK
- in-memory configuration
- demo store integration
- tests
- Docker Compose

## Phase 2

- percentage rollout
- targeting
- audit logs
- versioning
- polling
- Redis cache experiment

## Phase 3

- SSE
- reconnection
- stale-cache strategy
- observability
- load testing
- failure injection

## Phase 4

- GCP deployment
- Firestore adapter
- Pub/Sub propagation
- IAM
- Artifact Registry
- Terraform
- GitHub Actions

---

# 9. Explicit non-goals

Do not build initially:

- enterprise SSO
- SAML
- billing
- multi-region deployment
- A/B experimentation analytics
- complex rule DSL
- mobile SDKs
- native Java SDK
- Kubernetes
- service mesh
- multi-cloud deployment
- a full production e-commerce backend

These may be discussed, not implemented.

---

# 10. Success criteria

The project succeeds when:

1. A developer can create a flag from the dashboard.
2. The demo application consumes it through the SDK.
3. A flag can be turned on/off without rebuilding the demo app.
4. A 10% rollout deterministically selects users.
5. SDK evaluations normally execute locally.
6. The SDK can refresh configuration via polling.
7. The SDK can receive updates via SSE.
8. Update versions prevent stale writes.
9. The system survives temporary control-plane failures using cached configuration.
10. Tests cover core behavior and failure cases.
11. The system is containerized.
12. The infrastructure can be recreated with Terraform.
13. A GCP deployment exists within the project's cost guardrails.
14. A final report explains architecture decisions and measured behavior.



---

# FILE: DATA.md

# DATA.md

# Flagged — Data Model

## 1. Data principles

The feature flag database is the **control-plane source of truth**.

SDK memory and Redis are caches, not sources of truth.

Configuration distributed to clients is versioned.

---

# 2. Logical entities

```text
Project
  └── Environment
        ├── Flag
        │     ├── Target Rules
        │     └── Variants
        ├── Client Key
        └── Configuration Version

Audit Event
```

---

# 3. Local PostgreSQL schema

## projects

| Column | Type | Notes |
|---|---|---|
| id | UUID | PK |
| key | varchar | unique |
| name | varchar | required |
| description | text | nullable |
| created_at | timestamptz | required |
| updated_at | timestamptz | required |

## environments

| Column | Type | Notes |
|---|---|---|
| id | UUID | PK |
| project_id | UUID | FK |
| key | varchar | development/staging/production |
| name | varchar | display value |
| created_at | timestamptz | required |
| updated_at | timestamptz | required |

Constraint:

```text
UNIQUE(project_id, key)
```

## feature_flags

| Column | Type | Notes |
|---|---|---|
| id | UUID | PK |
| environment_id | UUID | FK |
| key | varchar | unique within environment |
| name | varchar | display value |
| description | text | nullable |
| type | varchar | boolean/variant |
| enabled | boolean | base state |
| rollout_percentage | numeric | 0–100 |
| version | bigint | optimistic version |
| created_at | timestamptz | required |
| updated_at | timestamptz | required |

Constraint:

```text
UNIQUE(environment_id, key)
```

## targeting_rules

| Column | Type | Notes |
|---|---|---|
| id | UUID | PK |
| flag_id | UUID | FK |
| attribute | varchar | e.g. plan |
| operator | varchar | equals/contains |
| value | text | comparison target |
| priority | integer | evaluation order |
| enabled | boolean | rule switch |

## client_keys

| Column | Type | Notes |
|---|---|---|
| id | UUID | PK |
| environment_id | UUID | FK |
| key_prefix | varchar | safe display prefix |
| key_hash | varchar | stored secret hash |
| status | varchar | active/revoked |
| created_at | timestamptz | required |
| revoked_at | timestamptz | nullable |

**Important:** full client secrets should not be stored in plaintext.

## audit_events

| Column | Type | Notes |
|---|---|---|
| id | UUID | PK |
| project_id | UUID | FK |
| environment_id | UUID | nullable FK |
| actor_id | UUID | admin identity |
| action | varchar | flag.updated, flag.created, etc. |
| entity_type | varchar | flag/environment/etc. |
| entity_id | UUID | affected entity |
| before_json | jsonb | previous state |
| after_json | jsonb | new state |
| created_at | timestamptz | event time |

---

# 4. Configuration document

SDK bootstrap response:

```json
{
  "environment": "production",
  "version": 42,
  "generatedAt": "2026-01-01T00:00:00Z",
  "flags": [
    {
      "key": "new_checkout",
      "type": "boolean",
      "enabled": true,
      "rollout": {
        "percentage": 10
      },
      "rules": []
    }
  ]
}
```

The SDK treats this as immutable configuration and replaces its in-memory snapshot atomically.

---

# 5. Why PostgreSQL locally and Firestore in GCP?

This is **not because the product fundamentally needs two databases**.

It is a deliberate learning and cost decision.

### Local PostgreSQL teaches

- normalized relational design
- joins
- foreign keys
- uniqueness
- transactions
- migration management
- indexes
- query behavior

### GCP Firestore teaches

- document modeling
- managed/serverless persistence
- read/write billing
- document-oriented access patterns
- cloud-native data access
- free-tier-aware design

The repository/service boundary means application behavior should not depend directly on SQL or Firestore SDK calls.

```text
Service layer
      │
      ▼
FlagRepository
   ┌──┴───────────┐
   ▼              ▼
Postgres       Firestore
adapter         adapter
```

This creates a useful engineering exercise:

> How much of the domain can remain unchanged when the persistence model changes?

---

# 6. Important trade-off

Firestore is **not a drop-in PostgreSQL replacement**.

Firestore changes:

- query patterns
- transaction semantics
- schema flexibility
- indexing
- data modeling
- consistency expectations
- cost behavior

Therefore the migration to Firestore is intentionally documented and tested rather than hidden behind a fake "universal database."

---

# 7. Caching data

## SDK

Primary cache:

```text
in-memory immutable snapshot
```

Properties:

- versioned
- read-only during evaluation
- atomically replaced
- supports last-known-good fallback

## Redis

Used as a learning experiment for:

- shared cache
- cache-aside
- invalidation
- TTL
- multiple API instances

Redis is not required for the final zero-cost cloud deployment.

---

# 8. Data retention

For the learning project:

- active flags: retained
- audit logs: retained for project lifetime
- revoked client keys: retained as metadata
- old flag versions: retain at least the latest N versions
- raw operational logs: rely on platform retention policies

Avoid unlimited historical growth.

---

# 9. Data invariants

1. Flag keys are unique per environment.
2. Configuration versions increase monotonically.
3. A revoked client key cannot access SDK configuration.
4. Admin keys cannot be used by the client SDK.
5. A lower version cannot replace a higher local snapshot.
6. Audit records are append-only.
7. A flag evaluation never mutates configuration.


---

# FILE: ARCHITECTURE.md

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



---

# FILE: SECURITY.md

# SECURITY.md

# Flagged — Security Model

## 1. Security objective

Protect:

- admin operations
- flag configuration integrity
- client credentials
- audit records
- cloud infrastructure

while keeping the demo simple enough to understand.

---

# 2. Threat model

Primary threats:

| Threat | Example |
|---|---|
| Credential theft | leaked admin token |
| Privilege escalation | SDK key calling admin API |
| Configuration tampering | unauthorized flag change |
| Client key abuse | public endpoint scraping |
| Secret leakage | tokens committed to Git |
| Replay/stale config | old update overwrites new state |
| Data exposure | admin-only configuration exposed |
| Denial of service | excessive flag/config requests |
| Misconfigured IAM | over-privileged Cloud Run service |
| Logging leakage | secret in logs |

---

# 3. Trust zones

```text
                 Untrusted
                    │
                    ▼
              Demo Browser
                    │
             scoped client key
                    │
                    ▼
              SDK endpoint
                    │
        ┌───────────┴───────────┐
        │                       │
   Control plane           Data plane
        │                       │
   admin auth              client auth
        │                       │
        ▼                       ▼
      DB/config            published config
```

---

# 4. Authentication

## Admin

For the learning MVP:

- username/email + password
- session/JWT
- secure password hashing

Do not invent cryptographic algorithms. Use a reputable password-hashing library.

## Client SDK

Use an environment-scoped client key.

The client key can read SDK-safe configuration but must not:

- create flags
- modify flags
- read admin audit data
- read credentials

---

# 5. Authorization

Minimum roles:

```text
ADMIN
VIEWER
```

Admin:

- create/update/delete configuration
- manage client keys
- view audit history

Viewer:

- read configuration through dashboard
- cannot mutate flags

SDK:

- evaluation/read-only configuration only

---

# 6. Key handling

Store only a hash of client secrets where possible.

Display only:

```text
ff_client_abc123••••••
```

When a key is created:

```text
generate
   ↓
show once
   ↓
hash
   ↓
store hash
```

Revocation:

```text
active → revoked
```

---

# 7. Secret management

Local:

```text
.env
.env.example
```

`.env` must be ignored by Git.

Cloud:

- prefer platform-injected secrets/variables;
- Secret Manager is optional if needed;
- never embed admin credentials in frontend assets.

Because this project prioritizes zero cost, any paid-secret-management feature must be evaluated before adoption.

---

# 8. SDK/browser security boundary

The browser SDK is not a trusted administrator.

A public client key should expose only the minimum configuration necessary for flag evaluation.

Never put:

```text
ADMIN_SECRET
DATABASE_URL
JWT_SIGNING_SECRET
SERVICE_ACCOUNT_KEY
```

into the browser.

---

# 9. API protections

Admin API:

- authentication required
- authorization required
- input validation
- rate limiting
- secure headers
- controlled CORS
- structured error messages

SDK API:

- scoped client authentication
- caching
- ETags/version checks
- rate limits appropriate to the learning environment

---

# 10. Configuration integrity

Every distributed configuration has a version.

SDK rule:

```text
accept incoming version
ONLY IF
incoming.version > local.version
```

This protects against stale updates.

---

# 11. Network security

Use HTTPS in deployed environments.

Never disable certificate validation to "make it work."

For local development, HTTP is acceptable within the developer machine.

---

# 12. Audit logs

Every mutation should generate an audit event containing:

- actor
- action
- resource
- timestamp
- old value
- new value

Do not log secrets.

---

# 13. Cloud IAM

Principle:

> grant the minimum permission needed.

The Cloud Run service should not automatically have broad project-level permissions.

Example desired separation:

```text
Cloud Run runtime
  ├── Firestore access
  └── Pub/Sub publish/consume as required
```

It should not have:

```text
Owner
Editor
Broad project admin
```

permissions.

IAM API usage itself is free according to Google's current pricing documentation.

---

# 14. Abuse scenarios

Test:

```text
invalid client key
revoked client key
expired admin session
oversized payload
too many requests
malformed targeting rule
attempt to mutate SDK endpoint
```

---

# 15. Security testing

Tools/practices:

- pytest security cases
- dependency audit
- secret scanning
- GitHub secret scanning where available
- Gitleaks
- OWASP API Security guidance
- manual abuse tests

---

# 16. Security definition of done

No release is complete if:

- secrets are committed;
- admin API can be called without authorization;
- SDK key can mutate configuration;
- revoked keys still work;
- stale configuration can overwrite newer configuration;
- sensitive values are visible in logs.


---

# FILE: SYSTEM-DESIGN.md

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



---

# FILE: COST-BOUNDARY.md

# COST-BOUNDARY.md

## Current cost policy

Target: **$0 for development** and **near-$0 for cloud demonstrations**.

The cloud portion is optional until the local system works.

## Current GCP pricing facts verified 2026-10-08

- Cloud Run request-based billing currently includes a free monthly allocation of 2 million requests, 180,000 vCPU-seconds, and 360,000 GiB-seconds under the published free tier.
- Pub/Sub currently includes the first 10 GiB of basic message-delivery throughput per billing account each calendar month.
- Firestore Standard currently provides a free tier of 1 GiB stored data, 50,000 document reads/day, 20,000 writes/day, 20,000 deletes/day, and 10 GiB/month outbound data transfer for one qualifying database.
- IAM API usage is free.
- Cloud Logging currently provides 50 GiB/project/month of logging storage in the published free allotment; retention beyond default periods can introduce charges.
- Artifact Registry currently shows up to 0.5 GiB of storage free per billing account before storage charges apply.
- Memorystore for Redis is provisioned infrastructure and is billed even when idle; do not include it in the default zero-cost cloud architecture.
- Cloud SQL is a paid managed service outside applicable trials/credits; it is not the default database for this project.

## Cost gates

Before cloud deployment:

- Create a billing budget/alert.
- Never use "min instances" on Cloud Run unless there is a learning reason.
- Avoid large container resources.
- Keep log volume low.
- Delete unused Artifact Registry images.
- Use the default Firestore database if relying on the free tier.
- Do not create Memorystore for the final project.
- Do not create a Cloud SQL instance for the normal path.

## Optional paid experiment

Cloud SQL may be used only as a documented experiment if the user has free credits or explicitly approves potential charges.

The project remains complete without it.

## Important

Free tiers are quotas, not a guarantee that the project can never incur charges. Pricing, free quotas, eligible regions, and billing requirements can change. Re-check official pricing pages immediately before provisioning.


---

# FILE: SPRINT-CALENDAR.md

# SPRINT-CALENDAR.md

| Sprint | Sessions | Focus | Major outcome |
|---:|---|---|---|
| 1 | 1–5 | Foundation & Domain | Reproducible local workspace |
| 2 | 6–10 | Python API & Database | FastAPI + PostgreSQL skeleton |
| 3 | 11–15 | Flag Management | Core flag CRUD + tests |
| 4 | 16–20 | Dashboard | Admin UI |
| 5 | 21–25 | SDK | Local evaluation + demo integration |
| 6 | 26–30 | Rollouts & Targeting | Deterministic evaluation |
| 7 | 31–35 | Caching & Polling | Low-latency config refresh |
| 8 | 36–40 | SSE & Consistency | Streaming update path |
| 9 | 41–45 | Resilience & Testing | Failure + benchmark evidence |
| 10 | 46–50 | GCP Foundation | Terraform + Cloud Run |
| 11 | 51–55 | Cloud Data & Events | Firestore + Pub/Sub |
| 12 | 56–60 | CI/CD & Finalization | Reproducible cloud system + final report |


---

# FILE: JIRA-BACKLOG.md

# JIRA-BACKLOG.md

# Flagged — Jira-Style Sprint Board

**Cadence:** 12 sprints × 5 working sessions = 60 sessions  
**Workflow:** Backlog → Ready → In Progress → Code Review → QA → Done

## Board conventions

### Issue hierarchy

```text
Epic
 └── Story
      └── Task
           └── Subtask
```

### Recommended Jira fields

- Issue Type
- Summary
- Description
- Epic Link
- Parent
- Sprint
- Priority
- Story Points
- Acceptance Criteria
- Learning Objective
- Dependencies
- GitHub Branch
- Status

- EPIC-1 — Foundation
- EPIC-2 — Backend & Data
- EPIC-3 — Flag Management
- EPIC-4 — Dashboard
- EPIC-5 — SDK
- EPIC-6 — Evaluation & Targeting
- EPIC-7 — Caching & Polling
- EPIC-8 — Streaming & Consistency
- EPIC-9 — Observability & Resilience
- EPIC-10 — GCP Infrastructure
- EPIC-11 — Cloud Data & Events
- EPIC-12 — CI/CD & Finalization

---

# Sprint 1 — Foundation & Domain

**Duration:** 5 working sessions

## FF-101 — Project charter and glossary

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 1  
**Epic:** EPIC-1

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-101-1** — Write problem statement
- [ ] **FF-101-2** — Define control/data plane terms
- [ ] **FF-101-3** — Write first architecture sketch

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-102 — Repository bootstrap

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 1  
**Epic:** EPIC-1

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-102-1** — Create monorepo structure
- [ ] **FF-102-2** — Configure Python tooling
- [ ] **FF-102-3** — Configure frontend/SDK workspace

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-103 — Local infrastructure

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 1  
**Epic:** EPIC-1

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-103-1** — Create Docker Compose
- [ ] **FF-103-2** — Run PostgreSQL locally
- [ ] **FF-103-3** — Add health checks and startup documentation

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-104 — Engineering workflow

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 1  
**Epic:** EPIC-1

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-104-1** — Set branch strategy
- [ ] **FF-104-2** — Add commit conventions
- [ ] **FF-104-3** — Create issue/PR templates

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 2 — Python API & Database

**Duration:** 5 working sessions

## FF-201 — FastAPI foundation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 2  
**Epic:** EPIC-2

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-201-1** — Create app factory
- [ ] **FF-201-2** — Add health/readiness endpoints
- [ ] **FF-201-3** — Configure structured error handling

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-202 — Database layer

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 2  
**Epic:** EPIC-2

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-202-1** — Configure SQLAlchemy
- [ ] **FF-202-2** — Create Alembic baseline
- [ ] **FF-202-3** — Implement DB session lifecycle

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-203 — Core schema

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 2  
**Epic:** EPIC-2

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-203-1** — Create projects/environments tables
- [ ] **FF-203-2** — Create feature_flags table
- [ ] **FF-203-3** — Add uniqueness/index constraints

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-204 — API tests

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 2  
**Epic:** EPIC-2

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-204-1** — Create pytest fixtures
- [ ] **FF-204-2** — Write CRUD integration tests
- [ ] **FF-204-3** — Add invalid-input tests

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 3 — Flag Management & Audit

**Duration:** 5 working sessions

## FF-301 — Project/environment CRUD

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 3  
**Epic:** EPIC-3

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-301-1** — Build create/list/update/delete endpoints
- [ ] **FF-301-2** — Validate environment keys
- [ ] **FF-301-3** — Document endpoint behavior

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-302 — Feature flag CRUD

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 3  
**Epic:** EPIC-3

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-302-1** — Build create/list/update/delete
- [ ] **FF-302-2** — Add version incrementing
- [ ] **FF-302-3** — Add optimistic update protection

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-303 — Audit trail

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 3  
**Epic:** EPIC-3

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-303-1** — Create audit_events table
- [ ] **FF-303-2** — Record mutations
- [ ] **FF-303-3** — Add audit read endpoint

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-304 — Admin authentication

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 3  
**Epic:** EPIC-3

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-304-1** — Implement login
- [ ] **FF-304-2** — Protect admin routes
- [ ] **FF-304-3** — Add authorization tests

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 4 — Dashboard

**Duration:** 5 working sessions

## FF-401 — Astro/React shell

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 4  
**Epic:** EPIC-4

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-401-1** — Create dashboard layout
- [ ] **FF-401-2** — Add routing/navigation
- [ ] **FF-401-3** — Configure API client

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-402 — Project/environment UI

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 4  
**Epic:** EPIC-4

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-402-1** — Project list
- [ ] **FF-402-2** — Environment selector
- [ ] **FF-402-3** — Environment state/loading/error UI

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-403 — Flag management UI

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 4  
**Epic:** EPIC-4

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-403-1** — Flag table
- [ ] **FF-403-2** — Create/edit form
- [ ] **FF-403-3** — Enable/disable control

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-404 — Audit UX

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 4  
**Epic:** EPIC-4

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-404-1** — Audit history page
- [ ] **FF-404-2** — Before/after display
- [ ] **FF-404-3** — Error and empty states

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 5 — SDK & Local Evaluation

**Duration:** 5 working sessions

## FF-501 — SDK package

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 5  
**Epic:** EPIC-5

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-501-1** — Create package structure
- [ ] **FF-501-2** — Define public SDK API
- [ ] **FF-501-3** — Add build/test pipeline

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-502 — Configuration bootstrap

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 5  
**Epic:** EPIC-5

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-502-1** — Implement config fetch
- [ ] **FF-502-2** — Validate config schema
- [ ] **FF-502-3** — Store immutable snapshot

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-503 — Evaluation engine

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 5  
**Epic:** EPIC-5

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-503-1** — Boolean evaluation
- [ ] **FF-503-2** — Default/fallback evaluation
- [ ] **FF-503-3** — Evaluation unit-test matrix

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-504 — Demo Store integration

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 5  
**Epic:** EPIC-5

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-504-1** — Integrate SDK
- [ ] **FF-504-2** — Add new checkout flag
- [ ] **FF-504-3** — Demonstrate live switch without rebuild

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 6 — Environments, Rollouts & Targeting

**Duration:** 5 working sessions

## FF-601 — Client keys

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 6  
**Epic:** EPIC-6

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-601-1** — Generate scoped keys
- [ ] **FF-601-2** — Hash stored secrets
- [ ] **FF-601-3** — Build revoke flow

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-602 — Environment isolation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 6  
**Epic:** EPIC-6

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-602-1** — Prevent cross-environment reads
- [ ] **FF-602-2** — Test staging/production separation
- [ ] **FF-602-3** — Add SDK environment configuration

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-603 — Percentage rollout

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 6  
**Epic:** EPIC-6

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-603-1** — Implement stable hashing
- [ ] **FF-603-2** — Build 0/50/100% cases
- [ ] **FF-603-3** — Test deterministic user assignment

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-604 — Targeting rules

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 6  
**Epic:** EPIC-6

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-604-1** — Define v1 rule model
- [ ] **FF-604-2** — Implement equals/contains
- [ ] **FF-604-3** — Test rule precedence

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 7 — Caching & Polling

**Duration:** 5 working sessions

## FF-701 — In-memory configuration cache

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 7  
**Epic:** EPIC-7

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-701-1** — Atomic snapshot replacement
- [ ] **FF-701-2** — Track version/age
- [ ] **FF-701-3** — Expose cache diagnostics

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-702 — Polling

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 7  
**Epic:** EPIC-7

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-702-1** — Add polling scheduler
- [ ] **FF-702-2** — Handle timeouts/errors
- [ ] **FF-702-3** — Measure stale window

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-703 — HTTP cache optimization

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 7  
**Epic:** EPIC-7

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-703-1** — Implement ETag/version conditional requests
- [ ] **FF-703-2** — Test 304 behavior
- [ ] **FF-703-3** — Benchmark request reduction

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-704 — Redis experiment

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 7  
**Epic:** EPIC-7

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-704-1** — Run Redis locally
- [ ] **FF-704-2** — Implement shared cache adapter
- [ ] **FF-704-3** — Document when Redis helps

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 8 — SSE & Consistency

**Duration:** 5 working sessions

## FF-801 — SSE stream

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 8  
**Epic:** EPIC-8

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-801-1** — Create stream endpoint
- [ ] **FF-801-2** — Define event schema
- [ ] **FF-801-3** — Handle client disconnects

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-802 — SDK stream client

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 8  
**Epic:** EPIC-8

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-802-1** — Connect to SSE
- [ ] **FF-802-2** — Update snapshot from events
- [ ] **FF-802-3** — Add stream status diagnostics

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-803 — Reconnect behavior

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 8  
**Epic:** EPIC-8

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-803-1** — Exponential backoff
- [ ] **FF-803-2** — Catch-up bootstrap
- [ ] **FF-803-3** — Test connection interruption

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-804 — Consistency controls

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 8  
**Epic:** EPIC-8

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-804-1** — Reject stale versions
- [ ] **FF-804-2** — Handle duplicates
- [ ] **FF-804-3** — Test out-of-order events

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 9 — Observability, Resilience & Load

**Duration:** 5 working sessions

## FF-901 — Structured observability

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 9  
**Epic:** EPIC-9

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-901-1** — Add request logs
- [ ] **FF-901-2** — Add evaluation telemetry
- [ ] **FF-901-3** — Add propagation metrics

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-902 — Tracing/metrics

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 9  
**Epic:** EPIC-9

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-902-1** — Instrument service boundaries
- [ ] **FF-902-2** — Expose latency metrics
- [ ] **FF-902-3** — Measure propagation delay

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-903 — Failure injection

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 9  
**Epic:** EPIC-9

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-903-1** — Break database
- [ ] **FF-903-2** — Break stream connection
- [ ] **FF-903-3** — Test stale-cache fallback

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-904 — Load testing

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 9  
**Epic:** EPIC-9

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-904-1** — Create Locust scenarios
- [ ] **FF-904-2** — Measure p50/p95/p99
- [ ] **FF-904-3** — Write performance report

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 10 — Terraform & GCP Foundation

**Duration:** 5 working sessions

## FF-1001 — Cost guardrails

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 10  
**Epic:** EPIC-10

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1001-1** — Create budget/alert
- [ ] **FF-1001-2** — Document free-tier assumptions
- [ ] **FF-1001-3** — Write cleanup checklist

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1002 — Terraform foundation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 10  
**Epic:** EPIC-10

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1002-1** — Create provider/module layout
- [ ] **FF-1002-2** — Create state configuration
- [ ] **FF-1002-3** — Add variables/outputs

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1003 — Artifact Registry

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 10  
**Epic:** EPIC-10

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1003-1** — Create repository
- [ ] **FF-1003-2** — Build container locally
- [ ] **FF-1003-3** — Push versioned image

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1004 — Cloud Run foundation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 10  
**Epic:** EPIC-10

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1004-1** — Deploy stateless API
- [ ] **FF-1004-2** — Configure environment variables
- [ ] **FF-1004-3** — Validate scale-to-zero behavior

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 11 — Firestore, Pub/Sub & IAM

**Duration:** 5 working sessions

## FF-1101 — Firestore adapter

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 11  
**Epic:** EPIC-11

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1101-1** — Map local domain to documents
- [ ] **FF-1101-2** — Implement repository methods
- [ ] **FF-1101-3** — Run parity tests vs PostgreSQL

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1102 — Pub/Sub propagation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 11  
**Epic:** EPIC-11

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1102-1** — Create topic/subscription
- [ ] **FF-1102-2** — Publish configuration events
- [ ] **FF-1102-3** — Consume and handle duplicates

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1103 — GCP IAM

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 11  
**Epic:** EPIC-11

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1103-1** — Create least-privilege runtime identity
- [ ] **FF-1103-2** — Limit Firestore permissions
- [ ] **FF-1103-3** — Limit Pub/Sub permissions

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1104 — Cloud observability

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 11  
**Epic:** EPIC-11

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1104-1** — Configure useful logs
- [ ] **FF-1104-2** — Validate log volume
- [ ] **FF-1104-3** — Create basic operational dashboard/queries

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Sprint 12 — CI/CD, Cloud Validation & Finalization

**Duration:** 5 working sessions

## FF-1201 — GitHub Actions CI

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 12  
**Epic:** EPIC-12

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1201-1** — Lint workflow
- [ ] **FF-1201-2** — Unit/integration test workflow
- [ ] **FF-1201-3** — Build artifact workflow

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1202 — Deployment workflow

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 12  
**Epic:** EPIC-12

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1202-1** — Deploy Cloud Run from trusted branch
- [ ] **FF-1202-2** — Use environment configuration
- [ ] **FF-1202-3** — Add rollback procedure

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1203 — End-to-end validation

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 12  
**Epic:** EPIC-12

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1203-1** — Test cloud SDK bootstrap
- [ ] **FF-1203-2** — Test Pub/Sub/SSE propagation
- [ ] **FF-1203-3** — Test failure fallback

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.
## FF-1204 — Final engineering package

**Issue Type:** Story  
**Priority:** High  
**Story Points:** 3–5  
**Sprint:** Sprint 12  
**Epic:** EPIC-12

**Definition of done:**

- [ ] Story behavior works locally.
- [ ] Tests cover the important path and at least one failure case.
- [ ] Documentation/notes explain the design.
- [ ] No secrets or paid infrastructure are introduced accidentally.
- [ ] Focused Git commit/PR exists.

**Subtasks:**

- [ ] **FF-1204-1** — Review ADRs
- [ ] **FF-1204-2** — Write architecture/benchmark report
- [ ] **FF-1204-3** — Record final demo and retrospective

**Learning checkpoint:** Explain what architectural concept this story introduced before marking it Done.

---

# Cross-cutting Tasks

## Documentation

- [ ] Keep `PRD.md` aligned with scope changes.
- [ ] Keep `ARCHITECTURE.md` aligned with real implementation.
- [ ] Add an ADR for material architecture changes.
- [ ] Maintain `SYSTEM-DESIGN.md` with measured evidence.
- [ ] Maintain `SECURITY.md` as security controls evolve.

## GitHub

- [ ] Protect `main`.
- [ ] Require CI checks before merge.
- [ ] Link PRs to Jira issues.
- [ ] Keep commits focused.
- [ ] Tag milestone releases.

## AI collaboration

- [ ] Use concept checkpoint before unfamiliar implementation.
- [ ] Ask AI to explain failing tests rather than patch blindly.
- [ ] Keep an AI/dev journal of notable lessons.
- [ ] Review AI-generated code for correctness and security.

## Final demo checklist

- [ ] Create a feature flag.
- [ ] Toggle it from the dashboard.
- [ ] See the demo app change without rebuilding.
- [ ] Configure a 10% rollout.
- [ ] Demonstrate deterministic assignment.
- [ ] Disconnect the service and demonstrate cached behavior.
- [ ] Show a configuration update reaching clients.
- [ ] Show metrics/logs.
- [ ] Show Terraform deployment.
- [ ] Explain at least three trade-offs.


---

# FILE: PROGRESS.md

# PROGRESS.md

# Flagged — 60-Day Progress Tracker

## How to use

Each day is one focused learning/engineering session. A day does not mean "finish all code"; it means complete the learning target, record evidence, and commit progress.

Suggested session structure:

```text
20–30 min  Learn/read
60–120 min Implement
20–45 min  Test/debug
10 min     Notes/commit
```

## Daily tracker

- [ ] Day 01 — Project charter, terminology, environment setup
- [ ] Day 02 — Read/annotate feature-flag concepts and LaunchDarkly/OpenFeature models
- [ ] Day 03 — Define control plane vs data plane; draw first architecture
- [ ] Day 04 — Repository bootstrap; GitHub branch/commit conventions
- [ ] Day 05 — Local Docker Compose skeleton
- [ ] Day 06 — FastAPI app shell and health endpoint
- [ ] Day 07 — Pydantic models and API conventions
- [ ] Day 08 — SQLAlchemy setup and database connection
- [ ] Day 09 — Alembic migrations
- [ ] Day 10 — Project/environment schema
- [ ] Day 11 — Flag schema
- [ ] Day 12 — CRUD API for projects/environments
- [ ] Day 13 — CRUD API for flags
- [ ] Day 14 — Validation/error handling
- [ ] Day 15 — API integration tests
- [ ] Day 16 — Admin authentication
- [ ] Day 17 — Authorization boundaries
- [ ] Day 18 — Audit event model
- [ ] Day 19 — Audit trail implementation
- [ ] Day 20 — Admin API cleanup and docs
- [ ] Day 21 — Astro + React dashboard shell
- [ ] Day 22 — Project/environment screens
- [ ] Day 23 — Flag list/create/edit UI
- [ ] Day 24 — Flag enable/disable workflow
- [ ] Day 25 — Dashboard tests
- [ ] Day 26 — SDK package skeleton
- [ ] Day 27 — SDK bootstrap endpoint
- [ ] Day 28 — Immutable in-memory config
- [ ] Day 29 — Boolean evaluation
- [ ] Day 30 — Demo Store integration
- [ ] Day 31 — Environment/client-key model
- [ ] Day 32 — Percentage rollout design
- [ ] Day 33 — Deterministic hashing implementation
- [ ] Day 34 — Targeting rules v1
- [ ] Day 35 — Evaluation precedence and test matrix
- [ ] Day 36 — Polling implementation
- [ ] Day 37 — ETag/version optimization
- [ ] Day 38 — Stale configuration and fallback
- [ ] Day 39 — Redis cache experiment
- [ ] Day 40 — Multi-instance cache behavior
- [ ] Day 41 — SSE endpoint
- [ ] Day 42 — SDK SSE client
- [ ] Day 43 — Reconnect/backoff behavior
- [ ] Day 44 — Out-of-order/duplicate update handling
- [ ] Day 45 — Propagation-latency benchmark
- [ ] Day 46 — Structured logging
- [ ] Day 47 — Metrics and traces
- [ ] Day 48 — Failure injection
- [ ] Day 49 — Load testing
- [ ] Day 50 — Performance tuning and report
- [ ] Day 51 — GCP project cost guardrails
- [ ] Day 52 — Terraform foundation
- [ ] Day 53 — Cloud Run deployment
- [ ] Day 54 — Firestore adapter
- [ ] Day 55 — Pub/Sub integration
- [ ] Day 56 — GCP IAM hardening
- [ ] Day 57 — GitHub Actions CI
- [ ] Day 58 — CD/deploy workflow
- [ ] Day 59 — End-to-end cloud validation
- [ ] Day 60 — Final demo, ADR review, documentation, retrospective

## Sprint tracker

- [ ] Sprint 1 — Domain, repo, local environment
- [ ] Sprint 2 — Python API + database foundation
- [ ] Sprint 3 — Core flag management + audit
- [ ] Sprint 4 — Admin dashboard
- [ ] Sprint 5 — SDK + local evaluation
- [ ] Sprint 6 — Environments + rollouts + targeting
- [ ] Sprint 7 — Polling + caching
- [ ] Sprint 8 — SSE + consistency
- [ ] Sprint 9 — Observability + resilience + load testing
- [ ] Sprint 10 — Terraform + GCP foundation
- [ ] Sprint 11 — Firestore + Pub/Sub + IAM
- [ ] Sprint 12 — CI/CD + cloud validation + final documentation

## ADR tracker

- [ ] ADR-001 — Local-first development and cloud-later migration
- [ ] ADR-002 — Modular monolith before microservices
- [ ] ADR-003 — Python + FastAPI for the control plane
- [ ] ADR-004 — Astro + React for dashboard and demo app
- [ ] ADR-005 — PostgreSQL as local source of truth
- [ ] ADR-006 — Firestore as default GCP persistence path
- [ ] ADR-007 — Persistence repository boundary
- [ ] ADR-008 — Evaluate feature flags in the SDK
- [ ] ADR-009 — Polling before SSE before Pub/Sub
- [ ] ADR-010 — Monotonic configuration versions
- [ ] ADR-011 — Deterministic hashing for percentage rollouts
- [ ] ADR-012 — Scoped read-only client keys
- [ ] ADR-013 — Do not require managed Redis
- [ ] ADR-014 — Cloud Run for stateless application hosting
- [ ] ADR-015 — Terraform for infrastructure
- [ ] ADR-016 — GitHub Actions for CI/CD
- [ ] ADR-017 — Observability is a core requirement

## Cost safety checklist

- [ ] Budget/alert configured before cloud provisioning
- [ ] No always-on paid cache created
- [ ] No unnecessary Cloud SQL instance created
- [ ] Cloud Run min instances = 0 unless deliberately testing otherwise
- [ ] Logs are bounded
- [ ] Artifact images are cleaned up
- [ ] Firestore free-tier database is the default path
- [ ] Pub/Sub usage monitored
- [ ] GCP resources deleted after experiments

## Evidence to record

For each major milestone, record:

```text
What I built:
What I learned:
What broke:
Why it broke:
How I fixed it:
What test proves it:
What trade-off I made:
What I would change at 10x scale:
Commit:
```


---

# FILE: progress/DAILY-PLAN.md

# DAILY-PLAN.md

# Flagged — 60-Working-Session Execution Plan

## Working assumption

- 5 sessions/week
- 12 weeks
- 2–4 focused hours/session
- Longer sessions may compress the schedule; shorter sessions may extend it
- The goal is learning evidence, not speed

## Session template

```text
1. Learn        20–45 min
2. Design       15–30 min
3. Implement    60–120 min
4. Test/debug   20–45 min
5. Document     10–20 min
6. Commit       5–10 min
```

## Phase 1 — Understand and bootstrap

### Day 1 — Project charter
Goal: understand exactly what a feature flag service solves.
Tools: GitHub, VS Code, Claude Code, Gemini.
Deliverable: problem statement + glossary.
Test: explain deployment vs release, control plane vs data plane without notes.
Commit: `docs: add project charter and glossary`

### Day 2 — Study reference architectures
Goal: inspect LaunchDarkly/OpenFeature concepts.
Deliverable: one-page comparison of commercial/reference concepts.
Experiment: identify which concepts are in/out of scope.
Commit: `docs: document feature flag domain concepts`

### Day 3 — First architecture
Goal: draw control/data-plane architecture.
Tools: Mermaid, draw.io/Excalidraw.
Deliverable: architecture v0.
Checkpoint: explain why database is not in the evaluation hot path.
Commit: `docs: add initial system architecture`

### Day 4 — Monorepo
Goal: create repository structure and boundaries.
Tools: Git, GitHub, pnpm, uv.
Deliverable: apps/services/packages/docs directories.
Test: clean clone setup.
Commit: `chore: bootstrap monorepo`

### Day 5 — Docker Compose
Goal: create local reproducible infrastructure.
Tools: Docker, PostgreSQL.
Deliverable: compose file + health checks.
Test: destroy/recreate environment successfully.
Commit: `infra: add local database compose setup`

## Phase 2 — Python/API/database

### Day 6 — FastAPI shell
Goal: create backend application and health endpoints.
Tools: FastAPI, pytest.
Test: unit + HTTP health check.
Commit: `feat(api): add fastapi service shell`

### Day 7 — Validation
Goal: learn Pydantic request/response validation.
Deliverable: API error contract.
Test: malformed payload cases.
Commit: `feat(api): add request validation`

### Day 8 — SQLAlchemy
Goal: connect service layer to PostgreSQL.
Deliverable: DB session dependency.
Test: connection test + transaction rollback fixture.
Commit: `feat(db): add sqlalchemy integration`

### Day 9 — Alembic
Goal: learn schema migrations.
Deliverable: first migration.
Experiment: migrate up/down in a clean database.
Commit: `infra(db): add alembic migrations`

### Day 10 — Core schema
Goal: implement projects/environments.
Deliverable: tables, constraints, indexes.
Test: duplicate environment rejection.
Commit: `feat(db): add project and environment models`

## Phase 3 — Flag management

### Day 11 — Flag model
Goal: model feature flags and version field.
Test: unique key per environment.
Commit: `feat(flag): add feature flag model`

### Day 12 — Flag CRUD
Goal: build create/list/update/delete.
Test: API integration suite.
Commit: `feat(flag): add flag crud endpoints`

### Day 13 — Versioning
Goal: prevent lost updates.
Experiment: simulate two clients updating the same flag.
Commit: `feat(flag): add optimistic version checks`

### Day 14 — Audit events
Goal: make changes observable.
Test: each mutation creates an audit record.
Commit: `feat(audit): record configuration changes`

### Day 15 — Admin authentication
Goal: protect control-plane endpoints.
Test: unauthorized/forbidden/success cases.
Commit: `feat(auth): protect admin endpoints`

## Phase 4 — Dashboard

### Day 16 — Astro/React shell
Goal: build dashboard skeleton.
Tools: Astro, React, TypeScript, Tailwind.
Commit: `feat(dashboard): add application shell`

### Day 17 — Project/environment UI
Goal: browse configuration scope.
Test: loading/error/empty states.
Commit: `feat(dashboard): add project environment views`

### Day 18 — Flag management UI
Goal: create/edit/toggle flags.
Test: API integration from browser.
Commit: `feat(dashboard): add flag management`

### Day 19 — Audit UI
Goal: inspect who changed configuration.
Commit: `feat(dashboard): add audit history`

### Day 20 — Dashboard hardening
Goal: validation, accessibility, error UX.
Test: browser smoke tests.
Commit: `fix(dashboard): harden admin workflows`

## Phase 5 — SDK and evaluation

### Day 21 — SDK contract
Goal: design public SDK API before implementation.
Deliverable: README examples + type definitions.
Commit: `docs(sdk): define client contract`

### Day 22 — Bootstrap
Goal: fetch environment configuration.
Test: malformed/timeout/401 responses.
Commit: `feat(sdk): add configuration bootstrap`

### Day 23 — Immutable cache
Goal: safely store configuration in memory.
Test: atomic replacement and snapshot reads.
Commit: `feat(sdk): add in memory config store`

### Day 24 — Evaluation
Goal: implement boolean evaluation.
Test: deterministic unit matrix.
Commit: `feat(sdk): add boolean evaluation`

### Day 25 — Demo store integration
Goal: integrate SDK into the demo application.
Demo: toggle a checkout UI without rebuilding.
Commit: `feat(demo): integrate feature flag sdk`

## Phase 6 — Rollouts and targeting

### Day 26 — Client keys
Goal: scope read-only SDK credentials.
Test: admin key rejected by SDK endpoint.
Commit: `feat(auth): add scoped client keys`

### Day 27 — Environment isolation
Goal: prevent cross-environment access.
Test: production client cannot read staging.
Commit: `feat(auth): enforce environment isolation`

### Day 28 — Percentage rollout
Goal: deterministic hashing.
Experiment: same user remains in same bucket.
Commit: `feat(eval): add deterministic percentage rollout`

### Day 29 — Targeting rules
Goal: support equals/contains.
Test: rule order and fallback cases.
Commit: `feat(eval): add targeting rules`

### Day 30 — Evaluation matrix
Goal: document precedence.
Deliverable: decision table.
Test: comprehensive rules + rollout matrix.
Commit: `test(eval): expand evaluation behavior matrix`

## Phase 7 — Caching and polling

### Day 31 — SDK age/version diagnostics
Goal: track snapshot age/version.
Commit: `feat(sdk): expose configuration diagnostics`

### Day 32 — Polling
Goal: periodically refresh configuration.
Test: server unavailable while polling.
Commit: `feat(sdk): add configuration polling`

### Day 33 — ETag/version optimization
Goal: reduce unnecessary payloads.
Test: 304/no-change path.
Commit: `feat(api): add conditional configuration fetch`

### Day 34 — Stale fallback
Goal: define last-known-good behavior.
Experiment: shut down API and keep demo running.
Commit: `feat(sdk): add stale configuration fallback`

### Day 35 — Redis lab
Goal: compare in-memory and shared cache.
Tools: Redis, Docker.
Deliverable: benchmark + trade-off notes.
Commit: `docs(cache): document redis experiment`

## Phase 8 — SSE and consistency

### Day 36 — SSE fundamentals
Goal: understand long-lived HTTP connections.
Deliverable: minimal SSE proof of concept.
Commit: `feat(stream): add sse proof of concept`

### Day 37 — Production-ish stream endpoint
Goal: stream version/update events.
Test: multiple clients.
Commit: `feat(stream): add configuration update stream`

### Day 38 — SDK stream
Goal: consume update events.
Commit: `feat(sdk): consume sse updates`

### Day 39 — Reconnect
Goal: exponential backoff and catch-up.
Test: terminate/restart server.
Commit: `feat(sdk): add stream reconnect handling`

### Day 40 — Ordering/idempotency
Goal: reject duplicates/out-of-order messages.
Test: versions 10, 12, 11.
Commit: `test(sdk): add update ordering guarantees`

## Phase 9 — Observability/resilience/performance

### Day 41 — Structured logging
Goal: logs with request IDs, environment, flag/config version.
Commit: `feat(obs): add structured logging`

### Day 42 — Metrics
Goal: measure evaluation latency and refresh failures.
Commit: `feat(obs): add evaluation metrics`

### Day 43 — Propagation measurement
Goal: measure admin change → client update.
Experiment: 100 update events.
Commit: `test(obs): measure configuration propagation`

### Day 44 — Failure injection
Goal: break DB, API, and stream intentionally.
Deliverable: failure matrix.
Commit: `test(resilience): add failure scenarios`

### Day 45 — Load testing
Goal: establish baseline with Locust.
Measure: p50/p95/p99, throughput, errors.
Commit: `test(perf): add load test scenarios`

## Phase 10 — GCP foundation

### Day 46 — Cost guardrails
Goal: configure budget/alerts and cleanup procedures.
Deliverable: cost checklist.
Commit: `docs(cost): add gcp cost guardrails`

### Day 47 — Terraform structure
Goal: provider, variables, outputs, state.
Test: plan with no changes.
Commit: `infra: bootstrap terraform`

### Day 48 — Artifact Registry
Goal: build/push versioned image.
Test: pull and run image locally.
Commit: `infra: add artifact registry`

### Day 49 — Cloud Run
Goal: deploy stateless API.
Test: scale-to-zero and cold start behavior.
Commit: `infra: deploy api to cloud run`

### Day 50 — Cloud logging/operations
Goal: inspect cloud logs and runtime behavior.
Commit: `ops: document cloud run operations`

## Phase 11 — Firestore/Pub/Sub/IAM

### Day 51 — Firestore model
Goal: map relational domain to documents.
Deliverable: mapping document and ADR.
Commit: `docs(data): document firestore mapping`

### Day 52 — Firestore adapter
Goal: implement repository adapter.
Test: domain-level parity suite.
Commit: `feat(db): add firestore repository`

### Day 53 — Pub/Sub topic
Goal: publish configuration-change events.
Test: event payload and version.
Commit: `feat(events): publish config updates`

### Day 54 — Pub/Sub consumer
Goal: consume events idempotently.
Test: duplicate delivery.
Commit: `feat(events): consume config updates`

### Day 55 — IAM hardening
Goal: least-privilege runtime identity.
Test: denied permission outside required resources.
Commit: `infra(security): tighten gcp iam`

## Phase 12 — CI/CD and finalization

### Day 56 — CI
Goal: lint + tests + build on pull request.
Commit: `ci: add github actions checks`

### Day 57 — CD
Goal: controlled deployment to Cloud Run.
Test: rollback procedure.
Commit: `ci: add cloud deployment workflow`

### Day 58 — Cloud E2E
Goal: test dashboard → API → Firestore → Pub/Sub → SDK/SSE.
Commit: `test(e2e): validate cloud architecture`

### Day 59 — Final benchmark and docs
Goal: compare baseline vs final system.
Deliverable: benchmark report and architecture evolution diagram.
Commit: `docs: add final benchmark report`

### Day 60 — Final capstone
Goal: perform complete demo and retrospective.
Deliverables:
- demo recording
- architecture walkthrough
- security walkthrough
- cost review
- ADR review
- "what I learned" retrospective
Commit: `docs: finalize project documentation`

## Completion standard

Do not mark a day complete because the code "exists."

Mark it complete when the learner can:

- explain the concept;
- demonstrate the behavior;
- show a test;
- describe a failure mode;
- point to the Git commit;
- state what remains imperfect.


---

# ADR Index and Decisions

## ADR-001 — Local-first development and cloud-later migration

Decision: develop and validate the entire core system locally before provisioning GCP resources.
Context: the project is intended as a learning exercise and must minimize cost.
Consequences: more work is required to make local infrastructure reproducible, but debugging is cheaper and architectural understanding is stronger.

## ADR-002 — Modular monolith before microservices

Decision: use a modular FastAPI service rather than multiple independently deployed microservices.
Context: the project already has distributed concerns in SDK propagation and eventing.
Consequences: fewer operational boundaries and easier debugging; later service splitting is an experiment, not a starting requirement.

## ADR-003 — Python + FastAPI for the control plane

Decision: Python/FastAPI.
Context: the learner explicitly wants to improve Python skills while building systems software.
Consequences: productive API development, strong typing/validation options, and useful ecosystem for testing and observability.

## ADR-004 — Astro + React for dashboard and demo app

Decision: Astro with React islands and TypeScript.
Context: the learner wants to improve Astro and React skills.
Consequences: frontend complexity stays bounded while interactive components remain available.

## ADR-005 — PostgreSQL as local source of truth

Decision: PostgreSQL is the initial local database.
Context: relational constraints, transactions, indexes, and migrations are valuable backend/cloud skills.
Consequences: the local model is richer than a key-value store and later requires an explicit cloud persistence mapping.

## ADR-006 — Firestore as default GCP persistence path

Decision: use Firestore for the low-cost GCP deployment path.
Context: the project prioritizes minimal spend and wants managed/serverless cloud practice.
Consequences: the data model must be intentionally adapted; Firestore is not treated as a drop-in PostgreSQL substitute.

## ADR-007 — Persistence repository boundary

Decision: isolate database operations behind a repository/service boundary.
Context: the project deliberately compares PostgreSQL locally with Firestore in GCP.
Consequences: domain logic can remain stable while persistence adapters vary; the abstraction must remain small and not become an accidental generic ORM.

## ADR-008 — Evaluate feature flags in the SDK

Decision: normal evaluations occur locally from an in-memory configuration snapshot.
Context: feature checks are on the application's hot path.
Consequences: low latency and resilience, but configuration synchronization becomes a first-class problem.

## ADR-009 — Polling before SSE before Pub/Sub

Decision: implement configuration propagation progressively: REST bootstrap → polling → SSE → Pub/Sub.
Context: each stage teaches a distinct distributed-systems concept.
Consequences: the project takes longer but makes trade-offs measurable rather than abstract.

## ADR-010 — Monotonic configuration versions

Decision: every configuration snapshot has a monotonic version; clients accept only newer versions.
Context: distributed update events can be duplicated or reordered.
Consequences: simple idempotency/staleness protection with a small state model.

## ADR-011 — Deterministic hashing for percentage rollouts

Decision: assign users to rollout buckets using a stable hash of flag key + subject key.
Context: random per-request assignment would cause users to flip between variants.
Consequences: stable assignment without server-side session state.

## ADR-012 — Scoped read-only client keys

Decision: SDK clients receive environment-scoped read-only keys; admin credentials are separate.
Context: browser applications are not trusted administrators.
Consequences: the public client can request only SDK-safe configuration.

## ADR-013 — Do not require managed Redis

Decision: Redis is local-only by default.
Context: managed Memorystore is provisioned and billable even when idle.
Consequences: shared-cache learning happens locally; the cloud architecture avoids a predictable always-on cost.

## ADR-014 — Cloud Run for stateless application hosting

Decision: use Cloud Run for the control/API service.
Context: it fits the project's existing GCP knowledge and supports scale-to-zero request-based deployment.
Consequences: the application must be stateless and externalize durable state.

## ADR-015 — Terraform for infrastructure

Decision: all GCP infrastructure must be reproducible with Terraform.
Context: the learner already has Terraform experience and wants deeper infrastructure practice.
Consequences: infrastructure changes become reviewable and repeatable; Terraform state must be handled securely.

## ADR-016 — GitHub Actions for CI/CD

Decision: use GitHub Actions for lint/test/build/deploy workflows.
Context: GitHub is the project's version-control platform.
Consequences: CI becomes a visible part of the engineering lifecycle.

## ADR-017 — Observability is a core requirement

Decision: telemetry is designed from the middle of the project rather than bolted on at the end.
Context: latency, propagation, stale state, and failure behavior are the actual system-design learning goals.
Consequences: the code includes measurable signals and the final report includes evidence.

