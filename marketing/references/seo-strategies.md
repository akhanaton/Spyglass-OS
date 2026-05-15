# SEO Strategies: Data-Driven Playbook

Verified, effective SEO strategies executable with the DataForSEO + GSC API + GA4 + PostHog stack. Each strategy maps to: the signal to detect, the data sources that surface it, the action to take, and the future command to build. Documented 2026-05-15.

This file is the specification source for `/strategy-review` and any specialist SEO commands built during DataForSEO integration.

---

## Strategy 1: Striking Distance Optimisation

**What it is:** Pages ranking positions 8-15 for keywords with meaningful search volume. A targeted improvement (stronger title, deeper content, better internal linking) often moves them to the top 5, where CTR jumps 3-5x.

**Signal to detect:**
- Position 8-15 in DataForSEO rank tracking
- Impressions > 0 in GSC (Google knows the page exists)
- Clicks low relative to impressions (CTR < 3%)
- GA4: decent engagement time when people do land (content quality is there)

**Data sources:** DataForSEO rank tracking + GSC API + GA4

**Action:** Update title tag, strengthen H1, deepen the weakest section, add FAQPage schema, add 2-3 internal links from higher-authority pages.

**Command to build:** Part of `/strategy-review` — weekly output includes "Striking Distance" list sorted by search volume × position gap × impressions.

**ExamPilot priority:** High from Phase 1. First articles will land in positions 8-20 before compounding to the top 5.

---

## Strategy 2: CTR Optimisation (Title & Meta Testing)

**What it is:** A page ranking position 3 should get ~10% CTR. If it's getting 2%, the title tag or meta description is failing — not the ranking. Fixing the click problem is faster than improving the rank.

**Signal to detect:**
- GSC API: query + page CTR vs. expected CTR for that position
- Expected CTR benchmarks by position (approximate): P1 ~28%, P2 ~15%, P3 ~10%, P4 ~7%, P5 ~5%, P6-10 ~2-4%
- Flag any page with CTR more than 40% below the position benchmark

**Data sources:** GSC API

**Action:** Rewrite title tag to be more specific, add power words, include the year, match exact search intent. Test meta description with a clear benefit statement.

**Command to build:** `seo-ctr-audit` — pulls all pages from GSC, calculates CTR gap vs. position benchmark, outputs ranked list of title improvement opportunities.

**ExamPilot priority:** Medium at Phase 0-1 (few pages, few impressions). High at Phase 2+ when content library grows.

---

## Strategy 3: Content Decay Detection

**What it is:** Pages that ranked well 3-6 months ago but are now losing position and impressions. Decay happens when content ages, competitors publish fresher material, or Google's algorithm re-evaluates E-E-A-T signals.

