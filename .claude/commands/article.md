---
name: article
description: Rigorous 4-step article pipeline for high-stakes content. SERP analysis → community research → article planning → section-by-section writing. More demanding than /write-article. Use for pillar content, competitive keywords, or featured snippet targets.
---

## Input

$ARGUMENTS

Expect: a primary keyword. Example: `cambridge a level maths integration by parts`.

If no keyword given, ask.

## Execution

### Step 1: SERP Analysis

Check `connections.md` for the DataForSEO connection status. If connected, use the DataForSEO module. If not, proceed with analytical inference from known SERP patterns.

Identify who ranks top-10 for this keyword. Pay close attention to:
- SaveMyExams
- PapaCambridge
- Physics & Maths Tutor
- Reddit threads
- YouTube results

Identify SERP features present for this keyword:
- Featured snippet (is there one? What format — definition, list, table, step-by-step?)
- AI Overview (is this keyword likely to trigger one?)
- People Also Ask (list the questions shown)
- Video carousel
- Image pack

Determine optimal word count from top 5 results. If top results average 1800 words, that is the floor — target 200-400 words more.

Identify 3+ content gaps: what does this keyword genuinely deserve that no current top-10 result provides? Examples:
- No worked example with mark scheme
- No exam-season urgency framing
- No coverage of common examiner traps
- No FAQ addressing the PAA questions
- No differentiation by exam board (Cambridge vs Edexcel)

Determine content format. Pick one:
- Step-by-step guide (how-to keyword)
- Worked example walkthrough (technique keyword)
- Comparison (vs keyword or "which is better")
- Definition + application (what is keyword)
- Exam strategy (how to revise / how to approach keyword)

Output a SERP brief:
```
## SERP Brief: [keyword]

**Top-10 ownership:** [who dominates and why]
**SERP features:** [list what's present]
**Optimal word count:** [target based on top 5 average + 200]
**Content format:** [chosen format and reason]
**Content gaps to address:**
1. [gap + why it matters]
2. [gap + why it matters]
3. [gap + why it matters]
```

### Step 2: Community Research (Reddit)

Check `connections.md` for the Reddit connection status. If connected, run `marketing/data_sources/modules/reddit_monitor.py`.

If not connected: draw on known patterns from r/alevel, r/6thForm, and r/CambridgeInternational to identify genuine student pain points for this topic.

Extract:
- Actual student language and phrasing (not textbook language)
- The most common mistake students make with this topic
- What confuses students most (where they get stuck)
- What resources they are currently using or recommending
- Any recurring frustrations about existing resources

Identify 5+ unique insights from community discussion to weave into the article. These should be specific — not generic observations like "students find this hard" but things like "students consistently confuse integration by parts with substitution when the integrand has a product that isn't obviously separable."

Output a community brief:
```
## Community Brief: [keyword]

**Student language samples:**
- "[actual phrasing students use]"
- "[actual phrasing students use]"

**Common mistakes:**
1. [specific mistake]
2. [specific mistake]

**What confuses them most:** [specific sticking point]

**Resources they currently use:** [list]

**5 insights to weave in:**
1. [specific insight]
2. [specific insight]
3. [specific insight]
4. [specific insight]
5. [specific insight]
```

### Step 3: Article Plan

Read these files in parallel:
- `marketing/templates/blog-article.md` — required structure
- `marketing/context/content-standards.md` — quality bar, GEO checklist, positioning rules
- `marketing/references/geo-platform-guide.md` — GEO optimization rules

Run `marketing/data_sources/modules/search_intent_analyzer.py` on the keyword if available, or classify manually using these rules:
- Starts with "how to" or "how do" → How-to intent
- Starts with "what is" or "what are" → Informational/definitional intent
- Contains "best", "top", "vs" → Comparison/navigational intent
- Contains "tips", "mistakes", "common" → Informational/advice intent
- Contains paper code (9709, WMA11) → Exam-specific informational intent

Run `marketing/data_sources/modules/article_planner.py` if available.

Build a section-by-section plan:

