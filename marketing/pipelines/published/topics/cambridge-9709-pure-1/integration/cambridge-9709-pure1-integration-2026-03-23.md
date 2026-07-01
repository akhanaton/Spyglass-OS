<!--
ARTICLE METADATA
=================
Title: A Level Maths Integration: Cambridge 9709 Pure 1 Guide
Slug: cambridge-9709-pure-1-integration
URL: /cambridge/9709/pure-1/integration/
Author: Teresa Gonzalez
Categories: Cambridge 9709
Tags: integration, pure 1, 9709, a level maths, cambridge, revision
Status: draft
Published At: 2026-03-23

SEO:
  Meta Title: A Level Maths Integration: 9709 Pure 1 Guide | ExamPilot (59 chars)
  Meta Description: Struggling with a level maths integration? This 9709 Pure 1 guide covers every technique with worked solutions, area problems, and examiner-flagged mistakes. (159 chars)

FAQs (for Sanity FAQ field + FAQPage schema):
  1. Q: Is integration harder than differentiation?
     A: Most students find integration harder because it requires pattern recognition rather than following a fixed set of rules. Differentiation has clear mechanical steps — bring the power down, reduce by one. Integration asks you to work backwards, which means recognising what was differentiated to produce the expression you're looking at. The good news is that 9709 Pure 1 only tests a small set of integration techniques, so with targeted practice, you can build that pattern recognition quickly.

  2. Q: How many marks is integration worth in 9709 Paper 1?
     A: Integration questions typically carry 15-20 marks out of 75 on Paper 1, roughly 20-27% of the paper. But integration also appears indirectly in questions that combine it with differentiation or coordinate geometry, so its true mark contribution is often higher. Calculus as a whole (differentiation + integration) accounts for 35-40% of Paper 1 marks.

  3. Q: Do I need integration by parts for Pure 1?
     A: No. Integration by parts and integration by substitution (the formal method) are Pure 3 topics. For Pure 1, you only need basic integration of powers of x, the reverse chain rule for expressions like (ax + b)^n, definite integrals, and finding areas under curves. If you are studying for Paper 1 only, focus on these techniques.

  4. Q: What is the difference between definite and indefinite integrals?
     A: An indefinite integral has no limits and produces a general expression plus a constant of integration (+C). A definite integral has upper and lower limits, and produces a specific numerical value — you evaluate the expression at both limits and subtract. In 9709 exams, indefinite integrals test whether you know the rules, while definite integrals test whether you can apply them to find areas or evaluate expressions.

  5. Q: Can I use a calculator for integration in 9709?
     A: You can use a scientific calculator in 9709 Paper 1, but you must show your working. The examiner awards marks for method, not just the final answer. If you use a calculator to check a definite integral but only write the answer, you will lose method marks. Always write out each integration step, substitute the limits, and show the subtraction.

Structured Data:
  - FAQPage schema (from FAQs above)
  - Article schema (author, datePublished, dateModified)
  - BreadcrumbList: Home > Cambridge 9709 > Pure 1 > Integration

Internal Links:
  - /cambridge/9709/pure-1/ (pillar, placeholder)
  - /cambridge/9709/pure-1/differentiation/ (spoke, placeholder)
  - /cambridge/9709/past-papers/ (pillar, placeholder)
  - https://www.exampilot.io/waitlist (CTA)
  - /blog/category/cambridge-9709 (category)

External Links:
  - https://www.cambridgeinternational.org (official syllabus)
  - Cambridge 9709 examiner reports (cited in common mistakes section)

Sanity Custom Blocks Used:
  - mathBlock (LaTeX equations)
  - calloutBlock (Exam Tip, Common Mistake, Examiner Says, Remember, Key Formula)
  - workedSolution (step-by-step solutions with annotations)
  - comparisonTable (integration methods comparison)
  - FAQ section (from post.faqs field)

Visual Assets Needed:
  1. Integration method decision flowchart (Excalidraw → SVG)
  2. Shaded area diagram: area under curve (Desmos/GeoGebra → SVG)
  3. Shaded area diagram: negative area trap (Desmos/GeoGebra → SVG)
  4. Shaded area diagram: area between curve and line (Desmos/GeoGebra → SVG)
-->

> *This guide is part of our [Complete Cambridge 9709 Pure 1 Revision Guide](/cambridge/9709/pure-1/) — your comprehensive resource for exam preparation.*

# A Level Maths Integration: Cambridge 9709 Pure 1 Guide

