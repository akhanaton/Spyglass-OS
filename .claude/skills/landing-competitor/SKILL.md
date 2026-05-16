---
name: landing-competitor
description: Analyse a competitor's landing page — headlines, CTAs, trust signals, objection handling, and content gaps. Use before writing any comparison page or topic hub that needs to out-rank a competitor. Works from a URL or a competitor name.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## When `/landing-competitor` runs

- Before writing any comparison page or topic hub that targets a competitor keyword
- When the user asks "what does [competitor]'s page look like?" or "how should we position against [competitor]?"
- As research input for `/landing-write comparison`

Expects a competitor URL or competitor name. Known competitor names:
- "SaveMyExams" → savemyexams.com
- "PapaCambridge" → papacambridge.com
- "Physics & Maths Tutor" or "PMT" → physicsandmathstutor.com

If a name is given without a URL, read `marketing/context/competitor-analysis.md` for the known domain and any cached observations.

If no input is provided, ask: "Which competitor do you want to analyse? (SaveMyExams, PapaCambridge, Physics & Maths Tutor, or paste a URL)"

## Execution

### Step 1: Fetch the page

Use WebFetch to retrieve the competitor's landing page or topic page HTML.

If a specific page URL is provided, fetch that URL directly.
If only a competitor name is given, fetch their homepage first, then check `marketing/context/competitor-analysis.md` for a more relevant page to analyse (e.g. their Cambridge 9709 hub if one exists).

If WebFetch fails or returns a blocked/empty response, proceed with known competitor patterns from `marketing/context/competitor-analysis.md` and note: "WebFetch blocked — analysis based on cached competitor observations."

---

### Step 2: Extract and analyse 6 elements

Work through each element in sequence. Quote exact text where available.

---

**Element 1: Above-fold analysis**

- H1: exact text (or closest equivalent if no H1 tag)
- Primary value proposition: what do they claim in one sentence?
- CTA above the fold: yes/no — exact button text if present
- Trust signals above the fold: list each one (e.g. "10 million students", exam board logos, review scores)

---

**Element 2: Headline and messaging**

- Primary positioning: how do they describe themselves? (e.g. "revision notes and past papers" vs "adaptive practice tool")
- Pain point they lead with: what problem does the page open with?
- Outcome they promise: what result does the student get?
- Tone: classify as one of — formal / peer / authoritative / friendly / neutral

---

**Element 3: CTA analysis**

- Primary CTA text (exact)
- Total CTA count on the page (estimate if full page not available)
- Action type: free trial / create account / view content / download / buy now
- Pricing shown: yes/no — if yes, what pricing model (free / freemium / paid)
- Friction level: low (one click) / medium (form required) / high (paywall immediate)

---

**Element 4: Trust signals**

- Student count or usage metric (exact text, e.g. "used by 3 million students")
- Testimonials: named/anonymous, outcome-specific or generic, exam-board-specific or general
- Exam board logos or accreditation markers: list any present
- Social proof format: quotes / stats / star ratings / logos / none
- Third-party validation: press mentions, awards, partnerships

---

**Element 5: Objection handling**

- Objections pre-empted: list each one (e.g. accuracy, exam alignment, value vs free alternatives)
- Risk reversal: free access / no credit card / money-back guarantee / none
- Content quality claims: how do they justify their content is trustworthy or accurate?
- What they do NOT address: flag objections a cautious student might still have

---

**Element 6: Content gaps and weaknesses**

- Questions the page does not answer (list 3-5)
- ExamPilot advantages not mentioned or not matched: adaptive practice, spaced repetition, knowledge state mapping, exam-board-specific question bank
- Vague or unverifiable claims: any stat or claim that lacks a source
- Mobile experience notes if observable from the HTML or metadata

---

### Step 3: Differentiation brief

Based on the analysis, produce:

**3 angles where ExamPilot is meaningfully different** (specific, not just "better"):
- Each angle should be a concrete capability difference (e.g. "adaptive difficulty vs static notes", "knowledge state visualisation vs topic list", "spaced repetition scheduling vs manual revision")
- Do not use "more engaging" or "better designed" — these are not differentiation angles

**3 specific objections their page raises that ExamPilot's comparison page must address:**
- These are gaps or weaknesses you found in Element 6 that ExamPilot can credibly fill
- Frame each as: "A student reading [competitor]'s page will still wonder: [question]. ExamPilot's page should answer: [answer]."

**Suggested H1 for an ExamPilot comparison page:**
- Must directly counter their positioning
- Format options:
  - "[Competitor] gives you notes. ExamPilot shows you what you don't know yet."
  - "The difference between [Competitor] and ExamPilot: one tests you, one teaches to the test."
  - Custom — adapt to what the analysis revealed about their actual positioning

**One trust signal format ExamPilot should prioritise:**
- Identify the trust format they use poorly or not at all (e.g. they have generic testimonials — ExamPilot should use grade-specific outcome quotes)
- Recommend the format + a placeholder example with [VERIFY]

---

### Step 4: Save output

Save to `marketing/pipelines/research/competitor-landing-[competitor-slug]-YYYY-MM-DD.md`

```yaml
---
type: competitor-analysis
competitor: ""
competitor_url: ""
page_analysed: ""
webfetch_success: true | false
created: YYYY-MM-DD
---

## Competitor: [Name]
### Page analysed: [URL]

### Above-fold analysis
[findings]

### Headline and messaging
[findings]

### CTA analysis
[findings]

### Trust signals
[findings]

### Objection handling
[findings]

### Content gaps and weaknesses
[findings]

---

## Differentiation brief

### 3 angles where ExamPilot is different
1. [angle]
2. [angle]
3. [angle]

### 3 objections ExamPilot's comparison page must address
1. [objection + recommended answer]
2. [objection + recommended answer]
3. [objection + recommended answer]

### Suggested H1 for comparison page
[headline option]

### Trust signal to prioritise
[format + placeholder example]

### Recommended next step
`/landing-write comparison "[ExamPilot vs competitor-name]"` — draft the comparison page using this brief.
```

After saving, show a one-paragraph summary and offer:
"Run `/landing-write comparison` next to draft a comparison page using this brief."
