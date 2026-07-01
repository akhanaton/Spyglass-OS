---
Meta Title: Binomial Expansion A Level: 9709 Series Guide | ExamPilot
Meta Description: Master binomial expansion a level, arithmetic and geometric progressions, and sum to infinity. Cambridge 9709 worked examples, common mistakes and exam tips.
Primary Keyword: binomial expansion a level
Secondary Keywords: geometric series a level maths, arithmetic progression a level, sum to infinity a level, binomial expansion a level maths, cambridge 9709 series, 9709 binomial expansion, convergence condition geometric series
URL Slug: /cambridge/9709/pure-1/series/
Internal Links: /cambridge/9709/pure-1/, /cambridge/9709/pure-1/quadratics/, /cambridge/9709/pure-1/trigonometry/, /cambridge/9709/pure-1/integration/, /cambridge/9709/past-papers/, https://www.exampilot.io/waitlist
External Links: Cambridge 9709 syllabus (cambridgeinternational.org), Cambridge examiner reports (cambridgeinternational.org)
Word Count: ~2,400
Content Type: topicPage
---

# Binomial Expansion A Level: AP, GP & Series for Cambridge 9709 Pure 1

> *This guide is part of our [Complete Cambridge 9709 Pure 1 Revision Guide](/cambridge/9709/pure-1/), your comprehensive resource for exam preparation.*

Binomial expansion a level questions in Cambridge 9709 follow a precise pattern -- get one coefficient wrong and every term after it collapses. Arithmetic and geometric progression questions ask you to build equations from conditions -- and students who can't set up the simultaneous equations lose the entire question.

This guide covers everything in Topics 1.6.1 to 1.6.5 of the [Cambridge 9709 Pure Mathematics 1 syllabus](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-9709/). 9709 binomial expansion is a mechanical skill. Arithmetic progression a level questions and geometric series a level maths problems are problem-solving skills. You need both, and they appear on Paper 1 every single session.

Series typically accounts for 7-10 marks out of 75 on Paper 1 (9-13% of your grade). None of the AP or GP formulae appear on the formula sheet. You must memorise them all.

## What Series Covers in 9709 Pure 1

Here is the exact syllabus scope:

- Binomial expansion of $(a + b)^n$ for positive integer $n$ only
- Binomial coefficients using Pascal's triangle and the $\binom{n}{r}$ notation
- Arithmetic progressions (AP): $n$th term and sum of $n$ terms
- Geometric progressions (GP): $n$th term, sum of $n$ terms, and sum to infinity
- The convergence condition $|r| < 1$ for sum to infinity

What's **not** in Pure 1: binomial expansion with fractional or negative $n$, partial fractions, and the infinite series expansion of $(1 + x)^n$ when $n$ isn't a positive integer. That's all Pure 3 content. Don't revise it for Paper 1.

Series connects to other Pure 1 topics. You may need to combine AP/GP skills with [quadratics](/cambridge/9709/pure-1/quadratics/) when setting up equations, or use series results alongside [integration](/cambridge/9709/pure-1/integration/) in multi-part questions.

## Binomial Expansion A Level: Positive Integer n

### Pascal's Triangle Method

Pascal's triangle gives you the coefficients for expanding $(a + b)^n$. Each row starts and ends with 1, and every interior entry is the sum of the two entries directly above it.

| Row | Coefficients | Expansion of |
|-----|-------------|--------------|
| 0 | 1 | $(a+b)^0$ |
| 1 | 1, 1 | $(a+b)^1$ |
| 2 | 1, 2, 1 | $(a+b)^2$ |
| 3 | 1, 3, 3, 1 | $(a+b)^3$ |
| 4 | 1, 4, 6, 4, 1 | $(a+b)^4$ |
| 5 | 1, 5, 10, 10, 5, 1 | $(a+b)^5$ |

For small values of $n$ (up to about 6), Pascal's triangle is the fastest route to a full expansion. Read the coefficients from the relevant row, then attach decreasing powers of $a$ and increasing powers of $b$.

### The General Term Formula

When a question says "find the coefficient of $x^3$" or "find the 4th term," you don't need the full expansion. Use the general term:

$$T_{r+1} = \binom{n}{r} a^{n-r} b^r$$

where $\binom{n}{r} = \frac{n!}{r!(n-r)!}$.

