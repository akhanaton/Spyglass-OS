---
name: rewrite
description: Rewrites an existing article from drafts or published pipeline with scope classification (light / moderate / complete).
---

## Input

$ARGUMENTS

Expect: file path to an existing article. Examples:
- `marketing/pipelines/published/cambridge-9709-integration-tips-2026-03-10.md`
- `marketing/pipelines/drafts/edexcel-wma11-differentiation-2026-04-22.md`

If no file path given, ask.

## Execution

### Step 1: Read the article

Read the file at the provided path. Extract:
- Primary keyword (from frontmatter `keyword:` field or H1)
- URL slug (from frontmatter or filename)
- Date created (from frontmatter `created:` or filename date)
- Current word count (estimate from line count)
- Quality score (from frontmatter `quality_score:` if present)
- Internal links present

### Step 2: Classify scope

Determine rewrite scope using these rules:

**Light (20-30% change)** — grammar fixes, freshness updates, voice alignment:
- Article is < 6 months old
- Quality score ≥ 75 (if present)
- User says "refresh", "update", or "voice fix"

**Moderate (40-60% change)** — restructure + update facts:
- Article is 6-12 months old OR
- Quality score 50-74 OR
- User says "restructure", "update facts", "improve"
- Missing key sections (Key Takeaways, FAQ, or fewer than 4 H2s)

**Complete (90%+ change)** — full rewrite preserving keyword and slug only:
- Article is > 12 months old OR
- Quality score < 50 OR
- User says "full rewrite", "start over", "completely redo"
- Significant structural problems (no GEO compliance, wrong funnel stage)

Ask user: "I've classified this as a **[scope]** rewrite based on [reason]. Confirm or choose a different scope (light / moderate / complete)?"

Do not proceed until scope is confirmed.

### Step 3: Load context

Read these files in parallel:
- `marketing/context/content-standards.md` — quality bar, GEO checklist, positioning rules
- `marketing/context/audience-segments.md` — messaging angles per segment

Also fetch voice guide:
```bash
cat references/voice-house.md
```

Read `marketing/templates/blog-article.md` for required structure if scope is moderate or complete.

### Step 4: Rewrite according to scope

**Light scope:**
- Fix grammar and readability issues
- Update any stale dates, exam session references, or statistics (flag with [VERIFY])
- Align voice with `references/voice-house.md`
- Update internal links if target pages have moved (preserve anchor text intent)
- Do NOT change H2 structure, word count target, or primary keyword placement

**Moderate scope:**
- Restructure sections for better answer-first flow
- Add Key Takeaways block if missing
- Expand FAQ to 4+ Q&A pairs if under that
- Update all facts and statistics (flag all with [VERIFY])
- Add GEO compliance elements (definition blocks, evidence sandwich)
- Refresh internal links (3-5, descriptive anchors)
- Add external authority links if missing (Cambridge, Pearson, .edu sources)
- Preserve primary keyword, URL slug, all existing internal links that still resolve

**Complete scope:**
- Rewrite from scratch following `marketing/templates/blog-article.md`
- Preserve ONLY: primary keyword, URL slug
- Target 2000-3000 words
- Apply full GEO optimization
- Insert 3-5 new internal links, 2-3 external authority links
- Flag all exam board claims with [VERIFY]

Rules that apply at all scopes:
- No "AI tutor", "AI-powered", "revolutionary" language
- Pricing exact: EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr
- Full entity names: "Cambridge International AS & A Level Mathematics 9709"
- First CTA within first 500 words

### Step 5: Run quality check inline

Score the rewritten article across 5 dimensions (0-20 each, total 100):

1. **Keyword placement** — H1 present, first 100 words, 2+ H2s contain keyword variation, density 1-2%
2. **Structure** — 4-7 H2s, proper H1→H2→H3 hierarchy, 1800+ words
3. **GEO compliance** — answer-first intro, Key Takeaways block, FAQ 4+ Q&A, entity names spelled out
4. **Links** — 3-5 internal (descriptive anchors), 2-3 external (.edu, Cambridge, Pearson)
5. **Voice & positioning** — no banned phrases, pricing correct, [VERIFY] flags on all claims

Show score: `Quality score: [X]/100 ([Pass ≥75 / Review needed <75])`

### Step 6: Save

Save to `marketing/pipelines/drafts/rewrite-[slug]-YYYY-MM-DD.md`

Update YAML frontmatter:
```yaml
status: drafted
rewrite_scope: light | moderate | complete
rewrite_date: YYYY-MM-DD
original_file: [path to original]
quality_score: [score]
```

### Step 7: Report

Show:
- Scope applied and reason
- Word count before → after
- Sections changed (list H2s that changed)
- [VERIFY] flag count
- Quality score
- File saved to path

Ask: "Review the rewrite at [path]. Resolve [X] [VERIFY] flags before moving to review/."
