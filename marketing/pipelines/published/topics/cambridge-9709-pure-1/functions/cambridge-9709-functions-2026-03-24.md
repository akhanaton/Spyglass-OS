---
Meta Title: "A Level Maths Functions: Cambridge 9709 Pure 1 Guide | ExamPilot" (64 chars)
Meta Description: "A level maths functions guide for Cambridge 9709 Pure 1. Domain, range, inverse functions, composites, graph transformations, and examiner report mistakes." (156 chars)
Primary Keyword: a level maths functions
Secondary Keywords: cambridge 9709 functions, inverse functions a level maths, composite functions a level maths, domain and range a level maths, graph transformations a level maths
URL Slug: /cambridge/9709/pure-1/functions/
Content Type: topicPage
Sanity Type: topicPage
Slug: functions
Parent Hub: pure-1
Internal Links:
 - /cambridge/9709/pure-1/ (Pure 1 hub)
 - /cambridge/9709/pure-1/integration/ (Integration spoke)
 - /cambridge/9709/pure-1/differentiation/ (Differentiation spoke - placeholder)
 - /cambridge/9709/pure-1/quadratics/ (Quadratics spoke - placeholder)
 - /cambridge/9709/pure-1/trigonometry/ (Trigonometry spoke - placeholder)
 - https://www. exampilot. io/waitlist (Waitlist CTA)
External Links:
 - https://www. cambridgeinternational. org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-9709/ (Cambridge 9709 syllabus)
 - Cambridge 9709 examiner reports (cited for specific observations)
Word Count: ~2,800
---

# A Level Maths Functions: Cambridge 9709 Pure 1 Complete Guide

> *This guide is part of our [Complete Cambridge 9709 Pure 1 Revision Guide](/cambridge/9709/pure-1/) -- your comprehensive resource for exam preparation.*

A level maths functions is the first real algebra topic in 9709 Pure 1, and it tests skills you'll use across the entire paper. Every time you differentiate, integrate, or transform a graph, you're working with functions. Get the foundations right here and the rest of the syllabus clicks into place.

