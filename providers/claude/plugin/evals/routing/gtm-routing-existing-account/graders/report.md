---
type: llm
weight: 2
---

The user has a lead from Starbucks Coffee Chile and an existing CRM account for Starbucks
Corporation. The Delpha result returned Starbucks Corporation as the commercial parent,
relationship Member Firm/Franchise, confidence 1, an SEC filing as the source (sec.gov), and
Alsea, S.A.B. de C.V. in the chain as the franchisee operator: flagged as the ultimate financial
parent and discarded for GTM routing.

PASS if the reply does all of the following:
- states the decision at the start (first sentence, heading or opening line): route the lead under
  the existing Starbucks Corporation account, not as a new logo;
- cites at least one returned value: the Member Firm/Franchise relationship, the confidence 1
  (or 100%), or the SEC filing source;
- names Alsea as the financial owner or operator that was set aside (discarded) for routing.

FAIL if any of these holds:
- the reply's decision is a new logo, or routing under Alsea or a new Alsea account, or it
  presents Alsea as the commercial parent (naming Alsea as the financial owner is expected);
- it gives no routing decision, or gives it only after the analysis;
- it cites none of the relationship, the confidence or the SEC source;
- it does not mention Alsea;
- it claims that a CRM record was created, updated or re-routed.