Integration is where 9709 Paper 1 separates the A\* students from the rest. Not because it's harder than other topics — but because most revision resources teach it badly. They give you the rules and then throw past papers at you. That's like learning to drive by memorising the Highway Code and then entering a race.

This guide covers everything you need for a level maths integration in Cambridge 9709 Pure 1 — the rules, the methods, the exam traps, and the techniques that actually earn marks. It maps directly to Topics 1.8.1–1.8.5 of the [Cambridge 9709 syllabus](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-9709/).

If you've already covered [differentiation](/cambridge/9709/pure-1/differentiation/), you have a head start. Integration is differentiation in reverse — and understanding that connection is half the battle.

---

## What A Level Maths Integration Covers in 9709 Pure 1

A level maths integration is the reverse of differentiation. If differentiating a function gives you the gradient, integrating brings you back to the original function. In exam terms, it answers two types of questions: "find the expression" and "find the area."

### What's in scope for Paper 1

The Cambridge 9709 integration syllabus for Pure 1 covers these integration techniques a level students need to master:

- **1.8.1** — Integration as the reverse of differentiation
- **1.8.2** — Integration of \( (ax + b)^n \) for any rational \( n \) (except \( n = -1 \))
- **1.8.3** — Evaluating definite integrals
- **1.8.4** — Finding the area of a region bounded by a curve and lines
- **1.8.5** — Finding volumes of revolution about the x-axis (in some Paper 1 variants)

What's **not** in Pure 1: integration by parts, integration by substitution (the formal method), partial fractions, or trigonometric integrals. Those are Pure 3. For the trigonometry foundations, see our [Pure 1 trigonometry guide](/cambridge/9709/pure-1/trigonometry/).

### How many marks is it worth?

Integration questions typically carry **15–20 marks out of 75** on Paper 1. That's 20–27% of the paper from one topic. When you add in questions that combine integration with differentiation or coordinate geometry, calculus as a whole accounts for **35–40% of Paper 1 marks**.

<!-- calloutBlock: variant="key-formula" -->
<!-- title: Mark breakdown -->
<!-- body: Paper 1 = 75 marks total. Integration alone = 15–20 marks (20–27%). Integration + differentiation combined = 25–30 marks (35–40%). This is the single biggest topic cluster on the paper. -->

---

## Core Integration Skills You Need for Paper 1

### Basic integration: powers of x

The fundamental rule reverses the power rule for differentiation.

<!-- mathBlock: displayMode=true -->
<!-- latex: \int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1) -->
<!-- caption: The power rule for integration -->

Add one to the power, divide by the new power, and add the constant of integration.

<!-- workedSolution -->
<!-- question: Find \( \int (3x^2 + 4x - 5) \, dx \) -->
<!-- difficulty: easy -->
<!-- marks: 3 -->
<!-- steps:
  1. math: \int (3x^2 + 4x - 5) \, dx
     annotation: Integrate each term separately using the power rule.
  2. math: = \frac{3x^3}{3} + \frac{4x^2}{2} - 5x + C
     annotation: For each term, add 1 to the power and divide by the new power.
  3. math: = x^3 + 2x^2 - 5x + C
     annotation: Simplify the coefficients. Don't forget the +C — it's worth a mark.
-->

<!-- calloutBlock: variant="common-mistake" -->
<!-- body: Forgetting +C on indefinite integrals. Cambridge examiner reports flag this every single year. The constant of integration is worth one mark on its own — and losing it on multiple questions adds up fast. -->

Before integrating, convert roots and fractions into power notation. You cannot integrate \( \sqrt{x} \) directly — rewrite it as \( x^{1/2} \) first. The same applies to \( \frac{1}{x^2} \), which becomes \( x^{-2} \).

<!-- workedSolution -->
<!-- question: Find \( \int \frac{3}{\sqrt{x}} \, dx \) -->
<!-- difficulty: medium -->
<!-- marks: 3 -->
<!-- steps:
  1. math: \frac{3}{\sqrt{x}} = 3x^{-1/2}
     annotation: Rewrite the fraction as a power. This is the step most students skip — and then get stuck.
  2. math: \int 3x^{-1/2} \, dx = \frac{3x^{1/2}}{1/2} + C
     annotation: Apply the power rule: add 1 to -1/2 to get 1/2, then divide by 1/2.
  3. math: = 6x^{1/2} + C = 6\sqrt{x} + C
     annotation: Dividing by 1/2 is the same as multiplying by 2. Convert back to surd form if the question expects it.
