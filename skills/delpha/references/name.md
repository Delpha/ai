# Name

Use `validateAndNormalizeName` → `getNameResult` for a first/last name you already hold.
Both `first_name` and `last_name` are required. This does not search for people.

```json
{"first_name":"jane","last_name":"DOE"}
```

Read `normalized_value.first_name` and `normalized_value.last_name`, `label` and suggestions.
Name scores have a distinct shape:
- `accuracy` and `reversed` are scalar numbers.
- `validity`, `completeness`, `consistency` and `misspelled` are per-field objects
  with `first_name` and `last_name` numbers.
- Suggestions are grouped by first/last name, with a `value` and `score` per entry.

Do not flatten these objects or apply the common integer score assumptions.
Surface a possible swapped pair or spelling change for assessment rather than silently
substituting a different person's name. Treat missing `-1` signals accordingly.
Do not infer demographics or current employment.

REST: `POST /v1/name` → `GET /v1/name/{job_id}`.
[MCP execution](mcp.md) · [API reference](https://help.delpha.io/delpha-api-and-mcp/api/name).
