---
type: llm
weight: 3
---

PASS only if the reply covers all four checks, each with its status and its scores or confidence:
- commercial parent: Delpha is its own ultimate parent (independent, no parent above it), with
  confidence 0.9 (or 90%);
- website: https://delpha.io/ with label OK;
- legal identifier: SIREN 880524400 with label OK (the SIRET 88052440000012 may be named as the
  matched establishment) and its accuracy of 0.65;
- LinkedIn page: https://www.linkedin.com/company/delphainc/ with label OK and an accuracy of
  about 0.87.

FAIL if any of the four is missing or reported without a status or score, if another company is
named as Delpha's commercial parent or financial owner, if a reported value contradicts the
results, or if the reply claims a CRM record was created or updated.
