# Connections

Registry of every system your AIOS can reach. Filled by `/onboard` from Q4-Q7 answers; expanded over time as you wire new tools. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | Dodo Payments | not yet connected | — | — |
| 2 | Customer interactions | Reddit, TikTok (planned), Gmail, Loom | not yet connected | — | — |
| 3 | Calendar | Google Calendar (inferred from Gmail) | not yet connected | — | — |
| 4 | Communication | Discord (internal), Gmail | not yet connected | — | — |
| 5 | Project / task tracking | Coda | mcp (claude.ai native) | akhanaton@gmail.com | 2026-05-13 |
| 6 | Meeting intelligence | Google Workspace | not yet connected | — | — |
| 7 | Knowledge / files | Google Workspace, Coda, GitHub (second brain) | partial — GitHub via gh cli | PAT in keyring | 2026-05-13 |
| 8 | Shared skills | Coda | mcp (claude.ai native) | akhanaton@gmail.com | 2026-05-13 |
| 9 | Second brain / knowledge base | GitHub (`akhanaton/spyglass-wiki`) | gh cli | PAT in keyring | 2026-05-13 |
| 10 | SEO analytics | Google Search Console | script (gsc_analyzer.py) | not yet connected | — |
| 11 | SEO analytics | GA4 | script (ga4_analyzer.py) | not yet connected | — |
| 12 | Keyword research | DataForSEO | script (keyword_researcher.py) | not yet connected | — |
| 13 | Email marketing | Brevo | API | not yet connected | — |
| 14 | Community monitoring | Reddit API | script (reddit_monitor.py) | not yet connected | — |
| 15 | Blog CMS | Sanity | API | not yet connected | — |
| 16 | SEO research | Ahrefs | script (ahrefs_analyzer.py) | not yet connected | — |
| 17 | GTM signals — behavioral | PostHog | mcp (claude.ai native) + script | POSTHOG_API_KEY | 2026-05-15 |
| 18 | GTM signals — community | Reddit Monitor (Syften + reddit_monitor.py) | script | REDDIT_CLIENT_ID | not yet connected |
| 19 | GTM signals — SEO | GSC + DataForSEO | script | GSC_CREDENTIALS_PATH + DATAFORSEO_LOGIN | not yet connected |
| 20 | GTM signals — output (operational) | Coda Signals table | mcp (claude.ai native) | akhanaton@gmail.com | 2026-05-15 |
| 21 | GTM signals — CRM / enrichment | Attio | API | not yet connected | — |
| 22 | GTM signals — activation | Brevo (sequences) | API | not yet connected | — |

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever.
