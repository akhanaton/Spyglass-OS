---
name: repurpose
description: Converts a published or draft article into channel-specific versions. Outputs Reddit post, 3-email sequence, and TikTok script placeholder.
---

## Input

$ARGUMENTS

Expect: file path to a published or draft article. Examples:
- `marketing/pipelines/published/cambridge-9709-integration-tips-2026-03-10.md`
- `marketing/pipelines/drafts/edexcel-wma11-statistics-2026-05-01.md`

If no file path given, ask. If given a keyword instead, check `marketing/pipelines/published/` for a matching article.

## Execution

### Step 1: Read the source article

Read the full article. Extract:
- Title and primary keyword
- Key insight or surprising finding (for Reddit hook)
- 3-4 most actionable tips or steps
- Target audience segment (from frontmatter `target-segment:`)
- URL slug (for links)
- Any statistics or specific claims (carry [VERIFY] flags forward)

### Step 2: Load channel context

Read these in parallel:
- `marketing/references/repurposing-playbook.md` — repurposing rules and channel-specific guidelines
- `marketing/context/channel-playbooks.md` — operational rules per channel (Reddit, email, TikTok)
- `marketing/context/audience-segments.md` — tone and messaging for the target segment

### Step 3: Generate Reddit version

**Subreddit selection:**

Map audience segment to subreddit:
- `student-cambridge` → r/alevel (primary), r/CambridgeInternational (secondary)
- `student-edexcel` → r/alevel (primary), r/Edexcel (secondary)
- `resit-student` → r/alevel
- `general` → r/6thForm, r/alevel

Choose ONE primary subreddit. Note secondary option.

**Post structure (200-400 words):**

1. Hook (1-2 sentences): Start with a surprising stat, counterintuitive point, or specific question from the article. No "I wrote this article" framing. Example format: "Most students revising for 9709 P1 spend 80% of their time on the wrong topics."

2. Value body (3-4 tips): Extract 3-4 actionable, specific points from the article. Write each as a practical tip, not a summary. Use "you" not "students". Use bullet points.

3. Close (optional, 1-2 sentences): If including ExamPilot mention, lead with "I built a tool for this" style — never "check out ExamPilot". Keep it soft. Only include if article is MOFU/BOFU stage.

Rules:
- No em dashes
- Short sentences (2-3 per paragraph max)
- Specific exam board names in full on first mention
- [VERIFY] any facts carried from source article
- No "in conclusion", "in summary", or "I hope this helps"
- Title format options: question, counterintuitive claim, or specific promise ("How I went from failing 9709 P1 to an A in 6 weeks")

Save to `marketing/pipelines/outreach/reddit-[sub]-[slug]-YYYY-MM-DD.md`

```yaml
---
type: reddit-post
channel: reddit
subreddit: r/[name]
stage: [tofu|mofu|bofu]
target-segment: [segment]
source_article: [path]
status: drafted
created: YYYY-MM-DD
---
```

### Step 4: Generate email sequence (3 emails)

Target: Brevo email list. Mobile-first. Under 200 words each.

**Email 1 — Day 1: Hook + problem + article link**

Subject line: [Specific, student-relevant, no spam words]
Preview text: [Extends subject line, < 90 chars]

Structure:
- Opening: 1-2 sentences establishing the pain point this article solves
- Value bridge: 2-3 sentences on what they'll get from reading
- CTA button: "Read the guide →" linking to the article URL
- No ExamPilot pitch in Email 1

**Email 2 — Day 4: Go deeper on one tip**

Subject line: [Teases a single insight from the article, not covered in Email 1]
Preview text: [Sets up the insight]

Structure:
- Pick ONE tip from the article and expand it with 2-3 sentences of additional depth
- 2-3 practical sentences on HOW to apply it this week
- CTA: soft — "If this helped, [article link] has 3 more techniques like this"
- Optional soft mention: "I built ExamPilot to automate this for you — [link to free trial]"

**Email 3 — Day 8: Social proof + final CTA**

