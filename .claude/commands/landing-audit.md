---
name: landing-audit
description: CRO audit of an ExamPilot landing page. Runs a 5-module audit across above-fold, CTA quality, trust signals, friction, and scoring. Accepts a local file path or URL.
---

## Input

$ARGUMENTS

Expect: local file path or URL to a landing page. Examples:
- `marketing/pipelines/published/landing-cambridge-9709-pure-1.md`
- `https://exampilot.com/cambridge/9709-pure-1`
- `https://exampilot.com/pricing`

If not provided, ask: "Which landing page do you want to audit? Paste the URL or file path."

## Execution

### Step 1: Read the landing page

**If local file path:** Read the file directly.

**If URL given:** Fetch the page content via WebFetch. Extract:
- Full page text
- All headings (H1, H2, H3)
- All CTA button text and placement (above/below fold)
- Trust signals (testimonials, logos, statistics, guarantee text)
- Any pricing mentions

### Step 2: Load audience context

Read these in parallel:
- `marketing/context/audience-segments.md` — who we're writing for, their pain points, decision drivers
- `references/voice-house.md` — tone and language standards

Identify which audience segment this page targets:
- `student-cambridge` — Cambridge International 9709 student
- `student-edexcel` — Edexcel IAL student
- `resit-student` — student preparing for resit
- `parent` — parent evaluating for their child

Adjust audit criteria based on segment — parents care more about outcomes and safety, students care more about relevance and ease.

### Step 3: Determine page type and fold

Classify the page:
- **TOFU landing page** (blog article, topic hub): Visitor is problem-aware, not solution-aware. High friction on conversion ask.
- **MOFU page** (feature page, category hub): Visitor is solution-aware. Moderate conversion ask.
- **BOFU page** (pricing, comparison, free trial): Visitor is decision-ready. Hard conversion ask appropriate.

Estimate the fold: anything visible without scrolling on mobile (assume 667px viewport). First 200-300 words is typically above fold for a typical landing page layout.

### Step 4: Run 5-module audit

---

**Module 1: Above-fold check (25 points)**

| Check | Points | Result | Note |
|---|---|---|---|
| H1 contains specific benefit (not just keyword) | 5 | pass/fail | |
| H1 contains primary keyword | 5 | pass/fail | |
| H1 under 60 characters | 3 | pass/fail | |
| Value prop answers "why ExamPilot over SaveMyExams" | 7 | pass/partial/fail | |
| Primary CTA visible above fold | 5 | pass/fail | |

Value prop check: does the above-fold content make it clear what ExamPilot does differently from free alternatives (past paper sites) and paid alternatives (SaveMyExams)? ExamPilot's differentiator = adaptive practice, not static notes.

Module 1 score: X/25

---

**Module 2: CTA quality (25 points)**

| Check | Points | Result | Note |
|---|---|---|---|
| Exactly one primary CTA (not multiple competing CTAs) | 5 | pass/fail | |
| CTA copy is action + benefit (not generic "Sign Up") | 8 | pass/partial/fail | |
| CTA appears above fold | 4 | pass/fail | |
| CTA appears after at least one other major section | 4 | pass/fail | |
| No CTA says "Learn More" as primary (weak for BOFU) | 4 | pass/fail | |

Good CTA copy examples: "Start practising free", "Try ExamPilot free", "See how it works"
Bad CTA copy: "Sign Up", "Get Started", "Learn More", "Submit"

Flag: any CTA that contains B2B language ("Request a demo", "Contact sales", "Book a call") — wrong audience.

Module 2 score: X/25

---

**Module 3: Trust signals (25 points)**

| Check | Points | Result | Note |
|---|---|---|---|
| At least one trust signal above fold | 7 | pass/fail | |
| Exam board logos or official alignment claim (Cambridge, Pearson) | 6 | pass/partial/fail | |
| Student testimonial: specific outcome (not generic "great app") | 6 | pass/partial/fail | |
| Risk reversal present ("free trial", "no credit card required") | 6 | pass/fail | |

