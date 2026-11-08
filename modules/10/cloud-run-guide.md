# Optional Cloud Run staging path

Use this path only when the trainer has prepared a non-production Google Cloud project, region, service identity, and budget. A successful CI run does not authorize a cloud deployment. Follow the repository's deployment Skill and receive explicit approval for the exact target/revision before deployment.

## Preconditions

- A reviewed story branch or approved integration commit has passed required CI.
- The target Google Cloud project, region, service name, access mode, runtime identity, and rollback method are confirmed.
- The trainer confirms who may deploy and that the identity has only the required permissions.
- The Cloud Run service's current IAM/access policy is inspected. Do not make a public service private or a private service public as an incidental deployment change.
- The optional Dockerfile overlay has been added to the Target project as **ADD** at `Dockerfile`, and the resulting container starts with the `PORT` environment variable.

## Deploy from a local authorized environment

Use a trainer-provided command with explicit values, after approval. For example:

```bash
gcloud run deploy task-api \
  --source . \
  --project YOUR_TRAINING_PROJECT \
  --region YOUR_REGION \
  --no-allow-unauthenticated
```

The example requests a private service on creation; if updating an existing service, inspect its current access policy and use the approved setting. Do not run this against production. Prefer Workload Identity Federation over long-lived service-account keys when a GitHub Actions deployment path is configured.

## Verify and record

1. Inspect the Cloud Run service and confirm the newly created revision is ready and traffic is routed as intended.
2. Obtain the service URL and call `/healthz` using the service's approved authentication path. Do not expose a private service merely to make a smoke check convenient.
3. For a private endpoint, use an authorized identity-token flow or the trainer's prepared smoke-test method. Record the identity/access path without logging the token.
4. Inspect revision logs and request status. Record project, region, service, revision, URL/resource identifier, verification request/result, and logs checked.
5. If readiness or the health check fails, stop and report the evidence. Use rollback only through the approved procedure.

## GitHub Actions deployment extension

An optional later exercise may add a manual `workflow_dispatch` deployment job that references a protected GitHub `staging` environment and authenticates to Google Cloud through Workload Identity Federation. Use a dedicated deployment identity, the `id-token: write` permission only on that job, branch restrictions, and required environment reviewers where the repository plan supports them. Never use a service-account JSON key committed to the repository or trigger deployment automatically on every feature-branch push.
