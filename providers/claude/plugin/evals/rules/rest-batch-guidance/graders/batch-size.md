---
type: llm
weight: 2
focus: last_message
---

The Delpha REST batch route for email accepts 1 to 100 items per request, so 5,000 addresses need
at least 50 batch requests, each retrieved by the job id it returns.

PASS if the reply's guidance or code sends the addresses through the email batch route in chunks
of at most 100 items (50 or more requests for 5,000) and reads each batch's result by its job id.
Credit, but do not require: a test-mode key for a dry run that spends no Credits; reusing the same
idempotency key when retrying a submission; following Retry-After or backing off on 429.

FAIL if the reply sends more than 100 items in one request, puts all 5,000 addresses in a single
call, recommends one request per address as the main approach, or tells the user to do the bulk
run through MCP tools instead of the REST API.
