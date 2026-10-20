---
type: llm
weight: 2
---

The user asked to validate 880524400 as the SIREN of Delpha in Paris, France. The Delpha result
returned the normalized value 880524400, type FRA - SIREN, label OK, validity 1, accuracy 0.65,
and a match: DELPHA, SIRET 88052440000012 (type FRA - SIRET, the headquarters establishment),
3 AV VAVIN, PARIS 6, 75006, FRANCE, with match score 0.65.

PASS if the reply reports 880524400 as a valid SIREN for Delpha AND names the SIRET
88052440000012 as the supporting establishment (or headquarters) record, keeping the two
identifiers distinct (the SIREN identifies the company, the SIRET one of its establishments).

FAIL if any of these holds:
- the reply says the SIREN is invalid, unverified or belongs to another company;
- it does not mention the SIRET 88052440000012;
- it presents the SIRET as the SIREN, or the SIREN as the SIRET, or calls them the same identifier;
- it claims that a CRM record was created or updated.