-->

### Integrating (ax + b)^n — the reverse chain rule

When the expression inside the brackets is linear (of the form \( ax + b \)), you can integrate directly by adjusting for the coefficient of \( x \).

<!-- mathBlock: displayMode=true -->
<!-- latex: \int (ax + b)^n \, dx = \frac{(ax + b)^{n+1}}{a(n+1)} + C \quad (n \neq -1) -->
<!-- caption: The reverse chain rule for linear expressions -->

The key is the extra division by \( a \) — the coefficient of \( x \) inside the brackets. This compensates for what the chain rule would produce if you differentiated the result.

<!-- workedSolution -->
<!-- question: Find \( \int (2x + 3)^4 \, dx \) -->
<!-- difficulty: medium -->
<!-- marks: 3 -->
<!-- steps:
  1. math: \int (2x + 3)^4 \, dx
     annotation: The expression inside the brackets is linear (2x + 3), so we can use the reverse chain rule.
  2. math: = \frac{(2x + 3)^5}{2 \times 5} + C
     annotation: Add 1 to the power (4 → 5). Divide by the new power (5) AND by the coefficient of x inside the brackets (2).
  3. math: = \frac{(2x + 3)^5}{10} + C
     annotation: Simplify. You can check this by differentiating — the chain rule gives 5 × 2 × (2x + 3)^4 / 10 = (2x + 3)^4. Correct.
-->

<!-- calloutBlock: variant="common-mistake" -->
<!-- body: This method ONLY works when the expression inside the brackets is linear (ax + b). If you see \( (x^2 + 1)^3 \), you cannot use the reverse chain rule directly — you would need to expand or use a Pure 3 technique. In Pure 1, every integration question involving brackets will use a linear expression. -->

### Definite integrals in a level maths

A definite integral has limits — an upper value and a lower value. You evaluate the integrated expression at both limits and subtract.

<!-- mathBlock: displayMode=true -->
<!-- latex: \int_a^b f(x) \, dx = \Big[ F(x) \Big]_a^b = F(b) - F(a) -->
<!-- caption: Evaluating a definite integral -->

No +C needed for definite integrals. The constant cancels when you subtract.

<!-- workedSolution -->
<!-- question: Evaluate \( \int_1^3 (2x + 1)^3 \, dx \) -->
<!-- difficulty: medium -->
<!-- marks: 4 -->
<!-- steps:
  1. math: \int (2x + 1)^3 \, dx = \frac{(2x + 1)^4}{2 \times 4} = \frac{(2x + 1)^4}{8}
     annotation: Integrate using the reverse chain rule. No +C needed since this is a definite integral.
  2. math: \Big[ \frac{(2x + 1)^4}{8} \Big]_1^3 = \frac{(7)^4}{8} - \frac{(3)^4}{8}
     annotation: Substitute the upper limit (x = 3, so 2(3) + 1 = 7) and the lower limit (x = 1, so 2(1) + 1 = 3).
  3. math: = \frac{2401}{8} - \frac{81}{8} = \frac{2320}{8} = 290
     annotation: Calculate each term and subtract. Show this working — the method marks require it.
-->

### Finding areas under curves

Finding the area under curve a level questions ask about is where integration becomes visual. The area between a curve \( y = f(x) \), the x-axis, and two vertical lines \( x = a \) and \( x = b \) is given by the definite integral.

<!-- calloutBlock: variant="remember" -->
<!-- body: When a curve dips below the x-axis, the integral gives a negative value for that region. You must split the integral at the x-intercept and take the absolute value of each part. If you don't, the negative and positive areas partially cancel — giving you the wrong answer. This catches out a huge number of students every year. -->

**How to handle areas below the x-axis:**

1. Find where the curve crosses the x-axis (set \( y = 0 \), solve for \( x \))
2. Split the integral at each crossing point
3. Integrate each part separately
4. Take the absolute value of any negative results
5. Add the absolute values together

<!-- [IMAGE: Shaded area diagram showing a curve crossing the x-axis, with areas above and below shaded in different colours. Label: "Area above = positive integral. Area below = take |negative integral|. Total area = sum of both."] -->

### Area between a curve and a line

This is the most common integration question format in 9709 Paper 1. The area between a curve \( y = f(x) \) and a line \( y = g(x) \) is:

<!-- mathBlock: displayMode=true -->
<!-- latex: \text{Area} = \int_a^b \big[ f(x) - g(x) \big] \, dx -->
<!-- caption: Always subtract the lower function from the upper function -->

The setup matters more than the integration itself. Here's the method:

1. **Sketch** the curve and the line (even a rough sketch helps)
2. **Find the intersection points** — solve \( f(x) = g(x) \) to get the limits
3. **Identify which is on top** — between the limits, which function has the higher y-value?
4. **Subtract** the lower from the upper and integrate

<!-- workedSolution -->
<!-- question: The curve \( y = 6x - x^2 \) and the line \( y = 2x \) intersect at O(0, 0) and P. Find the area enclosed between the curve and the line. -->
<!-- difficulty: hard -->
<!-- marks: 6 -->
<!-- steps:
  1. math: 6x - x^2 = 2x \implies 4x - x^2 = 0 \implies x(4 - x) = 0 \implies x = 0 \text{ or } x = 4
     annotation: Find the intersection points by setting the curve equal to the line. So P is at x = 4.
  2. math: \text{Between } x = 0 \text{ and } x = 4\text{: curve} - \text{line} = (6x - x^2) - 2x = 4x - x^2
     annotation: The curve is above the line in this interval (check: at x = 2, curve = 8, line = 4). Subtract line from curve.
  3. math: \int_0^4 (4x - x^2) \, dx = \Big[ 2x^2 - \frac{x^3}{3} \Big]_0^4
     annotation: Integrate each term using the power rule.
  4. math: = \Big( 2(16) - \frac{64}{3} \Big) - \Big( 0 - 0 \Big) = 32 - \frac{64}{3} = \frac{96 - 64}{3} = \frac{32}{3}
     annotation: Substitute limits and simplify. Leave the answer as a fraction — don't convert to a decimal unless asked.
-->
<!-- examinerNote: Candidates who sketch the curve and line before integrating rarely make setup errors. Those who jump straight to algebra often subtract in the wrong order or use incorrect limits. A quick sketch takes 30 seconds and prevents the most common mistakes on this question type. -->

---

## Which Integration Method Should You Use?

This is the question students ask most about a level maths integration: "How do I know which method to use?" For 9709 Pure 1, the decision is simpler than you think — there are only three paths.

<!-- [IMAGE: Integration method decision flowchart (Excalidraw SVG). The flowchart should have three branches:
  START: "What does the integrand look like?"
  Branch 1: "Individual terms like x^n, x^{-2}, x^{1/2}" → "Use the power rule: add 1 to power, divide by new power"
  Branch 2: "(ax + b)^n where ax + b is linear" → "Use the reverse chain rule: divide by a(n+1)"
  Branch 3: "A combination or word problem" → "Simplify first, then apply Branch 1 or 2"
  Bottom note: "Always check: differentiate your answer to verify"
] -->

<!-- comparisonTable -->
<!-- caption: Integration techniques for 9709 Pure 1 -->
<!-- headers: ["Expression Type", "Method", "Example", "Key Step"] -->
<!-- rows:
  ["Individual powers of x", "Power rule", "\\( \\int 3x^2 \\, dx \\)", "Add 1 to power, divide by new power"],
  ["\\( (ax + b)^n \\)", "Reverse chain rule", "\\( \\int (2x+1)^3 \\, dx \\)", "Also divide by coefficient of x"],
  ["Roots or fractions", "Rewrite as powers, then power rule", "\\( \\int \\frac{1}{\\sqrt{x}} \\, dx \\)", "Convert to \\( x^{-1/2} \\) first"],
  ["Area questions", "Set up definite integral", "Area between curve and line", "Find limits from intersections", true]
-->

<!-- calloutBlock: variant="exam-tip" -->
<!-- body: If you're stuck, try this: differentiate each answer option mentally. The one that gives back your original expression is correct. This works because integration and differentiation are reverse operations. It takes 30 seconds and catches most errors. -->

---

## 5 Integration Mistakes That Lose Marks Every Year

These come directly from [Cambridge 9709 examiner reports](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-9709/) (2022–2025). They're not edge cases — examiners flag these in nearly every session.

### 1. Forgetting +C on indefinite integrals

The constant of integration is worth one mark. On a 4-mark question, that's 25% of the marks gone for six characters. Every indefinite integral needs +C. No exceptions.

