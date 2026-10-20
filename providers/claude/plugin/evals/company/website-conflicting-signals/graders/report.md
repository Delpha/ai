---
type: llm
weight: 2
---

The user asked to validate https://www.delpha.io as the website of Delpha, France. The Delpha
result returned label "No", validity 1 (the site is reachable), consistency 0 and accuracy 0.2
(nothing found ties the site to Delpha, France), and one alternative candidate,
https://delpha.ai/, with score 0.8.

PASS only if the reply does all of the following:
- reports that the site is reachable or technically valid (validity 1);
- reports that its identity match with Delpha, France is not supported (label No, low accuracy or
  consistency 0), and presents these two signals as disagreeing;
- presents https://delpha.ai/ as a candidate to review, not as a confirmed replacement.

FAIL if any of these holds:
- the reply calls https://www.delpha.io validated, confirmed or correct for Delpha;
- it ignores or dismisses the label No, the low accuracy or the consistency 0;
- it states that https://delpha.ai/ is Delpha's website as a verified fact, or says to replace
  the URL without review;
- it claims that a CRM record was created or updated.
