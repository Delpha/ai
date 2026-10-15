---
name: delpha-gtm-account-routing
description: Use when a lead or company needs commercial-parent resolution and a new-logo, territory or CRM-routing decision.
---

# Commercial-parent account routing

Resolve commercial identity, then assess routing using the user's CRM context.
Read the [parent reference](../delpha/references/ultimate-parent.md) for result semantics.

1. Obtain `company_name` and `website`. Normalize a supplied bare domain to an absolute HTTPS URL.
   If the website is unknown, use the [website tools](../delpha/references/website.md) to resolve
   it from available company signals, or ask for the missing identity information.
2. Submit `findAndValidateUltimateParent` once, with country when known.
   Retrieve the returned `job_id` with `getUltimateParentResult`.
   Only retrieve again after a returned `202`, after a wait; stop on terminal error.
3. Use `result.ultimate_parent` as the recommended commercial/GTM parent.
   Explain a distinct `ultimate_financial_parent` when relevant; do not replace the commercial
   parent with a passive entity just because it appears higher in the chain.
4. Read `relationship_type`, `confidence` and available evidence. Report missing or conflicting
   evidence and shared ownership. Confidence is 0–1; choose review thresholds for the task.
   A registry source label does not prove LEI verification when `lei_data` is null.
5. Assess new-logo status only from supplied or authorized CRM evidence:
   - Commercial parent confirmed present: route under that existing account.
   - Commercial parent confirmed absent: propose a new-logo route.
   - CRM presence unknown: resolve the parent and state what CRM check is needed.

Lead with the decision, then name the commercial parent, relationship, confidence and supporting
source when available. Include a concise route: queried company → commercial parent.
Use current returned evidence; reference examples are not fixed answers.

Do not infer CRM presence from public web data or brand familiarity.
Do not claim a CRM write occurred; applying a route needs a separate integration and authorization.
For legal/financial ownership questions, report the relevant ownership evidence and limitations
without treating a GTM routing decision as a compliance determination.
