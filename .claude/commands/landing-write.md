---
name: landing-write
description: Write conversion-focused landing pages for ExamPilot's Sanity CMS — topic hubs, comparison pages, feature pages. Produces a markdown draft + triggers /pre-write for the Sanity JSON scaffold. Run after /landing-research.
---

## Input

$ARGUMENTS

Expect either:
- A brief file path: `marketing/pipelines/research/landing-[slug]-YYYY-MM-DD.md`
- A topic + page type: e.g. `cambridge 9709 pure 1 -- topic-hub` or `examPilot vs savemyexams -- comparison`

If neither provided, ask: "What page are we writing? Share the brief path or describe the topic and page type (topic-hub / comparison / feature)."

## Execution

### Step 1: Load context

If a brief file path was given, read it first:
```
marketing/pipelines/research/landing-[slug]-YYYY-MM-DD.md
```

Always read these files in parallel:
- `references/voice-house.md` — voice and tone
- `marketing/context/audience-segments.md` — messaging angles per segment
- `marketing/context/content-standards.md` — quality bar, GEO checklist, positioning rules
- `marketing/references/copy-frameworks.md` — CRO principles and frameworks

Determine the target segment from the brief or topic. Options: student-cambridge, student-edexcel, resit-student, parent, tutor.

### Step 2: Classify page type and apply template

Identify which of the three page types applies. Use the topic or brief to decide:

---

**Topic hub page** (e.g. `/cambridge/9709-pure-1`) — 1500-2000 words

Structure:
- **H1:** [paper code] + [topic name] + "Complete Guide" or "Revision Hub" — ≤65 chars, primary keyword first
- **What you'll find here** — navigation block: list of subtopics as anchor links (scannable, not a wall of text)
- **What is [topic]?** — 2-3 paragraph overview, GEO answer-first: define clearly in the first sentence
- **Why this topic matters for your exam** — mark allocation, question frequency, which papers it appears in. Flag all claims with [VERIFY] unless sourced from the brief.
- **Key concepts** — one H2 per major concept:
  - 150-200 words per concept
  - Worked example per concept (Cambridge or Edexcel paper format as appropriate)
  - What students get wrong with this concept
- **Practice and revision strategy** — spaced repetition, how ExamPilot maps this topic
- **Frequently asked questions** — 4+ Q&A pairs, FAQPage schema-ready
- **Primary CTA:** "Practice [Topic] on ExamPilot" — links to free trial, no credit card framing

---

**Comparison page** (e.g. ExamPilot vs SaveMyExams) — 800-1200 words

Structure:
- **H1:** "[Product A] vs [Product B]: Which is better for [specific student type]?" — be honest in the framing
- **TL;DR** — 30-word summary at the very top, answer-first (GEO: assume this gets cited without the rest of the page)
- **Comparison table** — feature-by-feature, honest. Acknowledge SaveMyExams strengths where real. Dishonest comparisons damage trust more than they convert.
- **"Choose ExamPilot if..."** — specific scenarios where ExamPilot wins (adaptive practice, knowledge mapping, spaced repetition)
- **"Choose SaveMyExams if..."** — specific scenarios where SaveMyExams wins (note: this builds trust; do not skip)
- **ExamPilot differentiators** — adaptive practice vs static, spaced repetition, knowledge state mapping. Frame as mechanisms, not marketing claims.
- **Student verdict section** — social proof. If unavailable, insert: `[VERIFY: add student testimonial — name, exam board, specific improvement]`
- **CTA:** free trial, no credit card required, EUR pricing

---

**Feature page** (e.g. Adaptive Practice, Knowledge State) — 800-1200 words

Structure:
- **H1:** outcome-first framing — "Know Exactly Where Your Gaps Are" not "AI-Powered Diagnostics". The student's outcome, not the product feature.
- **Problem block** — describe the problem in student language. Concrete and specific.
- **Solution block** — how ExamPilot solves it. Plain language, no jargon. "Adaptive practice" not "AI-powered adaptive learning engine".
- **How it works** — 3-step process, numbered list, plain language. One sentence per step.
- **Concrete outcomes** — mechanism-based claims only. If quoting metrics (% improvement), flag with [VERIFY] unless confirmed.
- **Social proof** — named testimonial if available. If not: `[VERIFY: add student testimonial — name, exam board, specific outcome]`
- **CTA:** try it free

