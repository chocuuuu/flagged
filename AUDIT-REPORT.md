# Flagged pre-flight audit

**Audit date:** 2026-10-31
**Status:** Inventory, reconciliation, and local clean-clone checks complete.
Documentation/planning readiness is verified; product behavior and architecture
decisions remain subject to the implementation milestones and listed deferrals.

## Scope and worktree state

The inventory below covers the 45 tracked paths listed by `git ls-files` in the
working tree. The worktree had one pre-existing change at audit start:
`jira/JIRA-BACKLOG.csv` was deleted. This audit did not restore or otherwise alter it.
It is mentioned in `README.md` and the historical `FLAGGED-MASTER-PLAN.md`, but is
not the active generated Jira import.

`README` column means the file is named in the current `README.md` file list, start
instructions, or suggested layout. `Inbound references` lists direct references
observed in the Markdown documents; it is not a claim that the file is unused at
runtime.

## Phase 1 — Inventory

The entries in this section record the Phase 1 snapshot before reconciliation.
The rows for files changed during later phases are corrected below where relevant;
the supplemental inventory lists files added during the audit.

### Root and project documents

| File | Purpose / owning layer | Inbound references | README |
|---|---|---|---|
| `.gitignore` | Ignore rules / tooling | None found | No |
| `.github/workflows/gitleaks.yml` | Hosted secret-scan workflow / CI | `SECURITY.md` | No |
| `README.md` | Entry point and repository index / governance | `AGENTS.md`, `FLAGGED-MASTER-PLAN.md`, `docs/ARCHITECTURE-FREEZE-GATE.md` | Self |
| `PRD.md` | Scope, requirements, product success / authority | `AGENTS.md`, `FLAGGED-MASTER-PLAN.md`, `README.md`, `docs/TECHNICAL-DESIGN.md`, `jira/JIRA-BACKLOG.md` | Yes |
| `ARCHITECTURE.md` | High-level system architecture / architecture | `AGENTS.md`, `FLAGGED-MASTER-PLAN.md`, `README.md`, `docs/TECHNICAL-DESIGN.md`, `jira/JIRA-BACKLOG.md` | Yes |
| `DATA.md` | Data model and invariants / data | `AGENTS.md`, `FLAGGED-MASTER-PLAN.md`, `README.md`, `docs/ARCHITECTURE-FREEZE-GATE.md`, `docs/TECHNICAL-DESIGN.md` | Yes |
| `SECURITY.md` | Threat model and security requirements / security | `AGENTS.md`, `FLAGGED-MASTER-PLAN.md`, `README.md`, `jira/JIRA-BACKLOG.md` | Yes |
| `SYSTEM-DESIGN.md` | Distributed behavior and failure learning / design | `AGENTS.md`, `FLAGGED-MASTER-PLAN.md`, `README.md`, `docs/TECHNICAL-DESIGN.md`, `jira/JIRA-BACKLOG.md` | Yes |
| `SKILLS.md` | Learning roadmap / skills | `AGENTS.md`, `FLAGGED-MASTER-PLAN.md`, `README.md` | Yes |
| `COST-BOUNDARY.md` | Cost and provisioning guardrails / cost | `ARCHITECTURE.md`, `FLAGGED-MASTER-PLAN.md`, `README.md`, `docs/ARCHITECTURE-FREEZE-GATE.md`, `docs/SPRINT-CALENDAR.md`, `progress/DAILY-PLAN.md` | Yes |
| `CLAUDE.md` | Claude-specific agent workflow / governance | `AGENTS.md`, `FLAGGED-MASTER-PLAN.md`, `README.md` | Yes |
| `AGENTS.md` | Canonical repository agent instructions / governance | `CLAUDE.md`, `FLAGGED-MASTER-PLAN.md`, `README.md`, `docs/ARCHITECTURE-FREEZE-GATE.md` | Yes |
| `FLAGGED-MASTER-PLAN.md` | Historical consolidated snapshot / legacy planning | No inbound references found | No |

### Docs

