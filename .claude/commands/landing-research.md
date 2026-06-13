---
name: landing-research
description: Researches a landing page opportunity for ExamPilot's Sanity CMS. Outputs a content brief for topic hubs, comparison pages, and feature pages.
---

## Input

$ARGUMENTS

Expect: a keyword, topic, or page type. Examples:
- "cambridge 9709 integration" — topic hub page
- "examPilot vs savemyexams" — comparison page
- "adaptive practice feature" — feature page
- "/cambridge/9709-pure-1" — URL path to research

If not provided, ask: "What landing page do you want to research? (e.g. 'cambridge 9709 pure 1', 'ExamPilot vs SaveMyExams', or a target URL)"

## Execution

### Step 1: Classify page type

Based on the input, classify into one of four types:

**Topic hub** — e.g. "9709 Pure 1", "Edexcel WMA11":
- Aggregates all ExamPilot content for that exam paper
- TOFU/MOFU: student is looking for revision resources
- URL pattern: /cambridge/9709-pure-1, /edexcel/wma11

**Specific topic** — e.g. "integration by parts 9709", "WMA11 logarithms":
- Deep-dive into one technique or concept with practice
- TOFU: student is stuck on a specific topic
- URL pattern: /cambridge/9709-integration-by-parts, /blog/[topic-slug]

**Comparison** — e.g. "ExamPilot vs SaveMyExams", "best revision app cambridge 9709":
- Explicit comparison with named alternative or category
- MOFU/BOFU: student is evaluating options
- URL pattern: /blog/exampilot-vs-savemyexams

**Feature page** — e.g. "adaptive practice", "spaced repetition revision":
- Explains one ExamPilot feature through a student benefit lens
- MOFU/BOFU: student understands the problem, evaluating solutions
- URL pattern: /features/adaptive-practice

State: "Page type: [type]. Intent stage: [TOFU/MOFU/BOFU]. Target segment: [cambridge-9709 | edexcel-ial | resit | parent]."

### Step 2: Intent analysis

What is the visitor trying to accomplish when they land on this page?

- **Functional intent:** Find revision notes | Find past papers | Practice questions | Compare tools | Understand a concept
- **Emotional state:** Stressed before exam | Stuck on a topic | Evaluating options | Looking for efficiency
- **Next action wanted:** Start free trial | Read more | Download resource | Watch demo

Map to funnel stage:
- TOFU: visitor doesn't know about ExamPilot yet — don't lead with product
- MOFU: visitor is aware of the problem — lead with solution
- BOFU: visitor is comparing options — lead with differentiation

### Step 3: Check DataForSEO connection

Read `connections.md` and check if DataForSEO is connected.

DataForSEO is connected (row 12). Pull live volume + difficulty for the page's keyword cluster (worldwide default; add `--location <country>` for a market cut):
```bash
python3 marketing/data_sources/modules/keyword_volume.py --keywords "[page topic]" "[variation]" "..." --kd
```

If DataForSEO returns no data, proceed with manual competitive analysis.

### Step 4: Competitor analysis

For the target keyword/page type, analyze top 5 ranking pages from:
- SaveMyExams (savemyexams.com) — likely ranks for topic hub and revision queries
- PapaCambridge (papacambridge.com) — likely ranks for past paper and exam-specific queries
- Physics & Maths Tutor (physicsandmathstutor.com) — likely ranks for technique and worked solution queries

For each competitor page, identify:
- Headline / H1
- Primary CTA
- Number of content sections
- Word count (estimate)
- Trust signals used (student count, testimonials, logos)
- What they do well
- What's missing (ExamPilot's opening)

### Step 5: Content specification

Based on page type, define content scope:

**Topic hub page spec:**
- Word count: 1500-2500 words
- Sections: Introduction (what this paper covers), Topic breakdown (all sub-topics with links), How ExamPilot helps with this paper, Practice approach, FAQ
- CTAs: 3-4 CTAs — first above fold, after topic breakdown, after practice section
- Trust signals: ExamPilot's exam board specificity claim, student outcome [VERIFY]
- Sanity CMS note: Requires pre-write scaffold — run `/pre-write` for Sanity JSON before writing

**Specific topic page spec:**
- Word count: 1500-2500 words
- Sections: What is [topic], Step-by-step method, Common mistakes, Worked example, Practice with ExamPilot, FAQ
- CTAs: 2-3 CTAs — one after worked example, one at end
- Trust signals: Cambridge/Pearson alignment claim

**Comparison page spec:**
- Word count: 800-1500 words
- Sections: Quick verdict (ExamPilot wins for X if...), Feature comparison table, Deep dive on key differences, Who each is for, Pricing comparison, Final recommendation
- CTAs: 2 CTAs — after table, at end
- Pricing to include: ExamPilot EUR29/mo vs competitor pricing (if public — [VERIFY])
- Tone: Objective-sounding but ExamPilot-advantaged. No disparagement.
- Trust signals: Specific feature comparison (adaptive practice vs static notes)

**Feature page spec:**
- Word count: 800-1500 words
- Sections: What the feature does, Why it works (learning science basis), How students use it, Outcome (what improvement looks like), Try it free CTA
- CTAs: 2 CTAs — above fold + end
- Trust signals: Learning science basis (spaced repetition research) [VERIFY]

### Step 6: Headline and CTA recommendations

Generate 3 headline options for the page:

Option 1 (Specificity): "[Exam board] [Topic] — Practice until you can do it without thinking"
Option 2 (Outcome): "Go from stuck to confident on [Topic] — Cambridge 9709 style"
Option 3 (Urgency): "[Topic] in [paper code]: what the exam actually tests (and how to practice it)"

Adapt for the actual keyword — these are templates.

**Primary CTA recommendations:**
- For TOFU: "Start practising free" (not "Sign up")
- For MOFU: "See how it works" → demo or feature page
- For BOFU: "Try ExamPilot free — no credit card required"

**Trust signals to include above fold:**
- Exam board specificity ("Built for Cambridge 9709 and Edexcel IAL")
- Student-specific social proof [placeholder until available]
- Risk reversal ("Free trial, no credit card")

### Step 7: Save brief

Save to `marketing/pipelines/research/landing-[slug]-YYYY-MM-DD.md`

```yaml
---
type: landing-research
page_type: topic-hub | specific-topic | comparison | feature-page
keyword: ""
slug: ""
url_target: ""
intent_stage: tofu | mofu | bofu
target_segment: ""
word_count_target: ""
cta_count: 0
dataforseo_connected: true | false
competitors_analyzed: []
created: YYYY-MM-DD
---

## Landing Page Brief: [Page Title]

### Page Classification
[Type, intent, stage, segment]

### Intent Analysis
[What visitor wants to do + emotional state]

### Competitor Analysis
[Top 5 competitive pages: what they do, what's missing]

### Content Specification
[Sections, word count, CTAs, trust signals]

### Headline Options
1. [Option 1]
2. [Option 2]
3. [Option 3]

### Primary CTA
[Recommended CTA copy]

### Trust Signals to Include
[List]

### Recommended next step
`/pre-write [page type] "[keyword]"` — scaffold Sanity CMS structure
Then: `/landing-write [brief path]` — write the page content
```

### Step 8: Prompt

Show the brief summary and ask:
- "Research complete for [page type]: '[keyword]'."
- "Next: run `/pre-write` to scaffold the Sanity CMS structure, then write the page."
- "Or want to adjust the headline options or CTA first?"
