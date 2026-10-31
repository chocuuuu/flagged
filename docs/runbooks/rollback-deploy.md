# Roll back a deployment

**Status:** Draft for an explicitly approved future deployment. No deployment is
required by the local project path.

1. Identify the service, region, last known-good revision, and triggering change.
2. Confirm authorization and that rollback is permitted for the affected data/schema.
3. For an approved Cloud Run service, route traffic to the known-good revision with
   `gcloud run services update-traffic <service> --region <region> --to-revisions=<revision>=100`.
4. Verify health, SDK bootstrap, and configuration revision behavior.
5. Preserve logs and incident evidence without copying tokens or secrets.
6. Do not run Terraform apply/destroy or create cloud resources as part of this
   runbook without explicit approval.
