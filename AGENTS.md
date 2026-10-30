# AGENTS.md

# Flagged — Agent Operating Contract

## Mission

Build **Distributed Feature Flag & Configuration Platform** as an outcome-based, learning-first cloud engineering project. Its 12 milestones are an ordered guide, not a calendar or deadline.

The repository must remain understandable to a developer who did not watch the implementation happen.

## Architecture principles

1. **Local-first, cloud-later.**
2. **Control plane and data plane are explicitly separated.**
3. **Feature evaluation is local whenever practical.**
4. **The database is the source of truth; SDK memory is a distributed cache.**
5. **Configuration propagation must be observable and versioned.**
6. **Stateless services are preferred.**
7. **External managed services are optional experiments, never the default path.**
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
- Firestore (emulator/local by default; live use optional)
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

## ADR lifecycle and architecture freeze gate

- An ADR is `Proposed` while a decision is being evaluated, planned, or implemented. A detailed proposal is not evidence that the design works.
- Mark an ADR `Accepted` only in the milestone that implements its decision, after the relevant behavior or infrastructure has been tested and verified. Record the implementation and verification evidence in the ADR or its linked milestone/PR.
- When a decision is replaced, retain the original ADR and mark it `Superseded by ADR-XXX`; document the replacement decision in a new ADR.
- Before starting a milestone that crosses an architectural boundary, run the checklist in [docs/ARCHITECTURE-FREEZE-GATE.md](docs/ARCHITECTURE-FREEZE-GATE.md). A gate may authorize a bounded local milestone while leaving unrelated cloud or later-milestone decisions explicitly deferred. It must not label the whole architecture frozen while Tier 1 decisions for the upcoming work remain unresolved.
- A gate result records its scope, date, evidence, blockers, and deferred decisions. It does not change an ADR to `Accepted`; implementation verification does that at the point of delivery.

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
docs/ARCHITECTURE-FREEZE-GATE.md
docs/runbooks/
docs/benchmarks/
```

## AI collaboration protocol

Before each meaningful change, explain its purpose, assumptions, files involved, tests/evidence, and why the chosen option is preferred over alternatives. Cover compatibility, concurrency, performance, and cost whenever relevant. Afterward, report what was verified and any failures or remaining risks.

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

- The default development and validation path must not provision cloud resources or incur cloud-service charges.
- Prefer local services, emulators, and local adapters for cloud learning.
- Never treat free tiers, quotas, budgets, or alerts as guarantees that a workload cannot incur charges.
- Before any live cloud provisioning, stop and get explicit user approval. First identify every resource, check current official pricing and billing prerequisites, estimate likely costs, and document cleanup commands.
- Do not apply Terraform or enable a paid hosted workflow without that approval.
