# Audit changelog

## 2026-10-31

Every entry below is an audit edit. The pre-existing worktree deletion of
`jira/JIRA-BACKLOG.csv` was not restored, staged, or otherwise changed.

### Authority, plan, and progress

- `PRD.md` - standardized plan identity on 60 working sessions over 12 weeks.
- `README.md` - corrected start order and file/layout references; documented the
  canonical plan, generated Jira CSV, contract, audit artifacts, local cost boundary,
  and current legacy CSV worktree state.
- `docs/SPRINT-CALENDAR.md` - aligned sprint names and exact five-session ranges.
- `progress/DAILY-PLAN.md` - established the canonical 60-session plan; added goals,
  Test IDs/verification lines, evidence, and proposed commit messages; aligned the
  demo SDK integration point and referenced the shared API error contract.
- `progress/PROGRESS.md` - regenerated the derived session checklist and complete
  Proposed ADR tracker, including ADR-023.
- `FLAGGED-MASTER-PLAN.md` - marked the consolidated duplicate as historical and
  directed readers to current source documents; replaced its stale SSE examples
  with the selected event/data framing.
- `SKILLS.md` - aligned sprint learning objectives with the calendar and Jira.

### Jira source and enforcement

- `jira/JIRA-BACKLOG.md` - standardized FF keys and 3-point stories; aligned sprint
  names, learning objectives, and success/failure Test IDs; added demo storefront,
  auth, shared API error-contract tests, cost-gate, and CI-check coverage; made Redis
  strictly optional/local.
- `jira/FLAGGED-JIRA-IMPORT.csv` - regenerated from the Markdown source (12 epics,
  48 stories, 149 subtasks).
- `scripts/generate_jira_csv.py` - added deterministic CSV generation and drift
  checks for sprint names, objectives, story/subtask counts, and test evidence.
- `scripts/check_consistency.py` - added local checks for ADR references/status and
  tracker titles, sprint/session coverage, Jira drift, README paths, secrets,
  retired terminology, budget-gate ordering, and Cloud Run minimum instances.
- Jira count reconciliation - verified that the 149 source subtasks are intentional:
  three additional demo tasks in FF-504, one Cloud Run default in FF-1002, and one
  CI consistency-gate task in FF-1201; the other 45 stories have three subtasks each.
- ADR count reconciliation - verified that the initial inventory had 22 ADR files;
  ADR-023 was then added for repository structure, so the final tracker/checker count
  is 23 ADR files, not a count that includes a tracker or template.
- Session count reconciliation - verified 60 unique session headings (01–60) in
  `progress/DAILY-PLAN.md`.

### API, architecture, data, security, and cost

- `docs/API-CONTRACT.md` - completed the draft route inventory and auth/status
  details; documented health/readiness and project audit routes, unified error
  shape, SDK snapshot and conditional requests, `config.updated` revision payload,
  `Last-Event-ID`, and deferred Firestore behavior.
- `ARCHITECTURE.md` - aligned the SSE event framing and labeled Firestore/Redis as
  deferred or optional without changing the selected propagation approach.
- `SYSTEM-DESIGN.md` - replaced the conflicting JSON event example with the shared
  SSE event/data framing.
- `docs/adrs/ADR-021-sse-delivery-across-instances.md` - marked Firestore polling
  settings as future proposals and removed historical quota figures as current
  pricing guidance.
- `docs/DECISIONS-PENDING.md` - recorded the owner's three resolved choices and the
  non-owner validation deferrals; retained the ADR acceptance and pre-existing
  deletion constraints.
- `docs/adrs/ADR-004-astro-react.md` - recorded Tailwind in the frontend stack.
- `docs/adrs/ADR-022-sdk-payload-and-client-visible-fields.md` - clarified the
  client payload and variant boundary.
- `docs/adrs/ADR-023-repository-structure.md` - documented the existing layout
  without moving files or introducing application structure.
- `DATA.md` - marked variants out of MVP, aligned the snapshot shape and datastore
  deferral, documented Redis as a local experiment, and mapped data invariants to
  Jira test IDs.
- `SECURITY.md` - aligned client-key prefix/display behavior and mapped section 16
  invariants to Jira test evidence.
- `COST-BOUNDARY.md` - marked prices historical/re-verify, added the dated
  pre-provisioning checklist, GCS Terraform state and resource cleanup notes, budget
  alert caveat, Secret Manager coverage, and Cloud Run scale-to-zero requirement.
- `docs/COST-SOURCES.md` - added historical verification categories for GCS,
  Secret Manager, and hosted GitHub Actions; linked it from the cost boundary.
- `AGENTS.md` - documented the testing stack, coverage target, local CI gate, and
  dependency register policy.
- `CLAUDE.md` - linked the dependency/tooling register.
- `DEPENDENCIES.md` - added runtime/tool/version policy plus purpose, alternatives,
  standard-library suitability, maintenance, and cost rationale for dependencies.

### Templates and operational guidance

- `.env.example` - added placeholder-only local environment variable guidance.
- `.github/ISSUE_TEMPLATE/feature-or-task.md` - added the Jira-linked issue template.
- `.github/pull_request_template.md` - added a focused verification/cost checklist.
- `docs/benchmarks/README.md` - added benchmark evidence and bounded-run guidance.
- `docs/runbooks/local-setup.md` - added a local setup runbook draft.
- `docs/runbooks/database-reset.md` - added a guarded local database reset draft.
- `docs/runbooks/rollback-deploy.md` - added an approved-deployment rollback draft.
- `docs/runbooks/revoke-client-key.md` - added key revocation and verification steps.
- `docs/runbooks/stale-config-incident.md` - added stale configuration diagnosis
  and recovery steps.
- `docs/runbooks/cloud-teardown.md` - added explicit-approval cloud cleanup steps.

### Audit artifacts

- `AUDIT-REPORT.md` - preserved the Phase 1 inventory, labeled initial findings as
  historical, recorded reconciliations, risk levels, added-file inventory, and
  pass/deferred readiness evidence.
- `CHANGELOG-AUDIT.md` - records this file-by-file audit trail.
- Final validation evidence - a fresh clone of commit `f16bb37` passed the Jira
  generator check and consistency gate with a clean status; working-tree and
  29-commit Gitleaks scans reported no findings.

No application features were implemented, no dependencies installed, and no cloud
resources created. Gitleaks 8.30.1 was installed as a local scanner (not a project
dependency); both working-tree and local-history scans passed with no findings.
No existing file was deleted by the audit; the only deletion in the worktree was
present before the audit began.