Subject line: [Outcome-focused. Student result or achievement angle]
Preview text: ["Here's what worked for [student type]..."]

Structure:
- 2-3 sentences of social proof: a specific student type outcome (no fabricated quotes — use outcome framing: "Students who use spaced repetition for 9709 P1 topics score an average of X% higher" — [VERIFY] or remove)
- Brief ExamPilot pitch: 1-2 sentences maximum, benefit-first
- CTA button: "Start free" or "Try ExamPilot free" with trial link

Each email: plain text preferred, max 1 image if any, single CTA per email.

Save all 3 to `marketing/pipelines/emails/sequence-[slug]-YYYY-MM-DD.md`

```yaml
---
type: email-sequence
channel: email
emails: 3
source_article: [path]
target-segment: [segment]
status: drafted
created: YYYY-MM-DD
---
```

### Step 5: Generate TikTok script (P2 placeholder)

> NOTE: This is a Phase 2 asset — TikTok channel is not yet active. Save now, produce when ready.

**Script structure (30-60 seconds):**

Hook (0-3 seconds): Single question or shocking fact. Must work as on-screen text + voiceover. Example: "Most 9709 students revise the wrong topics. Here's what the data says."

Body (3-45 seconds): 2-3 key points in exam-tip format:
- Keep each point to 1 sentence + 1 supporting example
- Use exam-specific language (paper codes, topic names, mark schemes)
- Visual cue suggestions: [show past paper] [highlight formula] [show before/after score]

CTA (45-60 seconds): "Follow for A Level Maths revision tips. Link in bio for free practice questions."
- Never "download ExamPilot" at Phase 2 — brand awareness only

On-screen text recommendations: [list key phrases to display as text overlays]
Suggested audio: [trending audio note — update when producing]

Save to `marketing/pipelines/tiktok/script-[slug]-YYYY-MM-DD.md`

```yaml
---
type: tiktok-script
channel: tiktok
phase: P2
source_article: [path]
target-segment: [segment]
duration: 30-60s
status: placeholder
created: YYYY-MM-DD
---

[P2 — TikTok Phase 2. Requires video production. Do not activate until TikTok channel is live.]
```

### Step 5.5: Generate X version (build-in-public)

> Target audience: founders and builders (NOT students). Extract the BUILD process from the article, not the exam content.

Read `context/.whoami` to determine the author. Load `references/voice-{author}.md`.

**Standalone tweet:**

Extract one process insight from the article. What did we learn about BUILDING this content, not what the content teaches students?

Good examples:
- "Just published our 10th article on Cambridge 9709 revision. The internal linking alone took 2 hours. Here's what we learned about topical authority."
- "Wrote 3,000 words on integration techniques today. The Python content scorer gave it a 72. Tweaking the structure until it hits 80."

Bad examples:
- "Here's how to revise for 9709 Paper 1" (student content, not builder content)
- "Check out our latest article!" (marketing, not build-in-public)

Max 280 characters. No links (put in self-reply). No em dashes. No banned phrases.

**Thread flag:** If the article's creation involved an interesting multi-step process, decision, or failure, flag it: "[THREAD CANDIDATE] This article's creation story could make a good weekly thread. Run `/write-x --type thread` to expand."

Save tweet to `marketing/pipelines/outreach/x-post-{author}-{slug}-YYYY-MM-DD.md`

```yaml
---
type: x-post
channel: x
author: {author}
audience: founder
post-type: milestone
source: repurpose
source_article: {path}
status: drafted
date: YYYY-MM-DD
---
```

### Step 6: Show all outputs and prompt

Display all four versions (Reddit, Email Sequence, TikTok placeholder, X tweet) inline.

Ask: "Four repurposed assets created from '[article title]'. Which do you want to review first?
- Reddit post for [subreddit]
- Email sequence (3 emails for Brevo)
- TikTok script (P2 placeholder)
- X tweet (build-in-public)

Or say 'all look good' to move on."

Note: never auto-publish. All outputs go to `review/` when approved. Remind user to resolve any carried [VERIFY] flags before publishing.
