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

