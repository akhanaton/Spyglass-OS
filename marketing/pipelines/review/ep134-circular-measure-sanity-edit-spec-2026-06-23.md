---
type: sanity-edit-spec
article: cambridge/9709/pure-1/circular-measure
linear-issue: EP-134
seo-audit-score: 76 (pre-fix)
target-score: 82+
status: in-review
created: 2026-06-23
---

# EP-134 Sanity Edit Spec: Circular Measure Spoke

Apply all fixes in Sanity Studio before publishing. Tick each box when applied.

---

## Fix 1 — Key Takeaways block [REQUIRED — DoD]

**Where:** Add a plain-text block immediately before the first H2, after the article introduction.

**In Sanity:** Add a new `blockContent` block at the top of the body. Use a paragraph heading or styled block if the cluster template supports it — check how other restructured topic pages (e.g. Trigonometry, Integration) handle this block in Sanity.

**Content to add:**

```
Key Takeaways

• Circular measure in Cambridge 9709 Pure 1 covers radians, arc length, sector area, and segment problems — all examined in Paper 1.
• The most common examiner error: using degree mode instead of radians when calculating arc length or sector area, typically costing 2–3 marks.
• Core formula: arc length s = rθ and sector area A = ½r²θ only hold when θ is in radians — not degrees.
• ExamPilot's adaptive practice detects the degree/radian error and targets it with spaced-repetition questions calibrated to your exam level.
```

- [ ] Key Takeaways block added in Sanity, positioned before the first H2

---

## Fix 2 — H2/H3 restructuring [REQUIRED — DoD]

**Target:** 2 H2s in the body, with H3s nested under each. This matches the restructured cluster pattern.

**Current structure (confirmed via live page fetch 2026-06-23):**

H2 — What Circular Measure Covers in 9709 Pure 1
- H3 — What's in scope for Paper 1

H2 — Radians: The Unit That Makes the Formulae Work
H2 — Sector, Segment, and Triangle: The Three Regions
H2 — The Perimeter Trap
H2 — Composite Shape Problems
H2 — How Circular Measure Connects to Trigonometry
H2 — Summary
H2 — What to Do Next
H2 — Key Formulas
H2 — Worked Examples
H2 — Common Mistakes
H2 — Exam Tips
H2 — Frequently Asked Questions *(rendered from `faqs` Sanity field — not editable in body)*

**Target structure:**

**H2 — Understanding Circular Measure in Cambridge 9709**
- H3 — What Circular Measure Covers in 9709 Pure 1 *(keep existing heading, already descriptive)*
  - H4 — What's in scope for Paper 1 *(existing H3 — demote to H4 or fold into parent body)*
- H3 — Radians: The Unit That Makes the Formulae Work *(keep existing heading)*
- H3 — Sector, Segment, and Triangle: The Three Regions *(keep existing heading)*
- H3 — The Perimeter Trap *(keep existing heading)*
- H3 — Composite Shape Problems *(keep existing heading)*
- H3 — How Circular Measure Connects to Trigonometry *(keep existing heading)*

**H2 — Cambridge 9709 Circular Measure: Exam Practice and Formula Reference**
- H3 — Key Formulas
- H3 — Worked Examples
- H3 — Common Mistakes
- H3 — Exam Tips
- H3 — Circular Measure Formula Summary for Cambridge 9709 Pure 1
- H3 — What to Do Next: Practise Circular Measure on ExamPilot

FAQ remains as its own section (controlled by the `faqs` field, not the body).

**In Sanity:** Change each current H2 block's style to H3 in the body editor. The two new H2s are new `blockContent` blocks inserted at the correct positions.

- [x] H2 restructuring applied (2026-06-23) — most headings restructured
- [ ] Confirm remaining H2s resolved — verify final H2 count = 2 in rendered page

---

## Fix 3 — External authority links [REQUIRED — DoD]

**Current:** 1 external link (cambridgeinternational.org homepage, linked twice). Need ≥ 2 distinct authority links.

**Links to add:**

