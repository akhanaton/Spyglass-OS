---
name: write-article
description: Write a full SEO blog article (2000-3000 words) for ExamPilot. Follows the blog-article template with GEO optimization, FAQ schema, and [VERIFY] flags for human review.
---

## Input

$ARGUMENTS

Expect: topic from `marketing/pipelines/topics/` OR a freeform topic. Examples:
- "from topics/cambridge-9709-integration-tips-2026-05-14.md"
- "how to revise for cambridge 9709 pure 1 in 8 weeks"
- "common mistakes in edexcel WMA11 differentiation"

If no topic given, list available topics from `marketing/pipelines/topics/` and ask which one to write.

## Execution

### Step 1: Load context

Read these files in parallel:
- `marketing/templates/blog-article.md` — article structure and checklists
- `marketing/context/content-standards.md` — quality bar, review checklist, GEO checklist, positioning
- `marketing/context/audience-segments.md` — messaging angle for the target segment
- `marketing/context/funnel-strategy.md` — understand where this article sits in the micro-funnel
- `marketing/references/geo-platform-guide.md` — GEO content patterns (definition blocks, FAQ, evidence sandwich), platform-specific optimization
- `marketing/references/copy-frameworks.md` — headline formulas, section writing tips

If a keyword brief exists in `marketing/pipelines/topics/`, read it for keyword data, SERP landscape, and content angle.

### Step 2: Fetch wiki strategy

```bash
gh api repos/akhanaton/spyglass-wiki/contents/wiki/marketing/seo/seo-strategy.md --jq '.content' | base64 -d
```

Use for: URL architecture, keyword difficulty targets, pillar/spoke cluster mapping, content workflow requirements.

### Step 3: Determine article parameters

From the topic and context:
- **Primary keyword** (from brief or inferred)
- **Target segment** (cambridge-9709, edexcel-ial, resit, parent)
- **Funnel stage** (tofu or mofu for blog articles)
- **URL slug** (following wiki URL architecture)
- **Word count target** (2000-3000 words)

### Step 4: Write the article

Follow `marketing/templates/blog-article.md` structure:

1. **YAML frontmatter** with all required fields
2. **H1** with primary keyword
3. **Introduction** (150-250 words): answer the query directly in first 1-2 sentences (GEO requirement), then hook + value promise
4. **Key Takeaways** block: 3-5 standalone bullet points
5. **H2 sections** (4-7): each starts with answer-first structure. Use H3s for subsections.
6. **FAQ section**: minimum 4 self-contained Q&A pairs in conversational language
7. **Conclusion** (150-200 words): recap, next step, CTA

Rules:
- [VERIFY] flag every exam board fact, date, paper code, mark scheme claim, or statistic
- No "AI tutor", "AI-powered", "revolutionary" language
- "Learning science", "spaced repetition", "active recall", "exam readiness" instead
- Pricing must be exact: EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr
- Short paragraphs (2-4 sentences max)
- 3-5 internal links, 2-3 external authority links
- 2-3 contextual CTAs distributed through the body
- First CTA within first 500 words
- Full entity names: "Cambridge International AS & A Level Mathematics 9709"
- No generic filler phrases

### Step 5: Run checklists

After writing, verify against all three checklists from the blog-article template:
- SEO Checklist
- GEO Checklist
- Content Rules Checklist

Flag any items that don't pass.

### Step 6: Output

Save to `marketing/pipelines/drafts/[topic-slug]-YYYY-MM-DD.md`

### Step 7: Review prompt

Show the draft summary (not full article) and ask:
- "Article saved to drafts. [X] words, [Y] [VERIFY] flags to resolve."
- "Key sections: [list H2s]"
- "Ready for your review. Read the draft and resolve [VERIFY] flags before moving to review/."

Never auto-publish. Every article gets human review.
