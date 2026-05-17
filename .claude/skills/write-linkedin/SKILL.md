---
name: write-linkedin
description: Draft a LinkedIn post or article for ExamPilot's build-in-public presence. Teresa is the primary author. Adapts OS data sources (decisions log, Linear, PostHog, git) into professional educator-angle content. Human review gate before publishing. Trigger on "write a LinkedIn post", "draft something for LinkedIn", "write-linkedin", or any request to create LinkedIn content. One run = one draft saved to build-in-public/pipelines/outreach/.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI(TM) (c) 2026 Nate Herk. All rights reserved.
  The Three Ms of AI(TM) is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI(TM) (c) 2026 Nate Herk. All rights reserved.*

## What this skill does

Drafts LinkedIn content for ExamPilot's professional authority presence. Teresa's voice throughout. Adapts the same OS data sources used by `/write-x` but reframes everything as educator insight, not founder raw material.

**Bike Method Phase 1:** Every draft requires human review. No auto-publishing. Teresa copies approved drafts to Postiz dashboard manually.

**Audience:** CIE maths teachers at international schools, parents in professional roles, edtech professionals. NOT the indie hacker audience. NOT students.

## Flags

- `--author teresa|enitan` — defaults to `teresa`
- `--source decisions|linear|posthog|git|manual` — defaults to `manual` (freeform input)
- `--type post|article|carousel-outline` — defaults to `post`

If called with no flags and freeform text, treat as: `--source manual --type post --author teresa`

Examples:
```
/write-linkedin "We made a counter-intuitive choice about how we structure worked examples"
/write-linkedin --source decisions
/write-linkedin --type article "why students who understand integration still fail Paper 1"
/write-linkedin --source posthog --type post
/write-linkedin --type carousel-outline "5 things CIE students get wrong in Paper 1"
```

## Context files — read before drafting

```bash
# 1. Author's personal voice
cat references/voice-teresa.md   # if it exists; otherwise use voice-house.md as base, note the gap

# 2. LinkedIn strategy and angle adaptation rule
cat build-in-public/references/linkedin-strategy.md

# 3. Audience profile for LinkedIn
cat build-in-public/context/audience.md   # LinkedIn section

# 4. Channel rules for LinkedIn
cat build-in-public/context/channel-rules.md   # LinkedIn section

# 5. Content standards and banned phrases
cat marketing/context/content-standards.md
```

**Critical:** The draft must be written as Teresa the educator-parent, not Teresa the co-founder-building-in-public. Same source material, different lens.

## Execution — seven steps

### Step 1 — Determine source and extract content

Based on the `--source` flag:

**`decisions` (scan decisions/log.md):**
Read `decisions/log.md`. Show the 3 most recent entries. Ask Teresa which one to adapt, or auto-select if one is clearly most relevant to teachers/parents (exam strategy, content decisions, student learning insights).

Extract: the decision, the reasoning (why), and what it reveals about students or exam prep — not the product engineering angle.

**`linear EP-XX` (fetch a Linear issue):**
Use Linear MCP to fetch the specified issue. Extract: what was built and — critically — why it helps students. Focus on the student outcome, not the engineering process.

**`posthog` (pull metrics):**
Use PostHog MCP to query key product metrics. Pick the most educationally meaningful metric (not the business metric). Example: "students spent 3x longer on worked examples than practice questions" is a LinkedIn post. "We hit 1,000 sessions" is an X post.

Extract: the metric, what it reveals about how students actually learn or use exam prep tools.

**`git` (recent commits):**
```bash
git -C $SPYGLASS_PRODUCT_REPO log --oneline -10 --since="7 days ago"
```
Extract: what was built, and what pedagogical problem it solves. Frame the build, not the engineering.

**`manual` (freeform input / default):**
Take the user's input directly. Identify whether this is an educator insight, a milestone, a behind-the-scenes teaching moment, or an educator-recognition post. Expand into the correct format.

### Step 2 — Determine format

If `--type` was specified, use it. Otherwise:

- Default to `post`
- Upgrade to `article` if: the content warrants 800+ words of structured argument, or the user explicitly says "deep dive" or "think piece"
- Upgrade to `carousel-outline` if: the content is a numbered list (3-7 items) that each need a paragraph of explanation

### Step 3 — Apply the angle adaptation

Before drafting, explicitly state the frame shift:

> "X frame would be: [X version]. LinkedIn frame will be: [LinkedIn version]."

This forces the right lens before a single word is written. If you cannot articulate the LinkedIn frame, ask Teresa for her educator perspective on the source material before proceeding.

### Step 4 — Generate draft

**For posts (`post`):**

Load `build-in-public/templates/linkedin-post.md`. Generate a text post, 1,000-1,500 characters.

Rules:
- Determine post-type: insight, milestone, teaching-moment, educator-recognition, or behind-the-scenes
- Hook in first 2 lines (under 210 characters). Never start with "I" or "Excited to share."
- No links in post body. If a link is needed, end post with "Link in comments." Add `[COMMENT: paste link here]` below draft.
- 3 hashtags max at the end
- At least one specific detail: a student observation, a data point, a named exam topic, or a concrete outcome
- Line break between every paragraph

**For articles (`article`):**

Load `build-in-public/templates/linkedin-article.md`. Generate structured article, 800-1,500 words.

Rules:
- Title: specific and useful. Not vague.
- Opening: the problem and who it's for. No intro preamble.
- H2 sections with one idea each
- Flag all exam-board-specific claims with `[VERIFY]`
- Natural reference to ExamPilot if directly relevant — once only, never forced

**For carousel outlines (`carousel-outline`):**

Do not draft the full carousel (that requires design). Instead produce:
- Title slide copy (headline + subtitle)
- 6-10 slide titles with 1-2 bullet points per slide of what to include
- Final slide CTA copy
- Notes on what visual/example would work on each slide

### Step 5 — Scrub pass

Check the draft against these rules:
- No banned phrases: "game-changer", "revolutionary", "in today's digital landscape", "it's worth noting", "moreover", "furthermore", "in conclusion", "I'm excited to share", "proud to announce", "thrilled"
- No AI tells: "comprehensive", "robust", "cutting-edge", "seamless", "delve", "foster", "landscape", "testament"
- No links in post body (for posts)
- Post is 1,000-1,500 characters (for posts)
- Hook is under 210 characters and does NOT start with "I"
- Voice reads as educator-parent, not marketing copy or tech founder
- At least one specific, concrete detail (not vague generalisation)

If any rule is violated, fix it before showing the draft.

### Step 6 — Human review

Show the draft inline. Then ask:

1. "Does this sound like Teresa the educator, not Teresa the co-founder?"
2. "Any specific student observations, class experiences, or personal details to add?"
3. "Any [VERIFY] flags to resolve before this goes live?"

Wait for edits. Apply any changes Teresa requests.

### Step 7 — Save

Save the approved draft to:
- Posts: `build-in-public/pipelines/outreach/linkedin-post-teresa-{slug}-YYYY-MM-DD.md`
- Articles: `build-in-public/pipelines/outreach/linkedin-article-teresa-{slug}-YYYY-MM-DD.md`
- Carousel outlines: `build-in-public/pipelines/outreach/linkedin-carousel-teresa-{slug}-YYYY-MM-DD.md`

Apply YAML frontmatter from the appropriate template.

Remind: "Draft saved. Copy to Postiz to schedule. No auto-publish. Resolve any [VERIFY] flags before posting."
