---
name: marketing-psychology
description: Apply behavioral economics and persuasion principles to ExamPilot's marketing. Analyzes existing copy or suggests psychological framing for new content. Reference for exam-student-specific motivations, objections, and decision patterns.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

A thinking tool, not a content generator. Applies behavioral economics and persuasion principles to ExamPilot's marketing copy, UX flows, and content decisions. Use this before writing a pricing page, designing a CTA, reviewing email sequences, or planning a content angle. It identifies what psychological dynamics are at play in the target audience and how to use them honestly.

This skill works in two modes:
1. **Analyze mode:** Review existing copy and identify which principles are present, missing, or misapplied.
2. **Design mode:** For new content, suggest which principles to apply and how to implement them for this audience.

**Hard constraint:** This skill never recommends dark patterns, manufactured urgency, or techniques that exploit anxiety dishonestly. Exam students are 16-18 years old under genuine pressure. The guardrails in this skill are non-negotiable.

## When `/marketing-psychology` runs

- Before writing a pricing page or CTA — "What psychology should I apply here?"
- After writing a draft — "Review this for psychological effectiveness"
- When a conversion rate is disappointing — "Why might students be bouncing here?"
- When designing an email sequence — "Which principles should drive the nurture flow?"
- When a Reddit post or outreach message feels flat — "What's missing psychologically?"

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/audience-segments.md
```

## Execution — four steps

### Step 1 — Identify input and mode

Confirm:
1. **What to analyze or design:** paste copy, describe a page type, or describe the decision being made
2. **Mode:** analyze (review existing) or design (build new)
3. **Target segment:** cambridge-9709-student / edexcel-ial-student / resit-student / parent / tutor

If mode is unclear, default to analyze if copy is provided, design if only a page type or brief is provided.

---

### Step 2 — Apply the ExamPilot psychology framework

The principles below are ranked by relevance to this specific audience (16-18 year old A-Level Maths students). Apply them in the order they appear — earlier principles have higher impact for this context.

---

#### Principle 1: Loss aversion (highest impact for this audience)

**Why it matters for ExamPilot:** Students fear failing their exams more than they desire an A*. The emotion driving revision decisions is predominantly avoidance of a bad outcome, not pursuit of a good one.

**Honest applications:**
- "Don't leave gaps unfixed before your exam" outperforms "Get a better grade" for this audience
- "Know what you don't know before it's too late" creates legitimate urgency without manipulation
- Knowledge State gap visualization is inherently loss-averse framing — showing gaps creates natural motivation to close them

**Where to apply:**
- CTAs on topic hub pages (exam is real, timeline is real)
- Email subject lines during revision season
- Hero subheadline (after anchoring with the positive outcome in the headline)
- Re-engagement emails (natural, not manufactured)

**Guardrail:** Loss framing works because exam failure is a genuine risk. Do not exaggerate the risk or suggest ExamPilot is the only way to avoid it. "ExamPilot helps you identify gaps before the exam" — not "Without ExamPilot, you will fail."

---

#### Principle 2: Social proof (peer-specific)

**Why it matters:** 16-18 year olds are highly influenced by peer behaviour but are sceptical of corporate social proof. Generic testimonials ("ExamPilot helped me!") are ignored. Specific, peer-level evidence works.

**Honest applications:**
- "Students who practice 3x/week improve their Knowledge State score by [X]%" — if true and [VERIFIED]
- Paper code specificity increases credibility: "9709 Pure 1 students who..." is more trusted than "maths students who..."
- Geographic specificity where it fits: "Students in Dubai, Lagos, and Lahore preparing for the May session..."
- Peer language signals (use "practising", not "utilizing"; "weak topics", not "knowledge gaps")

**Where to apply:**
- Landing page social proof line (below hero)
- Email sequences (Email 3 in welcome is specifically social proof)
- Reddit posts (the most persuasive form: genuine peer experience)

**Guardrail:** Do not fabricate testimonials. Do not use specific names without consent. Do not invent outcome statistics. All specific claims carry [VERIFY]. Generic framing ("many students find") is acceptable if not quantified.

---

#### Principle 3: Progress and commitment

**Why it matters:** Once a student has invested time in ExamPilot (completed sessions, built a Knowledge State, seen their weak topics), they are more likely to continue — both because of sunk cost and because they can see their progress. This principle supports retention more than acquisition.

**Honest applications:**
- Show progress clearly in the product: "You've covered 12 of 24 Pure 1 topics"
- Email nurture: "Your Knowledge State from last week shows [improvement] — you've been putting in the work"
- Onboarding copy: "Start with just one topic" reduces activation barrier (small commitment → larger commitment)
- Free trial framing: position the trial as an investment, not a test ("build your Knowledge State, then decide")

**Where to apply:**
- Onboarding copy and first-session CTAs
- Email 4 in welcome sequence (Knowledge State spotlight)
- Re-engagement emails (reference their existing progress — "Your Knowledge State is still there")

**Guardrail:** Do not exploit sunk cost. Do not pressure students to continue with language like "don't waste the sessions you've already done." That is manipulative. Reference progress as positive motivation only.

---

#### Principle 4: Scarcity via natural urgency (exam calendar)

**Why it matters:** Exam dates are fixed. The window for effective revision narrows as the exam approaches. This creates genuine urgency that doesn't need to be manufactured.

**Honest applications:**
- "Your Cambridge 9709 Paper 1 is in 6 weeks" — specific and true
- "Mock season starts January 15" — anchors to the real calendar
- Exam-calendar email campaigns use the actual signal-registry.md dates — never approximate or fabricate
- The most powerful urgency message for resit students: "You have 10 weeks to the October sitting"

**Where to apply:**
- Exam-calendar email campaigns (see `/email-sequence`)
- Re-engagement Email 2 (exam timeline hook)
- Pricing page upgrade nudge during revision season
- Reddit posts around exam season (with transparent context)

**Guardrail:** Only use real exam dates from `marketing/gtm-engineering/signal-registry.md`. Never invent countdown timers or fake "limited time" offers. Never suggest the exam date is closer than it is. If an exam date is uncertain, do not use urgency framing.

**What NOT to do:**
- "Only 5 spots left" — false scarcity, not applicable to a software product
- Countdown timers on pricing pages without a real deadline behind them
- "Prices go up on [date]" unless it is genuinely true and confirmed

---

#### Principle 5: Authority and expertise signalling

**Why it matters:** Students need to trust that ExamPilot understands their specific exam. Generic "revision app" authority means nothing. Exam-board-specific authority is everything.

**Honest applications:**
- Paper codes signal insider knowledge: "9709/12" signals Cambridge expertise more than "Cambridge A-Level Maths"
- Mark scheme language ("method mark", "accuracy mark") in blog content signals familiarity with how exams are graded
- Citing Cambridge and Pearson specifications directly (with links) builds credibility
- The fact that ExamPilot is built for 9709 specifically — not adapted from a generic maths tool — is a genuine authority signal

**Where to apply:**
- Article meta descriptions (include paper code)
- Feature page copy (reference specific papers and topics)
- Topic hub headings (include full paper code and name)
- Blog content (reference official syllabi, use mark scheme terminology)

**Guardrail:** Authority is built on accuracy. Any specific claim about the exam (paper codes, topic weighting, mark allocation) must carry [VERIFY] and be confirmed before publishing.

---

#### Principle 6: Anchoring (pricing context)

**Why it matters:** Students (and their parents) have no natural anchor for what "good value" exam prep costs. Providing the right anchor shapes how they perceive ExamPilot's price.

**Honest anchors to use:**
- Tutoring cost: "EUR30-60 per session. ExamPilot's annual plan is less than two sessions — for a year of daily practice."
- Per-day cost: EUR12/month annual plan = EUR0.40/day — that is a real, not misleading, comparison
- Show annual price first (EUR12/mo equivalent), then monthly (EUR29/mo) — the anchor effect makes EUR29 feel high after seeing EUR12

**What NOT to anchor against:**
- "Normally EUR50/month, now EUR29" — not true, do not use fake original prices
- Competitor prices — only use if the comparison is accurate and fair

**Where to apply:**
- Pricing page (see `/copywriting` pricing page module)
- Email 5 of welcome sequence (upgrade offer)
- Nurture Email 3 (trial end, price stated)
- Parent-targeted messaging (EUR12/mo vs tutor hourly rate)

---

#### Principle 7: Objection pre-emption

**Why it matters:** Students arrive with unspoken objections. Addressing them before they raise them dramatically increases trust and conversion. The worst outcome is a student leaving without finding the answer to their hesitation.

**Key objections for ExamPilot and how to address them:**

| Objection | What they're really asking | Honest response |
|---|---|---|
| "Will this actually help me pass?" | Does it work for my specific exam? | Specificity: name their paper code, show how ExamPilot maps to their syllabus |
| "Is it just an AI chatbot?" | Is it gimmicky? | Positioning: "adaptive practice", "spaced repetition" — not "AI chat" |
| "My school gives me enough resources" | Why do I need this? | The practice gap: SaveMyExams gives you notes; ExamPilot makes you test yourself until you actually know it |
| "EUR29 a month is expensive for a student" | Is this worth it for me? | Anchoring: tutoring comparison, per-day cost, annual plan at EUR12/mo |
| "I can just do past papers myself" | Why pay for something I can do free? | The feedback gap: doing past papers without feedback on WHY answers are wrong doesn't close knowledge gaps |
| "I'll try it closer to the exam" | Procrastination/low urgency | Compound benefit: spaced repetition requires time to work; starting 8 weeks before the exam is meaningfully better than starting 2 weeks before |

**Where to apply:**
- FAQ sections on all pages (the most natural home for objection handling)
- Comparison pages (see `/copywriting` comparison page module)
- Email Nurture Email 1 (open-ended question surfaces their objection)
- Reddit posts and comments (answer the real question behind the question)

---

### Step 3 — Produce the analysis or design

**For Analyze mode:**

Review the provided copy against each principle. For each principle:
- Is it present? (mark as Active, Partial, or Missing)
- Is it applied correctly? (flag any manipulative or dishonest applications)
- What specific change would improve it?

Output format:
```
Marketing Psychology Analysis: [page type or piece]
Segment: [target segment]

