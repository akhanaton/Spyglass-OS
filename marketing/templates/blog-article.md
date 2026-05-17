# Blog Article Template

Use this template for all SEO blog content. Every article targets one primary keyword, one audience segment, and one funnel stage.

## Frontmatter

```yaml
---
type: blog-article
title: "[H1 — include primary keyword, under 60 chars]"
meta_title: "[50-60 chars, may differ from H1]"
meta_description: "[150-160 chars, directly answers the target query]"
primary_keyword: ""
secondary_keywords: []
target_segment: ""  # cambridge-9709 | edexcel-ial | tutor | parent | resit
funnel_stage: ""    # tofu | mofu | bofu
url_slug: "/blog/[slug]"
word_count_target: 2500
author: "Enitan Williams"
status: draft
date: YYYY-MM-DD
---
```

## Structure

### H1: [Title]

Primary keyword in first 100 words. Must directly answer the target query in the first 1-2 sentences. This is critical for AI search citation (GEO).

### Key Takeaways

Immediately after the introduction. 3-5 bullet points. Each is a standalone claim with specifics. Not a table of contents.

```markdown
> **Key Takeaways**
> - [Specific finding or recommendation #1]
> - [Specific finding or recommendation #2]
> - [Specific finding or recommendation #3]
```

### H2 Sections (4-7)

Each H2 starts with a complete, extractable answer in the first 2-3 sentences. This answer-first structure is required for GEO.

Use H3s to break complex sections. One idea per section.

Rules:
- Short paragraphs (2-4 sentences max)
- Bold key concepts
- Use bullet/numbered lists for scannability
- [VERIFY] flag on any exam board fact, date, or mark scheme claim you're not 100% certain about
- 2-3 contextual CTAs distributed through the body (not just at end)
- First CTA within the first 500 words

### FAQ Section

Minimum 4 self-contained Q&A pairs. These become FAQPage schema.

Write questions in natural conversational language students actually type:
- "What's the best way to revise for Cambridge 9709 Pure 1?"
- "How many past papers should I do for WMA11?"

Each answer must be complete without reading the rest of the article.

### Conclusion

150-200 words. Recap 3-5 key points. Clear next step. Final CTA.

## Linking

- 3-5 internal links (to other ExamPilot blog posts or landing pages)
- 2-3 external links to authoritative sources (Cambridge Assessment, Pearson, Ofqual)
- Descriptive anchor text with keywords

## SEO Checklist

- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in 2+ H2 headings
- [ ] Keyword density 1-2%
- [ ] 3-5 internal links
- [ ] 2-3 external authority links
- [ ] Meta title 50-60 characters
- [ ] Meta description 150-160 characters
- [ ] 2000+ words
- [ ] Proper H1/H2/H3 hierarchy

## GEO Checklist

- [ ] First 1-2 sentences directly answer the target query
- [ ] Key Takeaways block after introduction
- [ ] FAQ section with 4+ self-contained Q&A pairs
- [ ] Full entity names spelled out (Cambridge International AS & A Level Mathematics 9709)
- [ ] Official sources cited (Cambridge Assessment, Pearson)
- [ ] Conversational long-tail in FAQ questions

## Content Rules

- [ ] All [VERIFY] flags resolved before moving to review/
- [ ] Voice matches references/voice-house.md
- [ ] No "AI tutor", "AI wrapper", "AI-powered" language
- [ ] No generic filler ("in today's world", "it's no secret that")
- [ ] Pricing correct: EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr
- [ ] Factually accurate for the specific exam board
- [ ] No B2B school licensing or institution pricing (B2C2B referral partners only)

## File Output

Save to: `marketing/pipelines/drafts/[topic-slug]-YYYY-MM-DD.md`
