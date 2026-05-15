# SEO & Analytics Stack Reference

Tool decisions and architecture for ExamPilot's SEO intelligence loop. Researched and validated 2026-05-15. Re-verify pricing before purchasing — re-check DataForSEO API pricing at scale as usage grows.

---

## The Virtuous Loop Architecture

The goal is a closed feedback loop where every data source informs the next action, and Claude in the OS synthesizes them into strategy decisions — not just reports.

```
DataForSEO API
  → what keywords to target, what we're ranking for, competitor SERP positions
      ↓
Google Search Console API
  → ground truth: impressions, clicks, CTR, actual positions for our own pages
      ↓
GA4
  → which pages drive engaged sessions, where users drop off, traffic attribution
      ↓
PostHog
  → which sources produce activated trials, which convert to paid, retention by channel
      ↓
Claude (OS /strategy-review command)
  → synthesize all four sources → surface content gaps, channel shifts, KPI anomalies
      ↓
Action: publish article / update content / shift channel allocation
      ↓
DataForSEO tracks the result → loop repeats
```

This is not a dashboard exercise. The output of each `/strategy-review` run should be 3-5 specific, actionable decisions — not a status report.

---

## Data Sources: What Each Contributes

### DataForSEO API — Core programmatic SEO layer

**What it replaces:** Ahrefs, SEMrush, Mangools (long-term), Ubersuggest, SEO-Stack.

**Why it's the right choice at this stage:**
- Pay-per-call, not flat subscription. At startup-scale usage, cost is $12-28/mo vs $129-140/mo for Ahrefs Lite or SEMrush Pro.
- Programmatic: data comes into the OS directly, Claude analyzes it, no UI context-switching.
- Covers everything you need: SERP rank tracking, keyword volumes + difficulty, competitor SERP positions, backlink data, on-page/NLP analysis, Google Trends, historical SERP data.
- Scales with your actual usage — costs stay low until traffic justifies more frequent calls.

**Estimated API costs at Phase 0-1 scale:**

| Use case | Frequency | Est. monthly cost |
|---|---|---|
| Rank tracking (50 keywords) | Weekly | ~$2-5 |
| Keyword research bursts | ~200 lookups/mo | ~$5-10 |
| Competitor SERP snapshots | Monthly | ~$3-8 |
| On-page/NLP audits | Per new article | ~$2-5 |
| **Total** | | **~$12-28/mo** |

**Module to build:** `keyword_researcher.py` (already specced in P2 roadmap at `marketing/data_sources/modules/`).

**Implementation note:** DataForSEO has a sandbox environment for testing. Wire sandbox first, verify output format, then switch to live credentials.

---

### Google Search Console API — Ground truth layer

**What it gives you:** Actual impressions, clicks, CTR, and positions for every query and page on exampilot.io. The only data source that shows what Google is actually doing with your content.

**What it doesn't give you:** Competitor data, keyword volumes for terms you don't rank for, backlink data. GSC is self-referential — it only shows your own site.

**Module:** `gsc_analyzer.py` already exists at `marketing/data_sources/modules/gsc_analyzer.py`. Wire it in Phase 0 as soon as the first articles are indexed.

**Key queries to run weekly:**
- Queries with impressions > 0 but CTR < 2% (title/meta optimization opportunities)
- Pages losing impressions week-over-week (content freshness issues)
- Queries ranking positions 8-15 (low-hanging ranking improvements)
- New queries appearing for the first time (emerging keyword opportunities)

**Cost:** Free (Google Search Console API, standard quota).

---

### GA4 — Web behaviour layer

**What it gives you:** Traffic attribution (which channel brought this visitor), on-site behaviour (pages visited, session depth, scroll depth), goal completions (trial signups, pricing page views), conversion paths.

**Why it matters for the loop:** GSC tells you a page got 500 clicks. GA4 tells you whether those 500 people stayed, browsed to the trial page, and signed up — or bounced immediately. The gap between GSC clicks and GA4 engaged sessions reveals content quality issues that rank tracking can't surface.

**Module to build:** `ga4_analyzer.py` (specced in P2 roadmap). Use GA4 Data API v1 (free).

**Key metrics to pull into `/strategy-review`:**
- Organic sessions by landing page
- Bounce rate by acquisition source
- Trial page visits from organic traffic
- Session duration on content pages (proxy for engagement quality)

**Cost:** Free (GA4 standard API).

---

### PostHog — Product behaviour layer

**What it gives you:** What users do after they arrive — trial activation rate by source, feature usage, session depth inside the product, D7/D30 retention by acquisition channel, conversion funnel from trial to paid.

**Why it matters for the loop:** This closes the final link in the chain. SEO → GA4 → trial signup is visible. But whether that trial came from an r/alevel Reddit comment, an organic Google search for "9709 pure 1 revision", or a TikTok bio click — and whether *that specific acquisition type* produces students who actually activate and pay — is only visible in PostHog with proper UTM tagging.

**Already connected** to the OS. `posthog_marketing.py` module specced for P2.

**Key queries for the loop:**
- Activation rate (trial → first session) by acquisition source
- D7 retention by channel
- Trial-to-paid conversion by channel
- Most-used features among converting vs. churning users

---

## Tool Decisions

### Keep: Mangools / KWFinder (EUR29/mo annual)

Better than Ubersuggest for the current use case. KWFinder's KD scores are well-calibrated for low-competition, long-tail queries (KD 0-35) — exactly the target range for Phase 0-1. Cleaner interface, better SERP analysis per keyword.

