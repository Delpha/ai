---
description: Bulk email validation over REST; the reply uses the batch route in batches of at most 100 and calls no MCP tool.
max_turns: 20
allowed_tools: [Read, Glob, Grep, Skill]
tags: [rules, rest]
---

I have 5,000 email addresses in a CRM export and want to validate them all with the Delpha REST
API, from a Python script. How should I do it?
