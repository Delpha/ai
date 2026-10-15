# Phone

Use `validateAndNormalizePhone` → `getPhoneResult` to check a number you already hold.
The tool does not find phone numbers.

MCP accepts only `phone` and optional `country_code` (ISO alpha-2).
An international `+` number is self-locating. For national format, supply `country_code`.
REST's async route additionally accepts a recognized English `country` name.

```json
{"phone":"0672557378","country_code":"FR"}
```

Read the E.164 `normalized_value`, `phone_type`, `carrier`, `timezone`,
`zone` and `area`. Area can be a city, region or country, or empty when unknown.
Optional provider fields can be null.

Phone `scores.accuracy` is always `-1` (not assessed); do not gate acceptance on it.
`scores.confidence` rates normalization/parse reliability, not reachability.
Read discrete `validity` and `consistency` separately.
Line type alone does not prove SMS capability or current ownership.

REST async: `POST /v1/phone` → `GET /v1/phone/{job_id}`.
Synchronous `GET /v1/phone` accepts `phone` and optional `country`;
its result uses boolean `valid`, not the async score object.
Read [current pricing](credits-and-limits.md) for either route.

[MCP execution](mcp.md) · [API reference](https://help.delpha.io/delpha-api-and-mcp/api/phone).
