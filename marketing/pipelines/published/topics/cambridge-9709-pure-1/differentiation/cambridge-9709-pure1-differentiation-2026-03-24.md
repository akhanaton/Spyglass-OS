<!--
ARTICLE METADATA
=================
Title: A Level Maths Differentiation: Cambridge 9709 Pure 1 Guide
Slug: cambridge-9709-pure-1-differentiation
URL: /cambridge/9709/pure-1/differentiation/
Author: Teresa Gonzalez
Categories: Cambridge 9709
Tags: differentiation, pure 1, 9709, a level maths, cambridge, revision, chain rule, stationary points
Status: draft
Published At: 2026-03-24

SEO:
 Meta Title: A Level Maths Differentiation: 9709 Pure 1 Guide | ExamPilot (60 chars)
 Meta Description: Master A level maths differentiation for Cambridge 9709 Pure 1. Chain rule, stationary points, rates of change, and common exam mistakes with fixes. (158 chars)

FAQs (for Sanity FAQ field + FAQPage schema):
 1. Q: Is differentiation harder than integration?
 A: Most students find differentiation easier to learn because the rules are more mechanical, bring the power down, subtract one. The difficulty in differentiation comes from applied questions: optimisation word problems, connected rates of change, and "show that" proofs. Integration requires more pattern recognition. If you find the pure mechanics easy but struggle with word problems, that's normal, and it's fixable with structured practice.

 2. Q: Do I need the product rule or quotient rule for 9709 Pure 1?
 A: No. The product rule and quotient rule are Pure 3 topics. For Pure 1, you only need the power rule and the chain rule. If a question looks like it needs the product rule, it's probably asking you to expand the expression first and then differentiate term by term. Every differentiation question in Paper 1 can be solved with the power rule, the chain rule, or first principles.

 3. Q: How many marks is differentiation worth in Paper 1?
 A: Differentiation questions directly carry 15–20 marks out of 75 on Paper 1, roughly 20–27% of the paper. But differentiation also appears indirectly in coordinate geometry questions (finding tangent and normal equations) and optimisation problems that combine algebra with calculus. When you include these, differentiation's true mark contribution is closer to 30–35% of Paper 1.

 4. Q: What's the difference between dy/dx and f'(x)?
 A: They mean the same thing, the derivative. dy/dx is Leibniz notation and looks like a fraction (it behaves like one in chain rule problems). f'(x) is function notation and is often cleaner for simple derivatives. Cambridge 9709 uses both, so you need to be comfortable with either. The key point: dy/dx is not actually a fraction, but in connected rates of change problems, you can manipulate it as if it were one.

 5. Q: Can I skip first principles and just learn the power rule?
 A: You can for most questions, but Cambridge examiners test first principles directly, usually as a "show that" question worth 3–4 marks. It appears at least once every few exam sessions. The method itself is straightforward if you practise it three or four times. Skipping it is a gamble that risks free marks.

Structured Data:
 - FAQPage schema (from FAQs above)
 - Article schema (author, datePublished, dateModified)
 - BreadcrumbList: Home > Cambridge 9709 > Pure 1 > Differentiation

Internal Links:
 - /cambridge/9709/pure-1/ (pillar, placeholder)
 - /cambridge/9709/pure-1/integration/ (spoke, published)
 - /cambridge/9709/past-papers/ (pillar, placeholder)
 - https://www. exampilot. io/waitlist (CTA)
 - /blog/category/cambridge-9709 (category)

External Links:
 - https://www. cambridgeinternational. org (official syllabus)
 - Cambridge 9709 examiner reports (cited in common mistakes section)

Sanity Custom Blocks Used:
 - mathBlock (LaTeX equations)
 - calloutBlock (Exam Tip, Common Mistake, Examiner Says, Remember, Key Formula)
 - workedSolution (step-by-step solutions with annotations)
 - comparisonTable (differentiation rules comparison)
 - FAQ section (from post. faqs field)

Visual Assets Needed:
 1. Differentiation rule decision flowchart (Excalidraw → SVG + Mermaid comparison)
 2. Annotated chain rule worked solution (Excalidraw → SVG only)
 3. Stationary point classification diagram (Excalidraw → SVG + Mermaid comparison)
 4. Connected rates of change variable chain (Excalidraw → SVG + Mermaid comparison)
 5. Before/after exam answer comparison (Excalidraw → SVG only)
-->