---

### Step 3: Write the page

Apply these rules across all page types:

**Structure:**
- Lead every section with the most important point (BLUF: bottom line up front)
- Every H2 opens with a direct, extractable answer in the first 2 sentences
- No buried leads

**Voice:**
- UK English throughout: practise (verb), practice (noun), organisation, recognise, colour
- Short sentences, 15-20 words average
- No em-dashes — use commas, colons, or split into two sentences
- No AI tells: no "seamlessly", "delve into", "navigate", "foster", "tapestry", "leverage" (verb), "it's worth noting"
- No corporate language: no "enterprise", "scalable", "end-to-end", "holistic"
- Not "AI tutor". Not "AI-powered". ExamPilot is a learning science tool with adaptive practice.

**Content rules:**
- Flag all unverified claims with [VERIFY]
- No B2B school licensing or institution pricing. ExamPilot is always consumer-purchased.
- Teachers are B2C2B referral partners (see `references/voice-teacher.md`), not customers.
- EUR pricing only if mentioned: €29/mo, €69/3mo, €96/6mo, €144/yr. Never GBP or USD.
- CTAs: "Start practising free", "Try ExamPilot free" — action + benefit, not "Sign Up" or "Get Started"
- 3-5 internal links to related pages (e.g. `/cambridge/*`, `/pricing`, `/features`) using descriptive anchor text

**Social proof rules:**
- Named testimonials only — "Maya, Cambridge 9709" not "one of our students"
- Specific outcomes only — "improved from Grade D to Grade A*" not "saw real improvement"
- If none available, insert [VERIFY: add testimonial] placeholder — do not fabricate

### Step 4: Post-write checks

Run `marketing/data_sources/modules/landing_page_scorer.py [filepath]` if available.

If the module is unavailable, score inline across 5 pillars (0-20 each):

**Above-fold (20pts)**
- Headline benefit-driven, not feature-driven? (5pts)
- Primary keyword in headline? (3pts)
- Value proposition clear in first 2 sentences? (5pts)
- CTA visible without scrolling? (4pts)
- Trust signal above fold? (3pts)

**CTA quality (20pts)**
- CTA copy is action + benefit (not just "Sign Up")? (6pts)
- One clear primary CTA? (4pts)
- CTA appears after each major section? (5pts)
- CTA copy consistent throughout? (5pts)

**Trust signals (20pts)**
- Named testimonial with specific outcome? (7pts)
- Exam board alignment signals present? (5pts)
- Risk reversal statement ("free trial, no credit card")? (5pts)
- Student count or usage metric (with [VERIFY] if unconfirmed)? (3pts)

**Friction (20pts)**
- Reading level appropriate, short sentences? (5pts)
- No B2B language? (5pts — deduct 3 per instance found)
- No "AI tutor" or "AI-powered" phrasing? (5pts)
- Page length appropriate for this page type? (5pts)

**Structure (20pts)**
- Logical flow: problem → solution → proof → CTA? (8pts)
- FAQ section present (4+ Q&A)? (6pts)
- Internal links present (3-5)? (3pts)
- Pricing correct and EUR-only if mentioned? (3pts — deduct 5 if GBP/USD found)

Show score per pillar and total. Verdict:
- PASS (≥75/100) — draft can move to review
- NEEDS WORK (60-74) — list top 3 fixes before moving
- BLOCKED (<60) — must fix before saving

If BLOCKED, fix the highest-impact issues inline and rescore before saving.

### Step 5: Save + handoff

Save draft to `marketing/pipelines/drafts/landing-[slug]-YYYY-MM-DD.md`

YAML frontmatter:
```yaml
type: landing-page
channel: seo
stage: [tofu | mofu | bofu — match the page type: hub=tofu, comparison=mofu, feature=mofu/bofu]
target-segment: [student-cambridge | student-edexcel | resit-student | parent | tutor]
status: drafted
keyword: [primary keyword]
created: YYYY-MM-DD
page_type: [topic-hub | comparison | feature]
landing_score: [score]/100
```

After saving, prompt:
"Draft saved to `marketing/pipelines/drafts/landing-[slug]-YYYY-MM-DD.md`.

Run `/pre-write [slug]` to generate the Sanity CMS JSON scaffold for this page.

Before publishing: resolve all [VERIFY] flags and get human sign-off on testimonials and metric claims."