**Deprecate when:** DataForSEO `keyword_researcher.py` module is built and validated (Phase 2). Until then, Mangools is the human-facing keyword research UI.

---

### Deprecate: Ubersuggest

Redundant with Mangools in the stack. KD accuracy is weaker at the low-competition end. Site audit feature (the one thing it has over Mangools) is covered by Ahrefs Webmaster Tools for free.

**If on a subscription:** Cancel now.
**If on a lifetime deal:** Keep as a secondary data point but don't rely on it. Deprioritise.

---

### Add (free): Ahrefs Webmaster Tools (AWT)

Fills the site audit gap that neither Mangools nor Ubersuggest covers adequately. Requires domain verification at search.google.com/search-console and ahrefs.com/webmaster-tools.

**What it gives you:**
- Full site audit (5,000 crawl credits/month): broken links, missing schema, crawl errors, Core Web Vitals, indexing issues, duplicate content
- Own-site backlink data: who links to you, anchor text, referring domains
- Own-site keyword data: which keywords you rank for, at what positions

**What it doesn't give you:** Competitor data (that's behind the paid Ahrefs wall). You get your own site only — which is all you need at Phase 0.

**Cost:** Free.

---

### Rejected: SEO-Stack.io

GSC + GA4 data warehouse with AI querying. Not the right tool for this build because:
1. Works only with first-party data (your own GSC/GA4) — DataForSEO gives far richer data including competitor SERP data and keyword universe.
2. The AI querying layer it sells is what Claude in the OS already does, better, with full context of the business strategy.
3. Extended data history (the main differentiator) is a Phase 3+ concern — DataForSEO provides historical SERP data independently if needed.
4. Founder actively listing the business for sale ($1M ask on TrustMRR) — operational continuity risk.
5. [VERIFY] — does not appear to have a confirmed MCP server despite being discussed as an integration option. Confirm directly before designing around it.

---

### Rejected: Ahrefs Lite ($129/mo) / SEMrush Pro ($140/mo)

Both are too expensive for the current stage and provide no features you need that the free/low-cost stack doesn't cover:
- Keyword research: DataForSEO (programmatic) + Mangools (UI) covers this
- Rank tracking: DataForSEO covers this at a fraction of the cost
- Site audit: Ahrefs Webmaster Tools (free) covers this
- Backlink analysis: Not a priority until Phase 2-3 when you have a content library worth auditing

**When to revisit:** Phase 3, if organic sessions exceed 2,000/month and you need deeper competitor backlink analysis or daily rank tracking at scale (50+ keywords, daily cadence). At that point Ahrefs Lite pays for itself.

---

## Phase-Based Activation

| Phase | Action | Why |
|---|---|---|
| Phase 0 (now) | Wire `gsc_analyzer.py` to GSC API | Articles start indexing — need impressions and crawl error data immediately |
| Phase 0 (now) | Set up Ahrefs Webmaster Tools | Audit existing ~8 articles for technical issues before publishing more |
| Phase 0 | Wire DataForSEO rank tracking | Track 20-30 target keywords from day one — baseline before first article live |
| Phase 1 (Aug) | Wire `ga4_analyzer.py` | Results Day brings first real traffic — need attribution data immediately |
| Phase 1 | Wire PostHog marketing integration | First trials — need to know which sources activate and convert |
| Phase 2 | Build `/strategy-review` command | Enough data across all four sources to synthesize meaningful decisions |
| Phase 2 | Deprecate Mangools | DataForSEO `keyword_researcher.py` validated and covering the same ground |

---

## The `/strategy-review` Command (Phase 2 Design)

The weekly synthesis command. Pulls from all four data sources, runs a set of built-in strategy checks, and outputs a decision memo — not a dashboard, a numbered action list.

**Data pulls (in order):**
1. GSC API: last 30 days query + page performance (impressions, clicks, CTR, position)
2. DataForSEO rank tracking: position changes week-over-week for tracked keyword set
3. GA4: organic session quality (engagement rate, bounce rate, goal completions by landing page)
4. PostHog: activation + conversion rates by acquisition source (UTM-tagged)
5. Syften/RedShip: high-engagement Reddit threads from the past 7 days (for content opportunity detection)

**Built-in strategy checks (runs every time, do not build as separate commands):**
- **Striking distance** — pages at positions 8-15, sorted by search volume × position gap × impressions (Strategy 1)
- **Content decay** — pages losing 3+ positions over 8 consecutive weeks (Strategy 3)
- **Intent mismatch flags** — pages where your content format diverges from the dominant SERP format for its target keyword (Strategy 11)
- **Reddit-to-article opportunities** — high-upvote Reddit threads with confirmed DataForSEO search volume and no GSC coverage (Strategy 15)

**Output structure (fixed format every run):**
1. KPI snapshot vs. current phase targets (north star + top 3 leading indicators)
2. Striking distance list (top 5 pages, sorted by opportunity size)
3. Decaying pages list (any pages flagged this week)
4. Content opportunity queue (Reddit signals + cluster gaps cross-referenced)
5. Intent mismatch flags (any pages flagged)
6. Channel allocation check (actual demand gen vs. acquisition split vs. exam calendar target)
7. **Numbered action list: 3-5 specific things to do this week** — this is the only output that matters

The action list is what makes this a decision tool rather than a reporting tool. Every run ends with something to do, not something to read.
