---
name: research-serp
description: Analyzes top-10 SERP results for a keyword to determine optimal content format, word count, and SERP features before writing.
---

## Input

$ARGUMENTS

Expect: a keyword or topic to analyze. Examples:
- "cambridge 9709 integration by parts"
- "how to pass edexcel WMA11"
- "best revision tool for a level maths"

If not provided, ask.

## Execution

### Step 1: Load content standards

Read `marketing/context/content-standards.md` for:
- Exam board entity naming rules (use full official names on first mention)
- Positioning rules (ExamPilot = "learning science tool", not "AI tutor")
- Competitor naming conventions

### Step 2: Check DataForSEO connection

Read `connections.md` and check if DataForSEO is connected.

**If connected:** Run SERP analysis:
```bash
python3 marketing/data_sources/modules/serp_analyzer.py --keyword "[keyword]" --location 2826 --language en --results 10
```
Use live data for steps below.

**If not connected:** Proceed with manual structured analysis (Step 3).

### Step 3: SERP analysis

Work through each element systematically. For each, provide your best assessment based on known SERP patterns for A-Level Maths keywords if live data is unavailable.

**3a. Content types ranking**

Identify which content types occupy the top 10 positions:
- Revision note / study guide
- Past paper / mark scheme page
- Worked example / solution walkthrough
- Video (YouTube embed or native)
- Forum / Reddit thread
- Tool / practice platform
- Comparison / review article
- Wikipedia or encyclopedia

State: "Top 3 content types for this keyword: [type 1], [type 2], [type 3]"

**3b. Who ranks**

Identify which domains likely rank for this keyword among:
- SaveMyExams (savemyexams.com)
- PapaCambridge (papacambridge.com)
- Physics & Maths Tutor (physicsandmathstutor.com)
- YouTube / youtube.com
- Reddit (reddit.com)
- Cambridge official (cambridgeinternational.org)
- Pearson official (pearsonqualifications.com)
- Other edtech tools

Note: ExamPilot's current domain authority is low — this affects realistic ranking timelines.

**3c. SERP features**

Identify which SERP features are likely present:
- Featured snippet (answer box)
- AI Overview (appears for many educational how-to queries — HIGH priority if yes)
- People Also Ask (PAA) box — list up to 5 PAA questions if identifiable
- Video carousel
- Image pack
- Knowledge panel
- Sitelinks

If AI Overview appears: flag prominently — GEO optimization is CRITICAL for this keyword.

**3d. Average word count**

Estimate average word count from top 5 results based on content type norms:
- Revision note pages: typically 800-1500 words
- Comprehensive guides: 2000-4000 words
- Past paper listing pages: 300-800 words (mostly links)
- Worked solution posts: 600-1200 words

State: "Estimated average word count (top 5): [X] words. Recommended target: [Y] words."

**3e. Content gap opportunities**

Based on top-ranking content, identify what is NOT well covered:
- Missing exam board specificity (generic maths vs Cambridge 9709 specific)
- No practice problems with mark scheme approach
- No GEO-optimized FAQ
- No ExamPilot integration angle (how a tool helps, not just notes)
- Missing recent exam session examples ([VERIFY] for current)
- No comparison of 9709 vs Edexcel IAL approach for the same topic

### Step 4: Output report

**Recommended content format:** [format based on what ranks]
**Recommended word count:** [X-Y words]
**Target SERP features:** [list, with GEO priority if AI Overview present]

**Content gaps to exploit:**
1. [Gap 1 — specific]
2. [Gap 2 — specific]
3. [Gap 3 — specific]

**Suggested H2 structure to beat current top result:**
```
H1: [Primary keyword — specific, exam-board-named]
H2: What is [concept]? (Cambridge 9709 context)
H2: [Topic] step-by-step: the method
H2: Common mistakes in [topic] (A Level Maths)
H2: Worked example: [9709 past paper context]
H2: How to practice [topic] effectively
H2: [Topic] FAQ
```
(Adapt to keyword — this is a starting template)

**AI Overview present:** Yes / No / Likely
- If yes: "GEO optimization is critical. Prioritize answer-first intro, Key Takeaways, and self-contained FAQ."

**Realistic timeline to rank:** [Estimate based on KD and ExamPilot's current domain authority]

### Step 5: Save report

Save to `marketing/pipelines/research/serp-[keyword-slug]-YYYY-MM-DD.md`

```yaml
---
type: serp-analysis
keyword: ""
keyword_slug: ""
dataforseo_connected: true | false
top_content_types: []
key_competitors_ranking: []
serp_features: []
ai_overview_present: true | false | likely
recommended_format: ""
recommended_word_count: ""
content_gaps: []
analysis_date: YYYY-MM-DD
---

## SERP Analysis: [Keyword]

### Who Ranks
[Competitor breakdown]

### Content Types
[What format dominates]

### SERP Features
[List with AI Overview flag]

### Content Gaps
[Numbered list of opportunities]

### Recommended H2 Structure
[H1/H2 outline]

### GEO Priority
[Yes/No + reasoning]
```

### Step 6: Prompt

Show summary and ask:
- "SERP analysis complete. AI Overview: [Yes/No]. Recommended format: [X] at [Y] words."
- "Ready to run `/research-keywords [keyword]` for a full keyword brief, or `/write-article` to start drafting?"
