# Company legal identifier

Use `findAndValidateLegalID` → `getLegalIDResult` for a company's registered identifier.
Inputs are `name`, `website`, `legal_id`, `legal_id_type` and `address`.
The address is the company's registered address, not a person's location.

Supply a registry signal: `legal_id_type` or `address.country`.
Use the exact supported enum from the public API; unsupported registries are rejected
before Credit reservation. Do not advertise a registry absent from that enum.

```json
{"legal_id":"880524400","legal_id_type":"FRA - SIREN","name":"Delpha","address":{"city":"Paris","country":"France"}}
```

Read the top-level `normalized_value`, resolved `legal_id_type`, scores and `match`.
A supporting establishment SIRET can differ from a requested company SIREN.
Label each identifier by its returned type; never truncate a suggestion to manufacture a SIREN.

The returned match can include registration, address, industry, headcount or financial details;
fields may be missing. Preserve reported currency and dates. Do not assume financials are current
or convert amounts without an explicit conversion step.
Match quality and validation status are separate signals.

REST: `POST /v1/legal-id` → `GET /v1/legal-id/{job_id}`.
[MCP execution](mcp.md) · [API reference](https://help.delpha.io/delpha-api-and-mcp/api/legal-id).
