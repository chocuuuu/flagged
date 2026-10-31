# COST-BOUNDARY.md

## Default cost policy

The default project path is designed for **$0 in cloud-service charges**. Local development, tests, and cloud-learning exercises should use local services, emulators, or adapters wherever practical.

No live GCP resource is required to complete the project. Cloud architecture, Terraform configuration, IAM policy design, and service behavior can be studied and validated locally without applying infrastructure.

The default path also avoids paid hosted services. Before enabling hosted CI/CD or other external services, check their current quotas and billing terms.

Pricing notes in this repository were last checked on 2026-10-08 and are historical.
See [COST-SOURCES.md](docs/COST-SOURCES.md) for the service checklist.
Do not treat any price, quota, or free-tier statement as current. **Re-verify current
official pricing, billing prerequisites, and regional eligibility immediately before
any provisioning.**

## Default local learning path

- PostgreSQL and optional Redis run locally.
- Use a Pub/Sub emulator or local event-bus adapter for event-delivery exercises.
- Firestore is deferred as an implementation adapter. Use a local adapter for
  repository-boundary exercises unless the Firestore milestone is separately
  approved.
- Validate Terraform formatting and configuration locally. Do not run `terraform apply` by default.
- Use local CI commands as the required checks. Hosted CI/CD is optional and must be cost-checked before enabling.

## Live cloud opt-in gate

- Any live GCP deployment is an optional experiment and requires explicit user approval before provisioning. Before applying infrastructure, complete all of the following:

- Identify every resource and API that will be enabled.
- Check current official pricing, free-tier eligibility, and billing requirements for the selected region and configuration.
- Estimate expected use and identify what could generate charges.
- Specify resource limits, cleanup commands, and how to verify deletion.
- Keep instances at zero minimum where supported, constrain resources and log volume, and clean up stored images and data.

### Resource inventory, cost review, and cleanup

No current prices are asserted here. For every optional resource below, check the
official pricing and billing documentation again before use; record the date,
region, configuration, workload estimate, and cleanup evidence in the milestone
notes. Do not treat quotas, budgets, or alerts as caps.

| Service/resource | Default | Cost items to re-verify | Cleanup after an explicitly approved experiment |
|---|---|---|---|
| Cloud Run | Design/validation only; min instances = 0 | Requests, CPU/memory, networking, minimum instances, region | `gcloud run services delete <service> --region <region>` |
| Firestore | Deferred; local adapter/emulator only | Reads/writes/storage, database mode, region, indexes, backups | Export if needed, then delete the database using the documented current GCloud procedure; verify deletion |
| Pub/Sub | Emulator/local adapter | Messages, retention, delivery, networking | Delete subscriptions, then topics with `gcloud pubsub subscriptions delete <subscription>` and `gcloud pubsub topics delete <topic>` |
| Artifact Registry | Local image build by default | Stored image bytes, downloads, region, retention | Delete repository with `gcloud artifacts repositories delete <repository> --location <location>` |
| Cloud Logging / Monitoring | Local logs/metrics by default | Ingested/stored log volume, metric ingestion/retention, exports | Remove sinks/alert policies and delete retained log data where supported; verify remaining resources |
| IAM and enabled APIs | Least-privilege design only | Re-verify any service/API-specific charges and billing prerequisites | Remove bindings/service accounts no longer needed; disable APIs only after checking dependencies |
| Secret Manager | Optional; local environment configuration is the default | Secret storage/version operations, access volume, region, replication, and billing requirements | Disable dependent workloads, destroy secret versions, then delete the secret; verify deletion |
| Terraform state storage (GCS bucket) | Local state by default; remote bucket is optional | Stored bytes, operations, location, versioning, retention, locking strategy | Back up required state, remove state objects/versions, then `gcloud storage buckets delete gs://<bucket>`; verify bucket removal |
| GitHub Actions | Local checks required; hosted workflow optional | Current included minutes, runner usage, storage/artifact retention, organization terms | Disable workflow and remove retained artifacts/caches as applicable |
| Memorystore / Cloud SQL | Not part of default path | Re-verify full provisioned-instance and storage charges before any experiment | Delete the instance and associated backups/data using the current service-specific command; verify deletion |

**Dated pre-provisioning checklist (2026-10-31):**

- [ ] Re-check official pricing and billing requirements for every selected service,
      region, and configuration. The 2026-10-08 research is historical only.
- [ ] Confirm Cloud Run minimum instances is `0` in every Terraform resource and the
      planned configuration.
- [ ] Review budget/alert configuration before any cloud action; document that it is
      detection, not a hard spend cap.
- [ ] Record the resource inventory, workload estimate, and verified cleanup command
      for each resource.
- [ ] Obtain explicit user approval before enabling APIs, creating resources, or
      enabling paid hosted workflows.

Do not treat a free tier, budget, or billing alert as a spending cap. Do not create Cloud SQL or Memorystore on the standard path.

If the cost cannot be confidently bounded at $0, keep the experiment local or stop for a decision.
