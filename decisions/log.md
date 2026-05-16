# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.
```

Keep it terse. Future-you will thank present-you for capturing the *why*, not just the *what*.

---

## 2026-05-13 — GitHub MCP over git submodule for second brain

**Decision:** Connect the second brain GitHub repo via GitHub MCP server, not as a git submodule inside Spyglass-OS.

**Why:** Multiple writers (other apps, repos, Enitan, Teresa) and multiple readers. A submodule makes Spyglass-OS manage sync state across machines and tools — overhead that compounds. MCP means Claude queries live content; the sync problem disappears entirely. Submodule is a viable fallback if offline access becomes a requirement.

**Alternatives considered:** Git submodule with post-merge hook; symlink to separate local clone.

**Owner:** Enitan

---

## 2026-05-13 — OS is the desk, wiki is the library

**Decision:** Clear separation between Spyglass OS and spyglass-wiki. OS owns identity, voice, connections, and local config. Wiki owns all business, product, engineering, and operational knowledge. OS reads wiki at session start via `_session_context.md`. No duplication of knowledge between the two systems. OS CLAUDE.md "Knowledge base" section replaced with a live wiki read instruction.

**Why:** Both systems had overlapping control planes — two CLAUDE.md files, two decision logs, two session context concepts. The OS's static Knowledge base paragraph was a stale snapshot of what the wiki maintains dynamically at 117+ articles.

**Alternatives considered:** Merge OS into wiki (rejected — personal identity, voice samples, and per-machine connection config don't belong in a shared knowledge base); add `.claude/context/` distillation layer inside the wiki (rejected — wiki/ is already the distillation of raw/; the OS is already the distillation layer for non-coding sessions).

**Owner:** Enitan

---

## 2026-05-13 — Skills Library / Processes split in Coda

**Decision:** Two separate Coda pages in Spyglass HQ. Skills Library = AI/automation skills only (executable by Claude). Processes = human-followed SOPs. Hard boundary: if a human follows it, it's a process; if Claude runs it, it's a skill. Never mix.

**Why:** Without a home for SOPs, the Skills Library absorbs them and becomes a junk drawer within weeks. A named boundary forces the discipline at input time, not cleanup time.

**Alternatives considered:** Single unified table with a "type" column (rejected — mixing makes filtered views unreliable and blurs the AI-executable contract); SOPs in wiki (rejected — wiki is engineering/product knowledge, not operational runbooks for the team).

**Owner:** Enitan

---

## 2026-05-13 — Spyglass OS as operating layer, not a parallel track

**Decision:** Prioritise getting Spyglass OS to "significant leverage" threshold before using it to deliver other priorities (production readiness matrix, SEO/Growth planning).

**Why:** Treating it as a force multiplier means all subsequent work benefits from it. Running it as a side project means it never reaches the leverage threshold.

**Alternatives considered:** Deliver production readiness matrix first, set up AIOS in parallel.

**Owner:** Enitan

---

## 2026-05-14 — Marketing machine integrated into Spyglass OS

**Decision:** Build the ExamPilot marketing machine as an integrated part of Spyglass OS (commands at `.claude/commands/`, agents at `.claude/agents/`, data in `marketing/`). Not a sub-OS folder, not a separate repo.

**Why:** If marketing lives outside the OS, `/audit` and `/level-up` can't see marketing capabilities, breaking the force multiplier concept. The OS philosophy is that everything flows through the operating layer. Commands at root means they activate from the project CWD. Strategy lives in the wiki; operational rules and templates live in `marketing/context/` and `marketing/templates/`.

**Alternatives considered:** (1) Sub-OS folder with its own CLAUDE.md and skills (rejected: loses skill discoverability, /audit can't see it); (2) Separate repo like seomachine (rejected: fragments the operating layer, duplicates context, requires repo switching).

**Owner:** Enitan

---

## 2026-05-14 — 18-month marketing plan: stage-based KPIs + micro-funnel architecture

**Decision:** Adopted stage-based KPI evolution (Phase 0-3) combined with leading/lagging indicators over AARRR pirate metrics or a single universal north star. Each phase has 1-2 primary KPIs that shift as the business matures. Channel-specific KPIs measured independently against each channel's funnel role. Six additional decisions documented in the plan: Edexcel deferred, no paid ads (permanent), TikTok Phase 2, location SEO Phase 2, product-led SEO Phase 2, pillar+spoke as SEO foundation.

**Why:** 2-person team at pre-revenue stage. Premature optimization (measuring CAC before there are customers) creates noise. Stage gates force discipline: you prove activation before measuring revenue, you prove organic before scaling paid. The micro-funnel (TikTok → Reddit → SEO → AI Search → Website) is the discovery architecture; the B2C macro-funnel (awareness → advocacy) is the lifecycle.

**Alternatives considered:** (1) AARRR pirate metrics from day 1 (rejected: 5+ metrics is too many for early stage, no clear priority when they conflict); (2) Single north star metric throughout (rejected: "MRR" is meaningless at Phase 0, "signups" is meaningless at Phase 3); (3) Channel-agnostic KPIs only (rejected: each channel has a different funnel job, single metric distorts resource allocation).

**Owner:** Enitan & Teresa

---

## 2026-05-15 — Marketing plan v2: operational precision upgrade

**Decision:** Updated marketing plan from v1.0 to v2.0 in place (not a separate document). Key changes: (1) UAE promoted to Tier 1, Egypt demoted to Tier 2 based on verified data and traffic analysis. (2) Monthly demand gen/acquisition pulsing tied to exam calendar replaces static 70/30 phase split. (3) Formal phase gate scoring with weighted must-pass criteria replaces checklists. (4) Leading/lagging tags on every KPI. (5) Explicit failure definitions per phase. (6) Product-led SEO "bridge content" (examiner reports, curriculum analysis) starts Phase 0-1 instead of waiting for student data. (7) Programmatic SEO noindex-until-enriched protocol. (8) TikTok campaigns detailed with weekly themes, Results Day pre-production strategy. (9) Brevo wiring specified as Phase 0 first two weeks. (10) Exam board expansion sequencing formalized (CIE 0580 before Edexcel IAL for IGCSE-to-A-Level pipeline). (11) Competitive positioning section added. (12) Existing ~8 published articles factored into Phase 0 baseline.

**Why:** V1 was strategically sound but operationally vague in places. Phase gates were checklists without decision rules. Demand gen/acquisition split was static when the exam calendar naturally creates monthly pulsation. Geography data had unverified claims (Egypt "#1 IGCSE" from 2014). KPIs lacked leading/lagging classification, making it unclear what to act on daily vs review monthly. V2 is the same strategy with sharper instrumentation.

**Alternatives considered:** (1) Write v2 as a separate document and compare (rejected: creates two competing sources of truth); (2) Selective cherry-picking from v2 research (rejected: the improvements are interconnected -- phase gates depend on KPI tags, which depend on failure definitions).

**Owner:** Enitan

---

## 2026-05-15 — MRR projections revised upward with full 9709 expansion model

**Decision:** Replaced the EUR 1,500 Phase 3 MRR target with EUR 5,000-9,000 (300-500 paying users). Added a month-by-month growth projection model (Section 5.8) that accounts for each CIE 9709 unit launch expanding the addressable keyword surface, improving trial-to-paid conversion (15% single-unit → 22% multi-unit), and reducing churn (8-10% → 5-7%). Blended MRR per user is EUR 17-19 based on tier mix weighted toward quarterly/annual in price-sensitive international markets.

**Why:** The original EUR 1,500 target implicitly assumed ~75-100 paying users (from 500 total trials at 15% conversion). It did not account for the multiplicative effect of covering five 9709 units: each unit is a new acquisition channel (new keywords, new student segments, new Reddit questions), and multi-unit coverage improves both conversion and retention. With 130-180+ indexed pages by Nov 2027, the SEO footprint is 3-4x larger than a Pure-1-only model. 500 paying users is a stretch for Nov 2027 (more likely Q1 2028) but 300-350 is realistic at the moderate scenario.

**Alternatives considered:** Keeping EUR 1,500 as a conservative floor (rejected: it's so far below what the pricing math actually produces that it would give false comfort at Phase 3 if hit but still far below potential).

**Owner:** Enitan

---

## 2026-05-15 — No paid advertising, ever

**Decision:** ExamPilot will not run paid ads of any kind across any phase. This is a permanent strategic decision, not a deferral. All acquisition is organic: SEO, Reddit, TikTok organic content, email, and direct outreach. If a growth ceiling is hit in Phase 3+, the response is product expansion (new exam boards, geographies, subjects) and deeper organic channel investment.

**Why:** Organic acquisition builds compounding assets (content, community authority, email list, brand reputation). Paid acquisition stops the moment you stop paying. For a 2-person team with limited budget and a long-horizon content strategy, organic is the only channel that scales without linear cost increases.

**Alternatives considered:** Paid ads deferred to Phase 3 conditional on organic benchmarks (rejected: a conditional deferral creates ambiguity and temptation; a clean no removes the decision from the table permanently).

**Owner:** Enitan

---

## 2026-05-15 — SEO analytics stack: DataForSEO as core programmatic layer

**Decision:** Build the SEO intelligence loop on DataForSEO API + GSC API + GA4 + PostHog, synthesized by Claude via a `/strategy-review` command. Reject SEO-Stack.io. Deprecate Ubersuggest (redundant). Keep Mangools until DataForSEO `keyword_researcher.py` module is built and validated (Phase 2). Add Ahrefs Webmaster Tools (free) immediately for site audit coverage.

**Why:** DataForSEO is pay-per-call ($12-28/mo at startup scale) and covers everything Ahrefs Lite ($129/mo) and SEMrush Pro ($140/mo) provide programmatically — rank tracking, keyword research, competitor SERP data, backlink data, on-page NLP analysis. The AI querying layer SEO-Stack sells is what Claude in the OS already does, with full business context. The virtuous loop (DataForSEO → GSC → GA4 → PostHog → Claude → action) closes the feedback chain from keyword opportunity through to trial conversion and retention by source. Each layer answers a different question; together they surface decisions, not just reports.

**Alternatives considered:** SEO-Stack.io (rejected: first-party data only, redundant with DataForSEO, founder listing business for sale — continuity risk, MCP server unconfirmed); Ahrefs Lite (rejected: 4x cost, no features needed until Phase 3); SEMrush Pro (rejected: same cost issue, stronger on PPC which is not a Phase 0-2 priority); Mangools kept short-term as the human-facing keyword research UI until programmatic layer is validated.

**Owner:** Enitan

---

## 2026-05-15 — GTM Engineering signal architecture adopted

**Decision:** Added GTM Engineering as Enitan's formal function within Spyglass OS. Built a B2C-adapted signal architecture covering first-party (PostHog behavioral), second-party (Reddit community), and third-party (GSC/DataForSEO SEO + exam calendar) signals. Activation chain: PostHog → scored signal → Coda Signals table (operational) + Attio CRM (contact enrichment) → Brevo sequences. Phase 0 is command-driven (`/signal-review`); Phase 1 automates Attio enrichment and Brevo sequence triggers once those APIs are connected.

**Why:** The Marketing Machine (content, community execution) generates demand but has no intelligence layer to track who is paying attention, how engaged they are, or when they're ready to convert. A signal architecture closes the loop: every piece of content we produce, every Reddit post we answer, every blog article we publish — the behavioral response feeds back into a score that routes the right action to the right person at the right time. Adapted from B2B intent-signal architecture (workflows.io) for a B2C edtech context — no CRM deals, no SDR sequences, student behavioral signals instead of firmographic data.

**Alternatives considered:** (1) Integrate signals into the Marketing Machine only (rejected: Marketing Machine is Teresa's content/community domain; signal scoring and CRM enrichment are engineering concerns — clean separation avoids coordination friction); (2) Start fully automated from day 1 (rejected: no conversion data yet to validate scoring weights; premature automation fires wrong triggers automatically — worse than manual).

**Owner:** Enitan

---

## 2026-05-15 — Reddit tool stack: Syften + RedShip

**Decision:** Adopt Syften (€40/mo Standard) for brand/competitor monitoring and RedShip ($19/mo Starter) for Google-ranking thread discovery and reply drafting. Combined ~EUR 57/month. Activate F5bot (free) in Phase 0 to validate subreddit volume before spending. Add RedShip in Phase 1 ahead of Results Day.

**Why:** No single tool covers all requirements (subreddit monitoring + Google-rank detection + brand monitoring + reply drafting + manual-post-only workflow) at under EUR 80/mo. Syften is the strongest standalone monitoring tool with confirmed Reddit API compliance. RedShip is the only tool in this price range with an explicit weekly Google-ranking scan — finding threads that already rank on page 1 and staying in them compounds far longer than chasing new viral posts.

**Alternatives considered:** ReplyAgent (rejected: proxy accounts, incompatible with karma-building strategy); Redreach (rejected: DM automation creates ban risk, pricing opaque); ReplyDaddy (close but BYOK API costs push effective price to $69-99/mo, early-stage longevity risk); Brand24 (overkill, worse Reddit granularity at higher cost); SubHunt (watch list — similar Google-rank feature to RedShip at $12/mo but insufficient third-party validation). GummySearch is dead (shut down Nov 2025).

**Owner:** Enitan

---

## 2026-05-15 — /capture skill: OS↔wiki ingest pipeline automation

**Decision:** Built `/capture` as an AI-assisted skill (L2 autonomy, Bike Method Phase 1) that collapses the 4-step OS↔wiki capture pipeline — classify destination, draft in correct template, commit via gh api, lint + surface issues — into one command with a human review gate before every commit.

**Scoped via 3Ms Method interview:**
- Trigger: Enitan runs `/capture` with content (paste, file path, URL, or description)
- Data sources: input content + AGENTS.md (wiki conventions) + wiki templates
- Transformations: content → classified destination → drafted article → committed file → lint report
- Decision points: OS vs wiki? / which template? / lint issues auto-fixable or needs human?
- Destination: wiki article or OS file + optional `decisions/log.md` entry + `_session_context.md` update prompt
- Autonomy: L2 — AI drafts, human reviews and approves before any commit
- KPI: Time from "I want to capture this" to "lint-clean and committed" — target under 5 min (from ~15-30 min)

**Why:** The capture pipeline was a repeating attention tax on every useful piece of information encountered. At 3+ occurrences per week, the friction was real enough to cause skipped captures. The wiki cannot grow as a living knowledge system if ingestion is expensive.

**Alternatives considered:** Sub-agent for full pipeline (rejected: L4 too high for first build, no validation baseline yet); prompt template only (rejected: doesn't solve CWD-switching friction or lint parsing); local wiki clone for lint (rejected: machine-specific path, breaks for Teresa). All operations run via `gh api` — no local clone dependency. Phase 2 (auto-commit high-confidence types) available as an explicit edit to `bike-method-phase` once Phase 1 is validated.

**Owner:** Enitan

---

## 2026-05-16 — SEO write pipeline ported from seomachine into Spyglass OS

**Decision:** Ported the full blog article write pipeline from the seomachine repo into Spyglass OS, replacing the stub `/write-article` command with a proper skill and 4 sub-agents. Updated `references/voice-house.md` from a placeholder to the full ExamPilot brand voice guide.

**What was built:**
- `.claude/skills/write-article/SKILL.md` — 6-step write skill: pre-write confirmation, full article structure (GEO-first, APP formula, Key Takeaways, mini-stories, contextual CTAs, FAQ, conclusion), guardrails scrub pass, 4 post-write agents, quality gate, save + report
- `agents/seo-optimizer.md` — keyword density, heading structure, GEO compliance audit
- `agents/meta-creator.md` — 3 meta title + 3 meta description options with scoring patterns
- `agents/internal-linker.md` — passage-level link insertion with anchor text rules
- `agents/content-quality.md` — 5-dimension inline scorer (Voice 30%, Specificity 25%, Structure 20%, SEO 15%, GEO 10%), threshold routing
- `references/voice-house.md` — full ExamPilot brand voice: 5 pillars, tone by content type, messaging framework, terminology table, formatting standards, CTAs, what we never do

**Why:** The seomachine repo had the full execution layer; Spyglass OS had context files but no runnable write pipeline. Porting gives the OS the ability to go from research brief to reviewed draft in one command, with quality scoring built in.

**Alternatives considered:** Keep write pipeline in seomachine and call cross-repo (rejected: CWD friction, breaks Teresa's access); rebuild from scratch (rejected: seomachine's agent architecture was already validated).

**Owner:** Enitan

---

## 2026-05-16 — Python quality scorer and /pre-write skill added

**Decision:** Ported the 3-module Python quality scorer from seomachine and created a new `/pre-write` skill for Sanity CMS content scaffolding.

**Python scorer (`marketing/data_sources/modules/`):**
- `readability_scorer.py` — Flesch/Kincaid + structure analysis; targets Grade 8-10 / Flesch 60-70; graceful fallback if `textstat` not installed
- `seo_quality_rater.py` — 6-dimension SEO rating with ExamPilot defaults (1800-word min, 20-word sentence target, Cambridge/Pearson authority links)
- `content_scorer.py` — 5-dimension composite scorer; ExamPilot additions: banned brand phrases in Humanity scoring; exam codes (9709/12, WMA11, syllabus topic numbers) boosting Specificity; YAML frontmatter parsing in `main()`
- `requirements.txt` updated: added `textstat>=0.7.3`
- `write-article/SKILL.md` Step 5 updated: Python scorer is now primary; inline content-quality agent is fallback

**`/pre-write` skill (`.claude/skills/pre-write/SKILL.md`):**
- 5-step flow: classify content type → plan structure → build Sanity JSON scaffold → anti-regression checklist → save to product repo
- Reads `integration.json` as gold standard before every scaffold
- 10-type content taxonomy with folder mappings; full Sanity block type reference
- Writes to `/Users/enitan/Documents/Projects/spyglass/scripts/content/[folder]/[slug].json`

**Why:** The inline content-quality agent can't do Flesch scoring. The Python scorer gives real readability data. The /pre-write skill fills the gap for product content (topic pages, hub pages, feature pages) which previously required manual JSON construction.

**Alternatives considered:** Keep only inline scoring (rejected: loses Flesch accuracy, rhythm analysis); build Python scorer as external CI step only (rejected: more valuable in-session where Claude can act on results immediately).

**Owner:** Enitan

---

---

## 2026-05-16 — Full seomachine feature set ported into Spyglass OS

**Decision:** Ported every applicable feature from `akhanaton/seomachine` into Spyglass OS across three commits (`7e0af12`, `b50e66e`, `d61fadb`). 63 new files, ~15,500 lines. seomachine is now superseded by Spyglass OS for all ExamPilot marketing work.

**What was ported (summary):**

*Commands (14 new → 24 total):* /article, /rewrite, /optimize, /analyze-existing, /scrub, /research-serp, /research-gaps, /research-trending, /research-topics, /research-ai-citations, /priorities, /repurpose, /content-calendar, /cluster, /landing-research, /landing-write, /landing-audit, /landing-competitor

*Post-write agents (9 new → 12 total):* content-analyzer, editor, headline-generator, keyword-mapper, performance, cluster-strategist, cro-analyst, landing-page-optimizer

*Python modules (15 new → 21 total):* content_scrubber, keyword_analyzer, search_intent_analyzer, content_length_comparator, opportunity_scorer, competitor_gap_analyzer, diagram_generator, google_analytics, data_aggregator, article_planner, landing_page_scorer, above_fold_analyzer, cta_analyzer, trust_signal_analyzer, cro_checker

*Skills (17 new → 25 total):* seo-audit, copywriting, email-sequence, schema-markup, marketing-psychology, analytics-tracking, copy-editing, ab-test-setup, signup-flow-cro, onboarding-cro, paywall-upgrade-cro, free-tool-strategy, page-cro, form-cro, popup-cro, launch-strategy

*Context files (4 new):* target-keywords.md, internal-links-map.md, competitor-analysis.md, ai-citation-targets.md

**What was deliberately excluded:**
- `wordpress_publisher.py` + /publish-draft + /landing-publish — ExamPilot uses Sanity CMS, not WordPress
- `engagement_analyzer.py` — requires GA4 custom events; ExamPilot's GA4 is pageview-only
- `landing_performance.py` — requires conversion tracking not yet implemented
- `/paid-ads` skill — permanent no-paid-ads decision (logged 2026-05-15)
- Podcast-specific content (Castos references) — not applicable

**Why:** seomachine was built for ExamPilot but maintained as a separate repo, creating a split-brain problem — Teresa couldn't access it, commands were CWD-dependent, and the AIOS had no awareness of the full capability set. Consolidating into Spyglass OS gives both users access to the full marketing machine under one roof.

**Owner:** Enitan