<!-- calloutBlock: variant="examiner-says" -->
<!-- body: "A significant number of candidates omitted the constant of integration. This was particularly evident in questions requiring the general solution." — Cambridge 9709 Examiner Report, 2024 -->

### 2. Sign errors when integrating negative powers

When you rewrite \( \frac{3}{x^2} \) as \( 3x^{-2} \), the integration gives \( \frac{3x^{-1}}{-1} = -3x^{-1} = -\frac{3}{x} \). The negative sign trips students up because it appears as part of the rule, not from the original expression.

**Fix:** Always write out the power notation step separately. Don't try to jump from the fraction to the answer in one step.

### 3. Not splitting integrals when the area crosses the x-axis

If the question asks for the total area and the curve goes below the x-axis in part of the interval, you must split the integral. A single integral from \( a \) to \( b \) will give you the net area (positive minus negative), not the total area.

**Fix:** Before integrating an area question, check whether the curve crosses the x-axis in the given interval. Set \( y = 0 \) and solve.

### 4. Using the reverse chain rule on non-linear expressions

The reverse chain rule only works when the expression inside the brackets is linear (\( ax + b \)). Students sometimes apply it to expressions like \( (x^2 + 1)^3 \) — this is wrong and will cost all the method marks.

**Fix:** Before using the reverse chain rule, check that the bracket contains only a linear expression. If it doesn't, expand or use a different approach.

### 5. Not showing working on definite integrals

Using a calculator to evaluate a definite integral and writing only the final number loses all the method marks. Examiners need to see the integration step, the substitution of limits, and the subtraction.

<!-- calloutBlock: variant="examiner-says" -->
<!-- body: "Candidates who showed only the final answer for definite integrals, without displaying the integrated expression and the evaluation at limits, could not be awarded method marks." — Cambridge 9709 Examiner Report, 2023 -->

**Fix:** Always write: integrate → show the expression in square brackets with limits → substitute upper limit → substitute lower limit → subtract → simplify.

---

## How to Check Your Integration Answer in 30 Seconds

This is the single most powerful exam technique for integration, and almost nobody uses it consistently.

**Differentiate your answer.** If you get back to the original expression, your integration is correct. If you don't, you've found your mistake before the examiner does.

<!-- workedSolution -->
<!-- question: You integrated \( (2x + 3)^4 \) and got \( \frac{(2x + 3)^5}{10} + C \). Check this is correct. -->
<!-- difficulty: easy -->
<!-- marks: 0 -->
<!-- steps:
  1. math: \frac{d}{dx} \Big[ \frac{(2x + 3)^5}{10} + C \Big] = \frac{5(2x + 3)^4 \times 2}{10}
     annotation: Differentiate using the chain rule. The 5 comes down from the power, and the 2 comes from differentiating the bracket.
  2. math: = \frac{10(2x + 3)^4}{10} = (2x + 3)^4
     annotation: This matches the original integrand. The integration is correct.
-->

This check works for every integration in Pure 1. It takes 30 seconds. Build the habit now and you'll catch errors before they cost marks.

---

## How to Revise A Level Maths Integration for 9709

### The 3-stage approach

**Stage 1 — Learn the rules (Days 1–3).** Focus on the power rule and the reverse chain rule. Don't touch area questions yet. You need the mechanical skills to be automatic before you apply them.

**Stage 2 — Practice with structure (Days 4–10).** Work through sub-topics in this order:
1. Basic indefinite integrals (\( \int x^n \, dx \))
2. Reverse chain rule (\( \int (ax + b)^n \, dx \))
3. Definite integrals (evaluating with limits)
4. Area under a curve
5. Area between a curve and a line

Do five to eight questions per sub-topic before moving on. If you're getting more than one in four wrong, stay on that sub-topic.

**Stage 3 — Exam simulation (Days 11+).** Practice full integration questions under timed conditions. Use the [9709 Past Papers by Topic](/cambridge/9709/past-papers/) collection to find integration questions from real papers. Mark your work using the official mark scheme — this teaches you what examiners actually look for.

### How ExamPilot helps

ExamPilot's adaptive practice identifies exactly which integration sub-skills you need to work on. Instead of grinding through random questions, you practice the ones that target your specific gaps — with Ask Sparky available to guide you when you're stuck.

