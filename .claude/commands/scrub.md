---
name: scrub
description: Remove AI watermarks from a draft article — invisible Unicode chars, em-dash normalization, and AI-tell phrase flagging. Run on any draft before the quality gate. Wraps content_scrubber.py.
---

## Input

$ARGUMENTS

Expect: file path to a markdown article draft. Example:
- `marketing/pipelines/drafts/cambridge-9709-integration-2026-05-16.md`

If no file path given, ask: "Which draft should I scrub? Give me the file path."

## Execution

### Step 1: Verify file

Check the file exists at the given path. If it does not, surface the error immediately and stop.

If the file exists, read it and note the approximate word count.

### Step 2: Run the scrubber module

```bash
python3 marketing/data_sources/modules/content_scrubber.py [filepath] --report
```

If the module is available, use it. The --report flag returns a structured diagnostic without modifying the file. Review the output before applying changes.

If the module is not available, proceed to Step 3 and apply the rules inline.

### Step 3: Apply scrub rules

Apply these changes to the article content. Each is a mechanical fix — no editorial judgment required. Apply all of them:

**Invisible character removal:**
- Zero-width spaces (U+200B) → remove entirely
- Soft hyphens (U+00AD) → remove entirely
- Byte order marks (U+FEFF) → remove entirely
- Non-breaking spaces (U+00A0) → replace with regular space

**Em-dash normalization:**
Every em-dash (—) must be replaced. Context determines the replacement:
- Mid-sentence break (separates two related clauses): replace with a comma
- Before an explanation or elaboration: replace with a colon
- Parenthetical aside: replace with round brackets, or split into two sentences
- After a list item label: replace with a colon

Zero em-dashes should remain in the output. Do a final scan to confirm.

**Whitespace cleanup:**
- Three or more consecutive blank lines → collapse to two blank lines
- Trailing spaces at the end of any line → remove

### Step 4: Flag AI tell phrases

Do NOT auto-remove these. Identify every instance, show the line number and surrounding sentence, and let the user decide whether to keep, rewrite, or remove.

Phrases to flag:

| Phrase | Why it's flagged |
|---|---|
| "in today's world" | Filler opener — delete or rewrite |
| "let's dive in" | AI cliche — cut or rewrite as "here's what you need to know" |
| "it's worth noting" | Filler hedge — state the point directly |
| "at the end of the day" | Cliche — delete or rewrite |
| "game-changing" | Vague superlative — name the specific impact |
| "comprehensive guide to" | AI pattern — rewrite H1 to be benefit-driven |
| "leverage" (used as a verb) | Jargon — replace with "use", "apply", or "get more from" |
| "seamlessly" | Vague filler — delete or be specific |
| "delve into" | AI pattern — replace with "look at", "work through", or "cover" |
| "navigate" (metaphorical) | Vague — be specific about the action |
| "foster" | AI cliche — replace with "build", "develop", or "create" |
| "tapestry" | AI tell — delete and rewrite the sentence |
| "in conclusion" | Weak closer — cut and restate the core point directly |
| "it is important to note" | Hedge — state the point directly |
| "as we can see" | Filler — cut |
| "in summary" | Weak closer — cut |

Format the flags as:
```
AI TELL: Line [n] — "[flagged phrase in context]"
Suggestion: [replacement or action]
```

### Step 5: Report

Show a summary:
```
## Scrub Report: [filename]

**Invisible chars removed:** [count] (zero-width spaces: [n], soft hyphens: [n], BOMs: [n], NBSP: [n])
**Em-dashes replaced:** [count]
**Whitespace fixes:** [consecutive blank lines collapsed: n, trailing spaces removed: n]
**AI tells flagged:** [count] (see below — user review required)

[list of AI tell flags]
```

If zero changes were made across all categories, note: "No watermarks or AI tells found. Draft is clean."

### Step 6: Confirm next step

After reporting:

"Scrub complete. Review the [n] flagged AI tells above — rewrite or remove each before the quality gate.

Next: run `/optimize [filepath]` to audit SEO health, or run the full agent pipeline via `/write-article` if this is a fresh draft being finalized."