> *This guide is part of our [Complete Cambridge 9709 Pure 1 Revision Guide](/cambridge/9709/pure-1/), your comprehensive resource for exam preparation.*

# A Level Maths Differentiation: Cambridge 9709 Pure 1 Guide

A level maths differentiation is the topic that keeps showing up where you don't expect it. You see it labelled as a calculus question, but it's also hiding inside coordinate geometry problems, optimisation word problems, and rates of change questions that don't mention the word "differentiate" at all. Miss the fundamentals and it costs you marks across half the paper.

The rules themselves are straightforward. The power rule takes 30 seconds to learn. The chain rule takes five minutes. First principles takes a bit longer, but the method is fixed. The real difficulty in Cambridge 9709 differentiation isn't the mechanics, it's knowing how to apply them when the question doesn't look like a textbook exercise.

This guide covers everything you need for A-Level maths differentiation in Cambridge 9709 Pure 1. It maps directly to Topics 1.7.1–1.7.3 of the [Cambridge 9709 syllabus](https://www. cambridgeinternational. org), and every worked example uses the format the examiner expects.

If you've already covered [integration](/cambridge/9709/pure-1/integration/), you'll recognise some patterns in reverse. If you haven't, start here, differentiation comes first in the syllabus for a reason.

---

## What Differentiation Means in 9709 Pure 1

Differentiation finds the gradient of a curve at any point. A straight line has a constant gradient. A curve doesn't, the steepness changes as you move along it. Differentiation gives you a formula for that changing gradient.

In practical terms: you feed a function in, and you get the gradient function out. Substitute any x-value into the gradient function and you know exactly how steep the curve is at that point.

### What's in scope for Paper 1

The Cambridge 9709 differentiation syllabus for Pure 1 covers:

- **1.7.1**, The idea of a derived function; differentiation of power functions and simple polynomials
- **1.7.2**, The chain rule for differentiating composite functions of the form \( (ax + b)^n \)
- **1.7.3**, Applications: gradients, tangents and normals, stationary points, increasing and decreasing functions, connected rates of change, practical maxima and minima

What's **not** in Pure 1: the product rule, the quotient rule, differentiating trigonometric or exponential functions, or implicit differentiation. Those are Pure 3. For the [trigonometry foundations](/cambridge/9709/pure-1/trigonometry/) you'll need when trig appears in calculus, see our Pure 1 trig guide.

### How many marks is it worth?

Differentiation questions directly carry **15–20 marks out of 75** on Paper 1. But the true figure is higher. Coordinate geometry questions often require you to differentiate to find tangent gradients. Optimisation problems need differentiation to find maximum or minimum values. When you account for these, differentiation contributes **30–35% of Paper 1 marks**.

<!-- calloutBlock: variant="key-formula" -->
<!-- title: Mark breakdown -->
<!-- body: Paper 1 = 75 marks total. Differentiation alone = 15–20 marks (20–27%). Differentiation + integration combined = 25–30 marks (35–40%). Add indirect appearances in coordinate geometry and optimisation, and calculus touches over 40% of the paper. -->

---

## The A Level Maths Differentiation Rules You Need for Paper 1

### Power rule, the foundation

Every differentiation question in Pure 1 starts here. Bring the power down as a multiplier, reduce the power by one.

<!-- mathBlock: displayMode=true -->
<!-- latex: \frac{d}{dx}\big( x^n \big) = nx^{n-1} -->
<!-- caption: The power rule for differentiation -->

This works for any power, positive, negative, or fractional. But you must have the expression in power form first.

<!-- workedSolution -->
<!-- question: Differentiate \( y = 3x^4 - 5x^2 + 7x - 2 \) -->
<!-- difficulty: easy -->
<!-- marks: 3 -->
<!-- steps:
 1. math: \frac{dy}{dx} = 3(4)x^3 - 5(2)x + 7(1) - 0
 annotation: Apply the power rule to each term. Bring the power down, reduce by one. Constants disappear.
 2. math: = 12x^3 - 10x + 7
 annotation: Simplify the coefficients. The constant term -2 differentiates to 0.
-->

Before differentiating, convert roots and fractions into power notation. You cannot differentiate \( \sqrt{x} \) directly, rewrite it as \( x^{1/2} \) first. The same applies to \( \frac{1}{x^3} \), which becomes \( x^{-3} \).

<!-- workedSolution -->
<!-- question: Differentiate \( y = 4\sqrt{x} + \frac{6}{x^2} \) -->
<!-- difficulty: medium -->
<!-- marks: 4 -->
<!-- steps:
 1. math: y = 4x^{1/2} + 6x^{-2}
 annotation: Rewrite in power form. This is the step that most students skip, and then get stuck.
 2. math: \frac{dy}{dx} = 4 \cdot \frac{1}{2} x^{-1/2} + 6(-2)x^{-3}
 annotation: Apply the power rule to each term. Bring the power down, reduce by one.
 3. math: = 2x^{-1/2} - 12x^{-3} = \frac{2}{\sqrt{x}} - \frac{12}{x^3}
 annotation: Simplify and convert back to fraction form if the question expects it.
-->

<!-- calloutBlock: variant="common-mistake" -->
<!-- body: Sign errors with negative powers are flagged in the Cambridge 9709 examiner report every single year. The mistake: when differentiating \( x^{-2} \), students write \( -2x^{-1} \) instead of \( -2x^{-3} \). Always write the power notation step separately. Don't skip it. -->

### Chain rule in a level maths — the one that trips people up

The chain rule handles composite functions, expressions where one function sits inside another. In Pure 1, you'll only see the form \( (ax + b)^n \), but the principle matters.

<!-- mathBlock: displayMode=true -->
<!-- latex: \frac{d}{dx}\big[ (ax + b)^n \big] = n \cdot a \cdot (ax + b)^{n-1} -->
<!-- caption: The chain rule for linear composite functions in Pure 1 -->

The key: bring the power down as usual, then multiply by the derivative of what's inside the brackets. For \( (ax + b) \), the derivative of the inside is just \( a \).

<!-- workedSolution -->
<!-- question: Differentiate \( y = (3x + 2)^5 \) -->
<!-- difficulty: medium -->
<!-- marks: 2 -->
<!-- steps:
 1. math: \frac{dy}{dx} = 5(3x + 2)^4 \times 3
 annotation: Bring the power down (5). Reduce the power by one (5 → 4). Multiply by the derivative of the bracket contents (d/dx of 3x + 2 = 3).
 2. math: = 15(3x + 2)^4
 annotation: Simplify. Always write the chain rule multiplier explicitly before simplifying, it shows the examiner you know the method.
-->

The hardest part isn't the rule itself, it's knowing when to use it. If the expression has something other than plain \( x \) raised to a power, you need the chain rule.

<!-- workedSolution -->
<!-- question: Differentiate \( y = \frac{1}{(2x - 1)^3} \) -->
<!-- difficulty: medium -->
<!-- marks: 3 -->
<!-- steps:
 1. math: y = (2x - 1)^{-3}
 annotation: Rewrite the fraction as a negative power. This converts it into chain rule form.
 2. math: \frac{dy}{dx} = -3(2x - 1)^{-4} \times 2
 annotation: Power rule gives -3 and reduces the power to -4. Chain rule multiplier is 2 (derivative of 2x - 1).
 3. math: = -6(2x - 1)^{-4} = \frac{-6}{(2x - 1)^4}
 annotation: Simplify. Convert back to fraction form for the final answer.
-->

<!-- calloutBlock: variant="exam-tip" -->
<!-- body: For 9709 Pure 1, you only need two differentiation rules: the power rule and the chain rule. If a question looks like it needs the product rule, it's asking you to expand the expression first and then differentiate term by term. If you can't expand it, it's a Pure 3 question and won't appear on Paper 1. -->

### Differentiation from first principles at a level

First principles is the formal definition of the derivative. You'll need it for "show that" questions, which appear at least once every few exam sessions.

<!-- mathBlock: displayMode=true -->
<!-- latex: f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} -->
<!-- caption: The definition of the derivative from first principles -->

