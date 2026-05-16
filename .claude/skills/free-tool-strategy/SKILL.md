---
name: free-tool-strategy
description: Design and evaluate free tool ideas for ExamPilot as lead magnets — tools that provide genuine value to A-Level Maths students, build SEO authority, and convert to trial signups. Covers ideation, prioritisation, build-vs-buy, and GTM for each tool.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

A free tool is something ExamPilot can offer with no signup required (or minimal friction) that:
1. Provides genuine standalone value to A-Level Maths students
2. Demonstrates ExamPilot's expertise and positioning
3. Ranks for relevant search queries (SEO asset)
4. Converts users to trial signups as a natural next step

This skill covers three modes: ideating new tool concepts, prioritising a shortlist, and designing the GTM strategy for a specific tool.

**Bike Method Phase 1:** This skill produces strategies and copy. Build decisions require developer involvement. Nothing is implemented by this skill.

## When `/free-tool-strategy` runs

- "What free tools should we build?"
- "Brainstorm lead magnet ideas for ExamPilot"
- "Which free tool should we build first?"
- "Help me launch [specific tool]"
- When looking for low-friction acquisition channels before or after launch

## Context files — read at session start

```bash
cat references/voice-house.md
cat marketing/context/audience-segments.md
cat marketing/context/channel-playbooks.md
cat marketing/context/content-standards.md
```

## Execution — three modes

Identify the mode from the user's request.

---

### Mode 1: Ideation

Trigger: "brainstorm free tool ideas", "what lead magnets could we build", "give me free tool options"

Generate ideas across three tiers. Each idea includes: what it does, how it provides standalone value, what keyword it targets, and what the natural conversion path is.

---

#### Tier 1: High-fit (build first)

These are high value for the audience, available to build before launch (no post-launch data dependency), and directly demonstrate ExamPilot's positioning.

**Revision planner calculator**
- What it does: student inputs their exam date → gets a week-by-week revision schedule broken down by Pure 1 topics
- Standalone value: saves 30-60 minutes of planning work; a real, usable output
- SEO keyword: "Cambridge 9709 revision plan", "A-Level Maths revision schedule" [VERIFY search volume]
- Build effort: Medium — a date-input calculator with topic weighting logic; could be a React component or even a well-designed Google Sheet with a web wrapper
- Conversion path: "Your plan is ready — ExamPilot will track your progress against it. [Start free →]"
- Tracking: `free_tool_used` (tool: "revision-planner"), `free_tool_cta_clicked`

**Exam countdown**
- What it does: shows the number of days until Cambridge 9709 main sitting, Edexcel IAL, and other key dates
- Standalone value: immediate, useful at a glance; bookmarkable
- SEO keyword: "Cambridge 9709 exam date 2025", "when is A-Level Maths exam" [VERIFY]
- Build effort: Low — a simple date calculation; can be a static page with JavaScript
- Conversion path: "Exams in [N] days. Are you ready? [Find your gaps with ExamPilot →]"
- Seasonal: highest value in the 8 weeks before each sitting. Update dates annually.
- Tracking: `free_tool_used` (tool: "exam-countdown")

**Mark scheme decoder**
- What it does: explains Cambridge mark scheme notation — M1, A1, B1, ft, FT, cao, dep, AG, etc.
- Standalone value: a real reference tool — students genuinely do not know what "cao" means the first time they see it
- SEO keyword: "Cambridge mark scheme notation explained", "what does M1 mean mark scheme" [VERIFY]
- Build effort: Low — a static reference page or searchable glossary; no dynamic logic needed
- Conversion path: "Understanding marks is one thing. Earning them is another. [Practise with ExamPilot →]"
- Tracking: `free_tool_used` (tool: "mark-scheme-decoder")

**Paper code lookup**
- What it does: student selects Cambridge 9709 or Edexcel IAL → sees the full topic breakdown per paper, with official specification topics
- Standalone value: quick reference when students don't have the syllabus open
- SEO keyword: "Cambridge 9709 Pure 1 syllabus topics", "Edexcel IAL Maths paper topics" [VERIFY]
- Build effort: Low — static data; a well-structured page or filterable table
- Conversion path: "9709 Pure 1 has [N] topics. ExamPilot has practice questions for all of them. [Try free →]"
- Tracking: `free_tool_used` (tool: "paper-code-lookup")

