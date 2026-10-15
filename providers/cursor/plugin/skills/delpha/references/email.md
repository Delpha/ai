# Email

Use `findAndValidateEmail` → `getEmailResult`.

Validate an address with `email`, or recommend a business address using
`first_name`, `last_name` and `website` together. Partial recommendation inputs are rejected.
Providing an email plus the complete triple runs both paths.

```json
{"first_name":"Jane","last_name":"Doe","website":"https://acme.example"}
```

Submit once, then retrieve with the returned `job_id`; follow [MCP execution](mcp.md).
REST uses `POST /v1/email` then `GET /v1/email/{job_id}`;
see the [API reference](https://help.delpha.io/delpha-api-and-mcp/api/email).

Read `normalized_value`, `email_status`, `email_domain_qualification`,
`email_domain`, `label`, `scores` and suggestions separately.
A candidate address or high suggestion score is not a validated mailbox.
Catch-all domains accept nonexistent local parts; a Valid status there is weaker evidence.
Do not silently replace an invalid address with a suggestion.
Store status/qualification as metadata, never in the email-value field.

Common validity/consistency scores are discrete; see [score handling](../SKILL.md#interpret-and-apply).
Unknown and `-1` signals need review.
Delpha generates and verifies candidates rather than retrieving a contact database.

[API reference](https://help.delpha.io/delpha-api-and-mcp/api/email) ·
[Data sources](https://help.delpha.io/delpha-api-and-mcp/api/data-sources-and-privacy).