```
## Article Plan: [keyword]

**H1:** [primary keyword placed naturally, ≤60 chars, benefit-framed]
**Intent classification:** [type + reasoning]
**Word count target:** [from SERP brief]

**Key Takeaways block:**
- [takeaway 1 — specific and scannable]
- [takeaway 2]
- [takeaway 3]
- [takeaway 4 — optional]
- [takeaway 5 — optional]

**H2 sections:**

**H2: [title]**
Summary: [2-3 sentences — what this section covers and why it matters]
Content gap addressed: [which gap from SERP brief]
Word count target: [n words]

**H2: [title]**
[repeat for each section]

**FAQ section:**
- Q: [question from PAA or community research]
  A: [30-50 word direct answer]
- Q: [question]
  A: [answer]
- Q: [question]
  A: [answer]
- Q: [question]
  A: [answer]
[4+ Q&A minimum]

**Total word count target:** [sum of sections]
```

PAUSE. Show the plan to the user and ask: "Here's the article plan. Approve it as-is, or tell me what to adjust before I write."

Do not proceed to Step 4 until the user explicitly approves the plan.

### Step 4: Section-by-section writing

Only proceed after user approves the plan.

Read `references/voice-house.md` for voice and tone.

Write the article in this order. Do not write the full article at once — write each major block in sequence:

**Block 1: H1 + Introduction (150-200 words)**
- H1 must contain primary keyword
- First sentence answers the question directly (GEO-first)
- Second sentence establishes why this matters for their exam specifically
- No "in this article we will cover" or "let's dive in"
- Lead into the Key Takeaways block

**Block 2: Key Takeaways block**
- 3-5 bullet points
- Each point is scannable and complete on its own
- Primary keyword appears in at least one bullet

**Block 3: Each H2 section in order**
Write each H2 to its planned word count target. Per section:
- First 2 sentences answer the section question directly (extractable by AI Overviews)
- Include a worked example where appropriate (specific to Cambridge or Edexcel paper format)
- Weave in the relevant community insight (from Step 2 brief)
- UK English throughout

**Block 4: FAQ section**
4+ Q&A pairs. Requirements:
- Questions written in natural conversational language (how students actually ask, not keyword-stuffed)
- Each answer: 30-80 words, direct, no padding
- Pull questions from the People Also Ask list identified in Step 1 and from community research in Step 2

**Block 5: Conclusion (150 words)**
- Restate the core answer in a different framing (not a summary list)
- Next-step CTA: point to a specific ExamPilot practice feature
- Do not end with "good luck on your exams" or equivalents

**Requirements across all sections:**
- 2-3 mini-stories with specific names and outcomes (flag with [EDITOR FLAG: add mini-story] if you cannot verify — do not invent)
- 2-3 contextual CTAs placed at natural transition points (not forced)
- 3-5 internal links with descriptive anchor text
- 2-3 external authority links (Cambridge, Pearson, Ofqual, named research)
- Zero em-dashes — use commas, colons, or separate sentences
- No AI tells: no "it's worth noting", "delve into", "navigate", "seamlessly", "foster", "tapestry", "comprehensive guide to", "leverage" (verb)
- Flag all unverified exam board claims with [VERIFY]

**Post-write scrub pass:**
- No em-dashes remain
- No AI tell phrases remain
- UK English: practise (verb), practice (noun), organisation, recognise, colour
- No "AI tutor", "AI-powered", "revolutionary"
- Pricing exact if mentioned: EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr

**Run post-write agents in order:**
1. seo-optimizer
2. meta-creator
3. internal-linker
4. content-quality
5. editor (only if content-quality composite score ≥50)

**Quality gate:** Composite score ≥70 required to move to `marketing/pipelines/review/`. If below 70, surface the top 3 failing checks to the user and ask whether to fix inline or flag for human revision.

### Step 5: Save

Save to `marketing/pipelines/drafts/[slug]-YYYY-MM-DD.md`

YAML frontmatter:
```yaml
type: article
channel: seo
stage: tofu
target-segment: [student-cambridge | student-edexcel | resit-student — pick most specific]
status: drafted
keyword: [primary keyword]
created: YYYY-MM-DD
quality_score: [composite score from content-quality agent]
pipeline: article
```

### Step 6: Report

Show:
- SERP gaps addressed: [list which gaps the article covers]
- Word count: [actual]
- Quality score: [composite]/100
- [VERIFY] flags: [count]
- Community insights woven in: [count of the 5 identified]
- File saved to: [path]

Ask: "Review the draft at [path]. Resolve [X] [VERIFY] flags before moving to `marketing/pipelines/review/`."
