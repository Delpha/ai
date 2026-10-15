#!/usr/bin/env python3
"""Check the public content: skills, links, tool names, plugin manifests and the skill copies."""
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

from sync_skills import ROOT, sync

# provider: (manifest and MCP config inside providers/<provider>/plugin/, marketplace file at the root)
PLUGINS = {
    "claude": (".claude-plugin/plugin.json", ".mcp.json", ".claude-plugin/marketplace.json"),
    "codex": (".codex-plugin/plugin.json", ".mcp.json", ".agents/plugins/marketplace.json"),
    "cursor": (".cursor-plugin/plugin.json", "mcp.json", ".cursor-plugin/marketplace.json"),
}
MCP_URL = "https://mcp.delpha.ai/mcp"
# The 16 tools served by the Delpha MCP server; update with the MCP release notes.
TOOLS = {
    "findAndValidateUltimateParent", "getUltimateParentResult",
    "findAndValidateWebsite", "getWebsiteResult",
    "findAndValidateLegalID", "getLegalIDResult",
    "findAndValidateLinkedInCompanyPage", "getLinkedInCompanyPageResult",
    "findAndValidateEmail", "getEmailResult",
    "findAndValidateLinkedInProfile", "getLinkedInProfileResult",
    "validateAndNormalizePhone", "getPhoneResult",
    "validateAndNormalizeName", "getNameResult",
}
REST_ONLY = {"findAndValidatePhone", "findAndValidateName"}  # REST operationIds, named in rest-api.md
TOOL = re.compile(r"\b(?:findAndValidate\w+|validateAndNormalize\w+|get\w+Result)\b")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
JSON_BLOCK = re.compile(r"```json\s*\n(.*?)\n```", re.S)


def check_file(root, path, text):
    problems = []
    if "DDQ-" in text:
        problems.append("internal ticket reference")
    if path.suffix == ".json":
        json.loads(text)
    if path.name == "SKILL.md":
        head = text.split("---", 2)[1] if text.startswith("---\n") else ""
        fields = dict(line.split(":", 1) for line in head.strip().splitlines() if ":" in line)
        if fields.get("name", "").strip() != path.parent.name or not fields.get("description", "").strip():
            problems.append("frontmatter needs a name matching its folder and a description")
    if path.suffix == ".md":
        for name in sorted(set(TOOL.findall(text)) - TOOLS):
            if not (path.name == "rest-api.md" and name in REST_ONLY):
                problems.append(f"unknown MCP tool {name}")
        for target in LINK.findall(text):
            target = target.split("#")[0]
            if target and not re.match(r"[a-z][\w+.-]*:", target):
                local = root / target.lstrip("/") if target.startswith("/") else path.parent / unquote(target)
                if not local.exists():
                    problems.append(f"broken link {target}")
        for block in JSON_BLOCK.findall(text):
            json.loads(block)
    return problems


def validate(root=ROOT):
    listed = subprocess.check_output(["git", "ls-files", "-co", "--exclude-standard", "-z"], cwd=root)
    paths = [root / name for name in sorted(set(listed.decode().split("\0"))) if name]
    problems = []
    for path in paths:
        relative = path.relative_to(root)
        if path.is_symlink():
            problems.append(f"{relative}: symlinks are not allowed")
        elif path.suffix in {".md", ".json"} and path.exists():
            try:
                problems += [f"{relative}: {issue}" for issue in check_file(root, path, path.read_text())]
            except ValueError as error:
                problems.append(f"{relative}: malformed JSON ({error})")
    try:
        sync(root, check=True)
    except ValueError as error:
        problems.append(str(error))

    versions = []
    for provider, (manifest, mcp, market) in PLUGINS.items():
        package = Path("providers") / provider / "plugin"
        plugin = json.loads((root / package / manifest).read_text())
        entry = next(item for item in json.loads((root / market).read_text())["plugins"]
                     if item["name"] == plugin["name"])
        source = entry["source"]["path"] if isinstance(entry["source"], dict) else entry["source"]
        if (root / source).resolve() != (root / package).resolve():
            problems.append(f"{market}: source must point to {package}")
        if not re.fullmatch(r"\d+\.\d+\.\d+", plugin["version"]) or entry.get("version", plugin["version"]) != plugin["version"]:
            problems.append(f"{package}: version must be semver and match {market}")
        servers = json.loads((root / package / mcp).read_text())["mcpServers"]
        if servers.get("delpha", {}).get("url") != MCP_URL:
            problems.append(f"{package}/{mcp} must connect to {MCP_URL}")
        interface = plugin.get("interface", {})
        references = {plugin.get("skills"), plugin.get("mcpServers"), interface.get("logo"), interface.get("composerIcon")}
        for reference in sorted(references - {None}):
            if not (root / package / reference).exists():
                problems.append(f"{package}/{manifest}: missing {reference}")
        versions.append(f"{provider} {plugin['version']}")

    if problems:
        sys.exit("\n".join(problems))
    print(f"Release checks passed: {len(paths)} files; plugins {', '.join(versions)}.")


if __name__ == "__main__":
    validate()
