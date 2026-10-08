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
