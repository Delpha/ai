# Credits and limits

The app, MCP and REST share your team's Credit balance.

Read `GET https://api.delpha.io/v1/pricing` before planning usage. It needs no credential,
consumes no Credits and returns `result.use_cases[]` entries with `use_case`,
`operation` and `credits`. Prices can change; do not hardcode a table or assume a default
when pricing is unavailable.

## Accounting

A live submit reserves Credits before work starts.
The result read that delivers completion can settle that reservation or refund failed work.
Retrieval adds no additional charge and does not rerun the job, but can mutate accounting.
For batches, successful items settle and failed items are refunded.

Repeating a submission can create another job and charge.
REST callers should reuse an [idempotency key](rest-api.md#asynchronous-verification)
for a retry of the same intended job. MCP does not expose that header as a tool argument.

A `402` means an empty balance or exhausted key ceiling; inspect `code`.
Top up or resolve the ceiling/window before retrying.

New teams receive 100 free Credits. REST test keys return fixtures without reservations,
charges or ledger entries; MCP requires live credentials.
[Billing](https://app.delpha.ai/settings/billing),
[Usage](https://app.delpha.ai/settings/usage) and
[Developer logs](https://app.delpha.ai/developer/logs) show actual usage and balance.

Batch requests accept 1–100 items. Follow rate-limit headers and `Retry-After`.
Use a separate scoped key and budget for each integration.

[Pricing](https://delpha.ai/pricing) ·
[Credits guide](https://help.delpha.io/delpha-api-and-mcp/api/credits).
