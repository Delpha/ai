# Skills

Agents need instructions to use a service well. This folder holds Delpha's
[agent skills](https://agentskills.io): what to send to each Delpha tool, and how to read
the findings, scores and evidence that come back.

- [delpha](delpha/SKILL.md): tool selection, inputs, result interpretation and REST integrations.
- [delpha-gtm-account-routing](delpha-gtm-account-routing/SKILL.md):
  commercial-parent and new-logo decisions using supplied CRM context.

Install them with a [plugin](../README.md#get-started), or copy both folders
into any skills-aware client.

These are the canonical sources. After editing them, run `python3 scripts/sync_skills.py`
to update the plugin copy. See [contributing](../CONTRIBUTING.md).
