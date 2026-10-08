# COST-BOUNDARY.md

## Current cost policy

Target: **$0 for development** and **near-$0 for cloud demonstrations**.

The cloud portion is optional until the local system works.

## Current GCP pricing facts verified 2026-10-08

- Cloud Run request-based billing currently includes a free monthly allocation of 2 million requests, 180,000 vCPU-seconds, and 360,000 GiB-seconds under the published free tier.
- Pub/Sub currently includes the first 10 GiB of basic message-delivery throughput per billing account each calendar month.
- Firestore Standard currently provides a free tier of 1 GiB stored data, 50,000 document reads/day, 20,000 writes/day, 20,000 deletes/day, and 10 GiB/month outbound data transfer for one qualifying database.
- IAM API usage is free.
- Cloud Logging currently provides 50 GiB/project/month of logging storage in the published free allotment; retention beyond default periods can introduce charges.
- Artifact Registry currently shows up to 0.5 GiB of storage free per billing account before storage charges apply.
- Memorystore for Redis is provisioned infrastructure and is billed even when idle; do not include it in the default zero-cost cloud architecture.
- Cloud SQL is a paid managed service outside applicable trials/credits; it is not the default database for this project.

## Cost gates

Before cloud deployment:

- Create a billing budget/alert.
- Never use "min instances" on Cloud Run unless there is a learning reason.
- Avoid large container resources.
- Keep log volume low.
- Delete unused Artifact Registry images.
- Use the default Firestore database if relying on the free tier.
- Do not create Memorystore for the final project.
- Do not create a Cloud SQL instance for the normal path.

## Optional paid experiment

Cloud SQL may be used only as a documented experiment if the user has free credits or explicitly approves potential charges.

The project remains complete without it.

## Important

Free tiers are quotas, not a guarantee that the project can never incur charges. Pricing, free quotas, eligible regions, and billing requirements can change. Re-check official pricing pages immediately before provisioning.
