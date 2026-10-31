# Optional cloud experiment teardown

**Status:** Draft. Run only for resources created after explicit user approval.

1. Inventory the approved project, region, APIs, Terraform workspace/state, resource
   names, and data. Confirm the target project to avoid deleting unrelated resources.
2. Export any data/state that must be retained. Inspect the Terraform plan and
   resource inventory; stop if unexpected resources are present.
3. Delete service resources using the verified commands in `COST-BOUNDARY.md`.
   Remove Cloud Run services, Pub/Sub subscriptions/topics, Artifact Registry
   repositories/images, and optional databases as applicable.
4. Remove IAM bindings/service accounts and unused APIs only after checking other
   dependencies.
5. Empty and delete an optional GCS Terraform state bucket only after securely
   backing up required state and checking object versions/retention.
6. Run Terraform destroy only in the explicitly approved workspace and only after
   reviewing its plan. Never destroy shared or unknown resources.
7. Verify resource deletion in the console/CLI, inspect remaining data/log storage,
   and re-check billing reports after their normal reporting delay.
8. Record what remains, cleanup evidence, and any cost uncertainty.
