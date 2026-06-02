---
name: move-37
description: Find the off-board play. Forces the sediment-scan-then-counter-move pattern at any altitude — whole-business strategy, channel choice, landing page positioning, single artifact angle. Trigger on "what's our move 37 here", "find me an off-board play", "we're competing on the same axis", "/move-37", or any request for non-obvious strategic options. One run = one Move 37 artifact with 3 candidate plays and a sequencing recommendation.
bike-method-phase: 1
---

> Named for AlphaGo's Game 2, Move 37 (Lee Sedol match, 2016) — a move humans rated 1-in-10,000 because centuries of accumulated Go convention had made it culturally invisible. The Move 37 pattern isn't creativity. It's the discipline of naming the convention before proposing the counter-move.

## What this skill does

Walks the user through a 4-phase interview that forces the Move 37 thinking pattern: name the cultural sediment in the space, find what the sediment makes invisible, generate 3 plays that explicitly contradict sediment, stress-test each against complexity / cost / ceiling / risk, and recommend sequencing.

**The skill refuses to generate plays until the sediment scan is complete.** Without that discipline it becomes a brainstorm generator and loses the entire point.

**Altitude-invariant.** Same pattern works for "what's our Move 37 for ExamPilot revenue" and "what's our Move 37 angle for this Reddit post." Altitude is a question in the interview, not a different skill.

## What `/move-37` is NOT

- Not `/level-up`. `/level-up` finds leverage in *your own workflow*. `/move-37` finds leverage in *market positioning, strategy, or content angle*. Different lenses.
- Not a brainstorm. If sediment scan is skipped or shallow, skill stops and asks for more.
- Not auto-publish. Output goes to `marketing/pipelines/strategy/` for review. Decisions to act get logged separately.
- Not a multi-output planner. One run = one artifact = one decision: which Move 37 (if any) to pursue.

## When `/move-37` runs

- "What's our Move 37 here?"
- "Find me an off-board play."
- "We're competing on the same axis as everyone else."
- "I want to do something nobody else is doing."
- Before locking a strategic direction (channel mix, positioning, launch plan, pricing model)
- Before writing high-stakes content (pillar article, landing page hero, launch announcement) where the angle decision matters more than the execution
- After `/landing-competitor` reveals everyone is converging on the same playbook
- When `/weekly-pulse` or `/priorities` keeps surfacing the same conventional moves

## Inputs the skill reads automatically

Read at session start when scope is ExamPilot-related:

```bash
cat marketing/context/audience-segments.md
cat marketing/context/funnel-strategy.md
cat marketing/context/content-standards.md
```

Fetch from wiki for strategy grounding:

```bash
gh api repos/akhanaton/spyglass-wiki/contents/wiki/marketing/strategy.md --jq '.content' | base64 -d 2>/dev/null
gh api repos/akhanaton/spyglass-wiki/contents/wiki/marketing/positioning.md --jq '.content' | base64 -d 2>/dev/null
gh api repos/akhanaton/spyglass-wiki/contents/wiki/product/strategy/path-to-revenue.md --jq '.content' | base64 -d 2>/dev/null
```

If fetches fail, proceed with the context files only and flag missing wiki context inline.

Also scan `marketing/pipelines/strategy/` for prior Move 37 artifacts — do not re-propose plays that were already shelved unless the user explicitly asks.

## Execution — four phases

### Phase 0 — Frame the decision

Ask in order:

1. **What's the decision or artifact in play?** (free text — could be "ExamPilot's path to first 100 paying users", or "the angle for our Cambridge 9709 hub page")
2. **At what altitude?** (business / channel / campaign / single artifact)
3. **What's the implied competition or convention?** Who or what is the player you're tempted to copy or one-up? Could be a competitor, an industry default, or your own current plan.
4. **What's the commercial outcome you're optimising for?** Revenue, conversion rate, retention, attention, signups. Be specific.

Restate the frame back in one sentence. If the frame is fuzzy (e.g. "I want more growth"), refuse to proceed and ask for sharper inputs.

### Phase 1 — Sediment scan (the gate)

This is the phase that makes the skill different from a brainstorm. Do not skip or short-circuit it.

Generate **4-7 pieces of cultural sediment** in this space — the default assumptions the conventional player operates under without examining. Each entry has two parts:

- **Sediment:** the assumption (one line)
- **Why it persists:** what reinforces it (one line — usually a structural reason: market history, incumbent incentive, industry training, geographic bias)

Examples for grounding the skill (do not reuse verbatim — generate fresh for the actual frame):

- *Sediment: Students are the customer; tutors are an awareness channel. Why it persists: UK domestic market shaped competitor instincts; tutoring is a minority phenomenon in UK so its distribution power is invisible.*
- *Sediment: Exam prep brands lean aspirational ("achieve top grades"). Why it persists: aspirational framing tests well in brand surveys; resit framing feels off-brand to incumbents.*
- *Sediment: Results Day is one of 365 content days. Why it persists: content calendars are evenly weighted; the emotional intensity of the day isn't quantifiable in SEO tools.*

After listing, ask the user: *"Do these match what you see? Any I'm missing or wrong on?"* Iterate once. **If the user agrees too quickly without adding or correcting, push back: the sediment scan is only useful if it surfaces something the user already half-suspected.**

### Phase 2 — Invisibility map

For each piece of sediment, name **what it makes structurally hard to see**. Not "what's a different idea" — what is rendered invisible by the assumption.

Format:

```
Sediment: [assumption]
Makes invisible: [the option, segment, channel, angle, or opportunity that the sediment hides]
```

This is the bridge between sediment and play. A good invisibility entry passes the test: *if this assumption disappeared tomorrow, what would you suddenly be able to see?*

### Phase 3 — Generate 3 off-board plays

Generate exactly **3 candidate Move 37s**. Each play must:

1. Explicitly contradict at least one piece of named sediment. State which.
2. Be a *different game inside the same game* — not "more of X" but "instead of X."
3. Be commercially specific. Vague directional bets ("we should care more about tutors") fail the test. Operational specificity ("free Tutor Mode with multi-student dashboard, tutors get extended access when 3+ students convert") passes.
4. Include the **stress test row** (mandatory):

| Dimension | Detail |
|---|---|
| Complexity | Low / Medium / High — with one-line reason |
| Cost | EUR estimate or "EUR 0 — time only" |
| Timeline | Phase 0 / Phase 1 / Phase 2 — or specific weeks |
| Ceiling | Realistic outcome estimate tied to the commercial metric from Phase 0 |
| Key risk | The single biggest reason this fails |
| Sediment contradicted | Which assumption from Phase 1 this play breaks |

**If you can't fill a row, the play isn't ready — discard and generate another.**

### Phase 4 — Sequencing recommendation

Almost always the 3 plays stack rather than compete. Recommend:

- **Start now (Phase 0):** the lowest-cost, lowest-risk play — usually a positioning shift
- **Build during Phase 0, ship in Phase 1:** the play that needs runway
- **Scale in Phase 2:** the play with the highest ceiling but longest setup

If two plays genuinely conflict (e.g. one requires niche identity, another requires broad brand), say so and force a pick.

End with one line: *"If you can only run one, run [X] because [reason]."*

## Output contract

Every `/move-37` run produces:

1. **One artifact** saved to `marketing/pipelines/strategy/move-37-{slug}-{YYYY-MM-DD}.md`
2. **One-line entry** appended to `decisions/log.md` under today's date, linking to the artifact
3. **A one-screen close** in chat — the 3 plays as a stress-test table + sequencing line

### Artifact frontmatter (mandatory)

```yaml
---
type: move-37
status: proposed   # proposed | chosen | shipped | retired
altitude: business | channel | campaign | artifact
frame: "[restated decision from Phase 0]"
commercial-metric: "[the specific metric being optimised]"
plays:
  - name: "[play 1 name]"
    sediment-contradicted: "[which assumption]"
    ceiling: "[outcome estimate]"
  - name: "[play 2 name]"
    sediment-contradicted: "[which assumption]"
    ceiling: "[outcome estimate]"
  - name: "[play 3 name]"
    sediment-contradicted: "[which assumption]"
    ceiling: "[outcome estimate]"
recommendation: "[sequencing one-liner]"
outcome: TBD  # filled in later by user or /tune
created: YYYY-MM-DD
---
```

`outcome: TBD` is the feedback hook — `/tune` reads this monthly and asks the user to update it for any artifact with status `chosen` or `shipped`.

