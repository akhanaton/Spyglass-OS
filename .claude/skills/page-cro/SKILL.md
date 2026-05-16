---
name: page-cro
description: CRO audit and optimisation for any ExamPilot web page — not just landing pages. Applies to the homepage, Cambridge hub pages, topic pages, blog articles, and the pricing page. Identifies conversion friction and surfaces the highest-leverage fixes.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Audits and optimises any ExamPilot web page for conversion. Where `/landing-audit` handles new draft landing pages before they ship, `/page-cro` works on live pages or pages at any design stage — homepage, pricing, Cambridge hub pages, blog articles, topic pages.

Each page type has a different primary conversion goal. This skill adapts the audit and recommendations to that goal rather than applying a one-size-fits-all framework.

**Bike Method Phase 1:** This skill produces copy and UX recommendations. All copy is marked [VERIFY before shipping]. No code, no auto-save.

## When `/page-cro` runs

- "Audit the pricing page"
- "Check the homepage CRO"
- "The Cambridge hub page isn't converting — what's wrong?"
- "What's the one thing to fix on the blog article?"
- "Design the CRO for the features page"
- "Why is the topic page bounce rate so high?"

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/audience-segments.md
cat marketing/context/funnel-strategy.md
```

---

## Mode 1: Audit an existing page

Trigger: "audit the [page]", "check the CRO on [page]", "why isn't [page] converting"

### Step 1: Read the page

Accept: a URL or a local file path. If a URL is given, use WebFetch. If a file path, read the file.

If neither is provided, ask: "What page do you want to audit? (paste a URL or file path)"

### Step 2: Identify the conversion goal

Map the page type to its primary conversion goal:

| Page type | Primary conversion goal | Key event |
|---|---|---|
| Homepage | Trial signup | `cta_clicked` → `trial_started` |
| Pricing page | Plan selection / upgrade | `plan_selected` → `trial_started` or `upgraded` |
| Cambridge hub page | Trial signup or topic page click-through | `cta_clicked` |
| Blog article | Email signup or trial CTA click | `cta_clicked` |
| Topic page | Trial signup or deeper engagement | `session_started` |
| Features page | Trial signup | `cta_clicked` → `trial_started` |

State the conversion goal before running the audit.

### Step 3: Run the 5-pillar audit

Score each pillar 0-20. Total score out of 100.

---

**Pillar 1: Above-fold (0-20)**

- Is the primary value proposition clear within 5 seconds?
- Does the H1 name the problem or outcome (not just the product name)?
- Is there a CTA above the fold?
- Is the CTA copy specific to the conversion goal (not generic "Get Started")?
- Are there at least 2 trust signals visible above the fold without scrolling?

Score guidance: 18-20 = strong, 12-17 = needs refinement, 0-11 = blocked

---

**Pillar 2: CTA quality (0-20)**

- Is the primary CTA copy action-specific? ("Start practising free" beats "Sign Up")
- Is the CTA visually distinct (contrast, size)?
- How many CTAs on the page? (1-3 is good; 0 is missing; 4+ is dilution)
- Do secondary CTAs direct toward the same conversion goal or to a different one?
- Is there a friction-reduction line near the primary CTA? ("No credit card required", "Free trial")

Score guidance: 18-20 = strong, 12-17 = needs refinement, 0-11 = blocked

---

**Pillar 3: Trust signals (0-20)**

- Is there social proof relevant to the target audience (A-Level Maths students)?
- Are testimonials specific (named, outcome-referenced, exam-board-specific) or generic?
- Is ExamPilot's exam-board specificity claim stated? ("Built for Cambridge 9709 and Edexcel IAL")
- Is there a risk reversal near the conversion point?
- Are any claims vague or unverifiable? Flag each with [VERIFY]

Score guidance: 18-20 = strong, 12-17 = needs refinement, 0-11 = blocked

---

**Pillar 4: Friction (0-20)**

- Does the page load fast? (flag large image or script blocks if visible in source)
- Is the page scannable? (short paragraphs, headers, bullets)
- Are there distracting elements near the CTA (ads, competing links, clutter)?
- On mobile: is the CTA reachable without horizontal scroll?
- Does any copy create doubt or hesitation? (e.g. "cancel any time" is trust; "terms apply" near a CTA without context is friction)

Score guidance: 18-20 = strong, 12-17 = needs refinement, 0-11 = blocked

---

**Pillar 5: Structure and flow (0-20)**

- Does the page follow a logical awareness arc? (Problem → Solution → Proof → CTA)
- Does the page over-explain before the first CTA? (student should see a CTA within the first scroll)
- Is the page length appropriate for the funnel stage? (TOFU pages can be longer; BOFU pages should be tight)
- Does the footer CTA match the primary CTA or introduce a different action?
- Is there a clear next step if the student is not ready to convert? (link to a blog article, a demo, a free tool)

Score guidance: 18-20 = strong, 12-17 = needs refinement, 0-11 = blocked

---

**Pillar 6: Content-to-CTA ratio (blog articles only)**

This pillar applies only to blog articles. Skip for all other page types.

- Is there at least 1 contextual CTA per 600 words of content?
- Is the CTA relevant to the article topic (not just a generic "try ExamPilot")?
  - Example: an article about integration should CTA to "Practice integration on ExamPilot →", not just "Start your free trial"
- Is there a CTA in the first 200 words (above the scroll line for readers who skim)?
- Is the final CTA at the end of the article — after value has been delivered?

Score guidance: 4 = strong, 3 = acceptable, 2 = needs work, 1-0 = blocked
Add to total score as-is (0-20 equivalent: multiply by 5)

---

### Step 4: Verdict and top 3 fixes

**Verdict:**
- 80-100: PASS — ship with minor polish
- 60-79: NEEDS WORK — fix priority issues before launch
- 0-59: BLOCKED — significant rework required

**Top 3 fixes ranked by estimated conversion impact:**

For each fix:
- What to change (specific element)
- Before copy / After copy (if applicable)
- Why this fix outranks others (conversion rationale)

---

## Mode 2: Design for a new page

Trigger: "design the CRO for the [page type]", "what structure should the [page] follow"

### Step 1: Gather inputs

Need: page type + primary conversion goal + target audience segment

If not provided, ask for missing inputs.

### Step 2: Read audience segment context

```bash
cat marketing/context/audience-segments.md
```

Identify the motivations, objections, and decision triggers for the target segment.

### Step 3: Produce page structure with CRO rationale

For each section of the recommended page structure, state:
- Section name
- Content to include
- CRO rationale (why this section appears here in the flow)
- Copy direction (not full copy — direction for the writer)

### Step 4: Above-fold specification

Produce a specific above-fold design:
- Headline formula: [outcome] + [specificity] + [timeframe if applicable]
- Value proposition: one sentence, 15 words max
- CTA: 3 copy options ranked by expected performance
- Trust signal: which format, which claim, [VERIFY] flag if unconfirmed

### Step 5: CTA copy options

3 CTA copy variations for the primary CTA:
1. Action-led: starts with a verb ("Start practising free")
2. Outcome-led: names what the student gets ("See your knowledge gaps — free")
3. Urgency-appropriate: only if the exam date makes urgency genuine ("Practise now — [X] weeks to your exam")

---

## Mode 3: Quick fix

Trigger: "what's the one thing to fix on [page]", "one change to improve [page]"

1. Read the page
2. Identify the single highest-leverage fix — the change most likely to move the primary conversion metric
3. Produce:
   - The specific element to change
   - Before copy / After copy
   - Why this fix outranks all others

Do not pad with a full audit. One fix, one rationale, done.

---

## Output format

```
Page CRO: [Page name / URL]
---