Trust signal quality guide:
- Weak: "Students love ExamPilot" (generic)
- Medium: "Trusted by A Level Maths students" (category but no number)
- Strong: "Over [X] Cambridge 9709 students practising this week" [VERIFY if claim exists]
- Best: Named student testimonial with specific outcome ("I improved my P1 score from 45% to 72% using ExamPilot" — [VERIFY])

Flag any unverifiable or missing trust signals.

Module 3 score: X/25

---

**Module 4: Friction (25 points)**

| Check | Points | Result | Note |
|---|---|---|---|
| Reading level appropriate: simple, direct, no jargon | 7 | pass/partial/fail | |
| Page length appropriate for funnel stage | 6 | pass/partial/fail | |
| No B2B language or institutional framing | 7 | pass/fail | |
| No filler phrases that add length without value | 5 | pass/partial/fail | |

**Reading level guidance:**
- Student pages: write for a 16-year-old. Short sentences. No academic language in the copy (ironic for an academic tool).
- Parent pages: slightly more formal but still direct. No jargon.
- Run informal check: would a GCSE student understand every sentence? If not, flag.

**Page length by stage:**
- TOFU topic hub: 1500-2500 words is fine
- MOFU feature page: 800-1500 words
- BOFU pricing/comparison: 600-1200 words (shorter = less friction at decision stage)

**B2B language flags (automatic fail if found):**
- "school licensing", "institutional", "departments", "teachers and administrators"
- "enterprise plan", "volume pricing", "procurement"
- "our platform", "our solution" (sounds SaaS/B2B)

**Filler phrase flags:**
- "In today's digital world..."
- "It's important to note that..."
- "As you can see..."
- "We pride ourselves on..."
- "Cutting-edge AI technology"

Module 4 score: X/25

---

**Module 5: Score and threshold**

Total score: [M1 + M2 + M3 + M4] / 100

- 75-100: **Pass** — page is conversion-ready. Minor improvements only.
- 60-74: **Needs work** — fix critical issues before running paid traffic or publishing.
- Below 60: **Fail** — significant CRO problems. Do not promote until fixed.

### Step 5: Build prioritized fix list

**Critical (must fix before promoting this page):**
- Any Module 1 or 2 check that failed
- B2B language found (Module 4)
- No primary CTA above fold

**Quick wins (15-30 minutes each):**
- CTA copy rewrite
- Add risk reversal to CTA
- Add exam board specificity to value prop
- Fix filler phrases

**Strategic (schedule in next sprint):**
- Add student testimonial with specific outcome
- Add exam board logos above fold
- Split-test alternative headline

### Step 6: Save report

Save to `marketing/pipelines/research/landing-audit-[slug]-YYYY-MM-DD.md`

```yaml
---
type: landing-audit
source: [file path or URL]
page_type: tofu | mofu | bofu
target_segment: ""
audit_date: YYYY-MM-DD
total_score: 0
result: pass | needs-work | fail
module_scores:
  above_fold: 0
  cta_quality: 0
  trust_signals: 0
  friction: 0
---

## Landing Page CRO Audit: [Page Name]

### Score Summary
| Module | Score | Max | Result |
|--------|-------|-----|--------|
| Above-fold | X | 25 | pass/fail |
| CTA quality | X | 25 | pass/fail |
| Trust signals | X | 25 | pass/fail |
| Friction | X | 25 | pass/fail |
| **Total** | **X** | **100** | **pass/needs-work/fail** |

### Critical Issues
[Numbered, in order of conversion impact]

### Quick Wins
[Numbered, with specific copy suggestions where possible]

### Strategic Improvements
[Numbered]

### Recommended next step
[If score < 75: "Fix critical issues inline or run `/rewrite [file]` light scope for copy fixes"]
[If score ≥ 75: "Page is ready. Consider running paid traffic or `/content-calendar` to schedule promotion."]
```

### Step 7: Report

Show the score table and critical issues. Ask:
- "Score: [X]/100 — [Pass/Needs work/Fail]. [X] critical issues found."
- "Want me to rewrite the above-fold section and CTAs now, or review the full report first?"
