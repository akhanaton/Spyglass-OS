---
name: research-keywords
description: Research and prioritize keywords for a given topic. Outputs a structured keyword brief to the topics pipeline.
---

## Input

$ARGUMENTS

Expect: seed topic or keyword. Examples:
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

### Step 2: Check for DataForSEO connection

Read `connections.md` and check if DataForSEO (row 12) is connected.

**If connected:** Run keyword research via data module:
```bash
python3 marketing/data_sources/modules/keyword_researcher.py --seed "[keyword]" --location 2826 --language en
```

**If not connected:** Proceed with manual SERP analysis (Step 3).

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
