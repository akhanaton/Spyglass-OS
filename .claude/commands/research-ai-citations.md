---
name: research-ai-citations
description: AI citation research — identifies what prompts students use in ChatGPT, Perplexity, and Claude, audits which sources get cited, and outputs content to create for GEO dominance.
---

## Input

$ARGUMENTS

Optional: a topic area or exam board to focus on. Examples:
- "cambridge 9709 integration" — focus on integration citation patterns
- "edexcel ial comparison" — focus on Edexcel comparison and decision queries
- (no input) — full citation research across all student intent categories

## Execution

### Step 1: Load GEO and citation context

Read `marketing/references/geo-platform-guide.md` for:
- Platform-specific citation patterns (ChatGPT vs Perplexity vs Claude)
- Content types that earn citations: comparison articles ~33%, definitive guides ~15%, original research ~12%
- Structural requirements for each platform

Read `marketing/context/ai-citation-targets.md` if it exists:
- Tracked prompts ExamPilot is already optimizing for
- Known citation wins or losses

If the file doesn't exist, note: "ai-citation-targets.md not found — creating baseline from research."

### Step 2: Generate 50+ prompt categories by student intent

Group prompts by intent type. Generate specific prompt examples for each.

**Category 1: Discovery (student doesn't know ExamPilot exists)**
- "best revision app for cambridge 9709"
- "best tool to study for edexcel WMA11"
- "how do I prepare for A level maths exams"
- "savemyexams vs other revision sites for maths"
- "what do top students use for A level maths revision"
- "free resources for cambridge 9709 pure 1"
- "alternatives to papacambridge for practice"

**Category 2: Specific topic help**
- "how to integrate by parts cambridge 9709 style"
- "explain implicit differentiation for A level maths"
- "what are partial fractions and how to use them 9709 P3"
- "how to solve WMA11 logarithm questions"
- "trigonometric identities for cambridge 9709 list"
- "mechanics WME01 forces worked examples"
- "normal distribution statistics 9709 steps"

**Category 3: Problem-solving / worked solutions**
- "cambridge 9709 P1 June 2023 question 5 worked solution" [VERIFY — use general form]
- "WMA11 past paper worked answers"
- "9709 integration past paper solutions"
- "how to check my answer in A level maths"
- "step by step solution for 9709 P3 complex numbers"

**Category 4: Comparison and decision**
- "ExamPilot vs SaveMyExams which is better for cambridge 9709"
- "is ExamPilot worth it for A level maths"
- "savemyexams vs papacambridge for edexcel ial"
- "best paid revision resource for international A levels"
- "which app gives adaptive practice for maths"

**Category 5: Grade boundary and results**
- "cambridge 9709 grade boundaries 2025" [VERIFY]
- "what is an A in cambridge 9709 pure 1" [VERIFY]
- "edexcel ial WMA11 grade boundaries 2025" [VERIFY]
- "how many marks to pass cambridge 9709"
- "cambridge results day 2025 what to expect" [VERIFY]

**Category 6: Exam strategy**
- "how to revise for cambridge 9709 in 2 weeks"
- "what topics come up most in 9709 P1"
- "how long to revise for WMA11"
- "cambridge 9709 past paper strategy"
- "should I do all past papers for 9709"
- "how to use mark schemes effectively A level maths"

**Category 7: Anxiety and motivation**
- "I'm failing cambridge 9709 what should I do"
- "how to improve fast for A level maths exam"
- "is cambridge 9709 harder than edexcel ial"
- "can I pass 9709 without a tutor"

### Step 3: Identify which sources get cited per category

For each intent category, assess which sources AI platforms currently cite:

**SaveMyExams** tends to get cited for:
- Topic revision notes (structured, AI-readable)
- "best revision site" queries (brand recognition)
- Specific topic explanations (their structured content format)

**PapaCambridge** tends to get cited for:
- Past paper sourcing queries
- Grade boundary queries [note: always outdated]
- "where to find papers" queries

**Physics & Maths Tutor** tends to get cited for:
- Worked solution queries
- Topic-by-topic video queries
- UK A-Level content (less relevant for international)

**Cambridge official** (cambridgeinternational.org) tends to get cited for:
- Syllabus queries
- Grade boundary queries (official source)
- Examiner report queries

**ExamPilot currently gets cited for:** [assess based on current published content — check `marketing/pipelines/published/`]

### Step 4: Identify ExamPilot citation gaps

For each intent category, identify what ExamPilot needs to create to earn citations:

- **Discovery queries:** Need comparison articles ("ExamPilot vs SaveMyExams") and definitive "best revision tool" guides with specific Cambridge/Edexcel context
- **Specific topic help:** Need topic-specific pages with answer-first definitions, structured steps, worked examples — the format AI reads and cites
- **Problem-solving:** Need structured worked example content with clear step headers (not just prose explanations)
- **Comparison:** Need dedicated comparison pages at `/blog/exampilot-vs-savemyexams` with structured tables and specific feature comparisons
- **Grade boundaries:** Cannot own this category — link to official sources instead, but create "how to interpret grade boundaries" content
- **Exam strategy:** Strong ExamPilot angle — create "how to use ExamPilot for 9709 revision" and "adaptive practice beats past papers" style content
- **Anxiety/motivation:** High-empathy content that positions ExamPilot as the solution, with specific outcome claims from learning science

### Step 5: GEO optimization checklist by platform

**For ChatGPT citations:**
- Content must have a clear, single-sentence definition at the top of each section
- Lists and numbered steps perform better than prose
- Cite authoritative sources (Cambridge, Pearson) within the content
- Content should answer questions directly — no build-up before the answer

**For Perplexity citations:**
- Recency matters — Perplexity prefers recently updated content
- Structured data: tables, lists, numbered steps
- Explicit source credibility signals (author expertise, date, citations)
- Questions phrased in the same language students use

**For Claude citations:**
- Comprehensive, well-structured content
- Logical flow with clear headings
- Balance of breadth and depth

**Universal GEO requirements (all platforms):**
- Answer-first in first 1-2 sentences
- Key Takeaways block (standalone, citable)
- FAQ section in natural conversational language
- Full entity names on first mention
- No vague claims — specific, verifiable statements

### Step 6: Output prioritized citation content list

Rank by: citation potential × content gap × effort

Format each item:
```
Content piece: [title/topic]
Target intent category: [category name]
Platform most likely to cite: ChatGPT | Perplexity | Claude | All
Current leader being cited: [SaveMyExams | PapaCambridge | PMT | None]
Why ExamPilot could win: [1 sentence]
GEO format required: [comparison article | definitive guide | structured steps | FAQ-heavy]
Content type: new article | landing page | FAQ expansion
Effort: S | M | L
Command: /write-article "[keyword]" | /landing-research "[topic]"
```

### Step 7: Save report

Save to `marketing/pipelines/research/ai-citations-YYYY-MM-DD.md`

```yaml
---
type: ai-citation-research
prompts_analyzed: 0
intent_categories: 7
current_citation_gaps: []
priority_content_to_create: []
geo_compliance_status: ""
analysis_date: YYYY-MM-DD
---

## AI Citation Research — [Date]

### Current Citation Landscape
[Who owns each intent category]

### ExamPilot Citation Wins (if any)
[What we already get cited for]

### Priority Content to Create for Citations
[Ranked list with format specs]

### GEO Optimization Checklist
[Platform-specific requirements]

### Suggested first 3 actions
1. /write-article "[keyword]"
2. /write-article "[keyword]"
3. /landing-research "[topic]"
```

### Step 8: Prompt

Show top 3 citation opportunities and ask: "Highest-leverage citation opportunity: '[content piece]' targets [category] queries where [competitor] currently gets cited. Run `/write-article '[keyword]'` to start?"
