---
name: write-article
description: Write a full SEO blog article (2000-3000 words) for ExamPilot. Follows the blog-article template with GEO optimization, FAQ schema, and [VERIFY] flags for human review. Trigger on "write an article about", "draft a blog post", "write SEO content for", or when a research brief exists in marketing/pipelines/research/. One run = one draft saved to marketing/pipelines/drafts/.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Writes a complete, publish-ready SEO blog article for ExamPilot, then immediately runs four post-write agents (SEO, meta, internal links, quality). The draft lands in `marketing/pipelines/drafts/` with a quality score and a list of issues to resolve before human review.

**Bike Method Phase 1:** Every draft requires human review. All [VERIFY] flags must be resolved before the article moves to `marketing/pipelines/review/`. Do not auto-publish.

## When `/write-article` runs

- A research brief exists in `marketing/pipelines/research/`
- The user asks to write an article on a specific topic or keyword
- Following a `/research-keywords` run that produced a topic brief

## Context files — read at session start

Before writing a single word, load all of these into context:

```bash
# 1. Brand voice and tone
cat references/voice-house.md

# 2. Content standards and guardrails
cat marketing/context/content-standards.md

# 3. GEO and AI search optimization
cat marketing/references/geo-platform-guide.md

# 4. Audience segments
cat marketing/context/audience-segments.md

# 5. Blog article template and checklists
cat marketing/templates/blog-article.md

# 6. Channel playbooks (SEO section)
cat marketing/context/channel-playbooks.md
```

If a research brief was provided, also read it:
```bash
cat marketing/pipelines/research/{brief-filename}.md
```

Do not skip any of these reads. The article quality depends on the full context.

## Execution — six steps

### Step 1 — Pre-write confirmation

Extract or confirm these five parameters before writing:

| Parameter | Source | Example |
|---|---|---|
| Primary keyword | Research brief or user input | "Cambridge 9709 Pure 1 integration" |
| Target segment | `audience-segments.md` | cambridge-9709 |
| Funnel stage | Research brief or user input | tofu |
| Content type | Determine from brief | standard blog post |
| Target word count | Content type table in `voice-house.md` | 2000-2500 |

Show a one-line pre-write summary and ask: *"Does this look right before I write?"*

Do not proceed until confirmed.

---

### Step 2 — Write the article

Follow this structure exactly. Every rule below is mandatory unless marked optional.

#### Opening: Direct Answer First (GEO — non-negotiable)

The first 1-2 sentences of the article must directly answer the target query. AI search systems pull from the top of the page. Do not bury the answer.

**Pattern:**
> [Direct answer to the query in one sentence]. [One sentence of supporting context or qualifier].

Then the hook. Choose exactly one hook type:

| Hook Type | When to use | Pattern |
|---|---|---|
| Specific Scenario | Emotional connection, student situations | "When [Name] opened their 9709 results in August, the first thing they noticed was..." |
| Surprising Statistic | Data-driven topics | "[X]% of students revising for Cambridge 9709 make the same mistake on integration questions." |
| Counterintuitive Claim | Challenging assumptions | "The revision approach that feels most productive is usually the least effective." |
| Bold Statement | Confident takes | "Past paper grinding alone will not get you an A* on 9709 Paper 1." |
| Provocative Question | Assumption-checking | "What if the way you've been practising integration is actually reinforcing the wrong approach?" |

After the hook, apply the **APP Formula**:
- **Agree**: Acknowledge something the reader already feels or believes
- **Promise**: State exactly what they will learn or be able to do
- **Preview**: Brief overview of what's coming (can be a mini table of contents for longer articles)

Include the primary keyword within the first 100 words.

#### Key Takeaways Block (required, immediately after introduction)

```markdown
> **Key Takeaways**
> - [Specific finding or recommendation — include a number or named outcome]
> - [Specific finding or recommendation]
> - [Specific finding or recommendation]
> - [Optional fourth point if needed]
```

Rules:
- 3-4 bullet points
- Each is a standalone claim with specifics — not a teaser or table of contents entry
- Written after the full article body is drafted (so the takeaways are accurate)

#### Main Body (4-7 H2 sections)

