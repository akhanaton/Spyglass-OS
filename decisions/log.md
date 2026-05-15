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

**Decision:** Adopted stage-based KPI evolution (Phase 0-3) combined with leading/lagging indicators over AARRR pirate metrics or a single universal north star. Each phase has 1-2 primary KPIs that shift as the business matures. Channel-specific KPIs measured independently against each channel's funnel role. Six additional decisions documented in the plan: Edexcel deferred, paid ads conditional, TikTok Phase 2, location SEO Phase 2, product-led SEO Phase 2, pillar+spoke as SEO foundation.

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

## 2026-05-15 — Reddit tool stack: Syften + RedShip

**Decision:** Adopt Syften (€40/mo Standard) for brand/competitor monitoring and RedShip ($19/mo Starter) for Google-ranking thread discovery and reply drafting. Combined ~EUR 57/month. Activate F5bot (free) in Phase 0 to validate subreddit volume before spending. Add RedShip in Phase 1 ahead of Results Day.

**Why:** No single tool covers all requirements (subreddit monitoring + Google-rank detection + brand monitoring + reply drafting + manual-post-only workflow) at under EUR 80/mo. Syften is the strongest standalone monitoring tool with confirmed Reddit API compliance. RedShip is the only tool in this price range with an explicit weekly Google-ranking scan — finding threads that already rank on page 1 and staying in them compounds far longer than chasing new viral posts.

**Alternatives considered:** ReplyAgent (rejected: proxy accounts, incompatible with karma-building strategy); Redreach (rejected: DM automation creates ban risk, pricing opaque); ReplyDaddy (close but BYOK API costs push effective price to $69-99/mo, early-stage longevity risk); Brand24 (overkill, worse Reddit granularity at higher cost); SubHunt (watch list — similar Google-rank feature to RedShip at $12/mo but insufficient third-party validation). GummySearch is dead (shut down Nov 2025).

**Owner:** Enitan

---