The method is mechanical once you practise it a few times:

1. Write out \( f(x + h) \) by substituting \( x + h \) everywhere you see \( x \)
2. Compute \( f(x + h) - f(x) \)
3. Divide by \( h \)
4. Cancel \( h \) from every term
5. Let \( h \to 0 \)

<!-- workedSolution -->
<!-- question: Use differentiation from first principles to show that the derivative of \( f(x) = x^3 \) is \( 3x^2 \). -->
<!-- difficulty: medium -->
<!-- marks: 4 -->
<!-- steps:
 1. math: f(x + h) = (x + h)^3 = x^3 + 3x^2h + 3xh^2 + h^3
 annotation: Expand (x + h)^3 using the binomial expansion. Show every term, examiners need to see this.
 2. math: f(x + h) - f(x) = 3x^2h + 3xh^2 + h^3
 annotation: Subtract f(x) = x^3. The x^3 terms cancel.
 3. math: \frac{f(x + h) - f(x)}{h} = \frac{3x^2h + 3xh^2 + h^3}{h} = 3x^2 + 3xh + h^2
 annotation: Divide every term by h. This is why we can cancel, every term in the numerator has an h factor.
 4. math: \lim_{h \to 0} (3x^2 + 3xh + h^2) = 3x^2
 annotation: Let h approach 0. The terms with h vanish. This gives the derivative.
