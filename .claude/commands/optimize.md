---
name: optimize
description: Standalone SEO audit on any article (draft or published). Produces a prioritized action report — does NOT rewrite.
---

## Input

$ARGUMENTS

Expect: file path to an article (draft or published). Examples:
- `marketing/pipelines/published/cambridge-9709-integration-tips-2026-03-10.md`
- `marketing/pipelines/drafts/edexcel-wma11-statistics-2026-05-01.md`

If no file path given, ask.

## Execution

### Step 1: Read the article

Read the file at the provided path. Extract:
- Primary keyword (frontmatter `keyword:` or H1)
- URL slug (frontmatter or filename)
- Word count (estimate from content length)
- All H1, H2, H3 headings (list them)
- All internal links (href + anchor text)
- All external links (href + anchor text)
- Meta title and description (frontmatter `meta_title:`, `meta_description:`)
- FAQ section presence and Q&A count

### Step 2: Check DataForSEO connection

Read `connections.md` and check if DataForSEO is connected.

DataForSEO is connected (row 12). Pull live volume + difficulty for the primary keyword (worldwide is the default and truest for CIE/IAL; add `--location <country>` for a market cut):
```bash
python3 marketing/data_sources/modules/keyword_volume.py --keywords "[primary_keyword]" --kd
```
Use live volume and KD data in the audit. If DataForSEO returns no data, proceed with structural analysis only.

### Step 3: Run 6-dimension SEO analysis

Score each dimension: **Pass** / **Partial** / **Fail**

**Dimension 1: Keyword placement**
- [ ] Primary keyword in H1
- [ ] Primary keyword or close variation in first 100 words
- [ ] Primary keyword or variation in at least 2 H2s
- [ ] Keyword density: count primary keyword occurrences ÷ total word count. Target: 1-2%. Flag if <1% (under-optimized) or >2.5% (over-optimized)

**Dimension 2: Structure**
- [ ] H2 count is 4-7. Flag if <4 (thin) or >7 (fragmented)
- [ ] Heading hierarchy: H1 present (exactly 1), H2s present, H3s only under H2s
- [ ] Word count ≥ 1800. Note actual count. Flag if <1800.
- [ ] Introduction ≤ 300 words before first H2
- [ ] Conclusion present

**Dimension 3: Internal links**
- [ ] 3-5 internal links present (count them)
- [ ] All anchors are descriptive (not "click here", "read more", or bare URLs)
- [ ] No obvious broken internal URLs (paths that don't match known pipeline or site structure)
- [ ] Links distributed through body (not all clustered at end)

**Dimension 4: External links**
- [ ] 2-3 external links present (count them)
- [ ] Links point to authority sources only: cambridge.org, pearsonqualifications.com, ocr.org.uk, gov.uk, .edu domains, mathsisfun.com, khanacademy.org
- [ ] No external links to competitors (SaveMyExams, PapaCambridge, Physics & Maths Tutor) unless in explicit comparison context
- [ ] External links open in context (not mid-sentence drops)

**Dimension 5: Meta**
- [ ] Meta title present. Length 50-60 chars. Contains primary keyword.
- [ ] Meta description present. Length 150-160 chars. Includes keyword. Includes value hook.
- [ ] URL slug present in frontmatter. Lowercase, hyphenated, keyword-first.
- [ ] Frontmatter has all required fields: type, channel, stage, target-segment, status, keyword, created

**Dimension 6: GEO compliance**
- [ ] First 1-2 sentences answer the query directly (answer-first structure)
- [ ] Key Takeaways block present with 3-5 self-contained bullet points
- [ ] FAQ section present with 4+ Q&A pairs written in natural conversational language
- [ ] Full entity names used on first mention: "Cambridge International AS & A Level Mathematics 9709", "Edexcel International Advanced Level"
- [ ] Definition blocks present for technical concepts (spaced repetition, mark scheme, etc.)
- [ ] No "AI Overview" incompatible phrases: avoid "as I mentioned", "as we can see", forward-references between sections

### Step 4: Build action report

Group issues into three tiers:

**Critical — fix before publishing:**
- Any Fail on keyword placement (H1, first 100 words)
- Word count < 1800
- Meta title or description missing
- No FAQ section
- No Key Takeaways block

**Quick wins — 15 minutes each:**
- Any Partial scores that need minor fixes
- Keyword density outside 1-2%
- Anchor text is generic ("click here")
- External link count off by 1
- Meta length outside target range by < 10 chars

**Strategic — nice to have:**
- Additional H2 sections to improve coverage
- Definition blocks for technical terms
- Additional internal links to planned cluster articles

### Step 5: Save report

Save to `marketing/pipelines/research/optimize-[slug]-YYYY-MM-DD.md`

```yaml
---
type: seo-audit
article_file: [source path]
primary_keyword: ""
audit_date: YYYY-MM-DD
overall_result: pass | needs-work | fail
dimensions:
  keyword_placement: pass | partial | fail
  structure: pass | partial | fail
  internal_links: pass | partial | fail
  external_links: pass | partial | fail
  meta: pass | partial | fail
  geo_compliance: pass | partial | fail
---

## SEO Audit: [Article Title]

### Dimension Scores
[Table: Dimension | Result | Notes]

### Critical Issues
[Numbered list]

### Quick Wins
[Numbered list]

### Strategic Improvements
[Numbered list]

### Recommended next step
[/rewrite [file] with scope light | moderate | complete — or "no rewrite needed, fix inline"]
```

### Step 6: Report

Show the audit summary and ask:
- "Audit complete. [X] critical issues, [Y] quick wins."
- "Want to run `/rewrite` with [scope] to fix these, or fix inline?"
