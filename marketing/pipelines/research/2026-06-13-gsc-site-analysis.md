---
type: research-report
channel: seo
stage: tofu
target-segment: student-cambridge
status: drafted
created: 2026-06-13
author: Enitan (AIOS)
data-sources: Google Search Console (OAuth), DataForSEO (search volume)
window: 90 days (2026-03-15 to 2026-06-10, GSC dataState=final, ~3-day lag)
---

# ExamPilot Site Analysis — GSC + DataForSEO

**Date:** 2026-06-13 · **Window:** Last 90 days · **Property:** https://www.exampilot.io/

## Bottom line up front

We are pre-launch and already ranking on page 1 of Google for the exact CIE 9709 Pure 1 topics the August launch gates on. Demand is real and validated, and we hold those positions with no link building. That is the headline win.

The CTR story is more nuanced than an earlier draft of this report claimed (see the revision note in Method and caveats). Blended CTR is 0.84%. That is not the failure it looks like against the old 2-4% rule of thumb. Every ranking page here is an *informational* query, and 99.9% of AI Overviews fire on informational queries (Ahrefs 2026). AI Overviews now cut clicks to the #1 result by ~58% and informational CTR by ~61% since mid-2024. For AIO-exposed informational pages at position 7-9 in 2026, ~0.8% is roughly the new normal, not underperformance. Our own data proves the structural cause: the navigational homepage ("exampilot") sits at 4.9% CTR while the informational topic pages sit at 0.5-0.8% — same site, same week, same unknown brand. The gap is intent type plus AIO suppression, not bad titles.

This matches doctrine we already hold: per `wiki/marketing/seo/seo-strategy.md` (GEO point 13), informational pages are measured by citation share and brand-search lift, not clicks; the real click capture lives on navigational, comparison, and pricing pages. So the near-term levers are (a) own the AIO-free navigational and comparison SERPs where clicks still exist, and (b) optimise informational pages for AI citation, not CTR.

Two structural insights underneath that:
1. Our best topic pages report 0 volume in keyword-planner tools yet pull thousands of real impressions. The planner is blind to the informational long tail. This is the Tier 1 keyword thesis working as designed (we target these deliberately, see seo-strategy) — and the product pages are already realising it pre-launch.
2. CIE 9709 is an international exam. Measuring its demand from a UK lens shows near-zero. The market is in Pakistan, India, UAE, Egypt, Malaysia. Incumbents built for UK domestic boards under-serve it.

## Where we are — the numbers

Over 90 days: ~100 clicks, ~11,900 impressions across 11 indexed pages. Blended CTR 0.84%.

| Page | Clicks | Impressions | CTR | Avg Pos |
|---|---|---|---|---|
| /cambridge/9709/pure-1 | 29 | 3,682 | 0.8% | 7.0 |
| /cambridge/9709/pure-1/trigonometry | 24 | 3,034 | 0.8% | 8.8 |
| /cambridge/9709/pure-1/functions | 14 | 2,681 | 0.5% | 7.6 |
| /cambridge/9709/pure-1/integration | 14 | 926 | 1.5% | 8.1 |
| / (homepage) | 9 | 183 | 4.9% | 5.3 |
| /cambridge/9709/pure-1/differentiation | 7 | 694 | 1.0% | 9.6 |
| /cambridge/9709/pure-1/quadratics | 3 | 549 | 0.5% | 9.2 |
| /about | 0 | 36 | 0.0% | 3.6 |
| /waitlist | 0 | 41 | 0.0% | 5.2 |
| /blog/author/enitan-williams | 0 | 18 | 0.0% | 6.3 |
| /blog/author/teresa-gonzalez | 0 | 17 | 0.0% | 5.5 |

## What's working

