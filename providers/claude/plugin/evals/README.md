# Plugin evals

Behaviour tests for the Claude Code plugin, run with `claude plugin eval` (Claude Code 2.1.269 or
later; docs at https://code.claude.com/docs/en/plugin-evals). Each case sends a realistic request to
a fresh Claude Code session with only this plugin loaded, then grades the reply and the tool calls:
did it submit the right job once, read its result, report the returned values and caveats, and
avoid claims the result does not support. By default each case also runs without the plugin, and
the difference is what the plugin contributes.

| Folder | What the cases cover |
| --- | --- |
| `company/` | Commercial parent, website, legal identifier |
| `contact/` | Email, phone, LinkedIn profile |
| `command/` | `/delpha:verify-company` and `/delpha:verify-contact` |
| `routing/` | New-logo and routing decisions |
| `rules/` | Failed calls, unavailable tools, CRM writes, REST guidance |
| `negative/` | Requests the plugin must leave alone |

## Run

From the repository root, and pass the plugin path. `claude plugin eval delpha@delpha` would read
the installed copy of the plugin, not your working tree.

```sh
# One case, one run, with the plugin only
claude plugin eval providers/claude/plugin --case parent-sephora-brazil --runs 1 --ablation none -j 2 \
  --threshold 0.75 --no-publish

# The whole suite, with the no-plugin baseline (3 runs per case and arm)
claude plugin eval providers/claude/plugin -j 2 --threshold 0.75 --no-publish

# The CI invocation
claude plugin eval providers/claude/plugin --trust-plugin --ablation none --runs 2 -j 2 \
  --model claude-sonnet-5-5 --judge-model claude-sonnet-5-5 --threshold 0.75 \
  --max-cost-usd 20 --no-publish
```

- Always pass `--no-publish`, so the HTML report stays a local file.
- Pass `--threshold 0.75`, as CI does. Without it a case passes only at 1.0, and under
  `--ablation none` the skill-fired indicator is scored: a correct run that did not load the skill
  scores 0.99 and the command exits 1.
- Start with `-j 2` on a Claude subscription; more concurrent runs share the same rate limit.
- The first run asks whether to trust the plugin directory. Inside a Git repository, answering yes
  trusts the whole repository, for interactive sessions too. `--trust-plugin` skips the prompt.
- Results go to `evals/results/<timestamp>/` (ignored by Git) or `--output-dir`; without `--json`,
  each grader's result and explanation print as the run progresses.

## Cost

Every run and every judge vote is a real model call on your account. One run of a tool case costs
about $0.10 at list price with the default model, judge included. The full suite with its baseline
is about 100 agent runs, on the order of $10; the CI invocation is about 34 runs on Sonnet.
`--max-cost-usd` stops starting new runs once its list-price estimate is spent.

## Mocks

The Delpha MCP server is never started (the suite never passes `--allow-real-servers` or
`--mocks off`), and no Credit is spent. Each tool answers from a fixed
file in `mocks/delpha/<tool>.md`; a case can override a tool with its own `mocks/delpha/<tool>.md`.

- A mock body is the tool result: one line of JSON after the frontmatter, in the envelope the
  server returns (`code`, `message`, `status`, `status_code`, plus `job_id` on a submission, which
  the ultimate-parent result echoes, and `result` on a result). A failed submission is a tool error, written with `error: true` and the
  error text the client receives.
- Suite-wide mocks carry no `expect:` guard: a guard aborts every call that lacks one of its keys,
  so input checks live in the case that needs them.
- `mocks/delpha/_tools.json` is the production tool catalogue (names, titles, descriptions, input
  schemas, annotations), so the model sees the real tools. It is composed from the public OpenAPI
  document (https://delpha-static-ressources.s3.eu-west-1.amazonaws.com/openapi.json) by the
  server's own tool builder, the code that serves the tool list, and refreshed by the maintainers
  when the server changes; it cannot be regenerated from this
  repository. `scripts/check_release.py` checks that its tool names equal `TOOLS`. That check
  guards internal consistency only: `TOOLS` is edited by hand and CI never contacts the server, so
  a server-side rename is caught only when a maintainer updates `TOOLS`.

The fixtures (Sephora Brasil and LVMH, Delpha, the placeholder contact Jordan Rivera, Starbucks
Coffee Chile) are illustrative captures from the public API examples and recorded results. They
are not promised results: the live service can answer differently today.

## Writing a case

A case is a folder with `prompt.md` (frontmatter: `max_turns`, `allowed_tools: [Read, Glob, Grep,
Skill]`, `tags`) and one file per grader in `graders/`.

- Write the prompt as a user would. Never name a tool; name the product ("with Delpha") when a
  user with the plugin installed would.
- Name a tool in `tool_used` and `tool_order` graders by its full name,
  `mcp__plugin_delpha_delpha__<tool>`, or `Skill`. A short name silently counts zero calls.
- Pair a grader on the reply with one on the calls: an `llm` rubric with concrete PASS and FAIL
  conditions, a `regex` on a value only the fixture holds, and a `tool_used` or `tool_order` on
  the submission.
- Anchor on fixture-only values (a confidence, a label, a source URL), never on a famous name the
  model could answer from memory. The baseline arm has no tools, so memory is all it has.
- The skill-fired check (`tool_used: Skill`) is an indicator with `weight: 0.01`; a correct
  answer does not require the skill to fire. Checks that must count in both arms set `arm: both`;
  a check that passes with zero tool calls, such as `max: 0`, sets `arm: with-only`, because the
  baseline arm has no tools and would pass it for free.
- Weight the reply rubric so that its failure alone drops the run below 0.75: above a third of
  the other graders' total weight (`weight: 2` against four checks, `weight: 3` against eight).
- Use real, public example identities: the model recognises reserved test domains and refuses to
  spend a Credit on them. No Markdown links, no tool-shaped word other than the 16 real tool
  names, and no key-shaped literals, for `scripts/check_release.py` and the credential scan.

## CI

`.github/workflows/plugin-evals.yml` runs the suite on pushes to `main` that change the plugin or
the skills, and on manual dispatch with a run count and a case filter. It needs an
`ANTHROPIC_API_KEY` secret in the `evals` environment. Before the first run, store the key there,
restrict the environment's deployment branches to `main`, and set a spend limit on the key's
workspace: `--max-cost-usd` is a client-side list-price estimate, not a hard limit. A merge that
changes the plugin or this workflow starts a run, which fails without the secret. The job summary
lists each case's score, its verdict at the 0.75 threshold and any run error, and the results
are kept as a workflow artifact.
