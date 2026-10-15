# Commercial ultimate parent

Use `findAndValidateUltimateParent` → `getUltimateParentResult`.

Both `company_name` and `website` are required; use `country` when known.
Convert a supplied bare domain to an absolute HTTPS URL before calling.

```json
{"company_name":"Sephora Brazil","website":"https://www.sephora.com.br","country":"Brazil"}
```

Read these fields in `result`:
- `ultimate_parent`: recommended commercial parent, the operating group used for sales routing.
- `ultimate_financial_parent`: a distinct financial owner, when returned; do not substitute it
  for the commercial parent in GTM decisions.
- `relationship_type`, `confidence` (0–1), `ownership_chain`, `comment`,
  `source_url` and other available evidence.
- `is_discarded` flags entities set aside when choosing the commercial route.
- `lei_data` carries registry metadata only when a match exists; null is not verified LEI data.

Parent results use `confidence`, not the common `scores` / `normalized_value` shape.
The chain runs from the queried entity upward and can include financial or discarded entities.
Identify the selected parent from `ultimate_parent`, not simply the last chain element.
An independent company may be its own parent and have an empty chain.

For new-logo decisions, follow the [routing skill](../../delpha-gtm-account-routing/SKILL.md).
You also need supplied or authorized CRM evidence of account existence.
Explain uncertainty, shared ownership and contradictory/missing evidence.
Use the returned sources, not reference examples, as the current answer.
Do not present this verification as a completed legal or compliance determination.

REST: `POST /v1/ultimate` → `GET /v1/ultimate/{job_id}`.
[MCP execution](mcp.md) · [API reference](https://help.delpha.io/delpha-api-and-mcp/api/ultimate-parent).
