# Connections

Registry of every system your AIOS can reach. Filled by `/onboard` from Q4-Q7 answers; expanded over time as you wire new tools. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | Dodo Payments | not yet connected | — | — |
| 2 | Customer interactions | Reddit, TikTok (planned), Gmail, Loom | Gmail via gws cli | enitan@exampilot.io (OS keyring) | 2026-06-13 |
| 3 | Calendar | Google Calendar | gws cli | enitan@exampilot.io (OS keyring) | 2026-06-13 |
| 4 | Communication | Discord (internal), Gmail, WhatsApp | Gmail via gws cli | enitan@exampilot.io (OS keyring) | 2026-06-13 |
| 5 | Project / task tracking | Coda | mcp (claude.ai native) | akhanaton@gmail.com | 2026-05-13 |
| 6 | Meeting intelligence | Google Workspace (Docs, Drive, Sheets, Calendar) | gws cli | enitan@exampilot.io (OS keyring) | 2026-06-13 |
| 7 | Knowledge / files | Google Drive, Docs, Sheets, Coda, GitHub (second brain) | Drive/Docs/Sheets via gws cli; GitHub via gh cli | enitan@exampilot.io + PAT in keyring | 2026-06-13 |
| 8 | Shared skills | GitHub (`akhanaton/spyglass-os`) | git clone / gh cli | PAT in keyring | 2026-05-16 |
| 9 | Second brain / knowledge base | GitHub (`akhanaton/spyglass-wiki`) | gh cli | PAT in keyring | 2026-05-13 |
| 10 | SEO analytics | Google Search Console | script (gsc_analyzer.py) | OAuth (enitan@exampilot.io, token at ~/.config/gws/gsc_token.json) | 2026-06-13 |
| 11 | SEO analytics | GA4 | script (ga4_analyzer.py) | not yet connected | — |
| 12 | Keyword research | DataForSEO | script (keyword_volume.py, competitor_gap_analyzer.py, content_length_comparator.py, data_aggregator.py) | DATAFORSEO_LOGIN + DATAFORSEO_PASSWORD in marketing/data_sources/.env (apps@exampilot.io) | 2026-06-13 |
| 13 | Email marketing | Brevo | API | not yet connected | — |
| 14 | Community monitoring | Reddit API | script (reddit_monitor.py) | not yet connected | — |
| 15 | Blog CMS | Sanity | API | not yet connected | — |
| 16 | SEO research | Ahrefs | script (ahrefs_analyzer.py) | not yet connected | — |
| 17 | GTM signals — behavioral | PostHog | mcp (claude.ai native) + script | POSTHOG_API_KEY | 2026-05-15 |
| 18 | GTM signals — community | Reddit Monitor (Syften + reddit_monitor.py) | script | REDDIT_CLIENT_ID | not yet connected |
| 19 | GTM signals — SEO | GSC + DataForSEO | script | GSC: OAuth live; DataForSEO: .env live (apps@exampilot.io) | 2026-06-13 |
| 20 | GTM signals — output (operational) | Coda Signals table | mcp (claude.ai native) | akhanaton@gmail.com | 2026-05-15 |
| 21 | GTM signals — CRM / enrichment | Attio | API | not yet connected | — |
| 22 | GTM signals — activation | Brevo (sequences) | API | not yet connected | — |
| 23 | Social scheduling | Postiz (Standard plan) | API + dashboard | not yet connected | — |
| 24 | Community — WhatsApp | WhatsApp Business App (free P0-P1) → Wati P1+ | manual (P0), API (P1+) | not yet connected | — |
| 25 | Community — Facebook Groups | Facebook Groups (manual + Coda tracking) | manual | not yet connected | — |
| 26 | Build-in-public — LinkedIn | LinkedIn (Teresa personal account — content warm-up + teacher/parent outreach) | Postiz (scheduling) + manual (posting) | not yet connected | — |

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever.
