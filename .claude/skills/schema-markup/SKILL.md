---
name: schema-markup
description: Generate JSON-LD structured data for ExamPilot pages. Produces FAQPage, Article, BreadcrumbList, and EducationalContent schemas. Supports traditional rich results, featured snippets, and agent-readability — NOT an AI-citation lever (Ahrefs 2026: schema has no measurable effect on AI citations; the lever is answer-first extractable prose).
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Generates JSON-LD structured data markup for ExamPilot pages. Schema helps Google render traditional **rich results** and **featured snippets**, and makes pages more legible to crawling agents. It is **not** an AI-citation lever: Ahrefs' 2026 controlled study found schema markup has no measurable effect on whether a page is cited in AI Overviews or LLM answers. The AI-citation lever is **answer-first, extractable prose** (see `/seo-quality-check` section B and `seo-strategy` GEO point 13), plus entity and YouTube signals — not JSON-LD.

Schema is still worth generating for every blog article and topic page before it goes live — for rich results and agent-readability, just don't credit it for citations.

> **Doctrine note (2026-06-02):** This skill was reframed after the Ahrefs 2026 AI-search findings. Schema demoted from "core GEO/citation lever" to "rich-results + agent-readability". Don't reintroduce citation-probability claims.

This skill produces ready-to-embed JSON-LD blocks. It does not modify the source article — the developer or content manager pastes the output into the appropriate Sanity field or `<script>` tag.

## When `/schema-markup` runs

- After a blog article passes human review and is ready to publish
- When building a new topic hub page or landing page
- When auditing an existing page that may be missing schema
- After running `/seo-audit` and schema is listed as a Critical issue

## Context files — read at session start

```bash
cat marketing/references/geo-platform-guide.md
cat marketing/context/content-standards.md
```

## Execution — five steps

### Step 1 — Identify input

Determine what's being schemaed:

| Page type | Schema types to generate |
|---|---|
| Blog article | Article + FAQPage + BreadcrumbList |
| Topic hub page | LearningResource + BreadcrumbList |
| Pricing / feature page | BreadcrumbList only (unless FAQs present, then + FAQPage) |
| Comparison page | BreadcrumbList + FAQPage (if FAQ section exists) |

Ask if not obvious: "What type of page is this? Blog article, topic hub, pricing, feature, or comparison?"

If a file path is provided, read the article to extract:
- Title and meta_description from frontmatter
- Primary keyword and exam board from frontmatter
- FAQ section (H2 or H3 questions + answers)
- Publish date (`date` field in frontmatter)
- url_slug

---

### Step 2 — Generate Article schema (blog articles only)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Article title — from frontmatter title field]",
  "description": "[Meta description — from frontmatter meta_description field]",
  "author": {
    "@type": "Organization",
    "name": "ExamPilot",
    "url": "https://exampilot.io"
  },
  "publisher": {
    "@type": "Organization",
    "name": "ExamPilot",
    "logo": {
      "@type": "ImageObject",
      "url": "https://exampilot.io/logo.png"
    }
  },
  "datePublished": "[YYYY-MM-DD from frontmatter date field]",
  "dateModified": "[YYYY-MM-DD — same as datePublished unless the article has been updated]",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://exampilot.io[url_slug from frontmatter]"
  },
  "about": {
    "@type": "Thing",
    "name": "[primary_keyword from frontmatter]"
  },
  "educationalLevel": "A-Level",
  "audience": {
    "@type": "EducationalAudience",
    "educationalRole": "student",
    "audienceType": "A-Level Maths students"
  }
}
```

**Rules:**
- `headline` must match the H1 of the article exactly (or very closely). If there is a mismatch, flag it.
- Do not add `image` unless a real image URL is confirmed. Empty `image` fields can trigger schema errors.
- `dateModified` should only differ from `datePublished` if the article was actually updated. Use [VERIFY] if unknown.

---

### Step 3 — Generate FAQPage schema

Extract the FAQ section from the article. Look for headings that are either:
- `## FAQ` or `## Frequently Asked Questions`
- `### [Question text]` or `**Q: [Question text]**`

