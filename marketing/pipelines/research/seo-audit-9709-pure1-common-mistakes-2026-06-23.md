---
type: seo-audit
mode: single
article: "blog/9709-pure-1-common-mistakes-examiner-reports"
score: 93.5
health: healthy
date: 2026-06-23
---

# SEO Audit: Common Mistakes in Cambridge 9709 Pure 1 (From Examiner Reports)
Date: 2026-06-23
File: `marketing/pipelines/review/9709-pure-1-common-mistakes-examiner-reports-2026-06-23.md`

## Dimension Scores

```
  Crawlability & Indexation    15/15
  On-Page Optimization         25/25
  Content Quality              22.5/25
  Internal Linking             12.5/15
  External Linking             10/10
  E-A-T Signals                8.5/10
  ──────────────────────────────────
  Total                        93.5/100
  Health status: HEALTHY
```

## Dimension Detail

### D1: Crawlability & Indexation (15/15)
- YAML frontmatter complete: PASS — all required fields present (title, meta_title, meta_description, url_slug, primary_keyword, status, date)
- url_slug `/blog/9709-pure-1-common-mistakes-examiner-reports`: PASS — correct pattern, lowercase, hyphens only
- No noindex signals: PASS

### D2: On-Page Optimization (25/25)
- H1 contains primary keyword: PASS — exact match "Common Mistakes in Cambridge 9709 Pure 1" in H1
- Meta title: PASS — "Common Mistakes in Cambridge 9709 Pure 1 (5 Years of Data)" = 58 chars, keyword present
- Meta description: PASS — 156 chars, keyword present, ends with action phrase ("quick fixes that protect your score")
- Keyword in first 100 words: PASS — appears in first sentence of body
- Keyword density: PASS — primary phrase appears 5-6 times across H1, opening sentence, two H2s, FAQ Q1; healthy for a 6-word long-tail at ~2,300 words

### D3: Content Quality (22.5/25)
- Word count: PASS — ~2,300 words (≥1,800 threshold)
- Heading structure: PARTIAL — 9 H2 sections (7 content + FAQ + conclusion); guideline is 4-7. Note: if CMS renders FAQ as a structured component (not H2), topical count is 7 — within range. Only 1 explicit H3 detected; guideline requires at least 2.
- FAQ section: PASS — 5 Q&A pairs, ≥4 minimum met; FAQPage JSON-LD present
- Key Takeaways block: PASS — 5-bullet block immediately after introduction; each is a standalone claim
- Reading level: PASS — appropriate for 16-18 year olds; short paragraphs; technical terms contextualised

### D4: Internal Linking (12.5/15)
- Link count: PASS — 5 internal links: `/cambridge/9709/pure-1/circular-measure`, `/cambridge/9709/pure-1/integration`, `/cambridge/9709/pure-1/trigonometry`, `/cambridge/9709/pure-1`, `/` (homepage CTA)
- Target validity: PARTIAL — `/integration` and `/trigonometry` confirmed live by Teresa; others consistent with live URL pattern. `internal-links-map.md` shows stale URL structure (`/cambridge/pure-1/` vs actual `/cambridge/9709/pure-1/`) — update map before next internal-linker run
- Anchor text: PASS — all descriptive; no "click here" / "read more" violations; "See how it works →" is acceptable CTA-style anchor for homepage

### D5: External Linking (10/10)
- Count: PASS — 2 external authority links (minimum 2)
- Quality: PASS — both point to `cambridgeinternational.org`; no competitor links
- [Verify both URLs are live before CMS publish]

### D6: E-A-T Signals (8.5/10)
- [VERIFY] flags resolved: PASS — zero unresolved flags; all replaced with [VERIFIED] editorial tags
- Author attribution: PASS — `author: "Teresa González (Reviewed by)"` in frontmatter + full reviewer byline section
- Source citations: PARTIAL — examiner quotes attributed with specific paper/year/question (strong); no numerical statistics with sources (deliberate per brief — qualitative framing to avoid unverified numerical claims)

### GEO Bonus (informational)
- Answer-first H2s: ✓ each H2 opens with a direct, extractable answer sentence
- Full entity name: gap — first body-text mention uses "Cambridge 9709 Pure 1" not "Cambridge International AS & A Level Mathematics (9709)"; full name appears in the external link anchor (line 42) but not as a prose entity
- Extractable passages: ✓ Key Takeaways bullets and H2 opening sentences are clean 40-60 word extractions

---

## Action List

### Critical (block publishing)
None. Article is CMS-ready.

### Important (fix at CMS stage)

1. **Strip [VERIFIED] annotations from body copy**
   All `[VERIFIED: ...]` and `⚠ Local copy watermarked` inline tags must be removed from the published version. They are editorial markers only.

2. **Confirm Cambridge URL public accessibility**
   In-article FAQ answer Q2 says "They're free to access." The verification note flags some reports may be login-gated (School Support Hub). Confirm both Cambridge URLs are publicly accessible, then either keep the copy or soften to "freely available for most sessions."

### Optional (nice to have)

3. **H2/H3 structure** — If CMS renders FAQ as a structured component (not H2), topical H2 count is 7 (in range). Otherwise consider demoting "The bottom line…" to a styled conclusion callout. Adding one H3 to the differentiation or final-habits section satisfies the 2-H3 guideline.

4. **Full entity name in prose (GEO)** — Add "Cambridge International AS & A Level Mathematics (9709)" on first body-text mention. Improves entity recognition by AI engines.

5. **Update `marketing/context/internal-links-map.md`** — Cambridge topic URL entries show `/cambridge/pure-1/` but live structure is `/cambridge/9709/pure-1/`. Update before next internal-linker agent run.
