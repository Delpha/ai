# Website

Use `findAndValidateWebsite` → `getWebsiteResult`.

Supply `website` to validate a URL. To discover a site, omit it and supply company
signals such as `name` plus `country`, or `linkedin`.
MCP accepts `website`, `name`, `country` and `linkedin`; only REST additionally accepts `email`.
Use absolute HTTPS URLs and provide known identity signals even when validating.

```json
{"website":"https://www.se.com","name":"Schneider Electric Industries SAS","country":"France"}
```

Read `normalized_value`, `label`, `scores` and `recommendations`.
Reachability (`validity`) and identity agreement (`accuracy` / `consistency`) differ.
A live site can be a poor or contradictory match for the supplied legal entity.
A high recommendation score alone does not establish ownership.
Report disagreement instead of describing all successful checks as a confirmed company match.

Do not write a raw input URL back as the canonical value.
Treat `-1` as missing where allowed and explain limited evidence.
[Score handling](../SKILL.md#interpret-and-apply).

REST: `POST /v1/website` → `GET /v1/website/{job_id}`.
[MCP execution](mcp.md) · [API reference](https://help.delpha.io/delpha-api-and-mcp/api/website).
