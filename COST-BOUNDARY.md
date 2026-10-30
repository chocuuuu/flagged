# COST-BOUNDARY.md

## Default cost policy

The default project path is designed for **$0 in cloud-service charges**. Local development, tests, and cloud-learning exercises should use local services, emulators, or adapters wherever practical.

No live GCP resource is required to complete the project. Cloud architecture, Terraform configuration, IAM policy design, and service behavior can be studied and validated locally without applying infrastructure.

The default path also avoids paid hosted services. Before enabling hosted CI/CD or other external services, check their current quotas and billing terms.

## Default local learning path

- PostgreSQL and optional Redis run locally.
- Use a Pub/Sub emulator or local event-bus adapter for event-delivery exercises.
- Use Firestore's local emulator for document-model experiments where practical; otherwise test the repository boundary with a local adapter and document the limitation.
- Validate Terraform formatting and configuration locally. Do not run `terraform apply` by default.
- Use local CI commands as the required checks. Hosted CI/CD is optional and must be cost-checked before enabling.

## Live cloud opt-in gate

- Any live GCP deployment is an optional experiment and requires explicit user approval before provisioning. Before applying infrastructure, complete all of the following:

- Identify every resource and API that will be enabled.
- Check current official pricing, free-tier eligibility, and billing requirements for the selected region and configuration.
- Estimate expected use and identify what could generate charges.
- Specify resource limits, cleanup commands, and how to verify deletion.
- Keep instances at zero minimum where supported, constrain resources and log volume, and clean up stored images and data.

Do not treat a free tier, budget, or billing alert as a spending cap. Do not create Cloud SQL or Memorystore on the standard path.

If the cost cannot be confidently bounded at $0, keep the experiment local or stop for a decision.
