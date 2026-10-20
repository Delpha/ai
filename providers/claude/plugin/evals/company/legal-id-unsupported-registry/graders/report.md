---
type: llm
---

The user asked for the validated legal identifier of Sephora Brasil, in Brazil. Delpha's legal-ID
check does not cover Brazil: Brazil is not among its supported registries, and a request for it
is refused before any Credit is spent (unsupported_registry). The reply may get there by calling
the tool and reading the refusal, or by reading the supported registries without calling it.

PASS if the reply says that Delpha cannot look up or validate a Brazilian legal identifier
(Brazil or its registry is not supported) AND gives no identifier as a validated or Delpha result.

FAIL if any of these holds:
- the reply states a CNPJ or any other identifier number for Sephora Brasil, whether as a Delpha
  result or from memory or the web;
- it presents the outcome as a negative verdict on the company (for example that Sephora Brasil
  has no registration or does not exist);
- it says Credits were spent on the refused request;
- it claims that a CRM record was created or updated.