**Worked example:** Find the coefficient of $x^2$ in the expansion of $(2 + 3x)^5$.

Here $a = 2$, $b = 3x$, and $n = 5$. The $x^2$ term occurs when $r = 2$:

$$T_3 = \binom{5}{2} \times 2^{5-2} \times (3x)^2$$

$$= 10 \times 8 \times 9x^2$$

$$= 720x^2$$

The coefficient of $x^2$ is **720**.

Notice that you must raise both the 2 and the $3x$ to the appropriate powers. The most common binomial expansion a level error is writing $\binom{n}{r} \times (3x)^r$ and forgetting the $2^{n-r}$ entirely. That mistake loses every mark.

### Sign Tracking in $(a - b)^n$

> **Common mistake:** When expanding $(a - b)^n$, the signs alternate. Students who lose track of this lose marks on nearly every term. Treat $b$ as $(-b)$ and raise $(-b)$ to the $r$th power. Even powers give positive terms; odd powers give negative terms.

**Worked example:** Expand $(1 - 2x)^4$.

Here $a = 1$, $b = -2x$, $n = 4$. Using Pascal's row 4 (1, 4, 6, 4, 1):

$$= 1 \times 1^4 \times (-2x)^0 + 4 \times 1^3 \times (-2x)^1 + 6 \times 1^2 \times (-2x)^2 + 4 \times 1^1 \times (-2x)^3 + 1 \times 1^0 \times (-2x)^4$$

$$= 1 - 8x + 24x^2 - 32x^3 + 16x^4$$

The alternating pattern $+, -, +, -, +$ comes from the powers of $(-2x)$. Write $(-2x)^r$ with the brackets every time and the signs take care of themselves.

Priya was consistently getting the right magnitude but wrong sign on her binomial expansion answers. Her tutor spotted the issue in thirty seconds: she was writing $-2x^r$ instead of $(-2x)^r$, losing the alternating sign pattern entirely. Once she committed to always writing the brackets, her sign errors disappeared.

### Finding the Term Independent of x

"Find the term independent of $x$" means find the term where the power of $x$ is zero. These questions typically involve expressions like $(x + \frac{1}{x})^n$ or $(x^2 + \frac{1}{x})^n$.

**Worked example:** Find the term independent of $x$ in $(x + \frac{1}{x})^6$.

The general term is:

$$T_{r+1} = \binom{6}{r} x^{6-r} \left(\frac{1}{x}\right)^r = \binom{6}{r} x^{6-r} \times x^{-r} = \binom{6}{r} x^{6-2r}$$

For the term independent of $x$, set the power of $x$ to zero:

$$6 - 2r = 0 \implies r = 3$$

$$T_4 = \binom{6}{3} = 20$$

The term independent of $x$ is **20**.

The method is always the same: write the general term, express everything as powers of $x$, set the total power to zero, solve for $r$.

ExamPilot's [Smart Review](https://www.exampilot.io/waitlist) targets binomial expansion questions at the intervals where you are most likely to make coefficient errors, building accuracy before exam day.

## Arithmetic Progressions (AP)

### nth Term and Sum Formulae

An arithmetic progression has a constant common difference $d$ between consecutive terms. The two formulae you need:

| Formula | Expression | Use when |
|---------|-----------|----------|
| $n$th term | $u_n = a + (n-1)d$ | Finding a specific term |
| Sum of $n$ terms | $S_n = \frac{n}{2}(2a + (n-1)d)$ | Finding the total of the first $n$ terms |
| Sum (alternative) | $S_n = \frac{n}{2}(a + l)$ | When you know the last term $l$ |

Here $a$ is the first term, $d$ is the common difference, and $n$ is the number of terms.

### Setting Up Equations from Conditions

The harder arithmetic progression a level questions give you two conditions and ask you to find $a$ and $d$. The method is straightforward: translate each condition into an equation, then solve simultaneously.

**Worked example:** The 5th term of an AP is 17 and the 12th term is 45. Find the first term and common difference.

Condition 1: $u_5 = a + 4d = 17$

Condition 2: $u_{12} = a + 11d = 45$

Subtract equation 1 from equation 2:

$$7d = 28 \implies d = 4$$

Substitute back: $a + 16 = 17 \implies a = 1$.

