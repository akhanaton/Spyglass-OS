---
name: seo-quality-check
description: Publishing gate for ExamPilot content. Runs the SEO and LLM optimization checklist against a draft before it moves to review/. Flags issues, scores the content, routes to author for fixes. Does not auto-block — it reports.
bike-method-phase: Machine
attribution: Trailblazer Marketing SEO Brothers corpus (ingested 2026-05-18) + ExamPilot content-standards.md
---

# /seo-quality-check

Run this before any blog article or landing page moves from `drafts/` to `review/`. It applies the full ExamPilot SEO and LLM optimization checklist, scores the content, and surfaces the highest-leverage fixes.

**Trigger:** `/seo-quality-check [file path]` or paste content directly.

---

## Step 1 — Read the content

Read the full draft. If a file path is given, read it. If pasted, use the pasted content.

Identify:
- Content type (blog article / landing page / topic page / comparison page)
- Target keyword (from YAML frontmatter or first paragraph)
- Funnel stage (TOFU / MOFU / BOFU)
- Word count (approximate)

---

## Step 2 — Run the checklist

Score each item: ✅ Pass / ⚠️ Fix / ❌ Fail / N/A

### A. On-Page Fundamentals

| Check | Standard | Score |
|-------|----------|-------|
| Target keyword in H1 | Naturally included, not stuffed | |
| Target keyword in first 100 words | | |
| Keyword density | 0.5–1% (5–10 uses per 1,000 words) | |
| Title tag length | 42–60 characters, keyword front-loaded | |
| Meta description | 150–160 chars, keyword included, CTA present | |
| URL slug | Keyword included, hyphens, ≤60 chars, no dates | |
| Word count | Blog: ≥1,800 words; Pillar: ≥3,000 words; Landing page: ≥800 words | |

### B. Structure and Readability

| Check | Standard | Score |
|-------|----------|-------|
| Answer-first structure | First 2–3 sentences after each H2 = complete extractable answer | |
| Key Takeaways block | 3–5 standalone bullet points immediately after introduction | |
| Paragraph length | ≤4 sentences per paragraph | |
| Heading hierarchy | H1 → H2 → H3 only, no skipped levels | |
| Tables / numbered lists | Used for comparisons and sequential processes | |
| FAQ section | ≥4 Q&A pairs, conversational phrasing, self-contained answers | |

### C. LLM Chunk Optimization

| Check | Standard | Score |
|-------|----------|-------|
| Ancestor headings rule | Every H2 and H3 descriptive enough to stand alone (not "Step 1", "Conclusion", "Overview") | |
| Long-tail conversational headers | ≥2 H2s phrased as natural student questions ("How do I...?", "What is...?", "When should I...?") | |
| Logical connectors | Causal relationships stated explicitly ("Because X, Y happens") where appropriate | |
| Query fan-out links | Article links to ≥3 related subtopic pages that would answer adjacent subqueries | |

### D. Authority and E-E-A-T

| Check | Standard | Score |
|-------|----------|-------|
| Statistics with sources | At least 2 cited statistics with source name and date | |
| Official source links | Links to exam board specs, Ofqual, Cambridge Assessment | |
| Author byline | Author with credentials present on blog posts | |
| Entity naming | Full exam board names used ("Cambridge International AS & A Level Mathematics 9709") | |
| Exam-specific accuracy | All board-specific facts flagged [VERIFY] where uncertain | |

### E. Internal Linking

| Check | Standard | Score |
|-------|----------|-------|
| Minimum internal links | ≥3 contextual internal links for blog articles | |
| Anchor text quality | Descriptive keyword-rich anchor text (not "click here") | |
| No orphan risk | New page will be linked from ≥1 existing page | |
| Pillar link | Blog articles link to their parent pillar/hub page | |

### F. GEO Technical

| Check | Standard | Score |
|-------|----------|-------|
| FAQPage schema | Present (auto-generated from Sanity faq array) | |
| Image alt text | All images have descriptive alt text including target keyword | |
| Last updated date | Visible on page | |
| CTA present | Appropriate for funnel stage | |

### G. Positioning and Voice

| Check | Standard | Score |
|-------|----------|-------|
| No "AI tutor" / "AI wrapper" language | Uses: "learning science", "spaced repetition", "active recall", "exam readiness" | |
| No B2B pricing/licensing language | ExamPilot is always consumer-purchased | |
| Exam board accuracy | Content is specific to the correct exam board (9709 ≠ Edexcel) | |
| No AI filler phrases | No "In today's world", "It's no secret", "At the end of the day", "Let's dive in" | |
| Pricing correct | EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr if mentioned | |

---

## Step 3 — Score and route

Count scores:
- ✅ = 2 points
- ⚠️ = 1 point (fixable but noted)
- ❌ = 0 points

**Score tiers:**

| Score | Verdict | Action |
|-------|---------|--------|
| 90%+ | PUBLISH READY | Minor polish only. Move to `review/`. |
| 75–89% | NEEDS FIXES | List ⚠️ and ❌ items. Author fixes before moving to `review/`. |
| 60–74% | SIGNIFICANT GAPS | Return to author with prioritized fix list. Focus on LLM optimization and E-E-A-T first. |
| <60% | REWRITE | Structural issues. Draft needs a revision pass before quality check is re-run. |

---

## Step 4 — Report

Output format:

```
## SEO Quality Check — [Title]

**Type:** [blog / landing page / topic page]
**Target keyword:** [keyword]
**Word count:** [count]
**Score:** [X/Y] ([%]) — [VERDICT]

### Critical fixes (❌)
- [Item]: [What's wrong] → [How to fix]

### Recommended fixes (⚠️)
- [Item]: [What's wrong] → [How to fix]

### Passed (✅)
[List passed items or "All checks passed" if score is 90%+]

### Highest-leverage fix
[Single most impactful thing to do right now]
```

Do not auto-edit the draft. Surface findings only. Author makes the fixes.

---

## Sources

Built from:
- `marketing/context/content-standards.md` — ExamPilot quality bar
- `wiki/marketing/seo/llm-seo-mechanics.md` — LLM chunk optimization rules
- `wiki/marketing/seo/seo-strategy.md` — Technical SEO requirements
- SEO Brothers corpus: on-page crash course, AI search crash course, Google AI signals research
