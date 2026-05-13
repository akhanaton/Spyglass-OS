# Connections

Registry of every system your AIOS can reach. Filled by `/onboard` from Q4-Q7 answers; expanded over time as you wire new tools. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | Dodo Payments | not yet connected | — | — |
| 2 | Customer interactions | Reddit, TikTok (planned), Gmail, Loom | not yet connected | — | — |
| 3 | Calendar | Google Calendar (inferred from Gmail) | not yet connected | — | — |
| 4 | Communication | Discord (internal), Gmail | not yet connected | — | — |
| 5 | Project / task tracking | Coda | mcp | — | — |
| 6 | Meeting intelligence | Google Workspace | not yet connected | — | — |
| 7 | Knowledge / files | Google Workspace, Coda, GitHub (second brain) | partial — GitHub via gh cli | PAT in keyring | 2026-05-13 |
| 8 | Shared skills | Coda | not yet connected | — | — |
| 9 | Second brain / knowledge base | GitHub (`akhanaton/spyglass-wiki`) | gh cli | PAT in keyring | 2026-05-13 |

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever.
