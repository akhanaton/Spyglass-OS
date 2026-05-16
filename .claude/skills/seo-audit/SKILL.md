---
name: seo-audit
description: Comprehensive SEO health check for ExamPilot content. Audits crawlability, on-page optimization, keyword health, internal linking structure, and E-A-T signals. Run on individual articles or as a monthly batch audit.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Runs a comprehensive SEO health check on ExamPilot content. Different from `/optimize` (which is article-specific and produces a rewrite brief) — this is a structured audit that scores content against defined criteria and produces an action list. Works on a single article, a URL, or all articles in `marketing/pipelines/published/` as a batch.

## When `/seo-audit` runs

- Monthly batch audit of all published content
- Before moving a draft from `review/` to `published/`
- When a page's ranking position is declining unexpectedly
- When the user asks "is this article SEO-ready?" or "audit this content"

## Context files — read at session start

```bash
cat marketing/context/content-standards.md
cat marketing/context/internal-links-map.md
```

If batch mode: also read the list of published articles:
```bash
ls marketing/pipelines/published/
```

## Execution — five steps

### Step 1 — Identify input mode

Determine which mode applies:

| Mode | Input | Action |
|---|---|---|
| Single file | File path to a `.md` file | Audit that file |
| URL | A URL string | Read the URL content if accessible; otherwise ask user to paste the content or provide the file path |
| Batch | User says "batch" or "all articles" | Audit every file in `marketing/pipelines/published/` |

For batch mode, confirm before running: "Found [n] articles in published/. Running batch audit — this may take a moment."

---

### Step 2 — Load the article

For each article being audited:
- Read the full file content including YAML frontmatter
- Extract: `title`, `meta_title`, `meta_description`, `url_slug`, `primary_keyword`, `word_count_target`, `status`, `date`
- Note any missing frontmatter fields immediately — they count against Dimension 1

---

### Step 3 — Run 6 audit dimensions

Score each dimension: **Pass** (full points) / **Partial** (half points) / **Fail** (zero points).

---

#### Dimension 1: Crawlability & Indexation (max 15 points)

| Check | Points | Pass condition |
|---|---|---|
| YAML frontmatter complete | 5 | All required fields present: title, meta_title, meta_description, url_slug, primary_keyword, status, date |
| url_slug format | 5 | Follows `/blog/[slug]` or `/cambridge/[topic-slug]` pattern. No spaces. Lowercase. Hyphens only. |
| No accidental noindex signals | 5 | No `noindex: true` in frontmatter unless intentional. Flag if present. |

**Partial scoring:** If 2 of 3 YAML fields are missing, score Partial on the frontmatter check.

---

#### Dimension 2: On-Page Optimization (max 25 points)

| Check | Points | Pass condition |
|---|---|---|
| H1 contains primary keyword | 5 | Primary keyword (or close variant) appears in the H1. Exact match not required — semantic match acceptable. |
| Meta title length and keyword | 5 | 50-60 characters. Contains primary keyword. No keyword stuffing. |
| Meta description quality | 5 | 150-160 characters. Contains primary keyword. Ends with an action-oriented phrase or implied CTA. |
| Keyword in first 100 words | 5 | Primary keyword appears within the first 100 words of body content (not counting frontmatter). |
| Keyword density | 5 | 1-2% density. Count occurrences / total word count. Flag if >2.5% (stuffing) or <0.5% (underuse). |

---

#### Dimension 3: Content Quality (max 25 points)

| Check | Points | Pass condition |
|---|---|---|
| Word count | 5 | ≥1800 words (body content, excluding frontmatter). |
| Heading structure | 5 | 4-7 H2 sections. At least 2 H3s under H2s. No skipped heading levels (no H4 without H3). |
| FAQ section | 5 | Present with minimum 4 Q&A pairs. Formatted as questions in H3 with answer in paragraph below. |
| Key Takeaways block | 5 | Present immediately after introduction. 3-4 bullet points. Each is a standalone claim with specifics. |
| Reading level | 5 | Appropriate for 16-18 year olds. Paragraphs ≤4 sentences. No academic jargon without explanation. Assess qualitatively. |

---

#### Dimension 4: Internal Linking (max 15 points)

