---
name: research-keywords
description: Research and prioritize keywords for a given topic. Outputs a structured keyword brief to the topics pipeline.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## When `/research-keywords` runs

- After `/research-gaps` identifies a Tier 1 or Tier 2 gap worth pursuing
- Before `/write-article` — every article should have a keyword brief first
- When the user names a topic and wants to know whether it's worth writing about

Expects a seed topic or keyword. Examples:
- "cambridge 9709 pure 1 integration"
- "best app for a level maths revision"
- "edexcel WMA11 past papers"
- "how to pass cambridge 9709"

If no seed given, ask.

## Execution

### Step 1: Load strategy context

Fetch the wiki SEO strategy for keyword prioritization framework and URL architecture:

```bash
gh api repos/akhanaton/spyglass-wiki/contents/wiki/marketing/seo/seo-strategy.md --jq '.content' | base64 -d
```

Read `marketing/context/content-standards.md` for entity naming rules (full exam board names).
Read `marketing/references/geo-platform-guide.md` for content types that get cited most (comparison articles ~33%, definitive guides ~15%, original research ~12%) and platform-specific optimization priorities.

### Step 2: Build + price the keyword cluster (DataForSEO is connected)

DataForSEO is live (connections.md row 12, creds in `marketing/data_sources/.env`). The OS-native tool is `keyword_volume.py` — it both expands seeds and prices keywords. Use the two modes together:

**a. Expand the seed into a related-keyword cluster:**
```bash
python3 marketing/data_sources/modules/keyword_volume.py --seed "[seed keyword]" --limit 40
```
Returns distinct related keywords (permutations collapsed) with worldwide volume + difficulty. Good for head terms that have real keyword-database coverage.

**b. For niche international exam terms, expansion will be thin** (CIE 9709 long-tail barely exists in any single-country keyword DB). There, generate 10-15 candidate variations yourself (see Step 3 patterns) and price them directly:
```bash
python3 marketing/data_sources/modules/keyword_volume.py --keywords "9709 pure 1 integration questions" "..." --kd
```

**Always pull worldwide first** (the default). CIE 9709 and Edexcel IAL are international exams — a UK-only lens understates true demand by ~100x+ (e.g. "9709 syllabus" is 20/mo UK vs 3,600/mo worldwide). Add `--location pakistan` (or india/uae/malaysia/egypt) for a core-market cut when geo-targeting matters.

Treat a reported `0` as "below the planner's floor", not "no demand" — the Google Ads planner is blind to the informational long tail. **Always cross-reference with live GSC impressions** (`gsc_analyzer.py --dimension query`) — that is the truest demand signal for our long-tail terms, and it catches what the planner misses.

**If DataForSEO ever returns no data** (auth/credit issue): fall back to the manual SERP analysis in Step 3.

### Step 3: Manual SERP analysis guidance

Since DataForSEO may not be connected yet, provide structured research guidance:

1. **Primary keyword variations** — generate 10-15 variations of the seed keyword including:
   - Paper code specific ("9709 P1 [topic]", "WMA11 [topic]")
   - Question format ("how to [topic] cambridge 9709", "what is [topic] in pure maths")
   - Comparison ("9709 vs edexcel [topic]")
   - Resource-seeking ("best [topic] revision notes 9709")

2. **Estimated difficulty tier** based on wiki's KD targets:
   - Month 1 targets: KD ≤ 20 (paper code + topic)
   - Month 2 targets: KD ≤ 25 (long-tail informational)
   - Month 3 targets: KD 25-35 (pillar pages)

3. **SERP landscape assessment:**
   - Who currently ranks? (PapaCambridge, SaveMyExams, Physics & Maths Tutor, YouTube)
   - Are there featured snippets or AI Overviews for this query?
   - Content type that ranks (listicle, guide, video, forum thread)

4. **Content angle recommendation:**
   - What format fits this keyword? (blog article, comparison page, past paper guide)
   - Which audience segment? (cambridge-9709, edexcel-ial, resit)
   - Which funnel stage? (tofu, mofu, bofu)
   - Recommended URL based on wiki URL architecture

### Step 4: Output keyword brief

Save to `marketing/pipelines/topics/` with this structure:

```yaml
---
type: keyword-brief
primary_keyword: ""
secondary_keywords: []
estimated_kd: ""
target_segment: ""
funnel_stage: ""
content_type: ""     # blog-article | comparison-page | past-paper-guide | pillar-page
recommended_url: ""
status: researched
date: YYYY-MM-DD
---

## Keyword Cluster
[List of 10-15 keyword variations with estimated intent]

## SERP Landscape
[Who ranks, content types, featured snippets, AI Overviews]

## Content Recommendation
[Recommended angle, format, word count, key sections to cover]

## Internal Link Targets
[Which existing or planned pages to link to/from]
```

### Step 5: Review prompt

Show the brief and ask:
- "Does this keyword align with our current priority (Month 1/2/3)?"
- "Ready to write, or should we research more variations first?"
