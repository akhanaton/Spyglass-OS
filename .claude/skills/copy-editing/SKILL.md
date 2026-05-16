---
name: copy-editing
description: Polish existing ExamPilot copy — blog drafts, landing pages, emails, Reddit posts. Applies the brand voice guardrails, removes AI tells, fixes sentence rhythm, and tightens copy without changing the argument or keyword placement.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

A surgical edit pass on copy that is mostly right but needs polish. Different from `/rewrite` (which is SEO-focused and may restructure content) and `/scrub` (which removes AI watermarks only). This skill applies all six edit passes: AI tell removal, em-dash removal, sentence rhythm, vague word replacement, voice check, and a before/after showcase of the most impactful edit.

The skill surfaces changes as an annotated list. The user applies the edits. Nothing is auto-saved.

**Bike Method Phase 1:** This skill produces an edit list and stops. The user decides what to apply.

## When `/copy-editing` runs

- A blog draft, landing page, or email is written and needs polish before review
- Copy feels stiff, corporate, or AI-generated but the argument is sound
- User asks to "clean up", "tighten", "polish", or "edit" existing copy
- After `/write-article` or `/copywriting` before moving to the review queue

## Context files — read at session start

```bash
cat references/voice-house.md
```

## Execution — six passes

### Step 0 — Confirm input

Ask for (or accept):
1. The copy to edit (paste or file path)
2. Content type: blog article | landing page | email | Reddit post | other

Show: *"Running 6-pass edit on [content type]. I'll flag changes without rewriting the argument or moving keywords. Ready."*

Do not proceed without the copy.

---

### Pass 1: AI tell removal

Scan for these phrases and flag every instance with a suggested replacement:

| AI tell | Replace with |
|---|---|
| "in today's world" / "in today's digital world" | delete or reframe to specific context |
| "let's dive in" / "let's explore" | delete — go straight to the content |
| "it's worth noting that" | delete — just say the thing |
| "at the end of the day" | be specific about what the conclusion actually is |
| "seamlessly" | delete or replace with what actually happens |
| "leverage" (as a verb) | "use", "apply", "build on" |
| "delve into" | "look at", "cover", "examine" |
| "navigate the complexities of" | be specific about what the complexity is |
| "tapestry" | never — delete and rephrase |
| "foster" | "build", "create", "develop" |
| "comprehensive guide to" | name what the article actually covers |
| "in conclusion" / "to summarise" | delete the signpost — just write the conclusion |
| "it's important to" / "it's crucial to" | delete — if it matters, the copy makes it matter |
| "game-changing" / "revolutionary" | delete — show the change, don't label it |
| "empower" | "help", "let", "give students the ability to" |

Output format for each flag:
```
AI tell found: "[original phrase]"
In context: "...full sentence containing the phrase..."
Suggested fix: "[replacement sentence]"
```

---

### Pass 2: Em-dash removal

Find every em dash (—) and flag it with the correct replacement:

**Rules:**
- Em dash before a clause (adds extra information) → comma
- Em dash before an explanation or definition → colon
- Two em dashes in one sentence → split into two sentences with a period

Output format for each flag:
```
Em dash found: "[original sentence with — ]"
Rule applied: [comma | colon | split to two sentences]
Suggested fix: "[corrected sentence]"
```

Flag count at the end: "[N] em dashes found and corrected."

---

### Pass 3: Sentence rhythm

Read through all sentences and flag any run of 3 or more consecutive sentences that are all within 5 words of each other in length (creates monotonous rhythm).

Suggest one restructuring where:
- One sentence is short (under 10 words)
- One sentence is medium (15-20 words)
- One sentence is longer (25-30 words)

Output format:
```
Rhythm issue found: [paragraph or section reference]
Original sentences:
  "[S1]" ([N] words)
  "[S2]" ([N] words)
  "[S3]" ([N] words)
Suggested restructuring:
  Short: "[revised short sentence]"
  Medium: "[revised medium sentence]"
  Long: "[revised longer sentence]"
```

