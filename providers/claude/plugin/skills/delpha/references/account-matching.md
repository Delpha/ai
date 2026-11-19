# Account matching

Use `matchAccounts` to decide which of your own account records is a given company.
It is the only Delpha tool that evaluates your records, and it answers in the same call:
there is no `job_id` and no result tool. A record is a Delpha match only when
`matchAccounts` returned it, with its confidence and evidence. A record picked out by any
other means is your own conclusion; Delpha makes no claim about it.

Delpha never reads your systems. You gather the candidate records (from a CRM connector,
a warehouse or a CSV), format them, and send at most 100 per call.

## Request

```json
{"reference":{"legal_name":"Sephora SAS","website":"https://www.sephora.com","country":"FR"},
 "candidates":[{"id":"001A","name":"Sephora","website":"sephora.fr","country":"France"},
               {"id":"001B","name":"Sephora Brasil","website":"sephora.com.br","country":"BR"}]}
```

- `reference`: the entity you are looking for. Its fields are `legal_name`,
  `commercial_name`, `website`, `country`, `legal_id`, `legal_id_type` and `lei`.
  You build it, for example from a commercial-parent result.
- `candidates`: your records. `id` and `name` are required. They can also carry
  `website`, `country`, `legal_id`, `legal_id_type`, `lei`, `parent_id` and `hierarchy`.
- `country` takes an English name, a common alias or an ISO alpha-2/alpha-3 code.
  It is compared as an ISO code, and a value either side cannot identify is not compared.
- Send every field you hold, even one that may lower a score. A mismatch is evidence too.
- `top_k` (1–25) caps the matches returned. `ultimate_job_id` links the match to the
  parent call it follows; it fills nothing in.

## Reading the result

- `match_status`:
  - `confident`: one record stands apart.
  - `ambiguous`: read the top two.
  - `no_match`: none of the records **you sent** is this entity.
- `matches`: best first. Each carries your `id` and `name`, a `confidence` (0–1,
  comparable within one response only), an `evidence_level` and every `signals` entry,
  with the two values compared.
- `settings`: the configuration each score was computed with.

`no_match` is complete only for the records sent. If your query was narrow, say what
was searched before calling the company absent from the CRM.

## Finding the candidates

A finished commercial-parent result read through MCP carries `crm_lookup`. Its
`identifiers` (domains, names, legal IDs, LEI, country) are search terms, and `templates`
gives a ready query per dialect (SOQL, SQL, HubSpot search). Run the query on the user's
system, then send the returned rows as `candidates`.

## Team recipes

`getAccountRecipe` returns the team's saved mapping from its system's columns onto the
candidate fields. Without one, it returns presets to detect the platform. `saveAccountRecipe`
stores the mapping so later sessions skip the mapping step; a second save for the same
platform replaces the first.

Both are free. Follow the tool descriptions on when to ask the user before saving.
CSV and other ad-hoc exports are mapped per run and never saved.

The match reserves and settles Credits in the same call; see [credits](credits-and-limits.md).
REST: `POST /v1/account-match` returns `200` with the same result.
[MCP execution](mcp.md) · [API reference](https://help.delpha.io/delpha-api-and-mcp/api).