-->

<!-- calloutBlock: variant="remember" -->
<!-- body: First principles proves why the power rule works, it's not just a formula you memorise, it's a mathematical result you can derive. Cambridge examiners test it to check that you understand what a derivative actually is, not just that you can apply the shortcut. Practise it three or four times and the 3–4 marks are essentially free. -->

---

## Applying Differentiation in 9709 Exams

This is where students who know the rules still lose marks. The mechanics are straightforward. The application is where it gets hard.

### Tangent and normal questions in a level maths

To find the gradient of a curve at a specific point, differentiate and substitute the x-value.

The **tangent** at a point is the straight line that touches the curve at that point and has the same gradient. The **normal** is perpendicular to the tangent.

<!-- mathBlock: displayMode=true -->
<!-- latex: \text{Gradient of tangent} = \frac{dy}{dx}\bigg|_{x=a} \qquad \text{Gradient of normal} = -\frac{1}{dy/dx}\bigg|_{x=a} -->
<!-- caption: The normal gradient is the negative reciprocal of the tangent gradient -->

<!-- workedSolution -->
<!-- question: The curve \( y = x^3 - 4x + 1 \) passes through the point P where \( x = 2 \). Find the equation of the tangent and the normal at P. -->
<!-- difficulty: medium -->
<!-- marks: 6 -->
<!-- steps:
 1. math: \frac{dy}{dx} = 3x^2 - 4
 annotation: Differentiate using the power rule.
 2. math: \text{At } x = 2: \frac{dy}{dx} = 3(4) - 4 = 8
 annotation: The gradient of the tangent at P is 8.
 3. math: y = 8 - 8 + 1 = 1, \text{ so P is } (2, 1)
 annotation: Find the y-coordinate by substituting x = 2 into the original equation. Don't skip this, it's a common source of lost marks.
 4. math: \text{Tangent: } y - 1 = 8(x - 2) \implies y = 8x - 15
 annotation: Use y - y_1 = m(x - x_1) with the gradient and the point.
 5. math: \text{Normal: } y - 1 = -\frac{1}{8}(x - 2) \implies y = -\frac{1}{8}x + \frac{5}{4}
 annotation: The normal has gradient -1/8 (negative reciprocal of 8). Same point, different gradient.
-->

<!-- calloutBlock: variant="common-mistake" -->
<!-- body: Two errors cost marks on tangent/normal questions every year. First: forgetting to find the y-coordinate. Students find the gradient, then try to write the equation without knowing the point. Second: mixing up the tangent and normal gradients. The tangent uses the gradient directly. The normal uses the negative reciprocal. If the tangent gradient is 8, the normal gradient is -1/8, not 1/8 and not -8. -->

### Stationary points in a level maths

Stationary points occur where the gradient is zero, the curve is momentarily flat.

1. Set \( \frac{dy}{dx} = 0 \) and solve for \( x \)
2. Find the y-coordinate by substituting back into the original equation
3. Classify the point using the second derivative

<!-- mathBlock: displayMode=true -->
<!-- latex: \frac{d^2y}{dx^2} > 0 \implies \text{minimum} \qquad \frac{d^2y}{dx^2} < 0 \implies \text{maximum} -->
<!-- caption: The second derivative test for classifying stationary points -->

<!-- [IMAGE: Stationary point classification diagram (Excalidraw SVG + Mermaid comparison). Decision tree showing: find dy/dx = 0 → find d²y/dx² at that point → if positive = minimum (curve bends upward) → if negative = maximum (curve bends downward) → if zero = use first derivative test (check sign change).] -->