| File | Purpose / owning layer | Inbound references | README |
|---|---|---|---|
| `docs/API-CONTRACT.md` | Draft v1 HTTP contract / API | `README.md`, `docs/ARCHITECTURE-FREEZE-GATE.md`, `docs/TECHNICAL-DESIGN.md` | Yes |
| `docs/ARCHITECTURE-FREEZE-GATE.md` | Pre-milestone architecture review / governance | `AGENTS.md`, `README.md`, `docs/TECHNICAL-DESIGN.md` | Yes |
| `docs/COST-SOURCES.md` | Historical pricing-source notes / cost | `COST-BOUNDARY.md` (linked during reconciliation) | No |
| `docs/LEARNING-LOG.md` | Learning retrospective template / learning | None found | No |
| `docs/SPRINT-CALENDAR.md` | 12-outcome roadmap / planning | `FLAGGED-MASTER-PLAN.md`, `README.md` | Yes |
| `docs/TECHNICAL-DESIGN.md` | Planning diagrams and sequences / design | `README.md`, `docs/ARCHITECTURE-FREEZE-GATE.md` | Yes |

### ADRs

| File | Purpose / owning layer | Inbound references | README |
|---|---|---|---|
| `docs/adrs/ADR-001-local-first-cloud-later.md` | Local-first/cloud-later / architecture | `docs/TECHNICAL-DESIGN.md`, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-002-modular-monolith.md` | Modular monolith / architecture | `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-003-python-fastapi.md` | Python/FastAPI / technology | `docs/TECHNICAL-DESIGN.md`, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-004-astro-react.md` | Astro/React / technology | `docs/TECHNICAL-DESIGN.md`, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-005-postgresql-local.md` | Local PostgreSQL / data | `docs/TECHNICAL-DESIGN.md`, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-006-firestore-cloud.md` | Optional Firestore / data | `docs/TECHNICAL-DESIGN.md`, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-007-repository-abstraction.md` | Persistence boundary / architecture | `docs/TECHNICAL-DESIGN.md`, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-008-local-evaluation.md` | SDK-local evaluation / SDK | `docs/TECHNICAL-DESIGN.md`, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-009-progressive-propagation.md` | Polling→SSE→Pub/Sub / propagation | `docs/TECHNICAL-DESIGN.md`, ADR-021, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-010-versioned-config.md` | Environment configuration revisions / data and SDK | ADR-019, ADR-021, ADR-022, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-011-deterministic-rollout.md` | Deterministic rollout / SDK | ADR-020, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-012-api-key-scoping.md` | Scoped client keys / security | ADR-022, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-013-no-managed-redis.md` | Redis local-only default / caching | `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-014-gcp-cloud-run.md` | Optional Cloud Run target / deployment | `docs/TECHNICAL-DESIGN.md`, ADR-021, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-015-terraform.md` | Terraform / infrastructure | `docs/TECHNICAL-DESIGN.md`, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-016-github-actions.md` | Optional hosted CI/CD / CI | `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-017-observability-core.md` | Observability / operations | `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-018-single-admin-authentication.md` | Single-admin authentication / security | `SECURITY.md`, `docs/TECHNICAL-DESIGN.md`, `progress/PROGRESS.md` | No |
| `docs/adrs/ADR-019-configuration-version-semantics.md` | Revision vs flag-version semantics / data and SDK | `docs/TECHNICAL-DESIGN.md`, ADR-020, ADR-021, ADR-022 | No |
| `docs/adrs/ADR-020-rule-precedence-and-rollout-bucketing.md` | Rule ordering and rollout / SDK | `ARCHITECTURE.md`, `DATA.md`, `FLAGGED-MASTER-PLAN.md`, `docs/TECHNICAL-DESIGN.md`, ADR-021, ADR-022 | No |
| `docs/adrs/ADR-021-sse-delivery-across-instances.md` | Cross-instance SSE delivery / propagation | `ARCHITECTURE.md`, `SYSTEM-DESIGN.md`, `docs/TECHNICAL-DESIGN.md` | No |
| `docs/adrs/ADR-022-sdk-payload-and-client-visible-fields.md` | SDK payload and client-visible fields / SDK contract | `docs/TECHNICAL-DESIGN.md`, ADR-020, ADR-021 | No |

### Jira and progress

| File | Purpose / owning layer | Inbound references | README |
|---|---|---|---|
| `progress/PROGRESS.md` | Derived 60-session checklist and ADR tracker (001–023) / progress | `FLAGGED-MASTER-PLAN.md`, `README.md`, `docs/SPRINT-CALENDAR.md`, `progress/DAILY-PLAN.md` | Yes |
| `progress/DAILY-PLAN.md` | Canonical 60-session plan / planning | `FLAGGED-MASTER-PLAN.md`, `README.md`, `docs/SPRINT-CALENDAR.md`, `progress/PROGRESS.md` | Yes |
| `jira/JIRA-BACKLOG.md` | Markdown Jira hierarchy and story definitions / backlog | `FLAGGED-MASTER-PLAN.md`, `README.md` | Yes |
| `jira/FLAGGED-JIRA-IMPORT.csv` | Generated FF-key Jira import dataset / backlog | `FLAGGED-MASTER-PLAN.md`, `README.md` | Yes |
| `jira/JIRA-BACKLOG.csv` | Older CSV export, tracked but absent from worktree / backlog | `FLAGGED-MASTER-PLAN.md`, `README.md`, `docs/SPRINT-CALENDAR.md` | Yes (stale reference) |

## Inventory flags at audit start

- `FLAGGED-MASTER-PLAN.md` is explicitly historical, duplicates current authority
  documents, and has no inbound links. It contains conflicting legacy day plans.
- `docs/COST-SOURCES.md` and `docs/LEARNING-LOG.md` have no inbound references found.
  ADR-002, ADR-013, ADR-016, and ADR-017 have no direct filename references outside
  the progress tracker.
- README lists `SPRINT-CALENDAR.md` at root although the existing file is in `docs/`.
  It says `jira/JIRA-BACKLOG.csv` is older, but that tracked file is currently
  deleted in the worktree.
- `docs/runbooks/`, `docs/benchmarks/`, the suggested app/service/package/
  infrastructure/test directories, and `docker-compose.yml` do not exist. FF-104-3
  calls for issue/PR templates, which are absent.
- README has `docs/API-CONTRACT.md`; the requested `docs/api/CONTRACT.md` does not
  exist. The existing contract is explicitly a draft.

## Phase 2 — Initial findings at audit start (superseded by final results below)

| Area | Evidence and conflict | Risk | Current resolution/status |
|---|---|---:|---|
| A. Plan identity | PRD, sprint calendar, progress, and current daily guide describe 12 outcome milestones with no fixed schedule. The historical master plan has a 60-session schedule and a separate progress checklist with different day content (Day 16: auth vs Astro/React). The current daily guide has no numbered day sessions. The historical 60-session guide has 60 unique session headings, but 26 lack a `Test:` line. | High | Needs canonical plan and user-specified 60-session structure reconciled. Do not treat the historical file as authoritative. |
| A. Naming and sprint mapping | Current authority docs use “milestone”; the historical package uses 12 sprints × 5 sessions. The current calendar does not specify session ranges. | High | Must define 60-session naming and exact ranges 1–5 through 56–60, then regenerate the secondary checklist. |
| B. Jira integrity | Markdown uses FF keys; import CSV uses numeric work item IDs and numeric parents. Markdown has 48 stories (four per milestone), each with three subtasks (144); CSV has 12 epics, 48 stories, 144 subtasks. Markdown estimates every story “3–5”; CSV gives every story 3. Every Markdown story has three listed subtasks, but no named test file/ID. | High | Counts presently agree; key/point/test evidence drift remains. CSV generator/check is not present. |
| C. ADRs | 22 ADR files exist and all are Proposed. The progress tracker lists only ADR-001–018. | High | Do not mark accepted without implementation verification: `AGENTS.md` explicitly requires evidence. Tracker alignment remains pending. |
| C. ADR architecture coverage | Existing ADRs cover datastore (005/006), evaluation (008), propagation (009/021), auth (012/018), SDK fields (022), cloud (014), caching (013), deployment (014/015), and repository structure boundary (007). | Medium | Coverage appears present; full reference/status checks remain for final pass. |
| D. Event/API | `ARCHITECTURE.md`, `SYSTEM-DESIGN.md`, ADR-021, and the draft API contract currently converge on `config.updated` and revision data. The API contract uses `Last-Event-ID`; it does not define `afterVersion`. The contract explicitly leaves audit retrieval unspecified. | Blocker | DP-001 and DP-002 require owner choices before contract changes. |
| D. Error/config shapes | The draft API contract defines one JSON error shape and SDK snapshot shape. `DATA.md` has a similar but not field-identical sample; its flag record has admin fields and the SDK payload omits them per ADR-022. | High | Reconcile only after confirming the approved contract and explicitly distinguish storage/admin flag shape from public SDK shape. |
| E. Data model | PRD marks variants as stretch; `DATA.md` uses `boolean/variant` without saying variant is out of MVP. ADR-022 leaves variant wire fields for later and excludes variant implementation from the first milestone. PRD lists three demo flags; FF-504 names only `new_checkout`. | High | Mark variants out of MVP in the data model and align demo stories with the PRD; Jira generator work remains pending. |
| E. Invariants | DATA describes atomic revision/audit behavior and other invariants, but a systematic mapping to individual test tasks is absent. | High | Needs test IDs/files in backlog and/or session plan. |
| F. Security | ADR-018 specifies Argon2id password verification and signed HttpOnly session cookies; SECURITY says single configured admin. Need verify older FF-304 wording and align backlog, not alter auth design. Security DoD is prose; no test-task mapping is evident. | High | Audit and update lower-level plan after route decisions. |
| G. Cost | COST-SOURCES says pricing references were checked 2026-10-08; COST-BOUNDARY contains a Firestore pricing/quota statement dated 2026-10-30. Neither alone establishes current prices for provisioning. GCS Terraform state storage is not listed. | High | Mark all pricing “re-verify before provisioning”; add service-specific cost and cleanup notes after resource inventory. |
| H. QA | No dependency/tooling manifests or CI gate are present. The Jira DoD has no concrete test-file field. The historical session plan has 26 missing Test lines. | High | Define stack/gate and test evidence without installing dependencies. |
| I. Tooling | Current docs mention technology names but no consolidated pinned-version matrix or dependency rationale table. | Medium | Create requested matrix and dependency register; pin only established choices and mark remaining versions for Sprint 1. |
| J. Demo | PRD names Home, Product list, Product detail, Cart, Checkout and three flags. FF-504 only explicitly names `new_checkout`; no Product detail/Cart task was confirmed in the inspected story. | Medium | Add explicit lower-layer story coverage and name the SDK integration point consistently. |
| K. Operations | No runbook directory/files exist. README's Start here links mostly exist, but its file index has the sprint path mismatch and stale CSV entry. | High | Create required runbook stubs and correct paths after reconciliation. |
| 3. Enforcement | No `scripts/check_consistency.py` exists. | High | Do not implement a misleading partial checker before pending contract and Jira-source decisions are resolved. |

## Phase 2 stop condition at audit start (resolved)

This was the stop point before the owner resolved DP-001 to DP-003. The audit
resumed after those choices and the final results below supersede the statuses in
the initial findings table.

## Supplemental inventory — audit additions

| File/path | Purpose / owning layer | Inbound reference or consumer | README |
|---|---|---|---|
| `.env.example` | Safe local environment template / security | SECURITY.md and local-setup runbook | No |
| `.github/ISSUE_TEMPLATE/feature-or-task.md` | Issue intake / collaboration | Jira FF-104-3 | No |
| `.github/pull_request_template.md` | Pull request checklist / collaboration | Jira FF-104-3 | No |
| `AUDIT-REPORT.md` | Audit evidence and readiness / governance | README.md, CHANGELOG-AUDIT.md | Yes |
| `CHANGELOG-AUDIT.md` | Traceable audit edits / governance | AUDIT-REPORT.md | Yes |
| `DEPENDENCIES.md` | Toolchain matrix and dependency rationale / tooling | AGENTS.md, CLAUDE.md, README.md, runbooks | Yes |
| `docs/DECISIONS-PENDING.md` | Owner decisions and explicit deferrals / governance | API contract, DATA.md, progress tracker | Yes |
| `docs/benchmarks/README.md` | Benchmark evidence guidance / operations | README suggested layout | No |
| `docs/runbooks/local-setup.md` | Local startup / operations | README suggested layout | No |
| `docs/runbooks/database-reset.md` | Local database reset / operations | README suggested layout | No |
| `docs/runbooks/rollback-deploy.md` | Approved deployment rollback / operations | README suggested layout | No |
| `docs/runbooks/revoke-client-key.md` | Client-key revocation / security operations | README suggested layout, API contract | No |
| `docs/runbooks/stale-config-incident.md` | Stale configuration response / operations | README suggested layout, API contract | No |
| `docs/runbooks/cloud-teardown.md` | Approved cloud cleanup / cost operations | README suggested layout, COST-BOUNDARY.md | No |
| `docs/adrs/ADR-023-repository-structure.md` | Records current layout without moving files / architecture | PROGRESS.md, consistency check | No |
| `scripts/check_consistency.py` | Local documentation consistency gate / tooling | AGENTS.md, Jira FF-1201, README | No |
| `scripts/generate_jira_csv.py` | Generate Jira import from Markdown / tooling | JIRA-BACKLOG.md and README | No |

The initial inventory covered 45 tracked paths. These additions are audit-created
files. The pre-existing deletion of `jira/JIRA-BACKLOG.csv` is outside the audit's
changes and has not been restored or otherwise altered.

## Final reconciliation results

| Area | Finding and evidence | Risk | Resolution / status |
|---|---|---|---|
| A. Plan identity and naming | Progress and daily plans had incompatible schedules; labels mixed days, working sessions, and weeks. | High | `progress/DAILY-PLAN.md` is canonical: 60 working sessions over 12 weeks, 12 sprints of five. Each session has a goal, Test ID/line, evidence, and proposed commit. `progress/PROGRESS.md` is its checklist. Calendar ranges cover 1-5 through 56-60 without gaps/overlaps. |
| A. Sprint names | Sprint 9/10 labels differed among backlog, skill focus, and calendar. | Medium | Jira, `SKILLS.md`, and `docs/SPRINT-CALENDAR.md` now share all 12 focus names. Generator rejects a mismatch. |
| B. Jira integrity | Markdown used FF keys; import CSV used numeric keys; estimates and evidence differed. | High | Markdown is the canonical FF-key source. Generator/check verifies 12 epics, 48 stories, 149 subtasks, unique keys/parents, four stories per sprint, 3 story points, Test IDs, and sprint objectives. The 149 are deliberate Markdown tasks: FF-504 adds FF-504-4/-5/-6 for demo flags/pages; FF-1002 adds FF-1002-4 for Cloud Run scale-to-zero; FF-1201 adds FF-1201-4 for the local/hosted consistency gate. The other 45 stories have three subtasks each. |
| C. ADR status and tracker | At start, 22 ADRs existed, all Proposed; tracker omitted later ADRs. AGENTS.md forbids acceptance without implementation verification. | High | The audit added ADR-023 for repository structure, so the checker now finds 23 actual ADR files (001–023); it does not count the tracker or templates. It verifies all filenames, titles, and actual Proposed statuses. None is falsely marked Accepted. All AGENTS architecture-change categories have an ADR. |
| C. Owner decisions | SSE cursor, audit-history route, and Firestore read model were undecided. | Blocker | DP-001/002/003 are resolved: keep `config.updated` with `{"revision":N}`, SSE ID equal to the revision, and `Last-Event-ID`; use the project audit route with optional environment filter; defer Firestore and retain PostgreSQL baseline. Details are in `docs/DECISIONS-PENDING.md`. |
| D. Event/API/error/config contract | Event naming, revision semantics, audit route, route inventory, and shared errors needed one source. | High | Existing `docs/API-CONTRACT.md` remains the single draft; no duplicate `docs/api/CONTRACT.md` was created. It defines health/admin/audit/SDK/SSE routes, auth, requests, responses, statuses, common error shape, conditional requests, `config.updated`, and the selected cursor. `DATA.md` and the API contract distinguish database/admin rows from the client snapshot. SDK types do not exist yet; implementation comparison is deferred. |
| E. Data model and invariants | Variants were PRD stretch but ambiguous in schema; demo coverage and invariant evidence were incomplete. | High | `DATA.md` marks variants out of MVP and maps seven invariants to Jira test IDs. FR-03 storage fields and FR-12 audit fields align. FF-504 covers all three demo flags, all five storefront pages, and the named SDK integration point. |
| F. Security | Key prefix/auth descriptions and security DoD needed alignment and test evidence. | High | Client keys use `ff_client_`, show once, and store a hash. ADR-018 auth is reflected in FF-304 and the day plan. Six SECURITY section 16 invariants map to Jira test IDs. Browser/demo credential prohibitions remain explicit. |
| G. Cost boundary | Pricing was historical; GCS state and service cleanup notes were missing; cloud-safety ordering needed verification. | High | `COST-BOUNDARY.md` labels pricing historical and requires a dated re-check. Resource inventory includes Cloud Run, Firestore, Pub/Sub, Artifact Registry, Logging/Monitoring, IAM, Secret Manager, GCS state, GitHub Actions, and managed-service exclusions with cleanup notes. Cloud Run min instances = 0 is explicit. FF-1001-1 is the budget/alert gate. No current prices are asserted. |
| H. QA and CI | Test-stack choices and CI gate were implicit; daily tests and Jira evidence lacked enforcement. | High | `AGENTS.md` defines pytest/httpx and planned 80% branch coverage, Vitest/strict TypeScript, component/browser tests, bounded Locust, Ruff/mypy/ESLint, secret scan, and local lint/type/unit/integration gate. FF-1201 aligns. Every session has Test and every story success/failure Test IDs. |
| I. Tooling | Versions and dependency policy were scattered. | Medium | `DEPENDENCIES.md` centralizes the runtime/tool/image matrix and purpose, alternatives, standard-library suitability, complexity, cost, and pin-at-Sprint-1 policy. No dependencies were installed. |
| J. Demo and SDK | Product detail/cart and actual integration target were not explicit in FF-504. | Medium | FF-504 covers Home, Product list, Product detail, Cart, Checkout, all PRD demo flags, and `apps/demo-store/src/components/FlaggedDemo.tsx`; Session 25 uses the same integration point. |
| K. Operations and entry path | Required runbooks were missing; README paths/layout needed correction. | High | Six runbook drafts cover local setup, database reset, rollback, key revocation, stale config, and cloud teardown. README start order and file/layout paths pass. Drafts defer unimplemented commands and live cloud actions. |
| 3. Enforcement | No local consistency gate or generated Jira source check existed. | High | Added local-only `scripts/check_consistency.py` and Jira generator. Checks cover ADR references/status/tracker, sprint/session map and fields, Jira generation/counts/points/parents, README paths, secret heuristics/Gitleaks if installed, retired terms, cost-gate ordering, and Cloud Run min instances. |

## Ready to start checklist

| Item | Result | Evidence / limitation |
|---|---|---|
| Canonical 12 x 5 plan and exact session ranges | PASS | `python scripts/check_consistency.py`: 12 sprints, 60 contiguous sessions. |
| Goal, Test, and proposed commit for all sessions | PASS | Checker validates all 60 session blocks; see `progress/DAILY-PLAN.md`. |
| Jira keys, hierarchy, points, sprint objectives, generated CSV | PASS | `python scripts/generate_jira_csv.py --check`; 12 epics, 48 stories, 149 subtasks. |
| ADR references and tracker title/status consistency | PASS | Checker confirms all 23 ADRs resolve and tracker matches; statuses correctly remain Proposed. |
| API/SSE/error/audit/config draft | PASS - IMPLEMENTATION DEFERRED | `docs/API-CONTRACT.md`, DP-001/002/003; SDK/API implementation types do not exist yet. |
| Data and SECURITY section 16 test mappings | PASS | Mapping tables in DATA.md and SECURITY.md; Jira success/failure IDs. |
| Cost inventory, cleanup notes, budget ordering, scale-to-zero | PASS | `COST-BOUNDARY.md` and checker; current pricing intentionally unasserted. |
| Testing/tooling/dependency policy and CI gate | PASS | `AGENTS.md`, `DEPENDENCIES.md`, Jira FF-1201; versions intentionally pin at Sprint 1. |
| Demo pages, flags, and SDK integration point | PASS | PRD, FF-504, Session 25. |
| Runbook stubs and README paths | PASS | Six runbooks; checker reports 28 README paths exist. |
| Local consistency check | PASS | `python scripts/check_consistency.py`: `CONSISTENCY CHECK PASSED`; secret scan reports `heuristics + Gitleaks`. No GitHub Actions dependency. |
| Gitleaks working-tree scan | PASS | `gitleaks detect --source . --no-git --redact --exit-code 1`: no leaks found. |
| Gitleaks local-history scan | PASS | `gitleaks git . --redact --exit-code 1`: 29 commits scanned; no leaks found. |
| Clean-clone execution | PASS | Cloned commit `f16bb37` to a new temporary directory. `python scripts/generate_jira_csv.py --check` passed (12 epics, 48 stories, 149 subtasks); `python scripts/check_consistency.py` passed (23 ADRs, 12 sprints/60 contiguous sessions, 28 README paths, Gitleaks). Clone `git status --short` was empty. The clone was removed after verification; the pre-existing legacy CSV deletion remains untouched in the source worktree. |
| Live pricing/provisioning | DEFERRED / NOT REQUIRED | Re-verify official pricing and obtain explicit approval before any cloud action. No resources were created. |
| Feature implementation and ADR acceptance | DEFERRED TO MILESTONES | Audit is planning/documentation only. Accept an ADR only after implementation and verification. |

### Audit result

The local-first planning baseline and repository checks are ready for Sprint 1's
local learning sessions. Clean-clone, working-tree Gitleaks, and local-history
checks passed. Do not begin live cloud work without current pricing review and
explicit approval. The historical
`FLAGGED-MASTER-PLAN.md` and pre-existing deleted legacy CSV remain untouched.
The API contract remains a draft and ADRs remain Proposed until implementation
evidence exists.
