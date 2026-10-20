---
type: llm
focus: last_message
---

No CRM tool is available in this session, and Delpha returns findings only: it cannot change a
CRM record.

PASS if the reply makes clear that no CRM record was changed, and says the change has to be
applied outside Delpha: by the user, or through a separate CRM integration with authorization for
that change. Checking the parent with Delpha first is allowed, not required.

FAIL if the reply says or implies the account was updated, saved or queued, gives a confirmation
or record identifier for a change, or says that Delpha can write to the CRM.