### Link A — Cambridge 9709 Programme page
- **URL:** `https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-9709/`
- **Anchor text:** `Cambridge International AS & A Level Mathematics 9709 programme`
- **Where:** Body text of the "What Circular Measure Covers in 9709 Pure 1" H3 — first sentence that references the qualification. The intro field doesn't support links (confirmed), so this is the earliest available placement.
- **Example sentence:** "Circular measure is a core topic in the [Cambridge International AS & A Level Mathematics 9709 programme](URL), examined in Paper 1 (Pure Mathematics 1)."

### Link B — Cambridge 9709 Syllabus (2026–2028)
- **URL:** [VERIFY] Navigate to Cambridge International → 9709 → Syllabus and Past Papers and copy the direct PDF or syllabus overview URL. The 2026–2028 syllabus document is the authoritative reference.
- **Anchor text:** `Cambridge 9709 syllabus (2026–2028)`
- **Where:** Key Formulas H3 or Exam Tips H3 — "All formulas listed here are drawn from the [Cambridge 9709 syllabus (2026–2028)](URL)."

### Link C — Optional: Cambridge examiner report (degree/radian error)
- If an examiner report explicitly cites the degree/radian error in circular measure (check 9709 Paper 1 or Paper 3 examiner reports from 2022–2024), add it with anchor: `Cambridge 9709 examiner report`
- **Where:** Common Mistakes H3 — supports the "most common error" claim with a cited source

- [x] Link A added (Cambridge programme page) — in "What Circular Measure Covers" H3 body (2026-06-23)
- [x] Link B — Cambridge syllabus link already present in article (pre-existing, confirmed 2026-06-23)
- [ ] Link C — optional, skip unless examiner report citation found

**DoD criterion met: ≥ 2 external authority links confirmed.**

---

## Fix 4 — Heading renames for GEO [DONE ✓]

**Confirmed done (2026-06-23).** Both headings renamed in Sanity.

| Previous heading | New heading |
|------------------|-------------|
| Summary | Circular Measure Formula Summary for Cambridge 9709 Pure 1 |
| What to Do Next | What to Do Next: Practise Circular Measure on ExamPilot |

---

## Fix 5 — CTA language [DONE ✓]

**Confirmed via live page fetch (2026-06-23).** CTA now reads "Join the ExamPilot waitlist" / "Join the Waitlist" — no "AI-powered" language present. No action required.

---

## Fix 6 — Duplicate internal link [DONE ✓]

**Confirmed via live page fetch (2026-06-23).** `/cambridge/9709/pure-1` appears once in the body ("Complete Cambridge 9709 Pure 1 Revision Guide"). The second "Pure 1" hit is the breadcrumb navigation — template-level, not a body link. No action required.

---

## Fix 7 — Full entity name on first mention [PARTIALLY DONE]

**Text change done (2026-06-23).** "Cambridge International AS & A Level Mathematics 9709" is now spelled out in the introduction.

**Link blocked:** The Sanity field where the intro text sits does not support inline hyperlinks. The Cambridge programme page link (Fix 3 Link A) cannot be placed there.

**Redirect Fix 3 Link A:** Place the Cambridge programme page link in the first available body field that supports hyperlinks — the "What Circular Measure Covers in 9709 Pure 1" H3 body text. See Fix 3 below.

- [x] Full entity name added in introduction
- [ ] Cambridge programme page link — move to Fix 3 Link A placement in body

---

## Post-application checklist

After all Sanity edits are applied:

- [ ] Preview the page and verify Key Takeaways block renders correctly (before first H2)
- [ ] Verify H2 count in rendered page = 2 (use browser Inspect → search for `<h2>`)
- [ ] Verify external links open correctly
- [ ] Verify no "AI-powered" language remains on the page *(Fix 5 confirmed done — but re-check after any template changes)*
- [ ] Run `/seo-audit` on the live URL once published — target score ≥ 82

---

## Definition of Done (EP-134)

| Criterion | Status |
|-----------|--------|
| Key Takeaways block present | Pending |
| H2 count ≤ 4 (target: 2) | Pending |
| ≥ 2 external authority links | Pending |
| /seo-audit score ≥ 76 | 76 pre-fix — re-run post-publish |
