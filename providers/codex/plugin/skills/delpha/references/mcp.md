# MCP connection and execution

Server: `https://mcp.delpha.ai/mcp` (Streamable HTTP).

Prefer Delpha OAuth sign-in. Clients discover the authorization server and use PKCE;
no client secret is needed. Manage access at
[Developer → MCP](https://app.delpha.ai/developer/mcp).

For headless clients, use `Authorization: Bearer <live-key>` through a secret environment
variable or protected credential store. Test-mode keys return `403 sandbox_key_unsupported`
over MCP; use REST for test mode.

## Connect

Codex:

```sh
codex mcp add delpha --url https://mcp.delpha.ai/mcp
codex mcp login delpha
```

Claude Code:

```sh
claude mcp add --transport http delpha https://mcp.delpha.ai/mcp
```

Then run `/mcp` and sign in. Follow the
[maintained guides](https://help.delpha.io/delpha-api-and-mcp/mcp) for other clients.
The Delpha plugins bundle the connection and skills.

## Contract

Use the tool list your client receives. The [hub](../SKILL.md#delpha) lists the eight
submit/result pairs. REST company search, batches, synchronous phone and pricing are not MCP tools.

Inputs are closed: unknown fields are rejected, including inside legal-ID `address`.
Phone accepts `country_code`, not REST's `country`. Website and LinkedIn tools
omit REST's `email` field.

Submit once, then call the matching result tool with its returned `job_id`.
It waits/polls internally. Only retrieve again after a returned `status_code: 202`,
after a wait. Do not launch concurrent result calls for one job.

The MCP envelope carries `message`, `status`, `status_code`, `code`, and `result`.
Result retrieval can settle/refund the original reservation, adds no additional charge and
is idempotent; its accounting effects mean it is not read-only.
REST idempotency headers are not MCP tool arguments.
A terminal error is an unresolved check, not a negative verdict about the entity.

[Release notes](https://help.delpha.io/delpha-api-and-mcp/mcp/release-notes) ·
[Credits](credits-and-limits.md) · [Security](security.md).
