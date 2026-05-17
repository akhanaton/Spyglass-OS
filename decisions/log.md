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

---

## 2026-05-16 — Continuous improvement adopted as core OS principle

**Decision:** Adopted continuous improvement as a core operating principle of Spyglass OS. Every repeatable function follows a three-step loop: Capture (inputs + outcomes), Review (at defined cadence), Adjust (change parameters, log with data). Created `references/continuous-improvement.md` (philosophy reference) and `/tune` skill (monthly review ritual). Added to CLAUDE.md as a foundational section alongside the 3Ms framework. All initial parameters across the OS are now explicitly labeled as estimates subject to data-backed adjustment. Linear: EP-51.

**Why:** The GTM Engineering signal architecture already embeds this pattern (weights are "initial estimates, adjust after 8-12 weeks"). Extending it to every OS function -- content, SEO, support, product, X -- creates a system that gets measurably better each month. Without this, parameter settings fossilize and drift from reality. With it, each monthly `/tune` cycle narrows the gap between what we assume and what the data shows.

**Alternatives considered:** Ad hoc improvements as needed (rejected: leads to inconsistent attention, some functions improve while others stagnate); quarterly reviews only (rejected: too slow for early-stage where conditions change weekly); automated parameter adjustment (rejected: premature, Phase 1 is human-approved adjustments only).

**Owner:** Enitan

---

## 2026-05-16 — Build-in-public on X integrated into Spyglass OS

**Decision:** Added X (Twitter) build-in-public as a new channel in Spyglass OS. Created `/write-x` skill (pulls from decisions log, Linear, PostHog, git, or freeform input), strategy reference, two templates (x-post, x-thread), and updated 7 existing files (channel playbooks, audience segments, funnel strategy, repurposing playbook, `/repurpose` command, `/weekly-pulse` command, connections.md). Postiz Standard ($29/mo, already planned for TikTok) handles scheduling. Incremental cost: $0. Enitan starts posting; Teresa joins when `voice-teresa.md` is populated with real writing samples. Full strategy in `references/x-build-in-public-strategy.md`. Linear: EP-50.

**Why:** Build-in-public on X serves a different audience (founders, indie hackers, edtech builders) than the student micro-funnel. It builds founder credibility, creates a launch-day amplification audience, and opens doors to advisors and partnerships. Research shows: 15-25% conversion from engaged X followers at SaaS launch, 6-month timeline to build launch-ready audience. Starting now (6 months before Phase 1 soft launch) is correctly timed. X is a parallel credibility channel, not a replacement for any student-facing channel.

**Alternatives considered:** Brand account only (rejected: personal accounts get 5-10x more engagement); delay until Phase 2 with TikTok (rejected: 6-month audience-building lead time means starting now is optimal); full automation pipeline (rejected: Phase 0 is manual copy-paste to Postiz, automation comes after n8n is wired in EP-49).

**Owner:** Enitan (infrastructure + posting), Teresa (posting, after voice file populated)

---

## 2026-05-16 — Spyglass OS full coverage assessment: gaps identified and prioritised

**Decision:** Completed a research-backed audit of Spyglass OS coverage across all functions. Two critical gaps identified that must be fixed before the first paid user: (1) involuntary churn is undocumented in wiring — ChurnWard ($29/mo, Dodo Payments integration confirmed) to be added; (2) no production observability — Sentry Team ($26/mo) to be added. Three strategic additions with outsized returns: WhatsApp via AiSensy for Tier 1 markets (UAE 85.8% penetration, India 500M+ users), student outcome data collection (the product moat — must collect from the first exam cohort), and n8n for event-driven activation chain (trial → Attio → Brevo → Discord). Full assessment in `references/os-coverage-assessment.md`. Linear: EP-49.

**Why:** Marketing machine is strong. Revenue operations and production observability have no wiring. Student outcome data is the single most defensible competitive advantage and has a one-year collection window tied to the exam calendar — missing the first cohort means waiting 12 months. WhatsApp is not optional for Pakistan/UAE/India markets; it is the primary communication channel in those geographies.