<!-- workedSolution -->
<!-- question: Find the stationary points of \( y = 2x^3 - 9x^2 + 12x - 4 \) and classify each one. -->
<!-- difficulty: hard -->
<!-- marks: 7 -->
<!-- steps:
 1. math: \frac{dy}{dx} = 6x^2 - 18x + 12 = 6(x^2 - 3x + 2) = 6(x-1)(x-2)
 annotation: Differentiate, then factorise to find where dy/dx = 0.
 2. math: \frac{dy}{dx} = 0 \implies x = 1 \text{ or } x = 2
 annotation: The stationary points occur at x = 1 and x = 2.
 3. math: \text{At } x = 1: y = 2 - 9 + 12 - 4 = 1 \implies (1, 1)
 annotation: Substitute x = 1 into the original equation to find the y-coordinate.
 4. math: \text{At } x = 2: y = 16 - 36 + 24 - 4 = 0 \implies (2, 0)
 annotation: Substitute x = 2 into the original equation.
 5. math: \frac{d^2y}{dx^2} = 12x - 18
 annotation: Differentiate again for the second derivative.
 6. math: \text{At } x = 1: \frac{d^2y}{dx^2} = 12 - 18 = -6 < 0 \implies \text{maximum at } (1, 1)
 annotation: Negative second derivative means the curve bends downward here. This is a maximum.
 7. math: \text{At } x = 2: \frac{d^2y}{dx^2} = 24 - 18 = 6 > 0 \implies \text{minimum at } (2, 0)
 annotation: Positive second derivative means the curve bends upward here. This is a minimum.
-->

<!-- calloutBlock: variant="exam-tip" -->
<!-- body: What if the second derivative equals zero at a stationary point? You can't conclude anything; it could be a maximum, minimum, or point of inflection. Fall back to the first derivative test: check the sign of dy/dx just before and just after the stationary point. If it goes positive → negative, it's a maximum. Negative → positive is a minimum. Same sign on both sides means it's a point of inflection. -->

### Increasing and decreasing functions

A function is **increasing** where \( f'(x) > 0 \) and **decreasing** where \( f'(x) < 0 \). These questions are really asking you to solve an inequality.

