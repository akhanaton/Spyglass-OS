# Where to start — recommendation (2026-06-14)

> Captured from the post-consolidation session on 2026-06-14, after rationalizing work tracking onto Linear (see `decisions/log.md` 2026-06-14 and memory `project-linear-rationalization`). Launch target: early–mid August 2026. This is a snapshot — once the QLP decisions below are made, re-prioritize.

## The one place to start: the three QLP decisions — EP-88, EP-89, EP-90

Your launch gates on one thing: **a student sees a vetted CIE 9709 QLP in a live session.** Everything else — content, email, SEO, YouTube — is sending traffic to a product that has to exist first. That product sits behind one dependency chain:

```
EP-88 IP posture ┐
EP-89 contract   ├─→ seed run (50 QLPs) ─→ EP-87 wire serving ─→ student sees a QLP
EP-90 synth model┘        ▲
                          └─ EP-101 tier-calc + EP-102 multi-board / re-point seed tooling
```

Those three are **decisions, not builds** — hours, not days:
- **EP-88** (IP posture for Cambridge-derived QLPs) ≈ 1hr legal review. Blocks first real extraction.
- **EP-89** (canonical QLPQuestionContext contract) ≈ a one-day contract diff. Prerequisite: dump the actual `qlp_phase3_contracts.py` schema from code and diff against the two wiki specs. Blocks SRS/seeding code.
- **EP-90** (synthesizer model for the seed run) ≈ a model choice. Also run the P0 Gemini Flash-Lite deprecation check + pre-stage the fallback. Blocks the seed run.

Until they're made, the engineer can't start the seed-pipeline code, can't run real extraction, can't seed. They're cheap, they unblock weeks of downstream work, and **only you can make them** — highest leverage on the board. Block 2–3 hours this week and settle all three.

## Then, in priority order

1. **Resolve the EP-87 unknown — your single biggest schedule risk.** Open question on the issue: *does the live `topic_id` path render a promoted QLP richly (misconception distractors, mark-scheme steps), or flatten it to a generic question?* That decides whether wiring serving is a small additive job (option a: wire promotion) or session-layer surgery (option b: mount the serving layer). You can't size the launch until you know this. Worth a code trace this week.
2. **Knock out the P0 code blockers** — EP-94 (hardcoded auth / bypass), EP-95 (SparxGate no-op), EP-96 (dead nav routes), EP-97 (PremiumGate `/upgrade`). 30min–4hr each. The matrix flags them as "must fix **before any testing**" — they're the warm-up that unblocks verifying every flow.

## One time-bomb on the parallel (Teresa) track — don't let it slip

**EP-52 (wire Brevo) is Urgent, due Jun 21** — a week out — and it blocks all four email sequences (EP-62/63/64) + landing capture. This track runs independently of QLP, so it shouldn't wait behind it.

## What NOT to start with

Content spokes (EP-67–74), YouTube (EP-78/80–86), P2/P3 cleanup. All real, none on the critical path to "a student sees a QLP."

## Offered next step (not yet done)

Tee up EP-89's prerequisite: dump the actual `qlp_phase3_contracts.py` schema and diff it against the two wiki specs, so the canonical contract can be settled in one sitting.