Conversion goal: [primary goal]
Target segment: [segment from audience-segments.md]

[Mode 1 — Audit]
Pillar scores:
  Above-fold:       [score]/20
  CTA quality:      [score]/20
  Trust signals:    [score]/20
  Friction:         [score]/20
  Structure/flow:   [score]/20
  Content-to-CTA:   [score]/20 (blog articles only)
  TOTAL:            [score]/100

Verdict: PASS | NEEDS WORK | BLOCKED

Top 3 fixes:
  1. [element] — Before: "[copy]" → After: "[copy]" — [rationale]
  2. [element] — Before: "[copy]" → After: "[copy]" — [rationale]
  3. [element] — [rationale]

[VERIFY] flags: [list all unconfirmed claims]

[Mode 2 — Design]
Page structure:
  [Section 1]: [content] — [CRO rationale]
  [Section N]: [content] — [CRO rationale]

Above-fold spec:
  Headline: [copy]
  Value prop: [copy]
  CTA options: 1. [copy] | 2. [copy] | 3. [copy]
  Trust signal: [format + placeholder]

[Mode 3 — Quick fix]
Single highest-leverage fix:
  Element: [what to change]
  Before: "[current copy or state]"
  After: "[recommended copy or state]"
  Why this one: [rationale]

Next step: Review recommendations. Pass copy to developer. Resolve all [VERIFY] flags before shipping.
```

---

## Guardrails

- No dark patterns in recommendations (fake scarcity, misleading claims, hidden pricing)
- All recommended copy carries [VERIFY before shipping]
- Under-18 audience: no anxiety exploitation — urgency framing only when exam is genuinely close
- EUR pricing only in any copy recommendations (€29/mo, €69/3mo, €96/6mo, €144/yr)
- All copy in UK English: "practise" (verb), "practice" (noun), "optimise", "recognised"

## What this skill does NOT do

- Does not audit forms (field labels, error messages, submission flow). Use `/form-cro` for that.
- Does not audit or write popups and modals. Use `/popup-cro` for that.
- Does not write the full page copy. Use `/landing-write` or `/copywriting` for that.
- Does not run A/B tests. Use `/ab-test-setup` for that.
- Does not auto-save output. Present inline; save only on user instruction.