### Artifact body

```markdown
# Move 37: [restated frame]

## Frame
- Altitude: [...]
- Convention being challenged: [...]
- Commercial outcome: [...]

## Sediment scan
[4-7 entries, each with sediment + why it persists]

## Invisibility map
[one entry per sediment item]

## Play 1: [name]
[2-3 sentence description of the play]
[stress-test table]

## Play 2: [name]
[same structure]

## Play 3: [name]
[same structure]

## Sequencing recommendation
[paragraph]

If you can only run one, run [X] because [reason].
```

## Critical implementation rules

1. **Sediment scan is the gate.** Skill refuses to generate plays until Phase 1 produces 4+ real sediment entries with reasons.
2. **Every play maps to a named sediment.** No "general good ideas." Each play must point to which assumption it contradicts.
3. **Stress test is mandatory.** Any play missing a row gets discarded, not waved through.
4. **Generate exactly 3 plays.** Not 2, not 5. The constraint forces ranking.
5. **Operational specificity over directional vision.** "Lean into resit" fails. "Become exclusively the resit recovery brand for 6-9 months with dedicated landing page hub, voice file, and Results Day positioning" passes.
6. **Altitude is asked once, then never used to gate logic.** Same pattern at every scope.
7. **Don't propose plays already shelved.** Check `marketing/pipelines/strategy/` for `status: retired` entries first.
8. **Read-only on existing files except the new artifact and `decisions/log.md`.**
9. **Output saves to `marketing/pipelines/strategy/` — never auto-publishes or ships anything downstream.**
10. **EUR only for cost estimates** (consistent with ExamPilot pricing convention).

## Continuous improvement hook

Each artifact has `status` and `outcome` fields. `/tune` runs monthly and:

1. Lists all Move 37 artifacts with `status: chosen` or `shipped` where `outcome: TBD`
2. Prompts user to update outcome (Won / Lost / Inconclusive / Still running)
3. After 6+ outcomes exist, surfaces patterns: which kinds of sediment-breaks worked, which didn't, in your specific context

Over time this builds a personal taxonomy of off-board moves that compound — the actual long-term asset of the skill.

## Guardrails

- Never claim a play is a Move 37 if it doesn't break a named piece of sediment. "Counter-positioning" is a Move 37 pattern; "do SEO better" is not.
- Never propose plays that violate ExamPilot principles in `marketing/context/content-standards.md` (no B2B school licensing, no "AI tutor" framing, EUR only, GDPR-safe).
- Do not use the skill to justify a decision the user has already made. If the user pre-commits to a play in Phase 0, push back: *"Want me to stress-test that one, or run a real Move 37 scan?"* Either is fine — but don't pretend the latter happened when the former did.
- Do not auto-update `status` or `outcome` fields. User edits those manually or via `/tune`.

## Verification (for the implementer)

- **Pre-committed-answer test.** User says "let's just do the tutor flywheel — give me a plan." Expected: skill offers to either stress-test that idea or run a real scan, doesn't pretend to discover what user already named.
- **Vague-frame refusal.** User says "I want more growth." Expected: skill refuses to proceed until frame is sharpened (which metric, what altitude, what convention).
- **Sediment-skip refusal.** User says "skip the sediment, just give me ideas." Expected: skill refuses, explains why the scan is the whole point, offers to make it fast.
- **Operational-specificity test.** A play comes out as "lean into resits." Expected: skill flags it as too vague and replaces with operational detail.
- **Repeat-shelved-play test.** A prior artifact has `status: retired` for "tutor flywheel." User runs `/move-37` again on similar frame. Expected: skill notes the prior retirement and asks whether to re-examine or skip.
- **Altitude-invariance test.** Run on "ExamPilot's path to first 100 students" and "the angle for this Reddit post about Pure 1 integration." Expected: same skill structure, both produce 3 plays with stress tests, neither requires a mode flag.

## What this skill does NOT do

- Does not write the content for a chosen play. Use `/write-article`, `/write-reddit`, `/landing-write`, `/email-sequence`, `/copywriting` etc.
- Does not build automations for a chosen play. Use `/level-up` for that.
- Does not track execution. Once chosen, the play moves to Linear via `references/execution-model.md` rules.
- Does not auto-update outcomes. User or `/tune` does that.
