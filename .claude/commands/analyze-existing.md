---
name: analyze-existing
description: Audits a published article for freshness, SEO health, and rewrite opportunity. Accepts a local file path or a URL.
---

## Input

$ARGUMENTS

Expect: local file path OR a URL to a published page. Examples:
- `marketing/pipelines/published/cambridge-9709-integration-tips-2026-03-10.md`
- `https://exampilot.com/blog/cambridge-9709-pure-1-tips`

If not provided, ask.

## Execution

### Step 1: Read the article

**If local file path:** Read the file directly. Extract frontmatter fields (keyword, created date, slug, status).

**If URL given:** Fetch the page content:
```
WebFetch the URL, extract main content text, headings, and metadata
```
Infer slug from URL path. Note: date may not be available from URL alone — check page content for a publish date.

Extract from either source:
- Primary keyword (from H1 or frontmatter)
- Publish/created date (frontmatter `created:`, filename date pattern, or page content)
- URL slug
- All H2 headings
- Internal link count
- External link count
- Word count estimate
- FAQ presence and Q&A count
- Key Takeaways block presence

### Step 2: Freshness check

Calculate article age from publish date to today (2026-05-16).

Flag freshness status:
- **Fresh** (< 3 months): No freshness concern
- **Aging** (3-6 months): Monitor. Check for outdated exam session references.
- **Stale** (6-12 months): Flag. Exam board facts, grade boundaries, and statistics may be outdated.
- **Outdated** (> 12 months): High priority for refresh. Very likely contains stale exam references.

Scan article body for:
- Specific exam session references ("June 2024 paper", "2023 grade boundary") — flag all as [VERIFY]
- Statistics with years attached — flag as [VERIFY]
- Any mention of "upcoming" or "next" exam dates — flag if date is now past

### Step 3: Content gaps check

Based on the article's H2 structure and content, identify what it doesn't cover:

1. **Questions not answered:** Generate 5-8 student questions this keyword would trigger that the article doesn't address. Use these intent patterns:
   - "how do I..." (procedural)
   - "what is..." (definitional)
   - "why does..." (conceptual)
   - "is [ExamPilot] good for..." (comparison/product)
   - "how many marks..." (exam-specific)

2. **Competitor coverage gaps (manual):** For the primary keyword, consider what SaveMyExams, PapaCambridge, and Physics & Maths Tutor typically cover that this article may omit:
   - SaveMyExams: topic-by-topic revision notes, worked examples
   - PapaCambridge: past paper links, mark schemes
   - Physics & Maths Tutor: step-by-step solutions, common mistakes

3. **GEO gaps:** What would an AI need to cite this article that's currently missing?
   - Definition blocks for key concepts
   - Standalone Key Takeaways
   - Self-contained FAQ
   - Structured data signals (clear H2 questions)

### Step 4: SEO health check

Run same 6-dimension check as `/optimize`:

| Dimension | Result | Notes |
|---|---|---|
| Keyword placement | pass/partial/fail | |
| Structure | pass/partial/fail | |
| Internal links | pass/partial/fail | |
| External links | pass/partial/fail | |
| Meta | pass/partial/fail | |
| GEO compliance | pass/partial/fail | |

See `/optimize` command for full dimension criteria.

### Step 5: Voice check

Read `references/voice-house.md`.

Check the article against these voice markers:
- Short sentences (3-4 sentences per paragraph max)
- No em dashes (use commas or restructure)
- Bullet points over long paragraphs
- Casual but professional tone
- No fluff phrases ("it's important to note", "in conclusion", "in today's world")
- No B2B framing ("school administrators", "institutional", "departments")

Flag: **Voice aligned** / **Minor drift** / **Significant drift**

### Step 6: Recommendation

Based on all signals above, output one of:

**Keep as-is:** Article is fresh (<3 months), SEO passes all dimensions, no content gaps, voice aligned.

**Light refresh:** Article is 3-6 months old OR has 1-2 minor SEO issues OR minor voice drift. Suggest `/rewrite light`.

**Moderate rewrite:** Article is 6-12 months old OR has 3+ SEO issues OR significant content gaps OR voice drift. Suggest `/rewrite moderate`.

**Full rewrite:** Article is >12 months old OR fails 3+ SEO dimensions OR content is structurally misaligned with current strategy. Suggest `/rewrite complete`.

Explain the recommendation in 2-3 sentences. Lead with the primary reason.

### Step 7: Save analysis

Save to `marketing/pipelines/research/analysis-[slug]-YYYY-MM-DD.md`

```yaml
---
type: article-analysis
source: [file path or URL]
primary_keyword: ""
slug: ""
article_age: ""        # e.g. "7 months"
freshness_status: fresh | aging | stale | outdated
seo_health: pass | needs-work | fail
voice_alignment: aligned | minor-drift | significant-drift
recommendation: keep | light-refresh | moderate-rewrite | full-rewrite
analysis_date: YYYY-MM-DD
---

## Article Analysis: [Title]

### Freshness
[Age, stale flags found]

### Content Gaps
[Questions not answered, competitor coverage gaps, GEO gaps]

### SEO Health
[Dimension table]

### Voice Check
[Pass/flags found]

### Recommendation
[Recommendation + reason]

### Suggested command
`/rewrite [file path] [scope]`
```

### Step 8: Report

Show the recommendation and ask: "Ready to run `/rewrite [scope]`, or do you want to review the full analysis first?"
