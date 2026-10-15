# LinkedIn

People: `findAndValidateLinkedInProfile` → `getLinkedInProfileResult`.
Companies: `findAndValidateLinkedInCompanyPage` → `getLinkedInCompanyPageResult`.

Validate a supplied `url`, or omit it to search.
For a person, provide `first_name` and `last_name` with employer context
(`company_name` and/or `website`) to distinguish namesakes.
For a company page, provide `company_name`, preferably its `website`.
Use `country` to disambiguate when known.
REST accepts an employer `email` signal on the profile route; MCP omits it.

```json
{"first_name":"Jane","last_name":"Doe","company_name":"Acme","website":"https://acme.example"}
```

```json
{"company_name":"Delpha","website":"https://delpha.io"}
```

Read the normalized `url`, `label`, `scores`, recommendations and available evidence.
Recommendation/match confidence and URL validation are separate.
If validity is 0 or the normalized URL is empty, report a candidate as unconfirmed even if
its recommendation score is high. Do not construct a missing profile URL.

`recommendation_status` can identify confident, ambiguous or no-match results;
handle future values gracefully. `fallback_used` indicates candidates outside the
requested employer; do not claim that employer is confirmed.
When `url_changed` and `suggested_url` are returned, distinguish the old URL from the suggested one.
Report titles as source-reported, without claiming independently verified current employment.

REST: `POST /v1/linkedin-profile` or `POST /v1/linkedin-company-page`, then its result route.
[MCP execution](mcp.md) ·
[Profile reference](https://help.delpha.io/delpha-api-and-mcp/api/linked-in-profile) ·
[Company-page reference](https://help.delpha.io/delpha-api-and-mcp/api/linked-in-company-page).