- **Page-1 rankings, pre-launch, with zero link building.** Seven topic pages sit at average positions 7.0-9.6. That is page 1 for a brand Google barely knows. The topical relevance of the /cambridge/9709/pure-1/* structure is doing real work.
- **Demand is concentrated exactly where the launch needs it.** Trigonometry, functions, integration, differentiation, quadratics. The August gate is 50 moderated CIE 9709 Pure 1 (Algebra) QLPs. Functions (2,681 impr) and quadratics (549 impr) are the Algebra-family pages already pulling demand. The content plan is aimed at proven demand, not a guess.
- **A brand footprint exists.** "exampilot" returns 30 impressions at position 4.3. People are also searching "a level pilot" and "a level copilot" — brand variants forming.

## CTR — read it by intent, not against the old benchmark

An earlier draft framed the 0.8% CTR as a leak worth a 3.8x fix from rewriting titles. That was wrong on two counts, and the correction matters for where effort goes.

**1. The 2-4% benchmark is pre-AI.** Current data on AI-Overview suppression:
- AI Overviews cut clicks to the #1 result by ~58%, up from 34.5% ten months earlier (Ahrefs, Dec 2025).
- Informational-query CTR fell ~61% since mid-2024; even non-AIO queries lost ~41% YoY (Seer Interactive).
- Position #1 CTR down 32%, position #2 down 39% in a 200K-keyword study (GrowthSRC).
- 99.9% of AI Overviews fire on informational queries (Ahrefs). Every page in the table above is informational, so it sits in the single most click-suppressed category. At position 7-9, AIO-exposed, ~0.8% is roughly the 2026 normal — not a failure to fix.

**2. For informational pages, clicks are the wrong KPI.** Our own `seo-strategy.md` (GEO point 13) already re-baselined: informational content is measured by **citation share and brand-search lift**, because AIO eats the clicks regardless of title quality. Optimising these titles for CTR is polishing a metric we have already decided not to chase here.

**Internal proof of the structural cause:** the navigational homepage ("exampilot") earns 4.9% CTR at position 5.3, while the informational topic pages earn 0.5-0.8% at similar positions. Same domain, same week, same unknown brand. The 6x gap is intent type plus AIO suppression. No title rewrite closes that.

**So where CTR work is still worth it (real, AIO-free clicks):**
- Navigational queries (brand SERP — see brand insight below). Near-zero AIO presence.
- Comparison / `/vs/` pages and pricing pages. Commercial intent, almost never AIO-triggered.
- The ultra-niche paper-code tail (e.g. `9709/13/o/n/24`) that is too obscure to trigger an AIO at all — here older CTR norms still apply and a clear title helps.

For the informational topic pages, the lever is GEO: answer-first prose, descriptive stand-alone headings, FAQ blocks, query fan-out coverage (per seo-strategy GEO section) — to win citation share, which is the KPI that actually moves.

**Measured (2026-06-13, DataForSEO SERP).** AIO presence is mixed, not blanket, and varies by geography (AIOs reshuffle every ~2 days, so this is a snapshot):

| Query | UK | Pakistan |
|---|---|---|
| 9709 trigonometry | AIO | no |
| 9709 functions | AIO | AIO |
| 9709 differentiation | AIO | no |
| 9709 integration | no | no |
| 9709 syllabus | no | no |
| cambridge 9709 pure 1 | no | no |
| a level maths past papers | no | no |
| 9709/13/o/n/24 | no | no |
| exampilot (brand) | no | no |

This confirms two things and refines one:
- **Suppression is real on our biggest pages.** Trigonometry, functions, and differentiation (3 of our top 4 by impressions) trigger AIOs in the UK. Citation share, not CTR, is the right KPI for these.
- **The AIO-free click targets are concrete.** Integration, "9709 syllabus", "a level maths past papers", the niche paper-code tail, and the brand term show no AIO. Title/meta CTR work is worthwhile on exactly these.
- **Geography softens the headline.** Pakistan shows fewer AIOs than the UK for the same terms. Since our audience skews international, real AIO exposure for our users is likely milder than the UK-centric 58% headline implies. Suppression is real but not uniformly deep for our market.

## The arbitrage insight — invisible long tail

DataForSEO (Google Ads volume) reports **0/mo** for "9709 trigonometry", "9709 functions", "cambridge 9709 pure 1", "cambridge 9709 pure 1 questions" and every topic-level term. Yet GSC shows those pages pulling 900-3,000 impressions each. The keyword planner buckets and rounds the informational long tail to zero because it is an ads-buying tool, blind to emerging and granular queries.

Implication: any competitor prioritising by ad volume will never target these terms. We rank for them already. This is exactly the Tier 1 keyword thesis ("volumes look small but intent is extremely high") confirmed with live data. Lean in. Do not let zero-volume reports talk us out of the pages that are working.

The plannable head terms that *are* in scope and real:
- **"9709 syllabus" — 3,600/mo worldwide, LOW competition.** We show at position 32.9. A dedicated, well-structured syllabus page is a clear opening.
- "a level maths past papers" — 27,100/mo worldwide, but Tier 3 (KD ~55), incumbent-dominated, and partly the out-of-scope UK domestic audience. Not a near-term play.

## The geography insight

| Keyword | UK vol/mo | Worldwide vol/mo |
|---|---|---|
| a level maths past papers | 9,900 | 27,100 |
| 9709 syllabus | 20 | 3,600 |
| cambridge 9709 | 10 | 110 |

A UK lens understates the in-scope market by ~180x on "9709 syllabus". Confirms the exam-board-first, geography-second positioning. SaveMyExams and Physics & Maths Tutor are built for UK domestic boards; the CIE 9709 international student is structurally under-served. That gap is the opening.

## Interesting / anomalies — worth a look

- **AI-conversation fragments are appearing as queries.** "ok more", "what about the others", "more examples", "help me", "anything else i need to know", "no no in english", "trong bài trên" (Vietnamese), "the graph of g is a translation 3 units down". These read like chat/copilot turns, not search queries. Either tutor-conversation content is being indexed (thin-content risk and possible index bloat) or our pages surface oddly for them. Worth a crawl/index hygiene check — confirm we are not indexing chat transcripts.
- **International reach is already showing.** Vietnamese text, "pakistan" as a query, "no no in english". The global CIE audience is finding us in-season.
- **We do not own our own brand SERP.** Homepage ranks position 4.3-5.3 for "exampilot". We should be #1. Likely a new-domain / homepage-title issue. Quick to check, easy to flag.
- **Past-paper-code searches are frequent.** "9709/13/o/n/24" and similar. High intent, and directly relevant to the open IP-posture decision — these users want past papers, and our posture on Cambridge-derived content shapes what we can serve them.

## Alignment with immediate plans

The path to first revenue gates on: QLP Pure 1 Algebra content seeded → Dodo Payments live → first conversion, against the August Results Day window. This analysis materially de-risks the content half of that:

- We are not guessing what to seed. Google already tells us trigonometry, functions, integration, differentiation, quadratics pull demand. Seed and surface those first.
- Results day (August) and the Sep-Oct resit window are the seasonal peaks. We are entering the run-up now, in-season, with page-1 positions already held. Timing favours acting on CTR immediately.

**One flag to reconcile:** the wiki (`path-to-revenue.md`) lists "SEO content: Not started". But seven topic pages are live and ranking. These appear to be the product's programmatic /cambridge/9709/pure-1/* routes, not the blog content programme. Both statements can be true, but the wiki should distinguish "product topic pages live and ranking" from "blog content programme not started" — right now it reads as if we have no organic presence, which is false.

## Recommended next moves

Ordered by where real clicks actually exist in the AI era (navigational and commercial first; informational by citation share).

1. **Lock down the brand SERP.** Navigational queries are AIO-free, so this is genuine click capture. Get the homepage to #1 for "exampilot" (currently pos 4.3-5.3). Highest-confidence click win on the board.
2. **Build a dedicated "9709 syllabus" page.** Real 3,600/mo head term, LOW competition, we already show at pos 33. Winnable, and not fully AIO-suppressed.
3. **Optimise the informational topic pages for citation share, not CTR.** Answer-first prose, descriptive stand-alone headings, FAQ blocks, query fan-out (per seo-strategy GEO section). Measure them by citation share + brand-search lift, not clicks — that is the KPI doctrine for informational pages.
4. **AIO-presence check — done (2026-06-13).** See the table in the CTR section. Title/meta CTR work is justified on the AIO-free terms (integration, "9709 syllabus", "a level maths past papers", the paper-code tail, brand); trigonometry/functions/differentiation are AIO-suppressed and should be managed via citation share. Re-check periodically since AIOs reshuffle every ~2 days.
5. **Run an index-hygiene check** on the conversational-fragment queries. Confirm chat transcripts are not being indexed.
6. **Feed this into the content seeding order** — prioritise QLP seeding for functions and trigonometry (highest demand, Algebra-family, launch-gated).
7. **Update target-keywords.md** with the live KD/volume reality: confirm the long-tail-arbitrage thesis, promote "9709 syllabus" to a near-term target.

## Method and caveats

- **Revision note (2026-06-13):** the CTR section was rewritten after review. The first draft benchmarked against a pre-AI 2-4% position-7-9 CTR and recommended title rewrites for a 3.8x gain. That ignored AI-Overview suppression and cut against our own informational-KPI doctrine. Corrected above: informational CTR is judged in the AI-era context and by citation share, not the old benchmark.
- GSC OAuth, property https://www.exampilot.io/, dataState=final (~3-day lag), 90-day window.
- DataForSEO Google Ads search_volume, worldwide + UK + Pakistan cuts. Ads volume rounds and buckets; it undercounts informational long tail by design — treat the 0s as "below the planner's floor", not "no demand". GSC impressions are the truer demand signal here.
- Positions are 90-day averages and move with seasonality. We are mid CIE May/June series heading into the August window, so impressions are riding the in-season wave.
- AIO-presence measured 2026-06-13 (DataForSEO SERP advanced, UK + Pakistan, top 10 queries). Snapshot only — AIOs reshuffle every ~2 days. SERP-API AIO detection can undercount (some AIOs load on interaction), so treat "no" as "no AIO observed at fetch", not a guarantee.
- DataForSEO spend: $0.225 (volume) + $0.07 (AIO presence) = ~$0.30 total. Account balance at first run: ~$47.94.

**CTR sources (AI-era):**
- [Ahrefs — AI Overviews reduce clicks by 58%](https://ahrefs.com/blog/ai-overviews-reduce-clicks/)
- [Seer Interactive — organic CTR down 61% on informational AIO queries](https://searchengineland.com/google-ai-overviews-drive-drop-organic-paid-ctr-464212)
- [GrowthSRC — position #1 CTR down 32%, #2 down 39%](https://growthsrc.com/google-organic-ctr-study/)
- Internal corroboration: navigational homepage 4.9% CTR vs informational topic pages 0.5-0.8% (this report's table).
