# Contributing

Bug reports and suggestions are welcome: [open an issue](https://github.com/Delpha/ai/issues).
Report vulnerabilities privately, as described in [SECURITY.md](SECURITY.md).

## Content

Document what the production Delpha MCP server, REST API and app serve today.
Use [delpha.ai](https://delpha.ai), the
[public OpenAPI](https://delpha-static-ressources.s3.eu-west-1.amazonaws.com/openapi.json)
and the [MCP release notes](https://help.delpha.io/delpha-api-and-mcp/mcp/release-notes) as sources.

Keep each `SKILL.md` focused on the decisions an agent needs, and put capability details in
its `references/`. Use illustrative examples without promising fixed lookup results.

## Making a change

1. Fork the repository and edit the canonical [skills/](skills/) — never the copies under `providers/`.
2. Run the checks (Python 3.10+, no dependencies):

   ```sh
   python3 scripts/sync_skills.py      # update the plugins' copies of skills/
   python3 scripts/check_release.py    # links, tool names, frontmatter, manifests
   ```

3. When a plugin's content changes, bump its `version` (each plugin has its own): in
   `providers/<client>/plugin/.<client>-plugin/plugin.json`, and for Claude Code and Cursor also in
   `.claude-plugin/marketplace.json` or `.cursor-plugin/marketplace.json`.
4. Open a pull request. CI runs the same checks and scans the Git history for credentials.

When the MCP server adds or renames a tool, update `TOOLS` in `scripts/check_release.py`.
