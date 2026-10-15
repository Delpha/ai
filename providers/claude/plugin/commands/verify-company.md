---
description: Verify a company — commercial parent, website, legal identifier and LinkedIn page
argument-hint: "[company name + website (+ country)]"
---

Use the Delpha MCP tools to verify the company described by: **$ARGUMENTS**

Follow the `delpha` skill and read each capability's reference before calling its tool.

1. Submit only the jobs the input supports, each once, then read each with its matching result tool:
   - `findAndValidateUltimateParent` — needs `company_name` **and** `website`.
   - `findAndValidateWebsite` — validate or discover the company's website.
   - `findAndValidateLegalID` — pass `address.country` or a `legal_id_type`.
   - `findAndValidateLinkedInCompanyPage` — `company_name`, preferably with `website`.
   Each submission reserves Credits; check the current prices at https://api.delpha.io/v1/pricing.
2. Report the commercial parent and any distinct financial parent, then each verified field with
   its status, scores or `confidence`, and the supporting evidence. Choose review thresholds for
   the task, and name missing or conflicting evidence instead of filling gaps.
3. These tools return findings only; they do not write to a CRM. Do not claim a change was applied.
