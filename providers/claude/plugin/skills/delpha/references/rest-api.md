# REST API

Base: `https://api.delpha.io`.
[Production OpenAPI](https://delpha-static-ressources.s3.eu-west-1.amazonaws.com/openapi.json)
is the request/response contract. [Full guides](https://help.delpha.io/delpha-api-and-mcp/api).

## Authentication and test mode

Send `Authorization: Bearer <Delpha API key>`. Create a key at
[Developer → API keys](https://app.delpha.ai/developer/api-keys).
Keys can have use-case scopes, expiry and a Credit ceiling.
No scopes means full access; a restricted key must allow the requested route.
OAuth client credentials are also documented in the API authentication guide.

Test-mode keys use the same routes/schemas, return canned fixtures and spend no Credits.
A fixture is not evidence about a real person or company. MCP serves live credentials only.

## Asynchronous verification

`POST /v1/<usecase>` returns HTTP `202`, a `job_id`, a `Location` poll URL and `Retry-After`.
`GET /v1/<usecase>/{job_id}` returns `202` while running, `200` on completion.

Use cases: `email`, `phone`, `name`, `website`, `legal-id`,
`linkedin-profile`, `linkedin-company-page`, `ultimate`.

REST operation IDs for phone/name remain `findAndValidatePhone` /
`findAndValidateName`; MCP wire names are `validateAndNormalizePhone` /
`validateAndNormalizeName`. REST ultimate submit is `submitUltimateParent`;
MCP uses `findAndValidateUltimateParent`.

Reuse a caller-generated `Idempotency-Key` when retrying the same intended submission.
Within 24 hours, the same caller, key and body replay the original job without a new reservation.
A changed body or in-progress claim can return `409`; inspect the stable error `code`.
Do not generate a fresh key for an ambiguous retry.

Follow `Retry-After`, use backoff and a deadline, and stop on terminal errors.
REST responses include `code` and `request_id`; errors can link to documentation.
Result retrieval can settle/refund the original reservation once; repeats add no charge.

See the [API guides](https://help.delpha.io/delpha-api-and-mcp/api). Read the operation schema for
accepted fields and enums; MCP has a narrower surface.

## Other public operations

- Batch: `POST /v1/<usecase>/batch` accepts `{"items": [...]}`, 1–100 items.
  Retrieve at `GET /v1/<usecase>/batch/{job_id}`. Preserve input positions for correlation.
  Successful items settle; failed items are refunded. Fetch expiring `result_url` links promptly.
- Company search: `GET /v1/company`, for example `account_name` and `country_code`.
  Follow published filters/pagination. This is a charged REST operation, not an MCP tool.
- Synchronous phone: `GET /v1/phone` accepts `phone` and, for national format, `country`.
  It returns boolean `valid`; do not assume the async score shape.
- Pricing: `GET /v1/pricing` is credential-free and consumes no Credits.
- Webhooks: configure at [Developer → Webhooks](https://app.delpha.ai/developer/webhooks).
  Verify signatures using the [webhook guide](https://help.delpha.io/delpha-api-and-mcp/api/webhooks).

## Status codes

| HTTP status | Action |
| --- | --- |
| 200 / 202 | Completed / accepted or running. |
| 400 / 422 | Correct input; do not retry unchanged. |
| 401 / 403 | Check credentials, mode, scope and access. |
| 402 | Resolve balance or key ceiling first. |
| 404 | Check job ID/access; do not infer another team's data. |
| 409 | Inspect `code`: idempotency conflict and expired reservation differ. |
| 429 | Respect `Retry-After`; keep retries bounded. |
| 500 / 502 / 504 | Surface the failure; do not automatically submit another paid job. |

[Errors](https://help.delpha.io/delpha-api-and-mcp/api/errors) ·
[Idempotency](https://help.delpha.io/delpha-api-and-mcp/api/idempotency) ·
[Credits](credits-and-limits.md).