---

#### Tier 2: Medium-fit (build post-launch or when data is available)

These are useful but depend on post-launch data or require more build effort.

**Topic difficulty ranker** (post-launch only)
- What it does: shows which Cambridge 9709 topics students find hardest, based on ExamPilot's aggregate session data
- Standalone value: high — tells students where to focus
- Data dependency: requires real session data from ExamPilot users. Do not build before launch — the data does not exist yet. Flag this clearly.
- Build effort: Medium — requires a PostHog query or database query piped to a public-facing display
- Conversion path: "See your personal topic difficulty profile — [sign up free →]"

**Predicted grade estimator**
- What it does: student inputs their recent past paper scores → gets an estimate of which grade band they are in, compared to recent grade boundaries
- Standalone value: Medium — useful but grade boundaries are already public; this adds the calculation step
- Data dependency: grade boundary data is publicly available from Cambridge [VERIFY — confirm reliable data source]
- Build effort: Medium — calculation logic plus grade boundary data maintenance each exam session
- Conversion path: "Your estimated grade is [X]. ExamPilot can help you move up one grade band by [exam date]. [Start free →]"

**Spaced repetition interval explainer**
- What it does: explains the maths behind spaced repetition, with an interactive visual showing how forgetting curves work
- Standalone value: educational content, not a tool — borderline for this tier
- SEO keyword: "spaced repetition for A-Level Maths", "how spaced repetition works" [VERIFY]
- Build effort: Low — could be a static article + interactive SVG or Lottie animation
- Conversion path: "ExamPilot applies spaced repetition automatically. [Try it free →]"

---

#### Tier 3: Low-fit (exclude for now)

These are excluded and the reason is noted to avoid revisiting them without new information.

| Idea | Why excluded |
|---|---|
| General maths calculator (not exam-specific) | Doesn't demonstrate ExamPilot's positioning. Competes with Wolfram Alpha, Desmos, etc. |
| Past paper PDF viewer | Copyright issues with Cambridge/Edexcel materials |
| Grade boundary tracker requiring data scraping | Legal and maintenance risk |
| AI question generator | Positions ExamPilot as an "AI tool" — contradicts brand positioning |
| Tools requiring significant backend infrastructure before launch | Chicken-and-egg problem — delays time to first tool live |

---

### Mode 2: Prioritisation

Trigger: "which free tool should we build first", "prioritise the tool list", "what's the highest ROI free tool"

Score each idea against five dimensions. Score each 1-3 (1 = low, 2 = medium, 3 = high).

| Dimension | What it measures |
|---|---|
| SEO value | Will it rank? Search volume for target keyword? |
| Conversion potential | Natural path to ExamPilot trial — how strong? |
| Build effort | 1 = 1-2 days, 2 = 1 week, 3 = 2+ weeks |
| Data dependency | 1 = requires post-launch data, 2 = needs external data, 3 = available now |
| Exam calendar timing | 3 = always useful, 2 = seasonal but predictable, 1 = narrow window |

**Build effort scoring is inverted:** 1 = high effort (bad), 3 = low effort (good)

**Priority score = SEO + Conversion + Build effort (inverted) + Data + Timing**

Present as a ranked table:

```
Free Tool Prioritisation
---

| Tool | SEO | Conversion | Effort (inv) | Data | Timing | Total |
|---|---|---|---|---|---|---|
| Mark scheme decoder | 2 | 2 | 3 | 3 | 3 | 13 |
| Exam countdown | 2 | 2 | 3 | 3 | 2 | 12 |
| Paper code lookup | 2 | 3 | 3 | 3 | 3 | 14 |
| Revision planner | 3 | 3 | 2 | 3 | 2 | 13 |
| Topic difficulty ranker | 3 | 3 | 2 | 1 | 3 | 12 |

Recommended first build: [highest score that is available now]
Reason: [brief explanation]

Second build: [next in list]
```

After ranking, show the recommended sequencing:
1. Build [Tool A] — lowest effort, available now, drives SEO
2. Build [Tool B] — medium effort, highest conversion potential
3. Revisit [Tool C] — post-launch when data is available

---

### Mode 3: GTM for a specific tool

Trigger: "help me launch [tool name]", "GTM for the revision planner", "how do I distribute [tool]"