This guide covers everything in Topic 1.2 of the [Cambridge 9709 syllabus](https://www. cambridgeinternational. org/programmes-and-qualifications/cambridge-international-as-and-a-level-mathematics-9709/) -- domain, range, composite functions, inverse functions, and graph transformations. Each section includes worked examples in the style of 9709 Paper 1, plus the common mistakes that Cambridge examiners flag every session.

**Ready to practise functions with questions calibrated to your level?** [Join the ExamPilot waitlist](https://www. exampilot. io/waitlist) for adaptive A-Level Maths practice.

---

## What A Level Maths Functions Means in 9709 Pure 1

A function is a rule that takes an input and produces exactly one output. You've been using functions since GCSE -- `y = 2x + 3` is a function -- but A-Level formalises the language. That language matters, because 9709 exam questions test whether you understand the terminology, not just whether you can do the algebra.

**Key terms you need:**

- **Function**: A rule that maps each input to exactly one output
- **Domain**: The set of allowed inputs (x-values the function accepts)
- **Range** (image set): The set of outputs the function actually produces (y-values)
- **One-one function**: Each output comes from exactly one input (passes the horizontal line test)
- **Many-one function**: Multiple inputs can produce the same output (e. g., f(x) = x^2 maps both 3 and -3 to 9)

### How Functions Appears in the Exam

Functions questions appear on every 9709 Paper 1, typically as Question 9 or 10 -- the longer, multi-part questions worth 8-12 marks. Graph transformations can also appear in trigonometry questions, which means functions knowledge is worth roughly 15-20% of your Paper 1 marks when you count both direct and indirect appearances.

**Common question formats:**
1. "Find the range of f" (complete the square, then state the range)
2. "Find f^{-1}(x) and state its domain"
3. "Find fg(x) and state its range"
4. "Explain why f does not have an inverse" (horizontal line test argument)
5. "Describe a sequence of transformations" (given before/after equations)
6. "Show that f is self-inverse" (prove ff(x) = x)

### What's NOT in Pure 1

The modulus function |f(x)| is Pure 3 only. Don't waste revision time on it for Paper 1. Exponential and logarithmic functions as a formal topic are also Pure 3, though basic exponentials may appear in context. Everything in this guide is strictly what the 2026-2027 syllabus requires for Pure Mathematics 1.

---

## Domain and Range in A Level Maths Functions

### Understanding Domain and Range

Domain and range confusion is the single biggest pain point for A level maths functions students. Here's the clearest way to think about it:

- **Domain** = what goes IN (the x-values the function accepts)
- **Range** = what comes OUT (the y-values the function actually produces)

For a linear function like f(x) = 2x + 1, the domain is all real numbers and the range is all real numbers. Straightforward.

Quadratic functions are where it gets interesting. Take f(x) = x^2 - 4x + 7 with domain x in R. To find the range, complete the square:

$$f(x) = (x - 2)^2 + 3$$

The minimum value is 3 (when x = 2), so the range is f(x) >= 3.

**The examiner report flags this repeatedly:** substituting a few x-values is not a valid method for finding the range. You need to complete the square (for quadratics) or sketch the graph (for other functions) to justify your answer.

### Function Notation

Two notations appear in 9709:
- **f(x) = 2x + 1** -- the most common form
- **f: x -> 2x + 1** -- mapping notation (read as "f maps x to 2x + 1")

Both mean the same thing. The exam uses both interchangeably, and you should be comfortable reading either. When writing your own answers, f(x) notation is simpler.

---

## Composite Functions in A Level Maths -- fg(x) Explained

A composite function is a "function of a function." You feed the output of one function into another.

$$fg(x) = f(g(x))$$

**The order rule that trips everyone up:** fg(x) means "do g first, then f." Read right to left.

Think of it like getting dressed: "socks then shoes" means you put socks on first, shoes second. fg(x) means you apply g first, f second. The function closest to x acts first.

[IMAGE: Composite function order diagram showing input -> g -> f -> output]

### fg(x) is NOT the Same as gf(x)

This is the most common procedural error Cambridge examiners flag in functions questions. Students read fg(x) left to right and apply f first. The examiner reports mention this mistake almost every session.

**Example**: f(x) = x^2, g(x) = x + 3

- fg(x) = f(g(x)) = f(x + 3) = (x + 3)^2
- gf(x) = g(f(x)) = g(x^2) = x^2 + 3

Completely different results.

### The Domain Condition for Composites

The composite fg(x) only exists when the range of g fits within the domain of f:

$$\text{Range of } g \subseteq \text{Domain of } f$$

This means it's possible for fg(x) to exist while gf(x) doesn't (or vice versa). If a question asks "state the domain of fg," you must check this condition.

**Example**: f(x) = sqrt(x) with domain x >= 0, and g(x) = 2x - 5 with domain x in R.

The range of g is all real numbers, which includes negative values. But f requires non-negative inputs. So fg(x) = sqrt(2x - 5) only exists for x >= 2.5.

Meanwhile, gf(x) = 2*sqrt(x) - 5 exists for all x >= 0, because the range of f (y >= 0) fits within the domain of g (all reals).

---

## Inverse Functions in A Level Maths -- Finding f^{-1}(x)

### What Is an Inverse Function?

An inverse function "undoes" what the original function does:

$$ff^{-1}(x) = f^{-1}f(x) = x$$

The domain of f^{-1} equals the range of f. The range of f^{-1} equals the domain of f. Everything swaps.

**An inverse only exists for one-one functions.** A many-one function like f(x) = x^2 (without a domain restriction) maps both x = 3 and x = -3 to y = 9. So if you tried to reverse it, the "inverse" would give two outputs for the input 9. That breaks the definition of a function.

[IMAGE: One-one vs many-one horizontal line test diagram]

The horizontal line test makes this visual: if any horizontal line crosses the graph more than once, the function is many-one and has no inverse (unless you restrict the domain).

**The examiner report reveals a critical misconception:** "A significant number of candidates thought that potentially square rooting a negative number was the issue, rather than the function not being one to one." Don't confuse "the function is undefined" with "the function is not one-one." They are different problems.

### How to Find the Inverse -- Step by Step

1. Write y = f(x)
2. Swap x and y
3. Rearrange to make y the subject
4. Replace y with f^{-1}(x)
5. **State the domain** (this is a free mark -- it equals the range of the original f)

**Example (linear):** f(x) = 3x - 7

1. y = 3x - 7
2. x = 3y - 7
3. y = (x + 7)/3
4. f^{-1}(x) = (x + 7)/3

**Example (quadratic with domain restriction):** f(x) = x^2 - 6x + 11, domain x >= 3

First, complete the square: f(x) = (x - 3)^2 + 2. The minimum is 2, so the range is f(x) >= 2.

1. y = (x - 3)^2 + 2
2. x = (y - 3)^2 + 2
3. x - 2 = (y - 3)^2
4. y - 3 = sqrt(x - 2) (positive root only, because original domain is x >= 3)
5. f^{-1}(x) = 3 + sqrt(x - 2), domain x >= 2

**Notice:** the domain of f^{-1} is x >= 2, which matches the range of the original f.

### Self-Inverse Functions

A self-inverse function is its own inverse: f(x) = f^{-1}(x), which means ff(x) = x.

**To prove a function is self-inverse**, compute ff(x) and show it simplifies to x.

**Example:** f(x) = (2x + 1)/(x - 2)

$$ff(x) = f\left(\frac{2x+1}{x-2}\right) = \frac{2 \cdot \frac{2x+1}{x-2} + 1}{\frac{2x+1}{x-2} - 2}$$

Multiply numerator and denominator by (x - 2):

$$= \frac{2(2x+1) + (x-2)}{(2x+1) - 2(x-2)} = \frac{4x + 2 + x - 2}{2x + 1 - 2x + 4} = \frac{5x}{5} = x$$

Since ff(x) = x, the function is self-inverse. This question type appears regularly in 9709 Paper 1.

### Sketching f(x) and f^{-1}(x) Together

The graph of f^{-1}(x) is the reflection of f(x) in the line y = x. When sketching both on the same axes:

1. Draw y = x as a dashed line first
2. Plot key points on f(x)
3. Reflect each point (a, b) to get (b, a) on f^{-1}(x)
4. Label both curves and the mirror line

[IMAGE: Inverse function reflection diagram with f(x) = x^2 and f^{-1}(x) = sqrt(x)]

Key detail: the graphs of f and f^{-1} always intersect on the line y = x. This means if a question asks you to solve f(x) = f^{-1}(x), you can solve f(x) = x instead.

---

## Graph Transformations -- A Level Maths Functions of y = f(x)

Graph transformations follow a set of rules. The challenge is that horizontal transformations do the opposite of what you'd expect.

### The Inside-Outside Rule

**Changes outside f() affect y and do what you expect:**
- y = f(x) + a -- translate up by a
- y = af(x) -- vertical stretch, scale factor a
- y = -f(x) -- reflection in the x-axis

**Changes inside f() affect x and are opposite:**
- y = f(x + a) -- translate LEFT by a (not right)
- y = f(ax) -- horizontal stretch, scale factor 1/a (not a)
- y = f(-x) -- reflection in the y-axis

### Why f(x + 3) Moves LEFT

This is the single most confusing point in graph transformations. Every student asks the same question: "Why does adding 3 move the graph left?"

[IMAGE: Horizontal shift explanation diagram]

Think about it this way: f(x + 3) asks "what does f see 3 units ahead?" At x = 2, f(x + 3) evaluates f(5). The output that used to happen at x = 5 now happens at x = 2. The whole curve arrives 3 units sooner -- so it shifts left.

Another way: to get the same output from f(x + 3) as you got from f(x), you need a smaller x-value. If f(5) = 10, then f(x + 3) = 10 when x = 2. The graph has moved left by 3.

### The Complete Transformation Table

| Transformation | Equation | Description | Direction |
|---|---|---|---|
| Vertical translation | y = f(x) + a | Translate up by a | As expected |
| Horizontal translation | y = f(x + a) | Translate LEFT by a | Opposite |
| Vertical stretch | y = af(x) | Stretch vertically, factor a | As expected |
| Horizontal stretch | y = f(ax) | Stretch horizontally, factor 1/a | Opposite |
| Reflection in x-axis | y = -f(x) | Flip upside down | -- |
| Reflection in y-axis | y = f(-x) | Flip left-to-right | -- |

### Combining Transformations

When a graph involves multiple transformations, deal with the inside of the brackets first (horizontal), then outside (vertical).

**Example:** Describe the transformations from y = f(x) to y = 3f(x - 2) + 1.

1. **Inside first:** (x - 2) means translate RIGHT by 2
2. **Outside next:** multiply by 3 means vertical stretch, scale factor 3
3. **Outside last:** + 1 means translate UP by 1

**Use correct vocabulary.** The 9709 syllabus explicitly requires the terms "translation," "reflection," and "stretch." Using "shift," "flip," or "squash" loses marks, even if your description is otherwise correct.

---

## Common A Level Maths Functions Mistakes That Cost Marks in 9709

These are drawn directly from Cambridge 9709 examiner reports. Each one costs students marks every session.

**Mistake 1: Getting fg(x) and gf(x) the wrong way round**
The fix: fg(x) = f(g(x)). The function closest to x acts first. Write it out as f(g(x)) every time until the order becomes automatic.

**Mistake 2: Confusing "no inverse" with "function is undefined"**
When asked "explain why f does not have an inverse," the answer is always about one-one, not about domain restrictions. A quadratic without domain restriction is many-one, so the inverse wouldn't be a function. Don't talk about square rooting negatives -- that's a different issue entirely.

**Mistake 3: Forgetting to state the domain of f^{-1}(x)**
The domain of f^{-1} equals the range of the original f. This is often worth a separate mark. If f has domain x >= 2 and range y >= 5, then f^{-1} has domain x >= 5. Always state it.

**Mistake 4: Graph transformation direction errors**
f(x + 3) shifts LEFT, not right. f(2x) is a horizontal stretch by factor 1/2, not 2. Use the inside-outside rule: changes inside f() affect x and are opposite to what you'd expect.

**Mistake 5: Using wrong transformation vocabulary**
Cambridge requires "translation," "reflection," and "stretch." Writing "the graph shifts up by 3" instead of "translation of 3 units in the positive y-direction" loses marks. Learn the correct terms and use them consistently.

---

## How to Revise Functions for 9709

### The 3-Stage Approach

**Stage 1: Master the concepts** (2-3 sessions)
Work through domain/range, notation, the inverse method, and the composite method. Use this guide as your reference. Don't move on until you can explain each concept without looking at notes.

**Stage 2: Apply to exam contexts** (3-4 sessions)
Do past paper functions questions by sub-topic. Start with inverse function questions (most straightforward), then composites, then transformations. Check your answers against mark schemes -- pay attention to where marks are awarded for stating domains and using correct vocabulary.

**Stage 3: Timed mixed practice** (ongoing)
Mix all sub-topics together under timed conditions. Functions questions in the actual exam combine concepts: you might need to find a composite, then find its inverse, then describe a transformation of the result. Practising mixed questions builds the fluency that scores full marks.

**Want adaptive practice that targets your specific functions gaps?** ExamPilot identifies exactly which sub-skills need work and serves questions at the right difficulty. [Join the waitlist](https://www. exampilot. io/waitlist) for A-Level Maths practice that actually adapts to you.

---

## Practice Questions (9709 Exam Style)

### Question 1 (Easy -- 4 marks)

The function f is defined by f(x) = 2x + 5 for x in R.

(a) Find f^{-1}(x). [2]
(b) Find ff(3). [2]

**Solution:**
(a) y = 2x + 5. Swap: x = 2y + 5. Rearrange: y = (x - 5)/2. So f^{-1}(x) = (x - 5)/2.
(b) f(3) = 2(3) + 5 = 11. ff(3) = f(11) = 2(11) + 5 = 27.

### Question 2 (Medium -- 5 marks)

The function f is defined by f(x) = x^2 - 2x + 5 for x >= 1.

(a) Find the range of f. [2]
(b) Find f^{-1}(x) and state its domain. [3]

**Solution:**
(a) Complete the square: f(x) = (x - 1)^2 + 4. Since x >= 1, the minimum is 4. Range: f(x) >= 4.
(b) y = (x - 1)^2 + 4. Swap: x = (y - 1)^2 + 4. Rearrange: (y - 1)^2 = x - 4, so y = 1 + sqrt(x - 4) (positive root, since original domain is x >= 1). f^{-1}(x) = 1 + sqrt(x - 4), domain x >= 4.

### Question 3 (Medium -- 6 marks)

Functions f and g are defined by f(x) = 3x - 1 and g(x) = x^2 + 2.

(a) Find fg(x) and simplify. [2]
(b) Find gf(x) and simplify. [2]
(c) Solve fg(x) = gf(x). [2]

**Solution:**
(a) fg(x) = f(x^2 + 2) = 3(x^2 + 2) - 1 = 3x^2 + 5
(b) gf(x) = g(3x - 1) = (3x - 1)^2 + 2 = 9x^2 - 6x + 1 + 2 = 9x^2 - 6x + 3
(c) 3x^2 + 5 = 9x^2 - 6x + 3, so 6x^2 - 6x - 2 = 0, giving 3x^2 - 3x - 1 = 0. By the quadratic formula: x = (3 +/- sqrt(9 + 12))/6 = (3 +/- sqrt(21))/6.

### Question 4 (Hard -- 8 marks)

The function f is defined by f(x) = (3x + 1)/(x - 3) for x!= 3.

(a) Show that f is self-inverse. [3]
(b) State the domain of f^{-1}. [1]
(c) Solve f(x) = x. [2]
(d) Hence state the coordinates where the graphs of y = f(x) and y = f^{-1}(x) intersect. [2]

**Solution:**
(a) ff(x) = f((3x+1)/(x-3)) = (3 * (3x+1)/(x-3) + 1) / ((3x+1)/(x-3) - 3). Multiply top and bottom by (x-3): numerator = 3(3x+1) + (x-3) = 9x+3+x-3 = 10x. Denominator = (3x+1) - 3(x-3) = 3x+1-3x+9 = 10. So ff(x) = 10x/10 = x. Since ff(x) = x, f is self-inverse.
(b) Since f is self-inverse, f^{-1} = f. Domain of f^{-1} is x!= 3 (same as f).
(c) (3x+1)/(x-3) = x. So 3x+1 = x(x-3) = x^2-3x. Rearranging: x^2-6x-1 = 0. By the quadratic formula: x = (6 +/- sqrt(36+4))/2 = (6 +/- sqrt(40))/2 = 3 +/- sqrt(10).
(d) f(x) = f^{-1}(x) intersects on y = x. So the points are (3 + sqrt(10), 3 + sqrt(10)) and (3 - sqrt(10), 3 - sqrt(10)).

---

## How Functions Connects to Other Topics

Functions isn't isolated -- it's the language that every other Pure 1 topic uses.

**Differentiation**: When you differentiate f(x) = x^3 - 2x, you're finding f'(x). The chain rule for differentiating composite functions like (2x + 1)^5 directly uses the concept of composition. If you understand fg(x), the chain rule makes more sense. See our [9709 differentiation guide](/cambridge/9709/pure-1/differentiation/) for more.

**Integration**: Integration is the reverse of differentiation, which is the same idea as an inverse function. When you integrate, you're "undoing" the derivative. The definite integral also requires understanding domain restrictions -- you can only integrate over an interval where the function is defined. See our [9709 integration guide](/cambridge/9709/pure-1/integration/) for the full method.

**Quadratics**: Completing the square to find the range of a quadratic function is pure functions territory. If your completing the square is shaky, that's worth revisiting in our [9709 quadratics guide](/cambridge/9709/pure-1/quadratics/) -- it appears in almost every functions question involving range or inverse.

**Trigonometry**: Graph transformations apply directly to trig graphs. When you meet y = 3sin(2x) + 1, you're applying a vertical stretch (factor 3), horizontal stretch (factor 1/2), and vertical translation (up 1) to y = sin(x). See our [9709 trigonometry guide](/cambridge/9709/pure-1/trigonometry/) for more on trig graph transformations.

---

## FAQs -- Cambridge 9709 Functions

**What's the difference between domain and range?**
The domain is the set of inputs (x-values) a function accepts. The range is the set of outputs (y-values) the function produces. For f(x) = x^2 with domain x in R, the domain is all real numbers but the range is f(x) >= 0, because a square is never negative.

**Is fg(x) the same as gf(x)?**
No. fg(x) = f(g(x)) means apply g first, then f. gf(x) = g(f(x)) means apply f first, then g. They usually give different results. For example, if f(x) = x^2 and g(x) = x + 1, then fg(x) = (x+1)^2 but gf(x) = x^2 + 1.

**How do I know if a function has an inverse?**
The function must be one-one: each output comes from exactly one input. Use the horizontal line test. If any horizontal line crosses the graph more than once, the function is many-one and has no inverse unless you restrict its domain.

**Why does f(x + 3) move the graph left, not right?**
Because f(x + 3) evaluates f at a point 3 units ahead. The output that used to happen at x = 5 now happens at x = 2 (since 2 + 3 = 5). The whole curve shifts left by 3. Changes inside f() are always opposite to what you'd expect.

**Do I need modulus functions for Pure 1?**
No. The modulus function |f(x)| is in Pure 3 only. Don't revise it for Paper 1. Focus on domain/range, composites, inverses, and graph transformations.

**What is a self-inverse function?**
A function where f(x) = f^{-1}(x), which means ff(x) = x. To prove a function is self-inverse, compute ff(x) and show it simplifies to x. Graphically, a self-inverse function is symmetric about the line y = x.

**How many marks are functions questions worth in Paper 1?**
Functions questions typically appear as Question 9 or 10, worth 8-12 marks. Graph transformations can also appear in trigonometry questions. In total, functions knowledge contributes to roughly 15-20% of Paper 1 marks.

---

## Summary

A level maths functions is the language of the entire course. Master the terminology (domain, range, one-one, many-one), the methods (finding inverses, forming composites, applying transformations), and the exam techniques (stating domains, using correct vocabulary, showing working), and you've built the foundation for everything else in Pure 1.

The most common marks lost in functions come from three places: getting composite function order wrong (fg vs gf), forgetting to state the domain of f^{-1}, and using incorrect transformation vocabulary. All three are avoidable with careful practice.

A level maths functions questions appear on every Paper 1. They are predictable, structured, and learnable. The students who score full marks are the ones who have practised enough to make the methods automatic.

**Ready to find out exactly where your functions gaps are?** [Join the ExamPilot waitlist](https://www. exampilot. io/waitlist) for adaptive practice that targets the specific sub-skills you need to work on.

> *Looking for past paper practice? See our [9709 Past Papers by Topic](/cambridge/9709/past-papers/) collection.*