**Every H2 section must open with a direct, extractable answer in the first 2-3 sentences.** This is the GEO answer-first requirement — AI systems extract passages by section. If the first sentence of a section doesn't answer the section's implied question, rewrite it.

Per-section rules:
- Short paragraphs (2-4 sentences maximum)
- Bold key concepts on first appearance
- Use numbered lists for sequential steps, bulleted lists for non-sequential points
- Use comparison tables for feature comparisons or technique comparisons
- `[VERIFY]` flag on any exam board fact, paper code, date, mark scheme claim, or statistic you are not 100% certain of

**Mini-Stories — 2-3 required per article**

Research shows facts wrapped in stories are 22x more memorable. Every article must include 2-3 mini-scenarios, each with:
- A specific person (use names: "Maya", "James", "a student in Lahore")
- A concrete situation with details (topic, exam sitting, score, time pressure)
- A clear outcome that illustrates the point

Placement:
- One in or near the introduction (hook)
- One in the middle sections (re-engage skimmers)
- One near the conclusion (reinforce the main point)

Length: 50-150 words each.

**Contextual CTAs — 2-3 required per article**

| Location | CTA Type | Example |
|---|---|---|
| After first major value section (within 500 words) | Soft (learn more) | "Curious how ExamPilot maps your 9709 knowledge gaps? [See how it works →]" |
| After proof/comparison section | Medium (try it) | "**Ready to find your actual weak spots?** Join the waitlist — no credit card needed." |
| End of article | Strong (convert) | "**[Join the ExamPilot Waitlist →]**" |

CTA rules:
- Make each CTA contextual to the section it appears in
- Vary format: inline text, bold callout, button-style
- Never use generic "Click here" text
- No more than 3 CTAs total
- Use "Join the waitlist" or "Check your exam readiness" pre-launch; "Try ExamPilot free" post-launch

#### GEO Content Patterns

Use these structural blocks throughout the article to maximize AI citation likelihood:

**Definition Block** (for "What is X?" sections):
```markdown
## What is [Term]?

[Term] is [1-sentence definition]. [1-2 sentences expanded]. [Why it matters for A-Level students].
```

**Step-by-Step Block** (for "How to X" sections):
```markdown
## How to [Action]

[1-sentence overview]

1. **[Step]**: [Clear action in 1-2 sentences]
2. **[Step]**: [Clear action in 1-2 sentences]
```

**Evidence Sandwich Block** (for credibility):
```markdown
[Claim].

Evidence:
- [Data point with source and year]
- [Data point with source and year]

[Concluding insight].
```

#### FAQ Section (required — minimum 4 Q&A pairs)

Write questions in the natural language students actually type into ChatGPT or Perplexity. Not SEO-speak.

Good: *"How many past papers should I do for Cambridge 9709 Pure 1?"*
Bad: *"What is the optimal past paper strategy for 9709?"*

Each answer must be complete without reading the rest of the article. Aim for 50-100 words per answer. These become FAQPage schema.

#### Conclusion (150-200 words)

- Recap 3-5 key points (not padding — the actual takeaways)
- Provide one clear next step
- Final CTA
- End on forward-looking note (exam outcome, grade target)

---

### Step 3 — Apply guardrails and scrub

After writing, before saving, apply these in sequence:

**ExamPilot positioning check:**
- No "AI tutor", "AI-powered", "AI wrapper", "game-changing", "revolutionary"
- Use: "learning science", "spaced repetition", "active recall", "exam readiness", "adaptive practice"
- Product name is always "ExamPilot" (one word, capital E and P)
- Feature names: "Ask Sparky", "Smart Review", "Exam Readiness Index (ERI)", "Question DNA" — all capitalised
- Exam board: "Cambridge International AS & A Level Mathematics 9709" on first mention, "Cambridge 9709" thereafter
- No B2B school/institution messaging. Consumer only.
- Pricing only in EUR: EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr. Never GBP or USD.

**Scrub pass:**
- Replace all em-dashes (—) with contextually appropriate punctuation: comma, semicolon, or period
- Remove generic filler phrases: "in today's world", "it's no secret that", "at the end of the day", "needless to say", "in conclusion" (as an opener), "leverage" (as a verb in student-facing content)
- UK English throughout: colour, analyse, organise, practise (verb)/practice (noun)
- Exclamation marks: maximum one per article
- Ellipsis: remove from published content