If no rhythm issues are found, state: "Sentence rhythm: no monotony detected."

---

### Pass 4: Vague word replacement

Flag every instance of these words and suggest a more specific replacement:

| Vague word | What to do |
|---|---|
| "many" | Replace with a number, "most [audience]", or "the majority of 9709 students" |
| "some" | "some students" (acceptable) or be specific |
| "various" | List the things. "Various topics" → "topics including [A], [B], and [C]" |
| "often" | When exactly? "Before mock exams", "in the final 4 weeks" |
| "sometimes" | Same — when? |
| "typically" | What is typical? Name it. |
| "significant" | How significant? Give a number or comparison. |
| "very" | Delete or replace with a specific intensifier. "Very difficult" → "the hardest topic in Pure 1" |
| "really" | Delete or rewrite the sentence to be inherently strong without it |
| "quite" | Delete — it weakens. "Quite hard" → "hard" |
| "things" | Name them. "These things" → "these topics / these questions / these skills" |
| "good" / "great" | What makes it good? Name the quality. |

Output format for each flag:
```
Vague word: "[word]"
In context: "...full sentence..."
Suggested fix: "[more specific replacement]"
```

---

### Pass 5: Voice check

Read for brand voice alignment against `references/voice-house.md`. Flag any sentence that sounds institutional, corporate, or teacher-to-student rather than confident-peer.

**Institutional phrases to flag:**
- "our platform provides" → "ExamPilot [does the specific thing]"
- "our solution enables" → "you can [specific action]"
- "we strive to" → delete — describe what it does, not what you aspire to
- "students are helped by" → "ExamPilot helps you" or rewrite in active voice
- "this tool is designed to" → "ExamPilot [does the thing]"
- Any third-person reference to the reader: "students can use this to..." → "you can..."

**Tone checks:**
- Is it direct? (Does it answer the question without preamble?)
- Is it peer-level? (Could a confident older student have written this?)
- Is it specific to A-Level Maths? (Or could it apply to any revision app?)

Output format for each flag:
```
Voice issue: [institutional | passive | wrong-person | generic]
Original: "[sentence]"
Suggested fix: "[revised sentence addressing student directly]"
```

---

### Pass 6: Final before/after

Identify the single paragraph or section where the combined edits have the most impact. Show a full before/after:

```
Most impactful edit — [section name or first few words]:

BEFORE:
"[original paragraph, unedited]"

AFTER:
"[paragraph with all Pass 1-5 edits applied]"

Changes applied: [list which passes fired on this paragraph]
```

---

### Output format

Present all six passes in sequence:

```
Copy-editing report: [content type]
---

Pass 1: AI tells
  [findings or "None found"]

Pass 2: Em dashes
  [findings or "None found"]

Pass 3: Sentence rhythm
  [findings or "No monotony detected"]

Pass 4: Vague words
  [findings or "None found"]

Pass 5: Voice check
  [findings or "Voice is on-brand"]

Pass 6: Before/after showcase
  [most impactful edit]

---
Summary: [N] AI tells | [N] em dashes | [N] rhythm issues | [N] vague words | [N] voice flags
Next step: Apply edits manually, then move to review queue — or say "save the corrected version" to write it to file.
```

**Save path** (only on user instruction): same path as the input file, with `-edited` appended before the date. Example: `marketing/pipelines/drafts/article-slug-edited-YYYY-MM-DD.md`

## What this skill does NOT do

- Does not rewrite the structure, argument, or keyword placement. Changes are at sentence level only.
- Does not auto-apply edits. The user reviews and applies.
- Does not check SEO signals (keyword density, heading structure, meta). Use `/optimize` for that.
- Does not scrub invisible Unicode characters or hidden AI watermarks — use `/scrub` for that.
- Does not fact-check. [VERIFY] flags from the original draft remain unchanged.
- Does not save anything without explicit user instruction.