**Signal to detect:**
- DataForSEO: pages losing 3+ positions over a rolling 8-week window
- GSC API: impressions declining week-over-week for 3+ consecutive weeks
- Not caused by a sitewide algorithm update (check if other pages are also declining — if yes, it's algorithmic not content-specific)

**Data sources:** DataForSEO rank tracking + GSC API

**Action:** Update publication date, refresh statistics and examples, add a new section addressing a question competitors now answer that you don't, strengthen internal links from newer articles.

**Command to build:** Part of `/strategy-review` — "Decaying Pages" list with weeks of consecutive decline and estimated traffic loss.

**ExamPilot priority:** Low at Phase 0 (nothing to decay yet). High at Phase 2-3 when the content library is 6+ months old.

---

## Strategy 4: Keyword Cannibalisation Detection

**What it is:** Two or more pages on your site competing for the same keyword. Google picks one to rank, often the wrong one, and both pages rank lower than either would alone. Very common when building pillar + spoke architecture (pillar and spoke can inadvertently target the same query).

**Signal to detect:**
- GSC API: the same query appearing across multiple pages in the search performance report
- DataForSEO: multiple ExamPilot URLs appearing in SERP for the same keyword
- Symptom: a query shows high impressions but low clicks spread across 2+ URLs

**Data sources:** GSC API + DataForSEO SERP data

**Action:** Decide which page should own the keyword. Consolidate content into the winner. Redirect the loser or reposition it to target a different but related query. Add a canonical tag if consolidation isn't possible.

**Command to build:** `seo-cannibalisation-check` — cross-references all GSC queries against the pages they appear on, flags any query served by more than one URL.

**ExamPilot priority:** Medium. Pillar/spoke architecture is specifically designed to avoid this, but it will naturally occur as the content library grows to 80+ pages.

---

## Strategy 5: Featured Snippet Targeting

**What it is:** Position 0 — the direct answer box above organic results. For education queries ("what is integration calculus", "how to find the discriminant"), featured snippets are common and capture 8-12% of clicks that would otherwise go to position 1.

**Signal to detect:**
- DataForSEO SERP data: which of your target keywords show a featured snippet?
- DataForSEO: which URL currently holds the snippet?
- GSC: your page ranks positions 2-5 for that keyword (prime striking distance for snippet theft)

**Data sources:** DataForSEO SERP features data

**Action:** Add a tightly formatted answer (40-60 words) directly under the H2 that matches the query. For "what" queries: definition block. For "how" queries: numbered steps. For "which" queries: comparison table. Match the format of the existing snippet — Google rarely changes the snippet format when it already likes one.

**Command to build:** `seo-snippet-opportunities` — queries where a snippet exists + ExamPilot ranks 2-10 + no snippet currently held by ExamPilot. Sorted by monthly search volume.

**ExamPilot priority:** High. Cambridge 9709 topic queries ("what is the chain rule", "how to solve quadratics 9709") are exactly the format that produces featured snippets. Early wins here compound into AI Overview citations.

---

## Strategy 6: Topic Cluster Gap Analysis

**What it is:** Systematic identification of keywords in your target topic clusters that you don't yet have content for. Fills holes in the pillar/spoke architecture before competitors do.

**Signal to detect:**
- DataForSEO keyword research: all keywords in the semantic cluster around each pillar (e.g., "cambridge 9709 pure 1 [topic]" permutations)
- GSC API: which of those keywords are you getting any impressions for? (proxy for existing content)
- Gap = keywords with search volume > 50/mo where you have zero impressions

**Data sources:** DataForSEO keyword research + GSC API

**Action:** For each gap keyword: does an existing spoke partially cover this? If yes, expand that spoke. If no, add it to the content calendar as a new spoke.

**Command to build:** `seo-cluster-gap` — takes a topic cluster (e.g., "9709 pure 1"), generates keyword universe via DataForSEO, cross-references against GSC impressions, outputs gaps sorted by search volume.

**ExamPilot priority:** High from Phase 0. The seomachine repo already has keyword maps for Pure 1 — this command automates what was done manually there, and will need to be re-run for each new 9709 unit as product expands.

---

## Strategy 7: People Also Ask (PAA) Targeting

**What it is:** Google surfaces "People Also Ask" question boxes for most informational queries. Answering PAA questions in your content earns SERP real estate and feeds AI Overview answers. Education queries have some of the highest PAA density of any niche.

**Signal to detect:**
- DataForSEO SERP data: PAA questions appearing for your target keywords
- Check: does your article currently answer those specific questions?
- GSC: impressions on the query but low CTR (PAA box may be diverting the click)

**Data sources:** DataForSEO SERP features data

**Action:** Add an FAQ section to the article that directly answers the PAA questions Google is showing. Use FAQPage JSON-LD schema. Keep answers to 40-60 words — this is also the optimal length for AI Overview extraction.

**Command to build:** `seo-paa-audit` — for each published article, pulls PAA questions for its target keyword, checks which questions the article already answers, outputs gaps. Feeds directly into content update queue.

**ExamPilot priority:** Very high. This directly supports the GEO strategy — PAA answers and AI Overviews pull from the same content signals. Every article that answers PAA questions is simultaneously optimised for Google and for ChatGPT/Perplexity.

---

## Strategy 8: Programmatic Page Enrichment Prioritisation

**What it is:** You have 120-180+ past paper landing pages planned. They'll be created as noindex until enriched. The question is which pages to enrich first. The answer is: the ones with the highest potential traffic that your competitors are already capturing.

**Signal to detect:**
- DataForSEO SERP data: search volume for "[paper code] [year] [session] past paper" queries
- DataForSEO competitor analysis: which past paper pages are SaveMyExams/PapaCambridge ranking for?
- Cross-reference with your noindex page list — highest-volume queries with competitor rankings = highest-priority enrichment

**Data sources:** DataForSEO keyword research + DataForSEO competitor SERP data

**Action:** Enrich the top 10-20 highest-volume noindex past paper pages first. Remove noindex, add unique content (difficulty rating, topic breakdown, misconception data), link to relevant pillar/spoke pages.

**Command to build:** `seo-programmatic-priority` — cross-references your noindex past paper URL list against DataForSEO search volumes and competitor rankings, outputs enrichment priority order.

**ExamPilot priority:** High from Phase 1. The noindex protocol is correct — this command makes sure the enrichment work happens in the right order.

---

## Strategy 9: Seasonal Keyword Pre-Staging

**What it is:** Exam-related search volume spikes are entirely predictable. "Cambridge 9709 results 2027", "a level resit 2027", "cambridge 9709 paper 1 2027 predictions" — these queries spike sharply 2-4 weeks before each exam event. Publishing content after the spike is too late.

**Signal to detect:**
- DataForSEO Google Trends integration: historical seasonal patterns for target keywords
- Build a seasonal calendar: when do "results day", "resit", "mock exam", "past papers" queries spike month-by-month?
- Cross-reference with your content publishing calendar — are high-seasonality keywords covered 4-6 weeks ahead of the spike?

**Data sources:** DataForSEO Google Trends + keyword historical volume

**Action:** Pre-stage seasonal content (write and review it) so it's ready to publish at the optimum window — typically 3-4 weeks before the search volume spike begins. For Results Day content, publish on the day (content is already written and scheduled).

**Command to build:** `seo-seasonal-calendar` — pulls historical search volume patterns for exam-related keywords, outputs a publishing calendar with recommended publish dates for each piece of seasonal content.

**ExamPilot priority:** Very high. The exam calendar is the marketing metronome — seasonal keyword pre-staging is the SEO expression of that principle.

---

## Strategy 10: Competitor Content Gap

**What it is:** Keywords your competitors (SaveMyExams, PapaCambridge, Physics & Maths Tutor) rank for in positions 1-10 that you have no content for at all. These are proven, traffic-generating topics in your niche — the competitor's ranking confirms demand exists.

**Signal to detect:**
- DataForSEO competitor keyword research: all keywords SaveMyExams/PapaCambridge rank for in positions 1-10
- Filter to: keywords relevant to Cambridge 9709 / IGCSE maths / exam preparation
- Filter out: keywords you already have content for (cross-reference GSC impressions > 0)
- Sort by: search volume × keyword difficulty (target KD 0-25 first)

**Data sources:** DataForSEO competitor analysis

**Action:** Add highest-priority gaps to the content calendar. For each gap: check whether an existing article can be expanded to cover it, or whether a new article is needed.

**Command to build:** `seo-competitor-gaps` — inputs a competitor domain, outputs keywords they rank P1-10 for that ExamPilot has no GSC impressions on, sorted by search volume × difficulty score.

**ExamPilot priority:** High from Phase 1. SaveMyExams has years of content. Their keyword footprint is a map of proven demand in your exact niche.

---

## Strategy 11: Search Intent Mismatch Detection

**What it is:** You've written a "how to" guide but Google is ranking listicles for that query. Or you've written a comparison page but Google wants a tutorial. The content format doesn't match what Google's algorithm has determined satisfies that query's intent — so it doesn't rank regardless of quality.

**Signal to detect:**
- DataForSEO SERP data: what content types dominate positions 1-3 for your target keyword? (listicle / guide / comparison / definition / tool)
- GSC: your page has impressions but below-average CTR — possible intent mismatch
- GA4: high bounce rate on the page — users expected something different

**Data sources:** DataForSEO SERP data + GSC API + GA4

**Action:** Reformat the page to match the dominant intent type. If positions 1-3 are all listicles, restructure your guide as a list. If they're all step-by-step tutorials, restructure your comparison. This is often a bigger ranking factor than content depth.

**Command to build:** Part of `/strategy-review` — flags pages where your content format diverges from the dominant SERP format for its target keyword.

**ExamPilot priority:** Medium. More relevant at Phase 2-3 when you have enough pages to audit systematically.

---

## Strategy 12: Internal Link Equity Distribution

**What it is:** Some pages accumulate authority (from backlinks, engagement signals, age). That authority can be passed to other pages via strategic internal links. High-authority pages linking to striking-distance pages accelerates their ranking improvement.

**Signal to detect:**
- DataForSEO backlink data: which ExamPilot pages have the most referring domains?
- GSC API: which pages have the highest impressions (proxy for authority)?
- Cross-reference: do those high-authority pages internally link to your striking-distance target pages?
- Gap = striking-distance pages not linked from any high-authority page

**Data sources:** DataForSEO backlink data + GSC API

**Action:** Add contextual internal links from your highest-authority pages to your striking-distance targets. Use descriptive anchor text (not "click here" — use the target keyword).

**Command to build:** Part of `seo-striking-distance` — for each striking distance page, check whether your top-10 authority pages link to it. Surface internal link gaps.

**ExamPilot priority:** Medium at Phase 1, High at Phase 2. More valuable once you have 20+ articles and some with established authority.

---

## Strategy 13: Zero-Click / AI Overview Monitoring

**What it is:** Google's AI Overviews are reducing organic clicks for informational queries. A page can rank position 1 and get half the clicks it would have gotten a year ago because an AI Overview answers the question above it. The right response is not to fight AI Overviews — it's to get cited inside them.

**Signal to detect:**
- DataForSEO SERP data: which of your target keywords now show an AI Overview?
- GSC API: impressions stable or growing but clicks declining — AI Overview is intercepting the click
- Track: does ExamPilot appear as a source citation inside the AI Overview?

**Data sources:** DataForSEO SERP features data + GSC API

**Action (two-part):**
1. For queries with AI Overviews where ExamPilot is NOT cited: optimise for citation (answer-first structure, FAQPage schema, cite official sources, entity optimisation). This is the GEO strategy applied specifically.
2. For queries with AI Overviews where you ARE cited: monitor that citation persists. These pages are performing their job.
3. Shift content effort for heavily-AI-Overview'd queries toward bottom-funnel queries (comparison pages, "best X" queries, specific tool questions) where AI Overviews are less common and clicks still happen.

**Command to build:** `seo-ai-overview-monitor` — queries where AI Overview is present + ExamPilot's click/impression trend + whether ExamPilot is cited. Flags queries where we're losing clicks to AI Overviews but not being cited.

**ExamPilot priority:** Medium now, High by Phase 2. AI Overviews are most common for exactly the informational education queries we target. Getting cited early compounds — AI systems tend to keep citing sources they've already established.

---

## Strategy 14: Backlink Gap Analysis

**What it is:** Domains linking to SaveMyExams, PapaCambridge, or Physics & Maths Tutor for Cambridge 9709 content — but not linking to ExamPilot. These are proven link sources in your niche: they've already decided this topic is worth linking to.

**Signal to detect:**
- DataForSEO backlink data: referring domains for each competitor
- Filter to: domains linking to competitor pages about Cambridge 9709 / IGCSE maths specifically
- Cross-reference: do any of those domains also link to ExamPilot? (if yes, they're already aware of you)
- Gap = domains linking to competitors but not to you

**Data sources:** DataForSEO backlink data

**Action:** For each gap domain: identify why they link to the competitor (resource list, blog post, directory, student forum). Determine whether ExamPilot could earn a similar link (reach out with your free tool, your examiner report analysis, your data-driven content).

**Command to build:** `seo-backlink-gap` — takes 3 competitor domains, outputs referring domains not linking to ExamPilot, sorted by domain rating.

**ExamPilot priority:** Low at Phase 0-1 (not enough content to earn links at scale). High at Phase 2-3 when product-led content and free tools give you something compelling to pitch.

---

## Strategy 15: Reddit-to-Article Signal Mining

**What it is:** Reddit is a gold mine of exact-match student language. High-upvote questions in r/alevel and r/CambridgeInternational are proof that the topic has demand, the phrasing resonates with students, and the question isn't being answered well enough elsewhere. If a question gets 200 upvotes, there's an article in it.

**Signal to detect:**
- Syften + RedShip: high-engagement Reddit threads on target topics
- DataForSEO keyword research: does the question topic (or close variant) have search volume?
- GSC: is ExamPilot already ranking for any related query?

**Data sources:** Syften/RedShip Reddit monitoring + DataForSEO keyword research + GSC API

**Action:** If a Reddit question has 100+ upvotes AND the topic has DataForSEO-confirmed search volume AND ExamPilot has no GSC impressions on it → add to content calendar immediately. Use the exact student language from the Reddit thread in the title and H2s.

**Command to build:** Part of `/strategy-review` — cross-references high-engagement Reddit threads (from Syften/RedShip) against keyword volumes (DataForSEO) and GSC coverage gaps. This is the channel where organic Reddit discovery feeds SEO strategy directly.

**ExamPilot priority:** Very high. This closes the loop between community intelligence and content strategy — and it's a compound advantage competitors without community presence don't have.

---

## Command Architecture: What Goes Where

### Inside `/strategy-review` (do not build as separate commands)

`/strategy-review` is the weekly synthesis command. These strategies run as sub-checks inside it — not as standalone commands — because they need the same data pull and the results are most useful when read together.

| Strategy | What it contributes to `/strategy-review` output |
|---|---|
| 1. Striking distance | "Striking Distance" section: pages at positions 8-15, sorted by volume × gap × impressions |
| 3. Content decay | "Decaying Pages" section: pages losing 3+ positions over 8 weeks |
| 11. Search intent mismatch | "Intent Mismatch" flags on any page where SERP format diverges from your content format |
| 15. Reddit-to-article signal mining | "Content Opportunities" section: high-upvote Reddit threads with confirmed search volume and no GSC coverage |

**`/strategy-review` full output structure:**
1. KPI snapshot vs. phase targets (north star + leading indicators)
2. Striking distance list (Strategy 1)
3. Decaying pages list (Strategy 3)
4. Content opportunity queue — Reddit signals + cluster gaps cross-referenced (Strategy 15 + feeds Strategy 6)
5. Intent mismatch flags (Strategy 11)
6. Channel allocation recommendation (demand gen vs. acquisition split based on exam calendar + PostHog conversion data)
7. 3-5 specific actions for the coming week

This is a decision memo, not a dashboard. Every run should end with a numbered action list.

---

### Standalone Commands (build separately)

These require dedicated runs, specific inputs, or on-demand use rather than a fixed weekly cadence.

| Priority | Command | Strategy | When to run | Phase to build |
|---|---|---|---|---|
| 1 | `seo-cluster-gap` | 6. Topic cluster gap | When starting a new content cluster | Phase 0-1 |
| 2 | `seo-seasonal-calendar` | 9. Seasonal pre-staging | Once per exam cycle (update quarterly) | Phase 0 |
| 3 | `seo-paa-audit` | 7. PAA targeting | After publishing or updating an article | Phase 1 |
| 4 | `seo-competitor-gaps` | 10. Competitor content gap | Monthly, or when expanding to a new unit | Phase 1 |
| 5 | `seo-programmatic-priority` | 8. Programmatic enrichment order | When batching past paper enrichment work | Phase 1 |
| 6 | `seo-snippet-opportunities` | 5. Featured snippet targeting | Monthly once 40+ pages indexed | Phase 1-2 |
| 7 | `seo-ctr-audit` | 2. CTR optimisation | Monthly once 20+ pages with impressions | Phase 2 |
| 8 | `seo-cannibalisation-check` | 4. Cannibalisation | Quarterly, or when adding a new cluster | Phase 2 |
| 9 | `seo-ai-overview-monitor` | 13. AI Overview / zero-click | Monthly | Phase 2 |
| 10 | `seo-internal-links` | 12. Internal link equity | After every 10 new articles published | Phase 2 |
| 11 | `seo-backlink-gap` | 14. Backlink gap | Quarterly, when running link-building sprints | Phase 2-3 |

---

## Data Source Requirements per Command

Quick reference for wiring DataForSEO endpoints when building each command:

| Command | DataForSEO endpoints | Other sources |
|---|---|---|
| `/strategy-review` | rank_tracking, serp_results, keyword_overview | GSC API + GA4 + PostHog + Syften/RedShip |
| `seo-cluster-gap` | keyword_ideas, keywords_for_site | GSC API |
| `seo-seasonal-calendar` | keyword_overview (historical volume) | — |
| `seo-paa-audit` | serp_features (PAA questions) | — |
| `seo-competitor-gaps` | competitor_keywords | GSC API |
| `seo-programmatic-priority` | keyword_overview, serp_results | Sanity CMS page list (noindex pages) |
| `seo-snippet-opportunities` | serp_features (featured snippets) | GSC API |
| `seo-ctr-audit` | — | GSC API only |
| `seo-cannibalisation-check` | serp_results | GSC API |
| `seo-ai-overview-monitor` | serp_features (AI Overviews, citations) | GSC API |
| `seo-internal-links` | backlinks (internal) | Sanity CMS page list |
| `seo-backlink-gap` | backlinks_competitors | — |
