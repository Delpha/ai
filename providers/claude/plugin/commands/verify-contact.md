---
description: Verify a business contact — email, phone, name and LinkedIn profile
argument-hint: "[email | name + company | phone]"
---

Use the Delpha MCP tools to verify the business contact described by: **$ARGUMENTS**

Follow the `delpha` skill and read each capability's reference before calling its tool.

1. Decide which fields the input supports, then submit each job once and read it with its matching
   result tool:
   - `findAndValidateEmail` — validate a supplied `email`, or recommend one from `first_name`,
     `last_name` and `website` together.
   - `findAndValidateLinkedInProfile` — `first_name` and `last_name` with the employer
     (`company_name` and/or `website`) so a namesake does not win.
   - `validateAndNormalizePhone` and `validateAndNormalizeName` — validate values you already
     hold; they do not discover people or numbers.
2. Report each field with its normalized value, status or label and scores. Label recommendations
   as candidates unless validated; never invent an email or profile URL. Choose review thresholds
   for the task.
3. These tools return findings only; they do not write to a CRM. Do not claim a change was applied.
