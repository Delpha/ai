---
type: llm
weight: 2
---

PASS if the reply gives the normalized number +33 6 72 55 73 78 (any spacing), says it is a
mobile line AND names the carrier Orange France. If it mentions the accuracy score of -1, it
treats it as not assessed for phone numbers.

FAIL if the reply calls the number invalid, gives a different line type or carrier, reports the
accuracy of -1 as a low, failed or negative result or lowers its verdict because of it, or gives a
verdict without a Delpha result.