Given a specific tool, produce a complete GTM brief.

---

**Template — apply to any tool:**

```
Free Tool GTM Brief: [Tool Name]
---

What it does (one sentence):
[Plain description of the tool's output]

Target audience:
[Specific segment — e.g. "Cambridge 9709 students 6-10 weeks before the main sitting"]

SEO target keyword:
[Primary keyword the landing page should rank for]
[VERIFY search volume via DataForSEO or similar before committing]

Landing page copy:

  Headline: [Outcome-led — what does the student get?]
  Subheadline: [Specificity — who is it for? How long does it take?]
  CTA (use the tool): "Use the [tool name] →" or "[Action] — it's free"
  Post-tool CTA: "Want to track your progress against this plan? [Try ExamPilot free →]"

Email capture (optional):
  Recommendation: show the tool output first, then offer to email it.
  "Want to save your [output]? Enter your email and we'll send it." (optional, not required to use the tool)
  If email is captured: add to Brevo with tag "free-tool-[name]" — do not trigger welcome sequence. Trigger a specific single-email follow-up 48 hours later.
  Under-18 GDPR: email capture requires clear consent notice. [VERIFY consent mechanism with Enitan before implementing]

Reddit distribution:
  Subreddits: r/alevel, r/6thForm, r/igcse (check which applies for IAL), r/CambridgeIGCSE [VERIFY subreddit relevance]
  Format: value-first post. Share the tool as a genuinely useful resource, not as promotion.
  Title format: "Built a free [tool name] for 9709 students — [what it outputs in one line]"
  Body: Brief context on why you built it + link + invitation to feedback ("Let me know if the topics are wrong — I want to fix it")
  Timing: post during active revision periods (Jan-April, Aug-Sept resit window)
  Do NOT: post as ExamPilot with a promotional tone. Reddit detects and rejects product promotion dressed as community contribution. [Follow channel-playbooks.md for Reddit rules]

Discord distribution:
  Post in relevant student Discord servers: A-Level / Cambridge AS/A Level communities [VERIFY active servers]
  Same value-first framing as Reddit

PostHog events to fire:
  - `free_tool_used` — properties: { tool: "[tool-slug]", exam_board: "cambridge|edexcel" (if selectable) }
  - `free_tool_email_captured` — if email capture is implemented
  - `free_tool_cta_clicked` — when the post-tool ExamPilot CTA is clicked
  - properties on cta_clicked: { tool: "[tool-slug]", time_on_tool: [seconds] }

Funnel to monitor in PostHog:
  `free_tool_used` → `free_tool_cta_clicked` → `trial_started`

Success metric:
  Primary: `free_tool_cta_clicked` / `free_tool_used` (conversion rate from tool use to CTA click)
  Secondary: `trial_started` attributed to `utm_source=free-tool&utm_medium=[channel]`

[VERIFY] flags: [list any]
Next step: Build the tool, set up UTM links for each distribution channel, then post to Reddit/Discord after testing.
```

---

### Guardrails

- Free tools must provide genuine value without signing up — they are not demos, teasers, or gated calculators
- Data used in tools must be accurate or clearly marked as estimated. Do not use made-up or approximated data to fill gaps.
- Do not build tools that depend on post-launch ExamPilot session data before that data exists
- All tools must be relevant to ExamPilot's core audience: 16-18 year old A-Level Maths students (Cambridge 9709, Edexcel IAL)
- No tools that suggest ExamPilot is an "AI tool" or "AI generator" — the brand positioning is learning science and adaptive practice
- Email capture: always optional, always with clear GDPR/PECR consent for under-18 users
- Do not scrape Cambridge or Edexcel copyrighted materials — past paper content is not available for redistribution without a licence [VERIFY Cambridge and Edexcel reproduction policies]

## What this skill does NOT do

- Does not build the tool. It designs the strategy. Developer implements.
- Does not conduct keyword research. Use `/research-keywords` for confirmed search volume data.
- Does not write the full landing page copy. Use `/copywriting` (topic hub module) or `/landing-write` for that.
- Does not write the Reddit post. Use `/write-reddit` for that, with this GTM brief as context.
- Does not upload to Brevo. Use `/email-sequence` for the follow-up email, and Brevo manual upload for the list.
- Does not auto-save. Present output inline; save only on user instruction.
