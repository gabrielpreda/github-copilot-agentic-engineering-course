# Review exercise — export completed tasks

The API team approved a small endpoint for clients that need to export completed tasks.

## Acceptance criteria

- `GET /tasks/export` returns completed tasks only, using the existing task response shape.
- The endpoint supports the same optional owner filter and authorization rules as task listing.
- Invalid filter input uses the API's existing 422 validation response.
- The existing list endpoint and its behavior remain unchanged.
- No new runtime dependency is needed for this JSON response.

The patch below was generated with Copilot assistance. Review it as an untrusted proposed change. It is intentionally flawed; it is not a patch for the course Target project.
