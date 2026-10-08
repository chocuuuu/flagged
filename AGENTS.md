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