**Alternatives considered:** Add more marketing tooling (rejected: already deep coverage); full help desk / NPS infrastructure (rejected: overkill at 100 users, confirmed by external benchmarks); Zapier over n8n (rejected: per-operation pricing compounds at scale, n8n is flat).

**Owner:** Enitan

---

## 2026-05-16 — Product owner OS layer: thin infrastructure, not a marketing-scale build

**Decision:** Build a minimal product owner layer in Spyglass OS — ~15% the size of the marketing infrastructure. Two Tier 1 items now (Linear MCP wiring + `/backlog-review` command; PostHog extended to `/product-pulse`). Four Tier 2 items at Phase 1 (`templates/prd.md`, `/spec` command, `/product-review` ritual, Coda Product Board view). Nothing in Tier 3 until 200+ users. Full assessment in `references/product-owner-strategy.md`. Linear: EP-47.

**Why:** Marketing runs continuously and in parallel — deep infrastructure pays. Product decisions at pre-launch are serial, low-frequency, and owned by one person. The risk isn't missing tooling; it's not having a fast path from signal → decision → shipped. Over-engineering creates overhead with no ROI until paying users generate real feedback.

**Alternatives considered:** Full product OS parity with marketing machine (rejected: wrong stage, wrong cadence, wrong size team); no product infrastructure at all (rejected: Linear is invisible to the OS today — that gap has a real cost).

**Owner:** Enitan

---

## 2026-05-16 — Customer support: thin insight-capture layer, not a support operation

**Decision:** Build a purposeful-but-thin customer support layer: Discord added to `connections.md`, `templates/support/` folder (6 templates), Coda support log table, and a `/feedback-digest` command. Phase 1 adds PostHog in-app feedback surveys and Attio wiring. No help desk, no NPS, no FAQ, no ticketing system. Full assessment in `references/customer-support-strategy.md`. Linear: EP-48.

**Why:** At alpha (100 students), support volume will be 3–8 contacts/week. The risk isn't operational overwhelm — it's losing the insight from early conversations. Framing support as user research determines the right infrastructure: optimise for insight capture, not ticket resolution. The `/feedback-digest` command is the lever — it turns every support touchpoint into a product intelligence input.

