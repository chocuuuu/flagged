# Dependency and tooling register

This is the planning inventory, not an instruction to install tools or provision
services. Versions not already deliberately selected remain **pin at Sprint 1**.
No new package is installed by this audit.

## Tooling matrix

| Component | Choice | Version/image policy |
|---|---|---|
| Python | Python | Pin at Sprint 1 |
| Python package manager | uv | Pin at Sprint 1 |
| Node.js | Node.js | Pin at Sprint 1 |
| JavaScript package manager | pnpm | Pin at Sprint 1 |
| TypeScript | TypeScript strict mode | Pin at Sprint 1 |
| Astro | Astro | Pin at Sprint 1 |
| React | React | Pin at Sprint 1 |
| Tailwind CSS | Tailwind CSS | Pin at Sprint 1 |
| FastAPI / Pydantic | FastAPI and Pydantic | Pin at Sprint 1 |
| SQLAlchemy / Alembic | SQLAlchemy and Alembic | Pin at Sprint 1 |
| PostgreSQL | Docker image | Pin a supported major/minor image at Sprint 1; never use floating `latest` |
| Docker | Docker Engine and Compose | Pin/document local minimum at Sprint 1 |
| Redis | Optional local experiment | Pin local image at Sprint 1 if used; no managed Redis |
| Terraform | Terraform CLI | Pin at Sprint 1 |
| GitHub Actions runner | Hosted workflow runner | Pin a supported runner image at Sprint 1; hosted runs remain optional |
| Google Cloud SDK | Local CLI for explicitly approved cloud exercises | Pin at Sprint 1 |

## Dependency rationale

| Dependency/tool | Purpose | Alternatives considered | Standard library suitability | Complexity / maintenance | Cost impact |
|---|---|---|---|---|---|
| Python | Control-plane language | TypeScript/Go | N/A - runtime | Standard runtime; pin locally | None by itself |
| FastAPI | Typed HTTP API | Flask, Django REST Framework | No - framework features | Adds framework lifecycle and routing concepts | None locally |
| Pydantic | Request/response validation | Dataclasses/manual validation | No - validation and schemas | Additional model conventions; integrated with FastAPI | None locally |
| SQLAlchemy | Relational persistence | psycopg directly | No - PostgreSQL ORM/session layer | ORM/session lifecycle adds concepts | None locally |
| Alembic | Schema migrations | Hand-written SQL only | No - migration history/tooling | Migration history to maintain | None locally |
| PostgreSQL | Local relational source of truth | SQLite | No - SQLite is not equivalent | Service setup, but exposes production-style transactions and constraints | Local resource use |
| uv | Python environment/dependency management | pip + venv | No - package and lock management | One package workflow to learn | None |
| Node.js | TypeScript/JavaScript runtime and frontend tooling host | Browser-only tooling | N/A - runtime | Pin locally; align tooling versions | None by itself |
| pytest | Python unit/integration tests | unittest | Yes for basics - unittest is viable | Plugin ecosystem; standard test runner | None |
| httpx | ASGI/API client tests | Starlette TestClient | No - async ASGI client | Adds client library; supports async HTTP testing | None |
| pytest-cov / coverage.py | Enforce the planned 80% branch-coverage threshold | Manual coverage inspection | No - coverage instrumentation | Adds coverage instrumentation/reporting | None |
| Ruff | Python lint and formatting | Flake8 + Black | No - lint and format tooling | Consolidates common checks | None |
| mypy | Python static type checks | Pyright | No - static type analysis | Requires typed boundaries and annotations | None |
| TypeScript | Typed SDK and UI | JavaScript | No - static type checking | Compiler configuration and declarations | None |
| pnpm | JavaScript package/workspace management | npm | No - package/workspace management | Workspace/store conventions | None |
| Astro | Dashboard and demo app shell | Vite/Next.js | No - web application framework | Island/server-rendering concepts | None locally |
| React | Interactive UI components | Astro-only components | No - component UI runtime | Component state and testing surface | None |
| Tailwind CSS | Utility-first UI styling | CSS modules/plain CSS | No equivalent - plain CSS changes the choice | Build-time utility configuration | None |
| Vitest | SDK unit tests | Node test runner/Jest | Yes for basics - Node test runner is viable | Test transform/config; compatible with Vite tooling | None |
| React Testing Library | Component behavior tests | Enzyme/manual DOM tests | No - component DOM testing | Encourages user-visible tests | None |
| Playwright | Browser end-to-end tests | Selenium/manual walkthrough | No - browser automation | Browser binaries and CI maintenance | Local compute; hosted execution can cost |
| ESLint | TypeScript/React linting | Biome | No - lint rules and analysis | Rule/config maintenance | None |
| Prettier | Consistent formatting, if selected at Sprint 1 | ESLint formatting/plain formatting | No equivalent - optional formatter | Extra config/tool unless unified | None |
| Docker Engine / Compose | Reproducible local services | Native installs | No - container runtime/orchestration | Container lifecycle and resource use | Local resource use |
| Redis | Optional cache-aside/shared-cache experiment | In-memory cache only | No - cross-process cache service | Extra local service; not required for normal path | Local resource use; managed service excluded |
| Locust | Bounded local load tests | k6/custom scripts | No - load generation/reporting | Load profiles and resource limits to maintain | Local compute; never run unbounded |
| Terraform | Reproducible infrastructure configuration | Manual console work | No - provider-backed infrastructure plans | State and provider lifecycle; apply prohibited by default | None for local validation; resources may cost money |
| Gitleaks | Secret scanning | GitHub secret scanning/manual search | No - regex heuristic is not equivalent scanning | Scanner config and false-positive review | Local use; hosted usage subject to current terms |
| Starlette session middleware | Signed admin session cookie | JWT/browser storage, server-side sessions | No - ASGI session integration | Middleware/session-key rotation | None locally |
| pwdlib (Argon2id) | Password verification in ADR-018 | Custom hashing/general hash rejected | No - hashlib is not Argon2id password hashing | One maintained crypto dependency | None locally |
| Cloud Run | Optional stateless runtime study | Local container | N/A - managed service | Deployment/IAM/operations concepts | To verify before provisioning |
| Firestore | Deferred optional persistence experiment | PostgreSQL/local adapter | N/A - managed service | Document/transaction model | To verify; deferred by DP-003 |
| Pub/Sub | Optional event-delivery experiment | Local event bus/emulator | N/A - managed service | At-least-once/idempotency concepts | To verify before live use |
| Artifact Registry | Optional image repository | Local image store | N/A - managed service | Registry lifecycle and cleanup | To verify before provisioning |
| Cloud Logging / Monitoring | Optional cloud observability | Local logs/metrics | N/A - managed services | Retention and telemetry configuration | To verify before use |
| IAM | Optional least-privilege cloud identity | Local role model | N/A - managed service | Policy review and cleanup | To verify before enabling services |
| GCS Terraform state bucket | Optional remote Terraform state | Local state | N/A - managed storage | Access control, locking/versioning, deletion | To verify; local state is default |
| GitHub Actions | Optional hosted CI | Local scripts | N/A - hosted CI service | Workflow/runner maintenance | To verify current usage terms; not required locally |
| Google Cloud SDK | CLI for explicitly approved cloud exercises and cleanup | Provider APIs/console | N/A - command-line tool | Install only for an approved cloud exercise; pin at Sprint 1 | No local cost; any resulting resources must pass the cost gate |
| Secret Manager | Optional managed secret storage | Local environment configuration | N/A - managed service | IAM, version lifecycle, and rotation to maintain | To verify before provisioning |