For each Q&A pair, generate one `mainEntity` entry:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text — exactly as written in the article]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer text — must be a complete, standalone answer]"
      }
    }
  ]
}
```

**Rules:**
- Maximum 10 Q&A pairs per schema. If the FAQ section has more than 10, select the 10 most specific and informative.
- Minimum 4 Q&A pairs. If the article has fewer than 4 FAQ pairs, flag this as a Critical issue: "FAQ section has only [n] pairs — minimum 4 required. Add more Q&As before generating schema."
- Answer text should be concise — aim for under ~200 characters so it can render cleanly as a featured snippet / rich result. This is a display guideline, not an AI-citation lever. If any answer is well over 200 characters, flag it:

```
FLAG: Answer to "[question]" is [n] characters — too long for clean featured-snippet display (~200 char guideline).
Suggested shortened version: "[condensed version]"
Offer to shorten: "Should I shorten this answer for featured-snippet display? The full answer will still appear on the page."
```

- Questions must be written as students naturally phrase them (conversational, not keyword-optimised). If a question reads like an SEO keyword rather than a natural question, flag it: "This question reads as keyword-optimised. Consider rewriting as: [natural phrasing suggestion]"

---

### Step 4 — Generate BreadcrumbList schema

For all page types:

**Blog article:**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://exampilot.io"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://exampilot.io/blog"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Article title]",
      "item": "https://exampilot.io[url_slug]"
    }
  ]
}
```

**Cambridge topic hub (e.g. 9709 Pure 1):**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://exampilot.io"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Cambridge A-Level Maths",
      "item": "https://exampilot.io/cambridge-a-level-maths/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Paper name — e.g. Pure Mathematics 1 (9709 Paper 1)]",
      "item": "https://exampilot.io/cambridge/[topic-slug]"
    }
  ]
}
```

**Pricing / Feature page:**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://exampilot.io"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[Page title — e.g. Pricing]",
      "item": "https://exampilot.io/[page-slug]"
    }
  ]
}
```

---

### Step 5 — Generate LearningResource schema (topic hub pages only)

For Cambridge 9709 and Edexcel IAL topic hub pages:

```json
{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "[Topic name — e.g. Cambridge 9709 Pure Mathematics 1 Practice]",
  "description": "[1-2 sentence description of what students will practise on this page]",
  "url": "https://exampilot.io/cambridge/[topic-slug]",
  "educationalLevel": "A-Level",
  "educationalAlignment": {
    "@type": "AlignmentObject",
    "alignmentType": "educationalSubject",
    "targetName": "[Exam board spec reference — e.g. Cambridge International AS & A Level Mathematics 9709 Syllabus]",
    "targetUrl": "[Cambridge or Pearson specification URL — [VERIFY]]"
  },
  "teaches": "[Topic name — e.g. Integration, Differentiation, Coordinate Geometry]",
  "assesses": "[Exam paper — e.g. Cambridge 9709 Paper 1 (Pure Mathematics 1)]",
  "provider": {
    "@type": "Organization",
    "name": "ExamPilot",
    "url": "https://exampilot.io"
  },
  "audience": {
    "@type": "EducationalAudience",
    "educationalRole": "student"
  },
  "inLanguage": "en"
}
```

**Rules:**
- `targetUrl` for Cambridge specification: `https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-9709/` — [VERIFY current URL]
- `targetUrl` for Pearson/Edexcel specification: `https://qualifications.pearson.com/en/qualifications/edexcel-international-advanced-levels/mathematics-2018.html` — [VERIFY current URL]
- `teaches` should list the main topics covered, not the full syllabus. Keep concise.

---

### Step 6 — Assemble and present

**For blog articles:** Combine all three schemas into a single output block.

```
Schema markup for: [Article title]
Generated: 2026-05-16

Schema types: Article + FAQPage + BreadcrumbList

Flags:
  - FAQ answers over 200 chars: [list or "none"]
  - [VERIFY] items: [list or "none"]
  - Missing fields: [list or "none"]

Implementation:
  Add the following <script> block to the <head> of the page, or to the
  "structuredData" field in the Sanity schema for this article.

--- JSON-LD ---

<script type="application/ld+json">
[Article schema JSON]
</script>

<script type="application/ld+json">
[FAQPage schema JSON]
</script>

<script type="application/ld+json">
[BreadcrumbList schema JSON]
</script>

--- END JSON-LD ---

Validate at: https://validator.schema.org/ before publishing.
```

**For Sanity CMS pages:** Note the field path:
```
In Sanity Studio: navigate to this page → SEO settings → Structured Data → paste the JSON (without the <script> tags).
```

## What this skill does NOT do

- Does not add schema to the source file. It outputs JSON-LD blocks for the developer or content manager to add.
- Does not validate the live page. Use https://validator.schema.org/ or Google's Rich Results Test for validation.
- Does not generate Product schema, Review schema, or Event schema. If these are needed, raise the requirement separately.
- Does not generate schema for pages that do not yet have confirmed URLs. Placeholder URLs in schema will fail validation.