**Alternatives considered:** Help desk tooling (Intercom/Zendesk — rejected: overkill until 500+ users with volume exceeding what two people can handle conversationally); NPS surveys (rejected: meaningless at alpha, no reliable baseline); FAQ pre-built (rejected: let the Coda log tell you what to write, don't guess).

**Owner:** Teresa (operations), Enitan (tooling)

---

## 2026-05-16 — OS structural audit: skills promoted to canonical layer, duplicates resolved

**Decision:** Ran a full coherence audit of Spyglass OS after the seomachine port. Four issues identified and fixed in commit `f6ab25c`:

1. **Skills are now the canonical execution layer.** 7 commands that existed only in `.claude/commands/` (scrub, content-calendar, research-topics, research-gaps, research-keywords, research-serp, landing-competitor) were promoted to proper `.claude/skills/{name}/SKILL.md` files with bike-method-phase frontmatter and 3Ms attribution. The `write-article` command was deleted — the skill was already a strict superset (adds APP formula, Python scorer, editor agent). 16 commands remain, all genuinely command-only with no skill twin.

2. **3 agents relocated.** `content-analyzer`, `cro-analyst`, and `landing-page-optimizer` were incorrectly nested under `.claude/skills/write-article/agents/` during the seomachine port. All three run after `/landing-write`, not `/write-article`. Moved to `.claude/agents/` (top-level).

3. **Hardcoded machine path fixed.** `/pre-write` skill hardcoded `/Users/enitan/Documents/Projects/spyglass/scripts/content/` in 4 places, breaking Teresa's access entirely. Replaced with `$SPYGLASS_PRODUCT_REPO` env var with a setup block at the top of the skill.

4. **connections.md row 8 corrected.** Entry said "Shared skills | Coda | mcp" — skills never moved to Coda. Updated to reflect reality: shared via `akhanaton/spyglass-os` GitHub repo via git clone / gh cli.

**Why:** The seomachine port added 63 files in 3 commits without a structural review pass. The command/skill duplication created maintenance drift risk (update the skill, command stays stale) and ambiguity about which implementation runs. Skills are the right canonical layer: they have discoverability metadata, phase tracking, and work regardless of CWD — the exact properties that make them shareable with Teresa.

**Alternatives considered:** Commands as canonical, delete duplicate skills (rejected: commands are the seomachine pattern we moved away from; loses bike-method-phase metadata and trigger-word discoverability); split commands/skills by role — commands for operational pipelines, skills for advisory (rejected: introduces new abstraction the OS doesn't support, most capabilities are operational anyway).

**Owner:** Enitan

---

## 2026-05-16 — Premium positioning validated: market large enough, pricing confirmed, channel gaps identified

**Decision:** Confirmed ExamPilot's premium positioning (single EUR price, no regional adjustment, targeting the segment that can afford it in every market). The addressable market is verified as large enough. Marketing channel mix has identified gaps that need addressing in a future session.

**Key findings:**
- TAM: 250,000-350,000 CIE + Edexcel IAL maths students/year (EUR36M-50M at annual pricing)
- ~95% of CIE students globally attend private/international schools — CIE IS the premium segment
- EUR29/month = 0.5-17% of annual school fees across all target markets; equivalent to 1-2 hours of tutoring
- Dodo Payments confirms support for all target markets (Nigeria, Pakistan, UAE, Malaysia, Singapore, etc.)
- No regional pricing adjustment needed — even Pakistan/Nigeria's top private school families can afford it

**Channel misalignments identified (modifications pending):**
1. Reddit should be repositioned as SEO/AI citation engine (not direct acquisition for premium international segment)
2. No parent-facing acquisition path exists (parent is the economic buyer in most target markets)
3. No school/teacher partnership model (one school = 50-200 students)
4. Discord should be deprioritized in favour of WhatsApp Communities (dominant in South Asia, Middle East, West Africa)
5. TikTok needs region-specific content (not UK-focused) — verified as THE platform for 16-18s in all target markets
6. Dual voice strategy needed (student-facing casual + parent-facing trust-building)
7. Postiz covers TikTok/X but NOT WhatsApp/Facebook Groups — WhatsApp Business App (free) covers Phase 0; Wati (~$30/month) for Phase 1

**What was NOT decided:** How and when to modify the marketing plan. Research saved to wiki (`wiki/marketing/target-market-analysis.md`) for future implementation session.

**Why:** Needed to verify the strategic assumption that a premium-only position wouldn't limit growth. Data confirms the market is large enough. The finding that CIE ≈ private school globally means we are not excluding anyone by pricing — we're just naming our natural audience.

**Alternatives considered:** Regional pricing (rejected by strategic preference — complexity, brand dilution, and the target segment can afford it); broader subject coverage to increase TAM (not rejected, but sequenced after 9709 is proven); lower price to capture expanding middle-class CIE segment in Pakistan/Nigeria (rejected — focus on who can afford it now, revisit only if premium segment proves insufficient).

**Owner:** Enitan

---

## 2026-05-16 — Build-in-public extracted to dedicated sub-OS

**Decision:** Extracted the build-in-public on X workstream from `marketing/` into a new top-level sub-OS `build-in-public/`. Previously, X infrastructure was spread across `references/x-build-in-public-strategy.md`, `marketing/templates/x-post.md`, `marketing/templates/x-thread.md`, and X sections inside three `marketing/context/` files (`channel-playbooks.md`, `audience-segments.md`, `funnel-strategy.md`).

New structure:
- `build-in-public/references/x-strategy.md` (moved from `references/x-build-in-public-strategy.md`)
- `build-in-public/templates/x-post.md`, `x-thread.md` (moved from `marketing/templates/`, save paths updated)
- `build-in-public/context/channel-rules.md`, `audience.md`, `funnel.md`, `repurposing-rules.md` (extracted from `marketing/context/` files, which now have one-line pointer stubs)
- `build-in-public/pipelines/outreach/` (new output folder — X drafts no longer go to `marketing/pipelines/outreach/`)

Skills/commands updated: `write-x/SKILL.md` (8 path edits), `repurpose.md` (3 edits), `tune/SKILL.md` (2 edits), `weekly-pulse.md` (pipeline scan fix), `CLAUDE.md` (`build-in-public/` added to "Where things live"). `marketing/` is now purely ExamPilot student-facing.

**Why:** Build-in-public on X was placed inside `marketing/` by path-of-least-resistance when the feature was first built. But by a 5-criteria workstream test (different goal, different audience, different KPIs, different voice, different cadence) it qualifies as a second workstream. The X strategy doc itself states: "It does NOT directly convert students." Keeping it in `marketing/` causes: `/weekly-pulse` conflating student funnel and builder metrics; `channel-playbooks.md` mixing incompatible audiences; future `/tune` parameter drift between workstreams. The workstream test that identified this is now documented in `EXPANSIONS.md`.

**Alternatives considered:** Leave in `marketing/`, add a comment (rejected: cost compounds as X content grows; a half-committed structure is worse than a clean one); partial extract — move only leaf files, leave context sections in `marketing/context/` (rejected: still requires reading two locations to understand the X channel, defeating the purpose).

**Owner:** Enitan

---

## 2026-05-17 — Marketing plan v3.0: channel realignment from target market analysis

**Decision:** Updated marketing plan from v2.0 to v3.0 based on target market analysis (`wiki/marketing/target-market-analysis.md`). The analysis validated premium positioning (CIE = 95%+ private school overlap, EUR29/month = 0.5-7% of school fees) but identified 7 channel misalignments. Six sub-decisions documented below.

**Sub-decisions:**

1. **Reddit repositioned from direct acquisition to SEO/AI citation seeding engine.** P0-P1 direct acquisition target reduced from 15-25 to 5-10 students. Primary role is now indexable content that ranks on Google and gets cited by AI tools. Subreddit priority reordered: r/CambridgeInternational (primary), r/alevel (secondary), r/6thForm (tertiary).

2. **Parent acquisition added as primary channel.** Facebook Groups (COALI 100K+ members, CIE parent communities), parent WhatsApp groups, "For Parents" landing page, parent email sequence in Brevo. Parent is the economic buyer in Tier 1 markets (Pakistan, UAE, Nigeria, Malaysia). New voice guide: `references/voice-parent.md`.

3. **School/teacher B2C2B partnership model added.** Teachers get free access and progress dashboard. They recommend to students/parents. Students purchase individually at consumer price. Not B2B -- no school licensing or institution pricing. New voice guide: `references/voice-teacher.md`. B2B prohibition in voice-house.md amended to: "No B2B school licensing or institution pricing. Consumer-only purchase model. School/teacher content uses referral-partner framing (B2C2B)."

4. **Discord demoted to secondary; WhatsApp Communities promoted.** CIE students in South Asia, Middle East, and West Africa are on WhatsApp, not Discord. WhatsApp has 100+ active student study groups in Pakistan alone. WhatsApp Business App (free) at Phase 0, Wati (~EUR30/month) evaluated at Phase 1.

5. **TikTok updated for region-specific content.** GST-optimized posting times (4pm-9pm GST for Pakistan/UAE after school). No UK slang. Universal exam identifiers (paper codes, topic names). Urdu subtitle consideration for Pakistan content (P2). Regional hashtags added.

6. **Growth projections not revised upward.** School partnerships are not modeled in projections until Phase 2 review when real conversion data exists. Follows OS principle that initial parameters are estimates requiring data-backed adjustment.

**Structural decisions:**

- Parent acquisition and school partnerships stay inside `marketing/` as channels, not sub-OSes. Both fail the EXPANSIONS.md workstream test (1/5 criteria -- only "different voice"). Creating sub-OSes for channels that share the same goal, KPIs, and cadence adds overhead without benefit for a 2-person team.
- Three new voice guides: voice-parent.md (parent-facing), voice-teacher.md (teacher/school-facing), voice-house.md amended for multi-audience awareness.
- P0-P1 student acquisition target increased from 40-70 to 50-95 through new channels.
- Five new GTM signals added: WhatsApp community join, WhatsApp broadcast click, Facebook Group mention, teacher referral click, school cohort signup.

**Why:** The marketing plan v2.0 was built before the target market analysis confirmed that CIE is essentially a private/international school product. Channel mix was optimized for UK domestic students (Reddit, Discord) rather than international private school students and their parents (WhatsApp, Facebook Groups, school partnerships). The micro-funnel architecture (TikTok -> Reddit -> SEO -> AI Search -> Website) remains correct for students; a parallel parent funnel is added alongside it.

**Alternatives considered:** (1) Create sub-OSes for parent acquisition and school partnerships (rejected: fails workstream test, adds management overhead); (2) Revise growth projections upward immediately (rejected: no conversion data for new channels yet); (3) Remove Reddit entirely from P0-P1 targets (rejected: overcorrection, Reddit still generates some organic direct interest); (4) Remove B2B prohibition entirely (rejected: B2C2B is not B2B, the prohibition protects against scope creep into enterprise sales).

**Execution completed:** All 6 waves implemented across 2 sessions. 19 OS files updated/created, 10 wiki articles updated, targeted lint PASS (4 minor issues fixed). Stale reference sweep confirmed zero remaining old targets, old B2B language, or Discord-as-primary references.

**Files touched (OS):** decisions/log.md, references/voice-parent.md (new), references/voice-teacher.md (new), references/voice-house.md, marketing/strategy/marketing-plan-2026-2027.md, marketing/context/audience-segments.md, marketing/context/content-standards.md, marketing/context/channel-playbooks.md, marketing/context/funnel-strategy.md, marketing/gtm-engineering/signal-registry.md, marketing/gtm-engineering/scoring-model.md, marketing/gtm-engineering/trigger-playbook.md, connections.md, CLAUDE.md, references/continuous-improvement.md, .claude/skills/launch-strategy/SKILL.md, .claude/agents/outreach-crafter.md, .claude/commands/landing-write.md, .claude/skills/free-tool-strategy/SKILL.md, .claude/skills/write-article/SKILL.md, marketing/templates/blog-article.md, marketing/references/launch-playbook.md, references/os-coverage-assessment.md.

**Wiki articles touched:** marketing/growth/marketing-plan.md, marketing/growth/gtm-engineering.md, marketing/growth/marketing-machine.md, marketing/INDEX.md, business/competitive/go-to-market.md, business/INDEX.md, product/strategy/beta-acquisition.md, product/INDEX.md, ai-automation-os/marketing-os/marketing-os-overview.md, _session_context.md.

**Skills identified (spec only, build via `/level-up`):** /write-whatsapp, /write-parent, /school-outreach.

---

## 2026-05-17 — LinkedIn added to build-in-public sub-OS, Teresa as primary voice

**Decision:** Added LinkedIn as a second channel inside `build-in-public/`, with Teresa as the primary (and currently only) author. LinkedIn is not a mirror of X — it is the same source material with a different frame: X = founder confession (peer-to-peer), LinkedIn = educator insight (professional authority). Incremental cost: $0 (Postiz Standard already covers LinkedIn).

**Why:** LinkedIn serves the B2C2B acquisition model directly. The teacher outreach already planned (channel-playbooks.md) is cold without a content warm-up layer. A teacher who has read 10 of Teresa's posts on CIE exam prep before receiving a DM is already half-sold. Teresa's educational background gives her natural authority with the teacher/parent audience on LinkedIn — the same authority that Enitan has with the indie hacker audience on X.

**Structural rationale:** LinkedIn sits inside `build-in-public/` (not `marketing/`) because the content source is the same as X — decisions log, milestones, product progress — just reframed. The student-facing content in `marketing/` is structurally incompatible. LinkedIn fails the sub-OS workstream test (only 2/5 criteria: different audience, different voice) so it stays as a second channel within the existing sub-OS.

**What was built:**
- `build-in-public/references/linkedin-strategy.md` — Full strategy: WHY, audience profiles, content pillars, angle adaptation rule, outreach integration, format guide, algorithm rules, anti-AI rules, timeline
- `build-in-public/templates/linkedin-post.md` — Post template with 5 post types, format rules, hook patterns
- `build-in-public/templates/linkedin-article.md` — Native article template for quarterly thought leadership
- `.claude/skills/write-linkedin/SKILL.md` — 7-step skill: source extraction, angle adaptation, format generation (post/article/carousel-outline), LinkedIn-specific scrub pass, human review gate, save
- `build-in-public/context/audience.md` — LinkedIn audience profile added (professional educator/parent)
- `build-in-public/context/channel-rules.md` — LinkedIn channel rules section added
- `build-in-public/context/funnel.md` — LinkedIn funnel added (content warm-up → outreach → B2C2B referral)
- `build-in-public/context/repurposing-rules.md` — LinkedIn repurposing rules and [LINKEDIN CANDIDATE] flag added
- `marketing/context/channel-playbooks.md` — LinkedIn outreach entry updated to reference build-in-public strategy

**Alternatives considered:** (1) LinkedIn as pure outreach channel only, no content (rejected: cold outreach without content warm-up is visibly cold — teacher clicks profile and sees nothing); (2) LinkedIn as a separate sub-OS (rejected: fails workstream test at 2/5 criteria — shares source material and cadence with X); (3) Enitan as primary LinkedIn voice (rejected: his authority with teachers/parents is lower than Teresa's; engineering frame is wrong for the professional educator audience).

**Owner:** Teresa (content + posting), Enitan (infrastructure).

---

## 2026-05-17 — OS execution model: Linear for tasks, OS for execution, wiki for knowledge

**Decision:** Established a three-tool execution model for operationalizing strategic plans in Spyglass OS. Linear handles one-time tasks with owners and deadlines. OS skills and rituals handle recurring execution and cadence-driven review. Wiki holds durable knowledge. No work should live in more than one place. Decision framework codified in `references/execution-model.md`.

**Why:** The marketing plan needed to be turned from a strategic document into actionable items. The initial instinct was to wire everything through OS rituals (`/weekly-pulse` phase gate scoring, `/tune` phase tracking). But Phase 0 is primarily one-time setup work — setup tasks don't fit rituals, which are designed for steady-state recurring execution. Forcing setup tasks into rituals means they either disappear between sessions or generate noise in the weekly review. Linear already exists, is MCP-connected, is used by Enitan for product (EP-XX issues), and Teresa can see it without running the OS. The right tool for the job.

**The framework:**
- One-time task, specific owner, deadline, dependencies → Linear
- Recurring execution, cadence-driven, data-triggered → OS skill or ritual
- Durable knowledge, reasoning, reference material → wiki
- Phase transitions → `decisions/log.md` via `/phase-gate` skill (to build)

**What would change this:** If Linear stops being used consistently by both founders, the task tracking layer collapses and everything migrates back to ritual-driven. The model only works if Linear is maintained.

**Alternatives considered:** (1) Ritual-only approach — all phase execution wired through `/weekly-pulse` and `/tune` (rejected: rituals are designed for steady-state recurring execution, not one-time project setup; forcing gate criteria into a weekly review creates noise and loses tasks between sessions); (2) Wiki-based tracker — a `phase-0-tracker.md` wiki article updated manually (rejected: wikis go stale fast, no owner accountability, no dependency tracking); (3) New OS infrastructure — a `/task` command or Coda task table (rejected: Linear already exists and is MCP-connected — adding new infrastructure for the same job is the wrong move).

**Owner:** Enitan

---

## 2026-05-17 — Phase 0 Foundation: Linear milestone + 24 issues + /weekly-pulse gate scoring

**Decision:** Operationalised the marketing plan Phase 0 by creating a Linear milestone ("Phase 0 — Foundation", target July 31 2026) with 24 issues (EP-52 to EP-75) and updating `/weekly-pulse` Step 7 to score the Phase 0 gate every Friday.

**What was built:**

*Linear milestone:* Phase 0 — Foundation (Alpha Launch project, target 2026-07-31). Gate: all 4 must-pass criteria met AND weighted score ≥ 65%. Hard override: August arrival triggers Phase 1 regardless.

*24 issues (EP-52 → EP-75):*
- EP-52: Wire Brevo (Enitan, Urgent, Jun 21) — blocks EP-55, EP-62, EP-63, EP-64
- EP-53: Audit existing ~8 articles (Teresa, Urgent, Jun 28) — blocks EP-67 through EP-73
- EP-54: Technical SEO foundation — CWV, GSC, robots.ts, /pricing.md, /llms.txt (Enitan, Urgent, Jun 21)
- EP-55: Landing page + waitlist signup (Enitan, Urgent, Jun 28)
- EP-56: 5-10 programmatic past paper pages (Enitan, High, Jul 20)
- EP-57: Bing + Brave Search verified (Enitan, Medium, Jul 5)
- EP-58: School/teacher outreach list — 5-10 schools Tier 1 (Enitan, High, Jul 15)
- EP-59: Teresa's LinkedIn profile complete (Teresa, Urgent, Jun 21)
- EP-60: Join + observe 2-3 Facebook parent groups (Teresa, High, Jun 21)
- EP-61: WhatsApp Business App + ExamPilot community (Teresa, Medium, Jul 5)
- EP-62: Waitlist email sequence 5 emails (Teresa, Urgent, Jul 5)
- EP-63: Student onboarding email sequence 6 emails (Teresa, High, Jul 10)
- EP-64: Parent email sequence 4 emails (Teresa, High, Jul 10)
- EP-65: "For Parents" landing page (Teresa, High, Jul 15)
- EP-66: Results Day content — staged, DO NOT publish early (Teresa, Urgent, Jul 20)
- EP-67: Pillar page Cambridge 9709 Pure Mathematics 1 (Teresa, Urgent, Jul 10)
- EP-68–70: Topic spokes — Coordinate Geometry, Quadratics, Series & Circular Measure (Teresa, High, Jul 15)
- EP-71–73: Strategy spokes — How to Pass, Common Mistakes, Best Resources (Teresa, High, Jul 20)
- EP-74: Examiner report analysis bridge content (Teresa, Medium, Jul 25)
- EP-75: Link building 3-5 referring domains (Enitan, Medium, Jul 28)

*`/weekly-pulse` Step 7 updated:* Queries Linear for EP-55, EP-62, EP-60, EP-61, EP-65 status; scores 9 gate criteria (4 must-pass + 5 weighted); outputs scorecard with ON TRACK / AT RISK / BLOCKED; surfaces single blocking item. Phase-aware — adapts to Phase 1+ once Phase 0 is passed.

**Why:** Applied the execution model (see 2026-05-17 execution model entry): Phase 0 is one-time setup work → Linear. Recurring gate check → ritual. Both wired.

**Key dependency chain:** EP-52 (Brevo) unblocks EP-55/62/63/64. EP-53 (article audit) unblocks EP-67–73. EP-59 (Teresa LinkedIn profile) must be done before Enitan acts on EP-58.

**Owner:** Enitan
