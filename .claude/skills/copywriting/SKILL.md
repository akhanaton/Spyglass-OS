---
name: copywriting
description: Write conversion-focused web copy for ExamPilot's Sanity CMS pages — homepage, pricing, feature pages, topic hubs, and comparison pages. Applies marketing psychology and ExamPilot's brand voice.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Writes web copy for ExamPilot's Sanity CMS pages: homepages, feature pages, pricing pages, topic hub pages, and comparison pages. This is conversion copy, not SEO blog content. Where `/write-article` produces long-form educational content, `/copywriting` produces tight, benefit-led copy for pages that need to convert visitors into trial signups or paid subscribers.

**Bike Method Phase 1:** All copy requires human review before it goes anywhere near the CMS. This skill produces a draft and stops. The user moves it forward.

## When `/copywriting` runs

- Building or updating a new Sanity CMS page
- Existing copy needs a refresh or improvement
- User asks to write a homepage, pricing page, feature page, topic hub, or comparison page
- Pre-launch page build

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/audience-segments.md
cat marketing/references/copy-frameworks.md
cat marketing/context/content-standards.md
```

## Execution — five steps

### Step 1 — Pre-write confirmation

Identify these four parameters before writing a single word:

| Parameter | Source | Example |
|---|---|---|
| Page type | User input | pricing |
| Goal | User input | convert free trial users to paid |
| Target segment | `audience-segments.md` | cambridge-9709 student |
| Existing copy to improve | User input (optional) | paste existing text, or "none" |

Show a one-line summary and ask: *"Does this look right before I write?"*

Do not proceed until confirmed.

---

### Step 2 — Write by page type

Apply the correct module below for the confirmed page type.

---

#### Homepage / Hero section

The hero is the most important copy on the site. Every word earns its place.

**Structure:**
1. **Headline** — benefit-driven, primary keyword, ≤60 characters. No full stops. Lead with the outcome students want.
2. **Subheadline** — expands the headline with specificity. Name the exam board and paper. ≤100 characters.
3. **Social proof line** — "[X] students practising with ExamPilot" or exam-board-specific. Do not fabricate numbers — use [VERIFY] if uncertain.
4. **Primary CTA button** — "Start Practising Free" (pre-launch: "Join the Waitlist"). Never "Sign Up" or "Register".
5. **Secondary CTA** — "See how it works" (links to feature section or product demo).

**Headline formulas (choose one, adapt):**
- "[Outcome] for [Specific Audience]" → "Pass Cambridge 9709 With Confidence"
- "Stop [Pain]. Start [Gain]." → "Stop Guessing Your Gaps. Start Knowing."
- "[Specificity signal] + [benefit]" → "Built for 9709. Every Question. Every Topic."
- "[Quantified outcome] [timeframe]" → "Know Your Exact Weak Topics in 10 Minutes"

**What NOT to write in the hero:**
- Feature lists (wrong place — that's the feature section)
- Vague claims ("the best", "the most powerful", "revolutionary")
- Anything about AI technology — focus on outcomes for students
- Generic educational language that could apply to any product

---

#### Pricing page copy

Pricing pages fail when they list features without addressing the real objection: "is this worth it?"

**Structure:**
1. **Page headline** — frame around value, not cost. Example: "Revision that pays off" or "Your exam prep, sorted."
2. **Anchor plan** — show the annual plan (EUR144/yr = EUR12/mo) as the primary option. This is the anchor.
3. **Plan options table** — all four tiers:

| Plan | Price | Per month equivalent |
|------|-------|----------------------|
| Monthly | EUR29/mo | EUR29/mo |
| Quarterly | EUR69/3mo | EUR23/mo |
| Semi-annual | EUR96/6mo | EUR16/mo |
| Annual | EUR144/yr | EUR12/mo |

4. **Value framing** — compare to tutoring cost in copy near the pricing table:
   "One session with a maths tutor costs EUR30-60. ExamPilot's annual plan is the same as two sessions — for a full year of daily practice."

5. **Risk reversal section** — answer "what if it doesn't work for me?":
   - Free trial details (what's included, how long)
   - Cancellation policy — easy, no penalty
   - What happens to their data if they cancel

6. **Pricing FAQ** (minimum 4 questions):
   - Do I need to pay upfront for the annual plan?
   - Can I switch plans later?
   - What happens when my trial ends?
   - Is VAT included in the price?

7. **Final CTA** — "Start your free trial" above the fold and at the bottom of the page.

**Pricing rules (non-negotiable):**
- EUR only. Never GBP, USD, or any other currency.
- Prices exactly: EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr.
- No "from" pricing. Show all tiers.

---

#### Feature page copy

Feature pages need to answer: "What does this actually do for me?"

**Structure per feature:**
1. **Feature headline** — lead with the outcome ("Know exactly where your gaps are"), not the feature name ("AI-powered diagnostics").
2. **3-part body:**
   - **Problem**: what the student experiences without this feature (1-2 sentences)
   - **Solution**: what ExamPilot does and how (2-3 sentences, specific, no jargon)
   - **Proof**: what changes as a result (1-2 sentences — use [VERIFY] if numbers are uncertain)
3. **Feature CTA** — soft: "See it in action" or "Try this feature free"

**ExamPilot feature names (always use these exact names, capitalised):**
- Ask Sparky
- Smart Review
- Exam Readiness Index (ERI)
- Question DNA

**Language rules:**
- "Adaptive practice" not "AI-powered learning"
- "Learning science" not "AI tutor"
- "Spaced repetition" and "active recall" are acceptable technical terms — they build credibility with students who know what they mean
- "Knowledge State" (capitalised) when referring to the user's topic map

---

#### Topic hub page (e.g. Cambridge 9709 Pure 1)

Topic hub pages serve a dual purpose: they help students navigate ExamPilot's content for a specific paper, and they rank for paper-code searches.

**Structure:**
1. **SEO heading** — include the paper code and full exam board name:
   "Cambridge International AS & A Level Mathematics 9709 Pure 1 (Paper 1)"
2. **What you'll find here** — 2-3 sentences. Name the topics covered (refer to the 9709 syllabus). Mention that questions are mapped to the specification.
3. **Topic list** — bulleted list of major topics in Pure 1: Functions, Coordinate geometry, Trigonometry, Differentiation, Integration, Binomial expansion, Series. Mark which are live on ExamPilot and which are "coming soon" ([VERIFY] exact availability).
4. **Social proof** — "Students preparing for 9709 Paper 1 use ExamPilot to [specific outcome]." Do not fabricate numbers. Use [VERIFY].
5. **CTA** — "Start a practice session on [topic]" — link to the specific practice session if the URL exists; otherwise use the main product CTA.

---

#### Comparison page (ExamPilot vs SaveMyExams)

Comparison pages work best when they are honest. Readers arrive suspicious of bias. Lead with fairness.

**Structure:**
1. **Headline** — neutral framing: "ExamPilot vs SaveMyExams: Which is right for you?"
2. **Opening paragraph** — acknowledge SaveMyExams' strengths first. This builds trust: "SaveMyExams has excellent topic summaries and past paper solutions. If you want static revision notes, it's a strong choice."
3. **The core difference** — explain what ExamPilot does differently in 2-3 sentences:
   "ExamPilot is an active practice tool, not a notes repository. It identifies which topics you don't actually know yet, then drills exactly those — using spaced repetition to make the knowledge stick."
4. **Comparison table** — feature by feature:

| Feature | ExamPilot | SaveMyExams |
|---------|-----------|-------------|
| Adaptive practice | Yes | No |
| Spaced repetition | Yes | No |
| Topic-by-topic knowledge mapping | Yes | No |
| Instant answer feedback | Yes | Partial |
| Past paper solutions | No | Yes |
| Revision notes | No | Yes |
| Cambridge 9709 specific | Yes | Partial |
| Edexcel IAL specific | Yes | Partial |
| Price | EUR12/mo (annual) | Free / Premium |

Note: Verify all competitor feature claims with [VERIFY] — do not publish inaccurate competitor comparisons.

5. **"Choose ExamPilot if..."** — 3-4 bullet points of specific situations where ExamPilot is the right call.
6. **"Choose SaveMyExams if..."** — 2-3 bullet points. Be honest. Don't force a recommendation.
7. **CTA** — "Try ExamPilot free for [X] days" — soft sell, not a hard close.

---

### Step 3 — Apply guardrails and scrub

After writing, before presenting the draft, apply these in sequence:

**Banned words and phrases — remove every instance:**
- "leverage", "optimize", "synergy", "streamline", "comprehensive", "game-changing", "revolutionary", "world-class", "best-in-class", "robust", "cutting-edge", "innovative", "empower"
- "AI tutor", "AI-powered", "AI wrapper"
- "Sign up" as a CTA (use "Start Practising Free", "Join the Waitlist", or "Try ExamPilot Free")

**Positioning check:**
- ExamPilot = "learning science tool", "adaptive practice", "spaced repetition platform"
- No B2B or school/institution messaging
- Pricing in EUR only — if any pricing appears, verify against the pricing rules above
- Product feature names match the official list (Ask Sparky, Smart Review, ERI, Question DNA)

**Voice check (from `references/voice-house.md`):**
- Short sentences. Under 20 words where possible.
- Bullet points over paragraphs for lists
- No em dashes — use commas, semicolons, or full stops
- UK English: colour, optimise, practise (verb) / practice (noun), programme

**[VERIFY] check:**
- Any statistic, student outcome claim, competitor feature claim, or product availability claim that cannot be confirmed from the research brief or known product facts must carry [VERIFY]

---

### Step 4 — Present draft for review

Show the full draft. Do not save to any file without explicit user instruction.

Format the presentation:
```
Page type: [type]
Target segment: [segment]
Goal: [goal]

