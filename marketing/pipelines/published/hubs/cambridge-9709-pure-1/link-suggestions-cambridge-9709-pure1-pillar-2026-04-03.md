# Link Audit and Suggestions: Cambridge 9709 Pure Mathematics 1 Pillar Page

**Agent:** Internal Linker
**File audited:** `cambridge-9709-pure1-pillar-2026-04-03.md`
**Date:** 2026-04-03

---

## 1. Current Internal Links -- Full Audit

All internal links listed in frontmatter and present in article body:

| # | URL | Anchor Text (in body) | Location in Article | Quality Assessment |
|---|---|---|---|---|
| 1 | /cambridge/9709/pure-1/functions/ | "A Level Maths Functions: Cambridge 9709 Pure 1 Guide" | Line 128, Topic 1.2 section | GOOD -- descriptive, keyword-rich, placed naturally within topic section |
| 2 | /cambridge/9709/pure-1/trigonometry/ | "A Level Maths Trigonometry: Cambridge 9709 Pure 1 Guide" | Line 172, Topic 1.5 section | GOOD -- descriptive, placed in-context |
| 3 | /cambridge/9709/pure-1/differentiation/ | "9709 P1 Differentiation: Exam Tips and Worked Solutions" | Line 206, Topic 1.7 section | GOOD -- matches the actual spoke article title closely |
| 4 | /cambridge/9709/pure-1/integration/ | "A Level Maths Integration: Cambridge 9709 Pure 1 Guide" | Line 221, Topic 1.8 section | GOOD -- descriptive, contextually appropriate |
| 5 | /cambridge/9709/past-papers/ | "9709 Past Papers hub" | Line 296 | WEAK -- anchor text "9709 Past Papers hub" is generic. Should be "Cambridge 9709 Past Papers: Complete Guide" or similar |
| 6 | /cambridge/9709/past-papers/ | "9709 past papers hub" | Line 395 | DUPLICATE URL (same as #5). Anchor text is lowercase variant. Both point to same placeholder URL. |
| 7 | https://www.exampilot.io/waitlist | "join the ExamPilot waitlist" | Lines 61, 246, 368, 444 | ADEQUATE -- consistent anchor text. Consider varying to "get your predicted grade" or "track your exam readiness" on 2 of the 4 occurrences. 4 occurrences of same URL is within limits for a pillar page CTA but ensure CMS doesn't flag as over-linking. |
| 8 | /blog/category/cambridge-9709 | (frontmatter only -- not in article body) | Not present in body | ISSUE -- this link is in the frontmatter but not used in the article body. Either add it to the body or remove from frontmatter internal links list. |

### URL formatting issue (critical)

All URLs in the article body currently have spaces:
- `https://www. exampilot. io/waitlist` (line 61, 246, 368, 444)
- `https://www. cambridgeinternational. org/...` (line 97)

These are formatting artifacts from the draft. Every URL must have spaces removed before publishing. They will 404 as written.

---

## 2. Anchor Text Quality Assessment

| Assessment | Count | Examples |
|---|---|---|
| Descriptive and keyword-rich | 4 | "A Level Maths Functions: Cambridge 9709 Pure 1 Guide", "9709 P1 Differentiation: Exam Tips and Worked Solutions" |
| Adequate but improvable | 2 | "join the ExamPilot waitlist", "9709 Past Papers hub" |
| Generic / weak | 0 | None |
| Missing from body | 1 | /blog/category/cambridge-9709 |

Overall anchor text quality is good. The four spoke links use the actual article titles, which is the correct approach for pillar-to-spoke linking.

---

## 3. Internal Linking Gaps -- Missing Opportunities

### Gap 1: No link to /cambridge/9709/ parent hub

The article lives at `/cambridge/9709/pure-1/` but there is no link up to the parent `/cambridge/9709/` hub page. Once the Cambridge 9709 parent hub is created, add a reference in the intro section: "...part of the [Cambridge 9709 complete qualification guide](/cambridge/9709/)." Even before the parent exists, include a placeholder link -- consistent with the spoke-to-pillar placeholder approach used in spoke articles.

**Add to:** Line 67-68, within "Cambridge 9709 is the Cambridge International AS and A Level Mathematics qualification."

### Gap 2: Spoke articles for Functions and Trigonometry linked once only

The functions and trigonometry spoke articles are linked once each (lines 128 and 172) within the topic breakdown sections. On a 4,400-word pillar page, these spokes should ideally be linked a second time in the conclusion/next-steps section.

**Check:** The conclusion (line 430-444) currently links all four spokes -- but functions and trigonometry are listed with different anchor text ("A Level Maths Functions: Cambridge 9709 Pure 1 Guide") while differentiation uses a slightly different format ("A Level Maths Differentiation: Cambridge 9709 Pure 1 Guide"). Confirm these match the actual page titles to avoid misleading anchor text.

### Gap 3: No link to /blog/category/cambridge-9709 in article body

This category page is listed in frontmatter internal links but does not appear anywhere in the body. The most natural placement is within the "Best Resources" section (line 342), where listing ExamPilot's Cambridge 9709 content category would add value:

> "For all ExamPilot content on this qualification, see our [Cambridge 9709 resource library](/blog/category/cambridge-9709)."

### Gap 4: No link to planned /cambridge/9709/common-mistakes/ spoke

The "Common Mistakes from Cambridge 9709 Examiner Reports" section (line 300) is the ideal place to reference the planned Common Mistakes spoke article. Even though it hasn't been written yet, add a forward-pointing placeholder link:

> "For a full topic-by-topic breakdown of examiner-flagged mistakes, see our [Cambridge 9709 Common Mistakes guide](/cambridge/9709/common-mistakes/) -- coming soon."

This builds the link structure before the article exists and creates a crawlable placeholder.

### Gap 5: No link to /cambridge/9709/best-resources/ planned spoke

The "Best Resources" section compares PapaCambridge, Save My Exams, PMT, and ExamPilot. The planned "Best Cambridge 9709 Revision Resources 2026" spoke (/cambridge/9709/best-resources/) should be linked here with a forward reference, similar to Gap 4.

---

## 4. Cross-Linking -- Spoke Article Integration

### Published spokes (4 confirmed from codebase):

| Spoke | URL | Currently linked from pillar? | Anchor text used |
|---|---|---|---|
| Integration | /cambridge/9709/pure-1/integration/ | YES (lines 221 + 438) | "A Level Maths Integration: Cambridge 9709 Pure 1 Guide" |
| Differentiation | /cambridge/9709/pure-1/differentiation/ | YES (lines 206 + 439) | "9709 P1 Differentiation: Exam Tips and Worked Solutions" / "A Level Maths Differentiation: Cambridge 9709 Pure 1 Guide" |
| Functions | /cambridge/9709/pure-1/functions/ | YES (lines 128 + 440) | "A Level Maths Functions: Cambridge 9709 Pure 1 Guide" |
| Trigonometry | /cambridge/9709/pure-1/trigonometry/ | YES (lines 172 + 441) | "A Level Maths Trigonometry: Cambridge 9709 Pure 1 Guide" |

All four published spokes are linked from the pillar -- this is correct hub-and-spoke architecture.

### Reverse linking (do these spokes link back to this pillar?):

This pillar page is new (2026-04-03). The spoke articles should already include placeholder links to `/cambridge/9709/pure-1/` (per the research brief's internal linking rules). Before publishing this pillar, verify each spoke article contains the back-link. If any are missing, add them:

- `cambridge-9709-pure1-integration-2026-03-23.md` -- check for /cambridge/9709/pure-1/ link
- `cambridge-9709-pure1-differentiation-2026-03-24.md` -- check for /cambridge/9709/pure-1/ link
- `cambridge-9709-functions-2026-03-24.md` -- check for /cambridge/9709/pure-1/ link
- `9709-pure1-trigonometry-2026-03-25.md` -- check for /cambridge/9709/pure-1/ link

### Spoke articles not yet written (link gaps in pillar):

The pillar's conclusion (line 436-442) links only the 4 published spokes. The planned spokes for Coordinate Geometry, Quadratics, Series/Circular Measure, and the strategy spokes (Common Mistakes, Best Resources, Past Papers) are not yet linked. The current text handles this correctly by saying "The five detailed guides in this series" -- but once those additional spokes are published, the conclusion list must be expanded and this count updated.

---

## 5. External Link Quality Assessment

| # | URL | Anchor Text | Location | Quality |
|---|---|---|---|---|
| 1 | https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-9709/ | "Cambridge 9709 syllabus" | Line 97 | GOOD -- authoritative source, relevant. Note URL has spaces in draft -- fix before publish. |
| 2 | "Cambridge 9709 examiner reports 2024/2025" | (frontmatter only -- not a real URL yet) | Frontmatter | PLACEHOLDER -- this needs a real URL. The 2024 examiner report URL from Cambridge International should be sourced and added to the body text. |

### Missing external links

The article makes several claims that require citations:

1. **"Cambridge 9709 is taken in over 160 countries"** (line 448) -- cite: Cambridge International About page or annual report. URL: https://www.cambridgeinternational.org/about-us/
2. **"The research on this is unambiguous: retrieval practice outperforms re-reading by a factor of two to three"** (line 259) -- this is a specific empirical claim. Cite: Roediger & Karpicke (2006) or similar peer-reviewed research. Without a citation, this may be challenged as unverified. Even linking to a reputable secondary source (e.g., The Learning Scientists) would strengthen E-E-A-T.
3. **Grade boundary data** (lines 409-412) -- stated as "historically" without source. Link to: https://www.cambridgeinternational.org/exam-administration/results-and-certificates/grade-thresholds/ to let students verify.
4. **Save My Exams price "around £60/year"** (line 357) -- verify this is current and add a note that pricing may change. Could become outdated quickly.

---

## 6. Broken and Placeholder Links

| Issue | URL | Action Required |
|---|---|---|
| CRITICAL: Spaces in all URLs | All exampilot.io and cambridgeinternational.org links | Remove spaces from every URL before publish |
| PLACEHOLDER: Past papers hub | /cambridge/9709/past-papers/ (×2 in body, ×1 in frontmatter) | Replace with live URL when past papers article is published, or mark as intentional placeholder |
| PLACEHOLDER: Examiner reports external URL | Listed in frontmatter as "Cambridge 9709 examiner reports 2024/2025" without a URL | Source the actual URL from cambridgeinternational.org |
| NOT LINKED: /blog/category/cambridge-9709 | In frontmatter but not in body | Add to body (see Gap 3 above) |

---

## 7. Link Count Summary

| Type | Current Count | Target | Status |
|---|---|---|---|
| Internal links (unique URLs) | 6 (4 spokes + past papers hub + waitlist) | 7-10 for a pillar page | SLIGHTLY LOW -- add category page and parent hub link |
| Internal link occurrences | ~10 (including multiple waitlist CTAs and duplicate past papers link) | Proportionate to 4,400 words | ACCEPTABLE |
| External links | 1 real + 1 placeholder | 2-4 | LOW -- add 2-3 citation links for claims |
| Waitlist CTA links | 4 | 3-5 for pillar page | ACCEPTABLE |

**Priority actions before publishing:**
1. Fix all URL spaces (CRITICAL)
2. Add parent hub link /cambridge/9709/ (HIGH)
3. Add /blog/category/cambridge-9709 to body (MEDIUM)
4. Add retrieval practice external citation (MEDIUM)
5. Add Cambridge grade boundaries external link (MEDIUM)
6. Confirm spoke back-links exist before this pillar goes live (HIGH)