| Check | Points | Pass condition |
|---|---|---|
| Internal link count | 5 | 3-5 internal links present. Fewer than 3: Fail. More than 5: Partial (over-dilution risk). |
| Link target validity | 5 | Link targets match known ExamPilot URLs from `internal-links-map.md` or are clearly valid product pages (/pricing, /cambridge-a-level-maths/). Flag any link to a slug not in the map as "unverified — check before publishing". |
| Anchor text quality | 5 | Anchor text is descriptive. No instances of "click here", "read more", "here", or "this article". |

---

#### Dimension 5: External Linking (max 10 points)

| Check | Points | Pass condition |
|---|---|---|
| External link count | 5 | 2-3 external authority links present. Zero external links: Fail. More than 4: Partial. |
| External link quality | 5 | Links point to Cambridge Assessment, Pearson, Ofqual, or other .edu, .gov, .ac.uk domains. No links to competitor sites (SaveMyExams, PapaCambridge) in body content. |

**Note:** External link validity (not broken) requires manual check. Flag all external links as "verify live before publishing."

---

#### Dimension 6: E-A-T Signals (max 10 points)

| Check | Points | Pass condition |
|---|---|---|
| [VERIFY] flags resolved | 4 | Zero unresolved [VERIFY] flags remaining in the content. Any present = Fail on this check. |
| Author attribution | 3 | `author` field present in frontmatter. For published content, author bio or byline should exist. |
| Source citation for statistics | 3 | Any statistic or numerical claim cites a named source with date. "Studies show..." without a source = Partial. |

**GEO bonus check (informational, no points deducted for failure):**
- Does each H2 section open with a complete, extractable answer in the first 2-3 sentences?
- Are full entity names used on first mention ("Cambridge International AS & A Level Mathematics 9709" not just "Cambridge A-Level")?
- Note GEO gaps as Optional actions.

---

### Step 4 — Calculate and present the score

**Total possible: 100 points**

| Score range | Health status | Action |
|---|---|---|
| 85-100 | Healthy | Ready for publishing / no urgent action |
| 70-84 | Good | 1-3 important fixes before next update |
| 50-69 | Needs work | Fix Critical and Important issues this sprint |
| Below 50 | Critical | Do not publish / unpublish if live; major revision required |

**Present the score like this:**

```
SEO Audit: [Article title or batch summary]
Date: 2026-05-16

Dimension Scores:
  Crawlability & Indexation    [X]/15
  On-Page Optimization         [X]/25
  Content Quality              [X]/25
  Internal Linking             [X]/15
  External Linking             [X]/10
  E-A-T Signals                [X]/10
  ─────────────────────────────────
  Total                        [X]/100
  Health status: [Healthy / Good / Needs Work / Critical]
```

---

### Step 5 — Action list

Categorize every failing or partial check into:

**Critical (block publishing):**
Issues that would actively harm SEO or user trust. Fix before moving to published/.
- Examples: missing meta title/description, zero internal links, unresolved [VERIFY] flags, word count below 1500

**Important (fix this sprint):**
Issues that meaningfully reduce performance but don't block publishing.
- Examples: keyword density out of range, FAQ section has only 3 Q&As, anchor text uses "click here"

**Optional (nice to have):**
GEO improvements, additional external links, minor style fixes.

For batch mode: produce a summary table sorted worst score to best:

```
Batch Audit Summary — [date]
| Article | Score | Health | Top Critical Issue |
|---------|-------|--------|-------------------|
| ...     | ...   | ...    | ...               |
```

---

### Step 6 — Save output

**Single article:** Save to `marketing/pipelines/research/seo-audit-[slug]-YYYY-MM-DD.md`

**Batch:** Save to `marketing/pipelines/research/seo-audit-batch-YYYY-MM-DD.md`

Frontmatter for the audit file:
```yaml
---
type: seo-audit
mode: single | batch
article: "[slug or batch]"
score: [n]
health: healthy | good | needs-work | critical
date: YYYY-MM-DD
---
```

Announce save path and top 3 critical issues at close.

## What this skill does NOT do

- Does not rewrite articles. For rewrites, run `/rewrite` or `/optimize` using this audit as input.
- Does not check live URL status (external links). Flags them for manual verification.
- Does not run DataForSEO rank data. For rank position data, use the `seo-analytics-stack.md` data module commands.
- Does not publish content. Publishing is always a manual step.