**[VERIFY] flag check:**
- Every exam board fact, paper code, mark scheme detail, official date, or external statistic should carry [VERIFY] if not sourced directly from the research brief
- Do not fabricate pass rates, topic frequencies, or CIE/Edexcel policy details

---

### Step 4 — Run post-write agents

After saving the draft, run these four agents sequentially. Each produces a findings block appended to the same draft file under a `## Post-Write Analysis` separator, or saved as a sidecar file at the same path with a `-analysis` suffix.

**Agent 1 — SEO Optimizer** (see `agents/seo-optimizer.md`)
- Keyword density and placement audit
- Heading structure check
- Internal and external link requirements

**Agent 2 — Meta Creator** (see `agents/meta-creator.md`)
- Generate 3 meta title options (50-60 characters)
- Generate 3 meta description options (150-160 characters)
- Recommend the best option with reasoning

**Agent 3 — Internal Linker** (see `agents/internal-linker.md`)
- Identify 3-5 internal link opportunities in the draft
- Suggest anchor text and target pages

**Agent 4 — Content Quality** (see `agents/content-quality.md`)
- Score the draft across 5 dimensions (target ≥70 composite)
- List the top 3-5 fixes ranked by impact
- Route recommendation: ready for review, or needs revision first

---

### Step 5 — Quality gate

Score the draft using the Python scorer when available; otherwise fall back to the inline content-quality agent.

**Primary: Python scorer**
```bash
python3 marketing/data_sources/modules/content_scorer.py marketing/pipelines/drafts/[filename].md
```
Requires `textstat` (`pip install textstat`). Produces a 5-dimension breakdown with priority fixes.

**Fallback: inline agent**
If the Python scorer is unavailable or errors, run the Content Quality agent (see `agents/content-quality.md`) and use its composite score.

Apply the same threshold logic from both paths:

- **Score ≥70**: Save to `marketing/pipelines/drafts/` — ready for human review
- **Score 50-69**: Apply the top 3 fixes from the scorer inline, re-score, then save
- **Score <50**: Save to `marketing/pipelines/drafts/` with a `_NEEDS_REVISION` prefix and a note block explaining what failed

Do not run more than one revision loop. If still below 70 after one revision pass, save with the prefix and surface the issues clearly.

---

### Step 6 — Save and report

**File path:** `marketing/pipelines/drafts/[topic-slug]-YYYY-MM-DD.md`

**Frontmatter** (from `marketing/templates/blog-article.md`):
```yaml
---
type: blog-article
title: ""
meta_title: ""
meta_description: ""
primary_keyword: ""
secondary_keywords: []
target_segment: ""
funnel_stage: ""
url_slug: "/blog/[slug]"
word_count_target: 2500
author: "Enitan Williams"
status: draft
date: YYYY-MM-DD
---
```

**One-screen close:**
```
Draft saved: marketing/pipelines/drafts/[filename]
Word count: [n] words
Quality score: [n]/100
Agents run: SEO optimizer ✓ | Meta creator ✓ | Internal linker ✓ | Quality analysis ✓
Issues to resolve before review:
  - [VERIFY] flags: [count]
  - Quality fixes: [top 1-3]
  - [Any other blocking issues]

Next step: Human review → resolve [VERIFY] flags → move to marketing/pipelines/review/
```

## What this skill does NOT do

- Does not auto-publish. Every draft requires human review.
- Does not resolve [VERIFY] flags — those require human fact-checking against official sources.
- Does not write for Edexcel IAL until Phase 1 (Cambridge 9709 content only at launch).
- Does not write topic pages (Sanity-structured content). Those are a separate pipeline.

## Phase advancement guide

| Phase | What changes |
|---|---|
| **1 (now)** | Full human review on every draft. All [VERIFY] flags resolved before moving to review/. Python scorer available in `marketing/data_sources/modules/content_scorer.py`. |
| **2** | Auto-apply top quality fixes before saving. High-confidence article types go directly to review/ queue. |
| **3** | Add DataForSEO SERP analysis to pre-write. Python scorer runs automatically pre-save, no manual trigger. |