--- DRAFT COPY ---

[Full copy here]

--- END DRAFT ---

[VERIFY] flags in this draft: [count and list]
Guardrails applied: banned words removed ✓ | pricing checked ✓ | voice scrubbed ✓

Next step: Review the draft. Tell me what to change, or say "save this" to write it to a file.
```

---

### Step 5 — Save (only on user instruction)

If the user confirms, save to:
- **New page:** `marketing/pipelines/drafts/copy-[page-type]-[slug]-YYYY-MM-DD.md`
- **CMS-ready format:** Note in the file header whether it needs `/pre-write` to generate the Sanity JSON scaffold

Frontmatter:
```yaml
---
type: web-copy
page-type: homepage | pricing | feature | topic-hub | comparison
target-segment: ""
goal: ""
status: draft
date: YYYY-MM-DD
---
```

## What this skill does NOT do

- Does not write blog articles. Use `/write-article` for SEO blog content.
- Does not auto-publish or push to Sanity CMS. Copy goes to drafts/ only.
- Does not generate Sanity JSON schema. Run `/pre-write` after this skill if a Sanity scaffold is needed.
- Does not write TikTok scripts, Reddit posts, or email sequences — those have dedicated skills.
- Does not fabricate student testimonials, user numbers, or product metrics. All social proof carries [VERIFY].