Principles present and effective:
  - [Principle]: [where it appears and why it works] ✓

Principles present but misapplied:
  - [Principle]: [what's wrong and how to fix it] ⚠

Principles missing (that should be added):
  - [Principle]: [where to add it and suggested copy]

Priority changes (ranked by likely impact):
  1. [Change] — expected to improve [metric] because [reason]
  2. [Change]
  3. [Change]

Guardrail flags (anything that should be removed or changed):
  - [Flag if any dark patterns, false urgency, or manipulative framing found]
```

**For Design mode:**

Recommend which principles to activate, in which order, with specific copy suggestions:

```
Marketing Psychology Design: [page type or content piece]
Segment: [target segment]
Goal: [conversion action]

Recommended principle stack (in order of application):
  1. [Principle] — [where to apply it] — [suggested copy direction]
  2. [Principle] — [where to apply it] — [suggested copy direction]
  3. [Principle] — [where to apply it] — [suggested copy direction]

Objections to pre-empt on this page:
  - [Objection]: [suggested response format]

Copy suggestions:
  - Headline: [option 1] | [option 2]
  - CTA: [option 1] | [option 2]
  - Social proof: [suggested format]

What NOT to use here:
  - [Any principle that would backfire for this specific context]
```

---

### Step 4 — Guardrail audit

Before presenting the output, check every recommendation against these filters:

**Remove anything that:**
- Creates false urgency (countdown timers with no real deadline, "limited spots" for a software product)
- Fabricates social proof (invented testimonials, unverified outcome statistics)
- Exploits exam anxiety dishonestly (implying students will fail without ExamPilot)
- Uses dark patterns (hidden costs, confusing cancellation flows, pre-checked boxes)
- Targets the age group inappropriately (under-18s — no pressure tactics, no FOMO exploitation)

**Flag for human review:**
- Any social proof copy that includes specific numbers or outcomes (must be [VERIFY]-checked)
- Any urgency copy that references specific exam dates (confirm against signal-registry.md)
- Any competitor comparisons that reference specific features (must be factually confirmed)

State the guardrail status at the end of the output: "No dark patterns found" or list any that were identified and removed.

## What this skill does NOT do

- Does not write finished copy. It analyses and advises. Use `/copywriting`, `/write-article`, or `/email-sequence` to produce the final text.
- Does not conduct user research. The audience profiles here are based on known segment data in `audience-segments.md`. For new validation, use PostHog data or run user interviews.
- Does not guarantee conversion improvements. These are principles that tend to work for this audience. Results depend on implementation quality and real-world testing.
- Does not override the guardrails. The guardrails in this skill cannot be argued around. If a tactic fails a guardrail check, it is not used regardless of how effective it might be.
