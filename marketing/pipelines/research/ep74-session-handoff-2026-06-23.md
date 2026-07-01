---
type: session-handoff
ticket: EP-74
title: "Examiner Report Analysis — Cambridge 9709 Bridge Content"
status: phase-1-in-progress
date: 2026-06-23
next-action: complete-phase-1-read-remaining-4-pdfs
---

# EP-74 Session Handoff — 2026-06-23

This document captures the full state of the EP-74 workflow at the end of the 2026-06-23 session. Read this at the start of the next session to resume without re-deriving context.

---

## What EP-74 is

**Linear ticket:** EP-74 — "Write + publish examiner report analysis (Cambridge 9709 bridge content)"
**Priority:** Urgent (overdue — original due date 2026-06-09)
**Owner:** Teresa
**Phase 0 milestone:** Yes (Alpha Launch project)

**Ticket scope:**
- Write an SEO bridge content article using Cambridge 9709 examiner report data
- Topic angle: what the examiner reports reveal about how students lose marks — pitched as a learning-science insight piece
- FAQPage schema is explicitly required (from EP-74 ticket description)
- Target: content that ranks for examiner-report-adjacent keywords and supports the Pure 1 pillar page (EP-67)

---

## 5-Phase Workflow Plan

The workflow was designed across two sessions. All phases are confirmed:

### Phase 1 — Extract intelligence from examiner reports (IN PROGRESS)
Read all 8 Cambridge 9709 examiner report PDFs. Extract Pure 1 (Papers 9709/11, /12, /13) findings: recurring mistakes, examiner language, mark-loss patterns, topic-by-topic signals. Produce a structured findings document for Teresa to review.

### Phase 2 — Keyword research
Run `/research-keywords` + `/research-serp` for examiner-report-related search terms.

### Phase 3 — Wiki check
Fetch relevant wiki articles via `gh api` to confirm no conflicting positioning.

### Phase 4 — Write article
Run `/write-article` using Phase 1 findings + Phase 2 keyword brief as input.

### Phase 5 — Post-production
Run `/copy-editing` + `/schema-markup` (FAQPage required) + `/seo-audit` + `/capture` (to wiki).

**Teresa's instruction:** Pause at the end of each phase for visual review before proceeding.

---

## Phase 1 Status: INCOMPLETE

### PDFs Location
`/Users/teresagonzalez/Documents/Spyglass/9709 Examiner Reports/`

### File Naming Convention
Cambridge's native naming: `9709_{s/w/m}{YY}_er.pdf`
- `s` = summer (May/June)
- `w` = winter (Oct/Nov)
- `m` = March

### 8 PDFs — Read Status

| File | Session | Status |
|------|---------|--------|
| `9709_m20_er.pdf` | March 2020 | READ ✓ |
| `9709_s21_er.pdf` | May/June 2021 | READ ✓ |
| `9709_s22_er.pdf` | May/June 2022 | READ ✓ |
| `9709_s23_er.pdf` | May/June 2023 | READ ✓ (largest file, 7.5MB, fully rendered ~64 pages) |
| `9709_s24_er.pdf` | May/June 2024 | NOT YET READ |
| `9709_w20_er.pdf` | Oct/Nov 2020 | NOT YET READ |
| `9709_w21_er.pdf` | Oct/Nov 2021 | NOT YET READ |
| `9709_w22_er.pdf` | Oct/Nov 2022 | NOT YET READ |

---

## Phase 1 Findings — Extracted to Date

The findings below were extracted from the 4 PDFs read in this session. The s23 findings are the most detailed (full rendering). The m20, s21, s22 findings were in context during the session but compacted — they are summarised at a higher level.

### From 9709_s23_er.pdf (May/June 2023) — DETAILED

**Paper 9709/11 — General examiner messages:**
- Candidates must show full working, especially for quadratics (factorisation / formula / completing the square — all must be visible)
- No calculator was available for Paper 1; unsupported answers receive no marks
- Definite integration: limits must be shown substituted, not just stated

**Paper 9709/11 — Q4 Circular Measure:**
- Most candidates correctly found the radian angle and arc length
- Stronger responses split the triangle into two right-angled triangles
- Common error: assuming triangle ABC was right-angled (it was not) → wrong area / perimeter calculations
- Common error: trying to find a segment area rather than a perimeter

**Paper 9709/11 — Q9 Rates of Change (differentiation):**
- Majority of candidates did NOT recognise that differentiation was needed → awarded zero marks
- Most common error: substituting h = 10 directly into the volume formula without differentiating

**Paper 9709/11 — Q10 Integration / Volume of Revolution:**
- Chain rule omitted in many scripts
- Power reduced rather than increased during integration (confusion with differentiation rule)
- Many candidates confused integrate vs differentiate direction

**Paper 9709/11 — Q11 Stationary Points:**
- Most candidates correctly found d²y/dx²
- Mark loss primarily from arithmetical errors in substitution, not conceptual misunderstanding