The AP is $1, 5, 9, 13, 17, \ldots$ with $a = 1$ and $d = 4$.

Every AP word problem in 9709 reduces to this pattern. Identify two conditions about the sequence, write two equations in $a$ and $d$, solve simultaneously. The algebra is typically straightforward -- the challenge is translating the words into equations.

Omar kept losing full marks on AP word problems even though his algebra was solid. The problem was that he'd jump straight to calculations without writing the two equations first -- he'd try to hold the conditions in his head and mix up which values went where. After he started writing $u_5 = a + 4d = \ldots$ and $S_8 = \frac{8}{2}(2a + 7d) = \ldots$ as his first step every time, his accuracy on these questions went from roughly 40% to near-perfect.

## Geometric Series A Level Maths: GP and Sum to Infinity

### nth Term and Sum Formulae

A geometric progression has a constant common ratio $r$ between consecutive terms. The three formulae:

| Formula | Expression | Use when |
|---------|-----------|----------|
| $n$th term | $u_n = ar^{n-1}$ | Finding a specific term |
| Sum of $n$ terms | $S_n = \frac{a(1 - r^n)}{1 - r}$, $r \neq 1$ | Finite sum |
| Sum to infinity | $S_\infty = \frac{a}{1 - r}$ | Infinite sum, only when $|r| < 1$ |

Here $a$ is the first term and $r$ is the common ratio.

> **The convergence condition:** The sum to infinity $S_\infty = \frac{a}{1-r}$ is only valid when $|r| < 1$. If $|r| \geq 1$, the series diverges and there's no finite sum. Cambridge examiners explicitly note that students who use the formula without stating $|r| < 1$ lose a mark every time. Write the condition before you write the formula.

### Why the Convergence Condition for Geometric Series Matters

When $|r| < 1$, each successive term gets smaller. The partial sums $S_1, S_2, S_3, \ldots$ approach a fixed value. That fixed value is $\frac{a}{1-r}$.

When $|r| \geq 1$, the terms don't shrink. The partial sums grow without bound (or oscillate), and no finite sum exists.

**Mini-scenario:** A ball is dropped from 10 metres. Each bounce reaches 60% of the previous height. What is the total distance the ball travels?

The heights form a GP with $a = 10$ and $r = 0.6$. Since $|0.6| < 1$, the sum to infinity exists:

$$S_\infty = \frac{10}{1 - 0.6} = \frac{10}{0.4} = 25$$

The total downward distance is 25 metres. (The total distance including upward bounces is $10 + 2 \times \frac{6}{1-0.6} = 10 + 30 = 40$ metres.)

### Setting Up Equations from Conditions

Just as with APs, the harder geometric series a level maths questions give you two conditions about a GP and ask you to find $a$ and $r$.

**Worked example:** The 3rd term of a GP is 12 and the 6th term is 96. Find the first term and common ratio.

Condition 1: $u_3 = ar^2 = 12$

Condition 2: $u_6 = ar^5 = 96$

Divide equation 2 by equation 1:

$$\frac{ar^5}{ar^2} = \frac{96}{12}$$

$$r^3 = 8 \implies r = 2$$

Substitute back: $a \times 4 = 12 \implies a = 3$.

The GP is $3, 6, 12, 24, 48, 96, \ldots$ with $a = 3$ and $r = 2$.

Notice the technique: dividing one GP equation by another eliminates $a$ and gives you an equation in $r$ alone. This is cleaner than substitution and works for every GP simultaneous equation problem.

**Mini-scenario:** A savings plan pays out amounts that form a GP. The first payment is $500 and the total of all payments (sum to infinity) is $2000. Find the common ratio.

$$S_\infty = \frac{a}{1-r} = 2000, \quad a = 500$$

$$\frac{500}{1-r} = 2000 \implies 1-r = 0.25 \implies r = 0.75$$

Check: $|0.75| < 1$, so the sum to infinity is valid.

## AP vs GP: How to Tell Which You Have

If a question doesn't explicitly say "arithmetic" or "geometric," check the relationship between terms:

| Feature | Arithmetic Progression (AP) | Geometric Progression (GP) |
|---------|----------------------------|---------------------------|
| Relationship | Constant **difference** $d$ | Constant **ratio** $r$ |
| Test | $u_2 - u_1 = u_3 - u_2$ | $\frac{u_2}{u_1} = \frac{u_3}{u_2}$ |
| $n$th term | $u_n = a + (n-1)d$ | $u_n = ar^{n-1}$ |
| Sum of $n$ terms | $S_n = \frac{n}{2}(2a + (n-1)d)$ | $S_n = \frac{a(1 - r^n)}{1 - r}$ |
| Sum to infinity | Does not exist (unless $d = 0$) | $S_\infty = \frac{a}{1-r}$, $|r| < 1$ |
| Key operation | Addition | Multiplication |

When reading a sum to infinity a level question, your first step is always to confirm you are dealing with a GP and that $|r| < 1$.

## 5 Binomial Expansion and Series Mistakes That Cost Marks in 9709

These come from [Cambridge 9709 examiner reports](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-9709/) and appear every session.

**Mistake 1: Forgetting to raise BOTH parts in binomial expansion.** In $(2 + 3x)^5$, each term has the form $\binom{5}{r} \times 2^{5-r} \times (3x)^r$. Dropping the $2^{5-r}$ gives the wrong coefficient on every term.

**Mistake 2: Not stating the convergence condition.** Before writing $S_\infty = \frac{a}{1-r}$, you must state that $|r| < 1$ (or show that it holds for the given $r$). Examiners dock a mark for this omission even when the final answer is correct.

**Mistake 3: Confusing AP and GP formulae.** Six formulae across two progression types. Under exam pressure, students substitute the common difference $d$ into a GP formula or the common ratio $r$ into an AP formula. The comparison table above exists to prevent this.

**Mistake 4: Sign errors in $(a - b)^n$.** Always write $(-b)^r$ with brackets. The brackets force you to track the sign correctly. Without them, students write $-b^r$ for every term, losing the alternating pattern entirely.

**Mistake 5: Not translating word problems into equations.** When a question says "the 3rd term is 12," your first action is to write $ar^2 = 12$ (GP) or $a + 2d = 12$ (AP). Students who try to solve in their heads without writing the equations make algebraic errors.

## FAQs -- Binomial Expansion A Level Maths & Cambridge 9709 Series

**Do I need Pascal's triangle or the general term formula?**

Both. Pascal's triangle is fastest for a full expansion of $(a + b)^n$ with small $n$. The general term formula $\binom{n}{r}a^{n-r}b^r$ is what you need when the question asks for a specific term or coefficient.

**Is binomial expansion in Pure 1 different from Pure 3?**

Yes. Pure 1 covers binomial expansion for positive integer $n$ only -- finite expansions with a set number of terms. Pure 3 extends to fractional and negative $n$, which gives infinite series and requires the convergence condition $|x| < 1$.

**How many marks is series worth in Paper 1?**

Typically 7-10 marks out of 75 (9-13%). Binomial expansion appears every session. AP and GP questions appear in most sessions but not always both.

**What is the hardest part of series?**

Setting up simultaneous equations from word problems. The algebra itself is straightforward once you have the equations. Translating "the sum of the first 8 terms is 120 and the 3rd term is 9" into two equations in $a$ and $d$ is the skill that separates strong answers from weak ones.

**Do I need to memorise AP and GP formulae?**

Yes. None of the sequence and series formulae are provided on the Cambridge 9709 formula sheet. You must know $u_n$, $S_n$ for both AP and GP, and $S_\infty$ for GP, by heart.

## Summary

Cambridge 9709 series splits into two skills. Binomial expansion a level questions reward mechanical precision -- track your coefficients, handle negative signs carefully, and set up the general term correctly for "find the coefficient" and "term independent of $x$" problems. Arithmetic progression a level and geometric series questions reward equation-building -- translate the conditions into simultaneous equations, solve for $a$ and $d$ (or $a$ and $r$), and remember the convergence condition for any sum to infinity a level question.

The five examiner report mistakes covered in this guide account for the majority of lost marks in 9709 series questions. Fix those five habits, and series becomes one of the most reliable scoring topics on Paper 1.

[Join the ExamPilot waitlist](https://www.exampilot.io/waitlist) for adaptive series practice that targets your specific gaps -- not random questions from a generic pool.

> *Looking for past paper practice? See our [9709 Past Papers by Topic](/cambridge/9709/past-papers/) collection.*