[Join the ExamPilot waitlist](https://www.exampilot.io/waitlist) for early access.

---

## Practice Questions — 9709 Exam Style

Test yourself with these exam-style integration questions. The worked solutions use the same step-by-step format the examiner expects.

<!-- workedSolution -->
<!-- question: Find \( \int (x^3 - 4x + 1) \, dx \) -->
<!-- difficulty: easy -->
<!-- marks: 3 -->
<!-- steps:
  1. math: \int (x^3 - 4x + 1) \, dx = \frac{x^4}{4} - \frac{4x^2}{2} + x + C
     annotation: Integrate each term using the power rule. Remember: x is the same as x^1, so integrating gives x^2/2, and constants become the constant times x.
  2. math: = \frac{x^4}{4} - 2x^2 + x + C
     annotation: Simplify the coefficients. The +C is essential.
-->

<!-- workedSolution -->
<!-- question: Evaluate \( \int_0^2 (3x^2 - 2x) \, dx \) -->
<!-- difficulty: easy -->
<!-- marks: 4 -->
<!-- steps:
  1. math: \int (3x^2 - 2x) \, dx = x^3 - x^2
     annotation: Integrate each term. No +C needed for a definite integral.
  2. math: \Big[ x^3 - x^2 \Big]_0^2 = (8 - 4) - (0 - 0) = 4
     annotation: Substitute x = 2 (upper limit) and x = 0 (lower limit), then subtract.
-->

<!-- workedSolution -->
<!-- question: Find \( \int \frac{4}{(3x - 1)^2} \, dx \) -->
<!-- difficulty: medium -->
<!-- marks: 3 -->
<!-- steps:
  1. math: \frac{4}{(3x - 1)^2} = 4(3x - 1)^{-2}
     annotation: Rewrite the fraction as a negative power. This is the crucial first step.
  2. math: \int 4(3x - 1)^{-2} \, dx = \frac{4(3x - 1)^{-1}}{3 \times (-1)} + C
     annotation: Apply the reverse chain rule. Add 1 to the power (-2 → -1). Divide by the new power (-1) and the coefficient of x inside the brackets (3).
  3. math: = -\frac{4}{3(3x - 1)} + C
     annotation: Simplify. Rewrite in fraction form if the question expects it.
-->

<!-- workedSolution -->
<!-- question: The curve \( y = x^2 - 4x + 3 \) crosses the x-axis at A and B. Find the area enclosed between the curve and the x-axis. -->
<!-- difficulty: hard -->
<!-- marks: 6 -->
<!-- steps:
  1. math: x^2 - 4x + 3 = 0 \implies (x - 1)(x - 3) = 0 \implies x = 1, \, x = 3
     annotation: Find where the curve crosses the x-axis by setting y = 0. These are your limits.
  2. math: \text{Between } x = 1 \text{ and } x = 3, \text{ the curve is below the x-axis}
     annotation: Check the sign. At x = 2, y = 4 - 8 + 3 = -1 < 0. The curve dips below the x-axis, so the integral will be negative.
  3. math: \int_1^3 (x^2 - 4x + 3) \, dx = \Big[ \frac{x^3}{3} - 2x^2 + 3x \Big]_1^3
     annotation: Integrate each term using the power rule.
  4. math: = \Big( 9 - 18 + 9 \Big) - \Big( \frac{1}{3} - 2 + 3 \Big) = 0 - \frac{4}{3} = -\frac{4}{3}
     annotation: Substitute limits and subtract. The result is negative because the curve is below the x-axis.
  5. math: \text{Area} = \Big| -\frac{4}{3} \Big| = \frac{4}{3}
     annotation: Take the absolute value. The area is always positive.
-->
<!-- examinerNote: This question tests whether you know to take the absolute value. The integral gives -4/3, but the area is 4/3. Candidates who write -4/3 as their final answer lose the last mark. -->

Want more practice? [Join the ExamPilot waitlist](https://www.exampilot.io/waitlist) for adaptive integration questions calibrated to your level.

---

## What to Do Next

A level maths integration is a marks goldmine on 9709 Paper 1 — if you avoid the common traps. You now have the rules, the decision framework, the examiner insights, and the practice questions. The next step is consistent, targeted practice.

Start with the sub-topic you find hardest. If the reverse chain rule trips you up, do 10 questions on it before moving on. If area questions confuse you, practise the setup — sketching and finding intersection points — before worrying about the integration itself.

> *Looking for past paper practice? See our [9709 Past Papers by Topic](/cambridge/9709/past-papers/) collection.*

> *Ready to tackle the other half of calculus? Read our [9709 Differentiation Guide](/cambridge/9709/pure-1/differentiation/) next.*
