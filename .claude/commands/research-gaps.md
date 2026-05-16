---
name: research-gaps
description: Identifies keywords that competitors rank for but ExamPilot doesn't. Produces tiered gap opportunities.
---

## Input

$ARGUMENTS

Optional: a specific competitor to focus on, or a topic area to narrow gaps. Examples:
- "savemyexams" — focus gap analysis on SaveMyExams
- "integration" — find integration-related gaps only
- (no input) — run full gap analysis across all three competitors

## Execution

### Step 1: Load competitor reference

Read `marketing/context/competitor-analysis.md` for:
- Competitor URLs and known content categories
- ExamPilot's current positioning vs each competitor

If the file doesn't exist, use these known competitor profiles:
- **SaveMyExams** (savemyexams.com): topic-by-topic revision notes, A-Level Maths coverage by module, exam board aligned (Cambridge + Edexcel + OCR)
- **PapaCambridge** (papacambridge.com): past papers, mark schemes, examiner reports — Cambridge International primary
- **Physics & Maths Tutor** (physicsandmathstutor.com): worked solutions, video walkthroughs, notes and worksheets, UK A-Level focus

### Step 2: Read ExamPilot's current published content

```bash
ls marketing/pipelines/published/
ls marketing/pipelines/topics/
```

Read each file's frontmatter (`keyword:` and `primary_keyword:` fields) to build a list of keywords ExamPilot already targets. Also note any topic files in `topics/` that are planned but not published.

Current coverage = published keywords + planned (in-topics) keywords.

### Step 3: Check DataForSEO connection

Read `connections.md` and check if DataForSEO is connected.

**If connected:** Run competitor gap analysis:
```bash
python3 marketing/data_sources/modules/competitor_gap_analyzer.py \
  --competitors "savemyexams.com,papacambridge.com,physicsandmathstutor.com" \
  --location 2826 --language en
```

**If not connected:** Run manual gap analysis (Step 4).

### Step 4: Manual gap analysis

For each of the three competitors, systematically identify content categories ExamPilot doesn't cover. Work through ExamPilot's exam board scope:

**Cambridge 9709 gaps (CAIE):**
- Pure Mathematics 1 (P1): functions, coordinate geometry, trigonometry, series, differentiation, integration
- Pure Mathematics 3 (P3): algebra, logarithms, trigonometry, differentiation, integration, vectors, complex numbers, numerical methods, differential equations
- Statistics 1 (S1): data representation, probability, discrete random variables, normal distribution
- Statistics 2 (S2): Poisson distribution, continuous random variables, sampling, hypothesis testing
- Mechanics 1 (M1): forces, kinematics, Newton's laws, energy and momentum

**Edexcel IAL gaps:**
- WMA11 (Pure 1): algebra, coordinate geometry, calculus basics
- WMA12 (Pure 2): further algebra, logarithms, trigonometry, calculus
- WST01 (Statistics 1): probability, distributions, hypothesis testing
- WME01 (Mechanics 1): kinematics, forces, dynamics

**Cross-board keyword gaps:**
- "how to revise [topic] a level maths"
- "[topic] past paper questions and answers"
- "common mistakes [topic] a level"
- "examPilot vs [competitor]" (comparison pages)
- "[exam board] grade boundaries [year]" [VERIFY]
- "a level maths [topic] worked examples"

For each topic gap, assess:
- Is this a keyword SaveMyExams ranks for? (likely yes for most revision notes)
- Is this a keyword PapaCambridge ranks for? (likely yes for past paper queries)
- Is this a keyword Physics & Maths Tutor ranks for? (likely yes for worked solutions)
- Does ExamPilot have any content for this? (check current coverage list from Step 2)

### Step 5: Cluster gaps into opportunity tiers

**Tier 1 — High priority (ship within 2 weeks):**
- Estimated KD ≤ 20 (paper-code-specific, long-tail)
- High student intent (topic + 9709/WMA11 + technique)
- Not covered by ExamPilot at all
- Examples: "9709 P1 trigonometry worked examples", "WMA11 differentiation common mistakes"

**Tier 2 — Medium priority (ship within 4-6 weeks):**
- Estimated KD 20-35
- High volume but competitive
- ExamPilot has adjacent content but not this exact angle
- Examples: "cambridge 9709 past papers", "edexcel ial statistics revision"

**Tier 3 — Low priority / backlog:**
- Estimated KD 35+
- Broad, high-competition terms
- Long-term authority play
- Examples: "a level maths revision", "best maths revision app"

### Step 6: Format output

For each gap, provide:
```
Keyword: [keyword]
Tier: 1 | 2 | 3
Competitor(s) ranking: SaveMyExams | PapaCambridge | PMT
Content type: revision-notes | worked-examples | past-paper | comparison | guide
Effort estimate: [S=1-2hrs | M=3-5hrs | L=6-8hrs]
Suggested command: /research-serp "[keyword]" → /write-article
```

### Step 7: Save report

Save to `marketing/pipelines/research/gaps-YYYY-MM-DD.md`

```yaml
---
type: gap-analysis
dataforseo_connected: true | false
competitors_analyzed: [savemyexams, papacambridge, physicsandmathstutor]
gaps_found: [total count]
tier_1_count: ""
tier_2_count: ""
tier_3_count: ""
analysis_date: YYYY-MM-DD
---

## Competitor Gap Analysis — [Date]

### ExamPilot Current Coverage
[List of published + planned keywords]

### Tier 1 Gaps — Ship Now
[Gap entries]

### Tier 2 Gaps — This Month
[Gap entries]

### Tier 3 Gaps — Backlog
[Gap entries]

### Recommended first actions
1. `/research-serp "[top Tier 1 keyword]"`
2. `/research-serp "[second Tier 1 keyword]"`
3. `/research-keywords "[top Tier 2 keyword]"`
```

### Step 8: Prompt

Show tier summary counts and ask: "Found [X] Tier 1 gaps, [Y] Tier 2, [Z] Tier 3. Which gap should we attack first? I can run `/research-serp` on any of these."
