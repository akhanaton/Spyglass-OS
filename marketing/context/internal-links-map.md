# Internal Links Map

Last updated: 2026-05-16

## How this file works

Maps ExamPilot's URL architecture and internal linking targets. The `/write-article` skill and `internal-linker` agent read this file when suggesting internal links for new articles. Update it every time a new page goes live.

**Rule:** Only add URLs to this file when they are confirmed live or confirmed in the Sanity CMS build plan. Do not speculate about future URLs.

---

## URL Architecture

```
https://exampilot.io/

/blog/[slug]                     → Blog articles (SEO content)
/cambridge/[topic-slug]          → Cambridge topic hub pages (product + SEO)
/cambridge-a-level-maths/        → Main Cambridge hub (pillar landing page)
/edexcel/[topic-slug]            → Edexcel IAL topic hub pages
/edexcel-ial-maths/              → Main Edexcel hub (pillar landing page)
/pricing                         → Pricing page
/features                        → Features overview page
/blog/                           → Blog index page
/about                           → About ExamPilot
```

---

## High-Priority Internal Link Targets

Every article should attempt to link to at least one of these pages if contextually relevant. These are the highest-value destinations for link equity.

| Page | URL | Anchor Text Examples | Priority | Status |
|------|-----|----------------------|----------|--------|
| Cambridge A-Level Maths hub | /cambridge-a-level-maths/ | "Cambridge 9709 practice", "Cambridge A-Level Maths", "9709 revision on ExamPilot" | Critical | Planned — add URL when live |
| Edexcel IAL hub | /edexcel-ial-maths/ | "Edexcel IAL practice", "WMA11 revision on ExamPilot" | Critical | Planned — add URL when live |
| Pricing page | /pricing | "ExamPilot plans", "start practising from EUR12/mo", "try ExamPilot free" | High | Planned — add URL when live |
| Features page | /features | "how ExamPilot works", "ExamPilot's adaptive practice", "Knowledge State feature" | High | Planned — add URL when live |

**Anchor text rules:**
- Never use "click here", "read more", "here", "this page", "this article"
- Anchor text must describe the destination (what the reader will find)
- Vary anchor text across the site — do not use the same exact anchor text for the same URL everywhere

---

## Cambridge Topic Hub Pages

Add to this table as Cambridge topic pages are built in Sanity CMS.

| Topic | URL | Paper Code | Status |
|-------|-----|------------|--------|
| Pure Mathematics 1 | /cambridge/pure-1/ | 9709 Paper 1 | Planned |
| Pure Mathematics 3 | /cambridge/pure-3/ | 9709 Paper 3 | Planned |
| Statistics 1 | /cambridge/statistics-1/ | 9709 Paper 5 | Planned |
| Mechanics 1 | /cambridge/mechanics-1/ | 9709 Paper 4 | Planned |
| Pure Mathematics 2 | /cambridge/pure-2/ | 9709 Paper 2 | Planned |

---

## Edexcel IAL Topic Hub Pages

Add to this table as Edexcel pages are built.

| Topic | URL | Paper Code | Status |
|-------|-----|------------|--------|
| Pure Mathematics 1 | /edexcel/pure-1/ | WMA11 | Planned |
| Pure Mathematics 2 | /edexcel/pure-2/ | WMA12 | Planned |

---

## Blog Article Cross-Links

Populated as articles are published. For each pair, indicate the linking direction: one-way (→) or mutual (↔).

| Source Article | Target Article | Suggested Anchor Text | Direction | Status |
|----------------|----------------|----------------------|-----------|--------|
| — | — | — | — | — |

*Update this table after each article is published. Run the internal-linker agent on each new article to identify cross-link opportunities with already-published content.*

---

## Pillar to Spoke Link Relationships

Hub-and-spoke architecture. Each pillar article should link to all its spoke articles, and each spoke should link back to its pillar.

| Pillar Article | Target URL | Spoke Articles | Spoke URLs | Status |
|----------------|------------|----------------|------------|--------|
| Cambridge 9709 Pure 1 Complete Guide | /cambridge/pure-1/ | Integration by parts guide, Differentiation from first principles, Coordinate geometry worked examples, Binomial expansion questions | /blog/[slug] per article | Planned |
| Cambridge 9709 Statistics 1 Complete Guide | /cambridge/statistics-1/ | Normal distribution guide, Probability distributions, Hypothesis testing | /blog/[slug] per article | Planned |
| How to revise for Cambridge 9709 | /blog/[slug] | All topic-specific guides | /blog/[slug] per article | Planned |

---

## Link Rules (enforced by `/seo-audit` and internal-linker agent)

**Count:**
- Minimum 3 internal links per blog article
- Maximum 5 internal links per blog article (diminishing returns beyond 5; dilutes equity)
- No minimum or maximum on product/hub pages — link to all relevant topic pages

**What counts as an internal link:**
- Links to any exampilot.io URL: /pricing, /features, /cambridge/*, /edexcel/*, /blog/*
- Product CTAs count: "Try Cambridge 9709 practice on ExamPilot [link]"

**What does NOT count as an internal link:**
- External links to Cambridge, Pearson, Ofqual, or any third-party site
- Empty `href` or javascript: links
- Links to PDFs or documents hosted externally

**Anchor text requirements:**
- Descriptive — tells the reader where they're going
- Relevant to the surrounding sentence — not shoehorned
- Varied across the article — no two links in the same article with identical anchor text
- UK English spelling in anchor text: "practise" (verb), "practice" (noun)

---

## Maintenance protocol

- Add every new live URL to the appropriate table above when it's published
- After each new article is published, run the internal-linker agent to update the Blog Article Cross-Links table
- Quarterly audit: check all links in the map are still live (use a link checker tool — not manual)
- If a URL changes (slug update, redirect), update all references in this file and ensure redirects are in place