1. Differentiate
2. Set up the inequality \( f'(x) > 0 \) (or \( < 0 \))
3. Solve to find the range of x-values

This connects directly to graph sketching. If you know where a function increases and decreases, you know its shape.

### Connected rates of change in a level maths

This is the hardest sub-topic in Pure 1 differentiation. Most students struggle with it, and the examiner reports confirm it.

The idea: if two quantities both change with time, you can connect their rates of change using the chain rule.

<!-- mathBlock: displayMode=true -->
<!-- latex: \frac{dy}{dt} = \frac{dy}{dx} \times \frac{dx}{dt} -->
<!-- caption: The chain rule for connected rates of change -->

<!-- [IMAGE: Connected rates of change variable chain (Excalidraw SVG + Mermaid comparison). Diagram showing: a chain of variables, e. g., Volume → Radius → Time, with dy/dt = dy/dx × dx/dt written below. Show how each "link" in the chain connects through the chain rule.] -->

The difficulty isn't the formula, it's identifying which variables connect to which, and finding the connecting derivative.

<!-- workedSolution -->
<!-- question: A spherical balloon is inflated so that its radius increases at a rate of 0.5 cm/s. Find the rate of increase of the surface area when the radius is 6 cm. [Surface area of a sphere: \( A = 4\pi r^2 \)] -->
<!-- difficulty: hard -->
<!-- marks: 5 -->
<!-- steps:
 1. math: \frac{dA}{dr} = 8\pi r
 annotation: Differentiate the surface area formula with respect to r. This is the connecting derivative.
 2. math: \frac{dr}{dt} = 0.5
 annotation: Given in the question, the radius increases at 0.5 cm/s.
 3. math: \frac{dA}{dt} = \frac{dA}{dr} \times \frac{dr}{dt} = 8\pi r \times 0.5 = 4\pi r
 annotation: Apply the chain rule to connect the rates.
 4. math: \text{When } r = 6: \frac{dA}{dt} = 4\pi(6) = 24\pi \text{ cm}^2\text{/s}
 annotation: Substitute the given radius. Leave the answer in terms of pi unless told otherwise.
-->

<!-- calloutBlock: variant="examiner-says" -->
<!-- body: "Many candidates could not identify the chain of variables needed for connected rates of change problems. A common error was attempting to differentiate the area formula with respect to time directly, without using the chain rule to connect through the radius.", Cambridge 9709 Examiner Report, 2023 -->

### Optimisation, maximum and minimum word problems

Optimisation questions are differentiation questions in disguise. The challenge isn't the calculus, it's translating the word problem into an expression you can differentiate.

**The method:**
1. **Read**, identify what you're maximising or minimising
2. **Express**, write it as a function of one variable (use constraints to eliminate others)
3. **Differentiate**, find the derivative
4. **Solve**, set the derivative to zero
5. **Verify**, use the second derivative to confirm it's a max or min
6. **Answer**, substitute back to find the actual value

<!-- workedSolution -->
<!-- question: A farmer has 40 m of fencing to enclose a rectangular pen against an existing wall. The wall forms one side of the rectangle. Find the dimensions that give the maximum area. -->
<!-- difficulty: hard -->
<!-- marks: 7 -->
<!-- steps:
 1. math: \text{Let width} = x \text{ m. Then length} = 40 - 2x \text{ m (fencing covers 2 widths + 1 length)}
 annotation: Set up variables. The wall replaces one length, so the fencing covers two widths and one length: 2x + L = 40, giving L = 40 - 2x.
 2. math: A = x(40 - 2x) = 40x - 2x^2
 annotation: Area = width × length. Now it's a function of x only.
 3. math: \frac{dA}{dx} = 40 - 4x
 annotation: Differentiate the area with respect to x.
 4. math: \frac{dA}{dx} = 0 \implies 40 - 4x = 0 \implies x = 10
 annotation: Set the derivative to zero and solve. The width is 10 m.
 5. math: \frac{d^2A}{dx^2} = -4 < 0 \implies \text{maximum}
 annotation: The second derivative is negative, confirming this is a maximum, not a minimum.
 6. math: L = 40 - 2(10) = 20 \text{ m. Area} = 10 \times 20 = 200 \text{ m}^2
 annotation: Substitute back to find the length and the maximum area. Always state both dimensions and the area in your answer.
-->

<!-- calloutBlock: variant="exam-tip" -->
<!-- body: In optimisation questions, the hardest step is step 2, expressing the quantity as a function of one variable. The question will always give you a constraint (like "40 m of fencing") that lets you eliminate the second variable. If your expression still has two unknowns, re-read the question, you've missed the constraint. -->

---

## Which Differentiation Rule Do I Use?

Students ask this constantly: "How do I know whether to use the power rule or the chain rule?" For Pure 1, the decision tree is simple.

<!-- [IMAGE: Differentiation rule decision flowchart (Excalidraw SVG + Mermaid comparison). The flowchart should have three branches:
 START: "What does the expression look like?"
 Branch 1: "Individual terms like x^n, constants, or sums of terms" → "Power rule: bring the power down, subtract one"
 Branch 2: "(ax + b)^n, something raised to a power, where the base isn't just x" → "Chain rule: power rule THEN multiply by derivative of the inside"
 Branch 3: "It looks complicated or has products/fractions" → "Rewrite first: expand, simplify, or convert to power form, then use Branch 1"
 Special case: "Show that f'(x) =..." → "First principles"
] -->

<!-- comparisonTable -->
<!-- caption: Differentiation rules for 9709 Pure 1 -->
<!-- headers: ["Expression Type", "Rule", "Example", "Key Step"] -->
<!-- rows:
 ["\\( x^n \\), constants, sums of terms", "Power rule", "\\( 3x^4 - 2x + 7 \\)", "Bring power down, subtract one from power"],
 ["\\( (ax + b)^n \\)", "Chain rule", "\\( (2x + 3)^5 \\)", "Power rule on outside, multiply by derivative of inside"],
 ["Roots, fractions, reciprocals", "Rewrite then power rule", "\\( \\frac{4}{\\sqrt{x}} \\)", "Convert to power form (\\( 4x^{-1/2} \\)) first"],
 ["\"Show that the derivative is...\"", "First principles", "\\( f(x) = x^2 + 3x \\)", "Use limit definition with h → 0"],
 ["Products like \\( x^2(x+1)^3 \\)", "Expand first, then power rule", "\\( x^5 + 3x^4 + 3x^3 + x^2 \\)", "No product rule needed in Pure 1", true]
-->

---

## 5 A Level Maths Differentiation Mistakes That Cost Marks Every Year

These come directly from Cambridge 9709 examiner reports (2022–2025). These are the errors examiners flag every single session.

### 1. Not converting to power notation before differentiating

You cannot differentiate \( \sqrt{x} \) or \( \frac{1}{x^2} \) directly. Students who try end up writing nonsense. Convert first: \( \sqrt{x} = x^{1/2} \), then \( \frac{1}{x^2} = x^{-2} \). Then differentiate.

**Fix:** Make conversion to power form the first line of every differentiation involving roots or fractions. Write it out even if you think you can do it mentally.

### 2. Sign errors with negative and fractional powers

Differentiating \( 6x^{-2} \) gives \( -12x^{-3} \), not \( -12x^{-1} \). The power goes from \( -2 \) to \( -3 \) (subtract one), not from \( -2 \) to \( -1 \). This trips students up because subtracting one from a negative number feels counterintuitive.

<!-- calloutBlock: variant="examiner-says" -->
<!-- body: "Errors in differentiating negative and fractional powers of x continue to be a significant source of lost marks. Candidates frequently make sign errors or fail to reduce the power correctly when dealing with terms such as \( x^{-2} \) or \( x^{1/2} \).", Cambridge 9709 Examiner Report, 2024 -->

**Fix:** Write out the full working: "power is -2, new power is -2 - 1 = -3." Don't skip the subtraction step.

### 3. Forgetting the chain rule multiplier

When differentiating \( (3x + 1)^4 \), students write \( 4(3x + 1)^3 \) and stop. The answer is \( 12(3x + 1)^3 \), you must multiply by 3, the derivative of the bracket contents. The missing multiplier costs the accuracy mark.

**Fix:** Always ask yourself after differentiating a bracket expression: "Did I multiply by the derivative of what's inside?"

### 4. Not showing sufficient working in "show that" questions

"Show that" means the answer is given. You earn marks for the method, not the result. Writing two lines and stating the answer loses marks. The examiner needs to see each algebraic step.

**Fix:** For first principles, show the expansion, the subtraction, the division by h, and the limit separately. For any "show that," write more steps than you think necessary.

### 5. Mixing up tangent and normal gradients

The tangent gradient comes straight from dy/dx. The normal gradient is the negative reciprocal: \( -\frac{1}{m} \). Students either forget the negative sign (writing \( \frac{1}{m} \)) or invert without negating.

<!-- calloutBlock: variant="remember" -->
<!-- body: Tangent: use the gradient directly. Normal: flip and negate. If the tangent gradient is 3, the normal gradient is -1/3. If the tangent gradient is -2/5, the normal gradient is 5/2. Test yourself: what's the normal gradient if the tangent gradient is -1? Answer: 1. -->

---

## How Differentiation Connects to Integration

Differentiation and integration are reverse operations. If you differentiate \( x^3 \), you get \( 3x^2 \). If you integrate \( 3x^2 \), you get \( x^3 + C \).

This gives you a powerful checking tool. Finished an integration question? Differentiate your answer. If you get back to the original expression, your integration is correct. Finished a differentiation question? Integrate your answer. If you get back to the original function (up to a constant), your differentiation is correct.

This connection also explains why the chain rule in differentiation creates the "reverse chain rule" in integration. If differentiating \( (2x + 3)^5 \) gives \( 10(2x + 3)^4 \), then integrating \( (2x + 3)^4 \) must give \( \frac{(2x + 3)^5}{10} + C \).

For the full picture, see our [9709 Integration Guide](/cambridge/9709/pure-1/integration/).

---

## How to Revise A Level Maths Differentiation for 9709

### The 3-stage approach

**Stage 1, Master the rules (Days 1–3).** Focus on the power rule and the chain rule. Practise 10 questions each. Include negative and fractional powers from the start, don't wait until they surprise you in an exam. Do one or two first principles questions.

**Stage 2, Apply to exam contexts (Days 4–10).** Work through sub-topics in this order:

1. Gradients at a point
2. Tangent and normal equations
3. Stationary points and classification
4. Increasing and decreasing functions
5. Connected rates of change
6. Optimisation word problems

Do five to eight questions per sub-topic before moving on. If you're getting more than one in four wrong, stay on that sub-topic.

**Stage 3, Exam simulation (Days 11+).** Practice full differentiation questions under timed conditions. Use the [9709 Past Papers by Topic](/cambridge/9709/past-papers/) collection to find differentiation questions from real papers. Mark your work using the official mark scheme, this teaches you what examiners reward and what they don't.

### How ExamPilot targets your differentiation gaps

ExamPilot's adaptive practice identifies exactly which differentiation sub-skills you need to work on. Instead of grinding through random questions, you practise the ones that target your specific gaps, whether that's the chain rule, connected rates of change, or setting up optimisation problems. Ask Sparky is available to guide you when you're stuck, without giving the answer away.

[Join the ExamPilot waitlist](https://www. exampilot. io/waitlist) for early access.

---

## Practice Questions, 9709 Exam Style

Test yourself with these exam-style differentiation questions. The worked solutions use the step-by-step format the examiner expects.

<!-- workedSolution -->
<!-- question: Differentiate \( y = 5x^3 - \frac{2}{x} + 4 \) -->
<!-- difficulty: easy -->
<!-- marks: 3 -->
<!-- steps:
 1. math: y = 5x^3 - 2x^{-1} + 4
 annotation: Rewrite 2/x as 2x^{-1} before differentiating.
 2. math: \frac{dy}{dx} = 15x^2 + 2x^{-2} = 15x^2 + \frac{2}{x^2}
 annotation: Apply the power rule to each term. Note: -2 × -1 = +2 (positive). Convert back to fraction form.
-->

<!-- workedSolution -->
<!-- question: Find the gradient of the curve \( y = (4x - 3)^3 \) at the point where \( x = 1 \). -->
<!-- difficulty: easy -->
<!-- marks: 3 -->
<!-- steps:
 1. math: \frac{dy}{dx} = 3(4x - 3)^2 \times 4 = 12(4x - 3)^2
 annotation: Differentiate using the chain rule. Power comes down (3), power reduces (3 → 2), multiply by derivative of inside (4).
 2. math: \text{At } x = 1: \frac{dy}{dx} = 12(4 - 3)^2 = 12(1)^2 = 12
 annotation: Substitute x = 1 into the derivative. The gradient at x = 1 is 12.
-->

<!-- workedSolution -->
<!-- question: Find the coordinates of the stationary point on the curve \( y = x^2 - 6x + 13 \) and determine its nature. -->
<!-- difficulty: medium -->
<!-- marks: 5 -->
<!-- steps:
 1. math: \frac{dy}{dx} = 2x - 6
 annotation: Differentiate.
 2. math: 2x - 6 = 0 \implies x = 3
 annotation: Set the derivative equal to zero and solve.
 3. math: y = 9 - 18 + 13 = 4 \implies (3, 4)
 annotation: Substitute x = 3 into the original equation to find the y-coordinate.
 4. math: \frac{d^2y}{dx^2} = 2 > 0 \implies \text{minimum at } (3, 4)
 annotation: The second derivative is positive, so the curve bends upward at this point, it's a minimum.
-->

<!-- workedSolution -->
<!-- question: The volume of a cube is increasing at a rate of 24 cm^3/s. Find the rate of increase of the side length when the side length is 4 cm. -->
<!-- difficulty: hard -->
<!-- marks: 5 -->
<!-- steps:
 1. math: V = x^3 \implies \frac{dV}{dx} = 3x^2
 annotation: Write the volume formula and differentiate with respect to the side length x.
 2. math: \frac{dV}{dt} = \frac{dV}{dx} \times \frac{dx}{dt} \implies 24 = 3x^2 \times \frac{dx}{dt}
 annotation: Apply the chain rule for connected rates. We know dV/dt = 24.
 3. math: \text{When } x = 4: 24 = 3(16) \times \frac{dx}{dt} \implies \frac{dx}{dt} = \frac{24}{48} = 0.5 \text{ cm/s}
 annotation: Substitute x = 4 and solve for dx/dt.
-->

Want more practice? [Join the ExamPilot waitlist](https://www. exampilot. io/waitlist) for adaptive differentiation questions calibrated to your level.

---

## What to Do Next

A level maths differentiation isn't just one topic on 9709 Paper 1, it's the foundation for almost half the marks. The rules are quick to learn. The application takes practice. And the exam traps are predictable if you know what to look for.

Start with the sub-topic you find hardest. If the chain rule confuses you, do 10 questions until the method is automatic. If optimisation word problems trip you up, practise the setup, translating words into algebra, before worrying about the calculus. If connected rates of change feels impossible, break it down: identify the chain of variables first, then find each derivative separately.

ExamPilot's adaptive practice identifies your weakest differentiation sub-skills and targets them with questions matched to your level. No more random past paper grinding. [Join the waitlist](https://www. exampilot. io/waitlist) for early access.

> *Looking for past paper practice? See our [9709 Past Papers by Topic](/cambridge/9709/past-papers/) collection.*

> *Differentiation and integration are reverse processes. Once you've mastered this guide, see our [9709 Integration Guide](/cambridge/9709/pure-1/integration/) to complete the picture.*
