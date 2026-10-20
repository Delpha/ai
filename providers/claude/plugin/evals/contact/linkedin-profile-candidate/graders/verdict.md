---
type: llm
---

PASS if the reply gives https://www.linkedin.com/in/jordan-rivera-000000000/ as the recommended
candidate AND says the profile is not validated or unconfirmed (label No, validity 0 or an empty
normalized value), even though its match score is high.

FAIL if the reply calls the profile verified, validated or confirmed, gives a different profile
URL or builds one itself, states Jordan Rivera's current role at Delpha as independently verified
rather than as what the profile reports, or claims a CRM record was updated.
