# Experiment Framework

Structured A/B testing and growth experimentation for ExamPilot. Adapted from marketingskills ab-testing patterns.

## Hypothesis Template

```
Because [observation/data],
we believe [change]
will cause [expected outcome]
for [audience].
We'll know this is true when [metric] changes by [amount].
```

**Weak:** "Changing the CTA might increase signups."
**Strong:** "Because Reddit visitors bounce at 70% on the landing page (PostHog data), we believe adding a Cambridge 9709 topic preview above the fold will increase signup rate by 15%+ for organic visitors. We'll measure visitor-to-signup rate."

## Test Types

| Type | When to use | Traffic needed |
|---|---|---|
| A/B | Two versions, single change | Moderate |
| A/B/n | Multiple variants of one element | Higher |
| Split URL | Different landing pages | Moderate |

MVT (multivariate) requires very high traffic. Not viable for ExamPilot at pre-launch/early stage.

## Sample Size Quick Reference

| Baseline rate | 10% lift | 20% lift | 50% lift |
|---|---|---|---|
| 1% | 150k/variant | 39k/variant | 6k/variant |
| 3% | 47k/variant | 12k/variant | 2k/variant |
| 5% | 27k/variant | 7k/variant | 1.2k/variant |
| 10% | 12k/variant | 3k/variant | 550/variant |

**Reality check for ExamPilot:** At pre-launch traffic levels, only bold changes (50%+ expected lift) will reach significance in reasonable timeframes. Focus on big swings, not micro-optimizations.

## Metrics Selection

For every test, define:

- **Primary metric:** Single metric that determines the winner. Tied to hypothesis.
- **Secondary metrics:** Explain why/how the change worked.
- **Guardrail metrics:** Things that shouldn't get worse. Stop the test if significantly negative.

**Example: Landing page headline test**
- Primary: Visitor-to-signup rate
- Secondary: Time on page, scroll depth
- Guardrail: Bounce rate on pricing page (downstream)

## ICE Prioritization

Score each hypothesis 1-10 on three dimensions:

| Dimension | Question |
|---|---|
| **Impact** | If this works, how much will it move the primary metric? |
| **Confidence** | How sure are we this will work? (Data, not gut.) |
| **Ease** | How fast and cheap can we ship and measure this? |

**ICE Score** = (Impact + Confidence + Ease) / 3

Run highest-scoring experiments first. Re-score monthly.

## Experiment Velocity Targets

| Metric | Early stage (now) | Growth stage |
|---|---|---|
| Experiments per month | 1-2 | 4-8 |
| Win rate | 30-40% (bold tests) | 20-30% (mature program) |
| Average test duration | 2-4 weeks | 2-4 weeks |
| Backlog depth | 5-10 hypotheses | 20+ hypotheses |

## Experiment Playbook Template

When a test wins, document the pattern:

```markdown
## [Experiment Name]
**Date:** YYYY-MM-DD
**Hypothesis:** [the hypothesis]
**Variants:** [control vs variant description]
**Sample size:** [n per variant]
**Duration:** [days]
**Result:** [winner/loser/inconclusive]
**Primary metric:** [metric] changed by [X%] (95% CI: [range])
**Guardrails:** [any guardrail metrics and outcomes]
**Segment differences:** [mobile vs desktop, new vs returning, Cambridge vs Edexcel]
**Why it worked/failed:** [analysis]
**Reusable pattern:** [the insight, e.g., "exam-board-specific social proof near CTA increases signup rate"]
```

## Pre-Launch Checklist

- [ ] Hypothesis documented
- [ ] Primary, secondary, and guardrail metrics defined
- [ ] Sample size calculated (use Evan Miller's calculator)
- [ ] Variants implemented and QA'd
- [ ] Tracking verified in PostHog
- [ ] Duration committed (no peeking and stopping early)

## The Peeking Problem

Looking at results before reaching sample size and stopping when it "looks significant" leads to false positives. Pre-commit to sample size and trust the process. If you must monitor, only check for technical issues (tracking broken, variant not rendering).

## Where Experiments Live

- Experiment log: `marketing/pipelines/experiments.md` (P2)
- Playbook entries: append to experiment log as tests complete
- Reference in monthly reports: `marketing/templates/marketing-report.md` has an experiment results section

Source: Adapted from coreyhaines31/marketingskills ab-testing skill