**Paper 9709/12:**
- Integration (Q1): well done by most candidates
- Binomial expansion (Q2): very well done
- Completing the square (Q3): partially done — many could start but struggled to complete
- Definite integration (Q5): most successful question on the paper

**Paper 9709/13 — Q6 Circular Measure:**
- Many excellent solutions across the cohort
- Radians used confidently
- Mark loss: accuracy — candidates who didn't write to 3 significant figures lost accuracy marks

---

### From 9709_m20_er.pdf, 9709_s21_er.pdf, 9709_s22_er.pdf — HIGH-LEVEL PATTERNS

These three PDFs were read in the same session. Full detail was in context but compacted. Key patterns noted:

**Circular Measure (recurring across years):**
- Radian vs degree confusion is persistent across all years
- Arc length and sector area: formula recall strong, but application to composite figures weak
- Perimeter vs area confusion: candidates frequently calculate area when perimeter is asked
- Working with non-right-angled triangle components requires sine rule / splitting into right-angled parts — frequently missed

**Differentiation and Integration (recurring):**
- Rates of change questions: recognition that dy/dx (or dV/dt etc.) is needed is the primary failure point
- Chain rule: the most consistently lost technique — especially in integration by substitution context
- Definite integration: limits substitution errors are the primary mark-loss mechanism
- Stationary points: second derivative test generally understood; substitution errors lose marks

**General Pure 1 Patterns (across all years):**
- Show-that questions: candidates frequently assume the result and work backwards
- Accuracy: 3 significant figures not maintained — systematic mark loss across all topics
- Unsupported answers: especially in quadratic questions, full method must be shown

---

## Next Steps for Phase 1 Completion

### Immediate next actions:
1. Read the remaining 4 PDFs in parallel:
   - `9709_s24_er.pdf`
   - `9709_w20_er.pdf`
   - `9709_w21_er.pdf`
   - `9709_w22_er.pdf`

2. Synthesise ALL 8 reports into a structured findings document covering:
   - By topic: Circular Measure / Differentiation / Integration / Algebra / Trigonometry / Functions
   - Per topic: top 3 recurring mistakes, exact examiner language used, mark-loss mechanism
   - Cross-year patterns: which errors are consistent vs improving
   - Quotable examiner phrases (for use as pull-quotes in the article)

3. Present structured findings document to Teresa for visual review → go-ahead for Phase 2

---

## Other Items Open from This Session

These are NOT part of EP-74 but were discussed and remain open:

### Circular Measure article (already published)
- SEO audit score: 76/100 Good (`marketing/pipelines/research/seo-audit-circular-measure-2026-06-22.md`)
- **Important — open actions:**
  - Add 1-2 external authority links (Cambridge 9709 syllabus page, examiner report, or Ofqual) — currently zero external links → External Linking dimension scored 0/10
  - Remove duplicate internal link to `/cambridge/9709/pure-1` (appears twice)
- **Nice to have:** GEO improvements (open first-paragraph sentences, add entity-specific stats per H2)

### EP-164 (Enitan)
- Template-level fix: group the 5 template-rendered H2 sections under a parent H2 to fix heading structure SEO issue on all topic pages

### GSC Migration (www → non-www)
- `www.exampilot.io` and `exampilot.io` are separate GSC properties
- The Circular Measure page at `https://exampilot.io/cambridge/9709/pure-1/circular-measure` cannot be indexed until the non-www property is properly set up
- **Change of Address tool issue:** exampilot.io not appearing in the dropdown — most likely cause: ownership level on the new property is Editor, not Owner. HTML tag verification may only grant Editor status.
- **Fix:** Verify ownership level on `https://exampilot.io` in GSC → if Editor, re-verify using DNS TXT record (grants Owner) → re-attempt Change of Address tool
- **Fallback:** Submit sitemap directly to the non-www property; 301 redirects will consolidate authority passively over 2-4 weeks even without Change of Address

### Internal links map maintenance
- `marketing/context/internal-links-map.md` references `/cambridge/` but live URL structure is `/cambridge/9709/` — needs updating before next internal linker agent run

### Pending Linear issues (not EP-74)
- **EP-68:** Spoke: Coordinate Geometry — due Jul 15, not yet started
- **EP-60:** Join + observe 2-3 Facebook parent groups — overdue (Jun 21), still to do
- **EP-59:** Teresa's LinkedIn profile — should be complete by now; confirm status

---

## Content Rules Reminders (for EP-74 article)

These apply specifically to this piece:

- No "AI tutor" or "AI-powered" language — use "learning science", "adaptive", "spaced repetition"
- No "5-7 marks on Paper 1" or any unverified numerical claim — see [VERIFY] rule
- Pricing: EUR only (Monthly EUR29, Quarterly EUR69, Semi-annual EUR96, Annual EUR144)
- FAQPage schema is required (explicit in EP-74 ticket)
- UK English throughout
- Key Takeaways block required immediately after introduction
- GEO: answer-first structure, extractable passages, full entity names on first mention ("Cambridge International AS & A Level Mathematics 9709")
- ExamPilot is a "bridge content" piece — not a product page; tone is educational insight, not promotional
