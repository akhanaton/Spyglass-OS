---
name: pre-write
description: Scaffold a Sanity CMS JSON structure for ExamPilot product content pages before writing begins. Determines content type, maps content to Sanity block types, and writes a validated scaffold to /Users/enitan/Documents/Projects/spyglass/scripts/content/. Run before /write-article for any non-blog content type.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Produces a Sanity JSON scaffold for a product content page — topic guides, hub pages, comparison pages, etc. The scaffold goes into the product repo (`/Users/enitan/Documents/Projects/spyglass/scripts/content/`) and becomes the structural brief for the content writer (or `/write-article` for blog posts).

**Bike Method Phase 1:** The scaffold must be reviewed by a human before any content is written against it. It is a structural plan, not final content.

## When `/pre-write` runs

- Before writing any non-blog ExamPilot product page
- When a new topic needs a Sanity JSON structure
- When adding a new content type to the pipeline

## Gold standard reference

Always read this before producing any scaffold:

```bash
cat /Users/enitan/Documents/Projects/spyglass/scripts/content/topics/cambridge-9709-pure-1/integration.json
```

That file is the canonical reference. Every scaffold you produce must be structurally consistent with it. Key things to observe:
- Top-level keys: `type`, `topicName`, `definition`, `metadata`, `assets`, `keyFormulas`, `examTips`, `workedExamples`, `practiceQuestions`, `commonMistakes`, `faq`
- The `metadata.seo` object: `metaTitle`, `metaDescription`
- How `mathBlock`, `calloutBlock`, `workedSolution`, `comparisonTable`, `image`, `list`, and `paragraph` types are structured within arrays
- How `workedSolution.steps` uses `math` (LaTeX string) and `annotation` (plain English)

## Content type taxonomy

| Type | Folder | When to use |
|---|---|---|
| `topicPage` | `topics/cambridge-9709-pure-1/` or `topics/edexcel-ial/` | Individual syllabus topics (integration, differentiation, vectors) |
| `hubPage` | `hubs/` | Topic cluster hub (Pure 1 hub, Statistics hub) |
| `featurePage` | `features/` | Product feature explanation (ERI, Ask Sparky, Smart Review) |
| `audienceSegmentPage` | `audience-segments/` | Segment landing (resit students, tutors, Cambridge students) |
| `alternativePage` | `alternatives/` | Competitor comparison (ExamPilot vs X) |
| `bestOfPage` | `best-of/` | Resource roundups (best 9709 revision resources) |
| `locationPage` | `countries/` | Country/region landing (A-Level Maths in Malaysia) |
| `pastPapersHub` | `hubs/past-papers/` | Past papers index and navigation |
| `qualificationSpoke` | `qualification-spokes/` | Qualification overview (Cambridge 9709, Edexcel IAL) |
| `landingPage` | `blog/` | Blog posts (use /write-article instead for blog content) |

## Sanity block types reference

| Block type | Use for | Key fields |
|---|---|---|
| `paragraph` | Prose text | `text` |
| `heading` | Section headers within content arrays | `level` (2-4), `text` |
| `mathBlock` | LaTeX equations | `latex`, `displayMode` (bool), `caption` |
| `calloutBlock` or `callout` | Tips, warnings, key facts | `variant` (exam-tip/warning/key-fact), `title`, `body` (array of strings) |
| `workedSolution` | Exam-style worked examples | `question`, `difficulty` (easy/medium/hard), `marks`, `steps[]` (each: `math`, `annotation`) |
| `comparisonTable` | Feature or technique comparisons | `caption`, `headers[]`, `rows[]` (each: `cells[]`, `highlight` bool) |
| `image` | Diagrams and visual assets | `file`, `alt`, `caption` |
| `list` | Numbered or bulleted lists | `style` (numbered/bulleted), `items[]` |
| `codeBlock` | Code examples | `language`, `code` |
| `faq` | FAQ pairs | `question`, `answer` |
| `ctaBlock` | Call to action | `variant`, `text`, `href` |

## Asset specifications

Visual assets are specified in the `assets` array and referenced by `file` name in content blocks.

| Diagram type | Tool | File format |
|---|---|---|
| Mathematical graphs, curves, shaded regions | matplotlib or Desmos | `.svg` |
| Decision flowcharts, process diagrams | Excalidraw | `.svg` |
| Comparison diagrams | Excalidraw | `.svg` |
| Step-by-step worked example illustrations | matplotlib | `.svg` |

Asset naming convention: `{topic}-{description}.svg`
Examples: `integration-method-flowchart.svg`, `integration-area-under-curve.svg`

Each asset entry needs: `file`, `label`, `alt` (screen-reader description of what the diagram shows), `caption`.

## Execution — five steps

### Step 1 — Classify and confirm

From the user's input or research brief, determine:

1. **Content type** — which of the 10 types fits?
2. **Exam board** — Cambridge 9709 or Edexcel IAL?
3. **Slug** — URL-safe, lowercase, hyphenated (e.g. `integration`, `pure-1-hub`, `examPilot-vs-x`)
4. **Output path** — which folder in the product repo?

Show a one-line summary:
> "Content type: topicPage | Exam board: Cambridge 9709 | Slug: vectors | Output: topics/cambridge-9709-pure-1/vectors.json"

Ask for confirmation before proceeding.

---

### Step 2 — Plan the content structure

Map what this page needs against the block types available:

- What sections are needed? (headings)
- Where do mathematical equations appear? (mathBlock)
- What worked examples are needed? (workedSolution — plan 2-3 minimum for topic pages)
- What visual assets are needed? (list each with a description of what it should show)
- What comparison tables are useful? (comparisonTable)
- What callouts should be included? (exam-tip, warning, key-fact variants)
- What FAQ questions will students ask? (4-6 minimum)

Output this as a content plan (plain language list, not JSON yet). Ask: *"Does this structure look right before I build the scaffold?"*

---

### Step 3 — Build the scaffold

Produce the full JSON scaffold following `integration.json` structure.

**Mandatory fields for every scaffold:**

```json
{
  "type": "[contentType]",
  "topicName": "[Human-readable name]",
  "definition": "[One-sentence definition for schema.org and GEO — complete standalone sentence]",
  "metadata": {
    "title": "[H1 title]",
    "slug": "[url-slug]",
    "topicName": "[Same as root topicName]",
    "definition": "[Same as root definition]",
    "practiceCtaText": "[CTA text for the practice button — specific to this topic]",
    "parentHub": "[parent hub slug]",
    "seo": {
      "metaTitle": "[50-60 chars including primary keyword]",
      "metaDescription": "[150-160 chars — direct answer to the searcher's intent]"
    }
  },
  "assets": [],
  "keyFormulas": [],
  "examTips": [],
  "workedExamples": [],
  "practiceQuestions": [],
  "commonMistakes": [],
  "faq": []
}
```

Rules:
- `definition` must be a complete standalone sentence (used by AI search engines for entity extraction)
- `practiceCtaText` must be specific to the topic — not generic "Practice now"
- `metaTitle` must include the primary keyword and fit within 60 characters (count carefully)
- `metaDescription` must directly answer the searcher's main question
- LaTeX in `mathBlock` uses double-escaped backslashes in JSON: `\\int` not `\int`
- `workedSolution.steps` must have at minimum 3 steps; each `annotation` must explain the mathematical reasoning in plain English, not just describe the algebra
- Every `callout` must have a `title` and at least one string in the `body` array
- Flag uncertain exam-board-specific facts with `"[VERIFY]"` as a suffix in the relevant text field

---

### Step 4 — Anti-regression checklist

Before saving, verify:

- [ ] All `mathBlock` entries have `displayMode` boolean set
- [ ] All `workedSolution` entries have `difficulty` and `marks` set
- [ ] All `image` references in content arrays match a file listed in the `assets` array
- [ ] `metaTitle` is ≤60 characters (count them)
- [ ] `metaDescription` is 150-160 characters (count them)
- [ ] `definition` is a complete sentence (not a fragment)
- [ ] No em-dashes (—) in any text fields — use comma, semicolon, or period
- [ ] `[VERIFY]` appended to any unverified exam-board fact, mark allocation, or percentage
- [ ] ExamPilot brand language correct: no "AI tutor", "AI wrapper", "AI-powered"

---

### Step 5 — Save and report

**Output path:** `/Users/enitan/Documents/Projects/spyglass/scripts/content/[folder]/[slug].json`

Write the scaffold using the Write tool. Do not commit to git — that is the developer's responsibility after human review.

**One-screen close:**
```
Scaffold saved: /Users/enitan/Documents/Projects/spyglass/scripts/content/[path]
Content type: [type]
Sections planned: [n] (keyFormulas, examTips, workedExamples, FAQ)
Assets specified: [n] visual assets
[VERIFY] flags: [count] — resolve against official Cambridge/Pearson sources before production

Next step: Human review → developer ingests to Sanity → /write-article for any companion blog content
```

## Readiness checklist before /write-article

The scaffold is complete when:
- [ ] Human has reviewed and approved the structure
- [ ] All [VERIFY] flags resolved or escalated
- [ ] Asset descriptions are clear enough for a designer to create them
- [ ] Worked examples have real mathematical content (not placeholder text)
- [ ] FAQ questions match what students actually search for (not SEO-speak)

## What this skill does NOT do

- Does not ingest the scaffold into Sanity — that is the developer's job
- Does not write blog articles — use `/write-article` for those
- Does not produce the visual assets — it specifies them for the designer
- Does not auto-publish or commit to git
