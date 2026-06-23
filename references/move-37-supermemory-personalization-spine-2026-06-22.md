---
type: move-37
status: proposed
altitude: business
frame: "Ship a genuinely adaptive, personalized learning experience at launch using assets already built or committed (misconception capture, ERI, supermemory, misconception-aware AI workflows) with minimal new development."
commercial-metric: "Activation → retention: the 'this actually adapts to me' moment in the first Drills sessions that drives trial-to-paid conversion."
plays:
  - name: "Supermemory as the personalization spine"
    sediment-contradicted: "Misconception data is a per-feature input + supermemory is deferred tutor-era enrichment"
    ceiling: "Every current and future AI feature personalizes from one write; cross-session memory becomes a platform property, not per-feature work."
  - name: "The deterministic mirror (zero-AI capture)"
    sediment-contradicted: "Adaptivity needs a big real-time engine + capture needs AI"
    ceiling: "Misconception signal on 100% of MCQ answers, zero latency, zero per-answer cost — the foundation everything else reads."
  - name: "Readiness narrative (ERI + misconceptions as the story)"
    sediment-contradicted: "Adaptivity = a black-box engine + adaptivity is blocked on full content"
    ceiling: "A legible, AI-narrated readiness story ('you keep dropping the constant of integration') — the launch trust/wow moment no black-box engine matches."
recommendation: "Run B now (foundation, fold into EP-87), build A on top during the first Drills slice, ship C in Phase 1. They stack; A is the architectural keystone."
outcome: TBD
created: 2026-06-22
---

# Move 37: Adaptive learning at launch from already-built assets

## Frame
- **Altitude:** Business / product feature strategy.
- **Convention being challenged:** The current build instinct — consume misconception data feature-by-feature (wire it separately into Drills, SRS, dashboard, ERI), treat supermemory as a deferred tutor-era nice-to-have, and assume "real adaptivity" needs a sophisticated new engine.
- **Commercial outcome:** The first-session "this gets me" moment that converts trial to paid. Felt personalization, not infrastructure.

## Sediment scan

1. **Adaptive learning means building a sophisticated real-time adaptive engine** (IRT, learner-theta, dynamic difficulty matching).
   *Why it persists:* That is what "adaptive learning" means in edtech literature and competitor marketing — the impressive-sounding version. The simple version doesn't demo as well in a pitch.

2. **Misconception data is a per-feature input — each feature must be separately wired to consume it.**
   *Why it persists:* The codebase is structured that way (MongoDB repos, feature-specific consumers). Engineers naturally wire point-to-point; nobody owns the cross-feature view.

3. **Supermemory is "conversational enrichment," deferred, a tutor-era leftover.**
   *Why it persists:* It was introduced for the Socratic chat. The pivot to the MCQ engine made chat feel legacy, so supermemory got tarred as legacy by association — even though it is feature-agnostic.

4. **Personalization requires capturing rich data (handwritten work, AI evaluation of reasoning).**
   *Why it persists:* The tutor-era design assumed AI evaluation of student work as the signal source. "Rich signal = AI inference" became the mental default.

5. **We can't ship real adaptivity at launch because the QLP content seed isn't ready.**
   *Why it persists:* Content is the genuine gating blocker for volume, so adaptivity feels blocked too. The two get conflated.

6. **Each AI feature needs its own context-assembly / prompt engineering.**
   *Why it persists:* Agents were built independently, each with its own tools and prompt. No shared context substrate.

## Invisibility map

- **Sediment 1 → makes invisible:** that a *cheaper* signal already exists — the deterministic distractor→misconception map sits on every served question. Most of the felt personalization comes from a tiny submit-side hook, not an engine.
- **Sediment 2 → makes invisible:** a shared memory layer where the signal is written **once** and every AI touchpoint reads it for free. One write, N readers — instead of N integrations that grow with every new feature.
- **Sediment 3 → makes invisible:** supermemory is a **student-keyed durable memory store** (`student_{userId}`), already SDK-wired front and back. It is the personalization spine for the *whole* product, not a chat feature.
- **Sediment 4 → makes invisible:** the MCQ distractor choice is a deterministic, zero-cost, zero-latency misconception signal. Capture needs **no** AI; only the *explanation* needs a model — and only on demand.
- **Sediment 5 → makes invisible:** even a thin seed (50 Pure 1 QLPs) with misconception tags is enough to demonstrate the adaptive loop on the highest-value topics. Adaptivity is gated on the hook + a flag, not on full content.
- **Sediment 6 → makes invisible:** if all student signal lands in supermemory, every agent's prompt enrichment is solved by one retrieval against `student_{userId}`. The container becomes the universal context substrate.

## Play 1: Supermemory as the personalization spine  ← the Move 37

Don't wire misconception consumption feature-by-feature. Add the committed deterministic capture hook (EP-87), and on each hit **write a durable student memory to supermemory** (`student_{userId}`) — e.g. "repeatedly drops the constant of integration; responds well to worked examples." Flip `SUPERMEMORY_ENABLED=true`. Now Drills' explanation generator, the knowledge-state one-liner, Socratic hints, and any future coaching all read the *same* memory. Personalization becomes a property of the platform, written once and consumed everywhere — including across sessions. MongoDB stays the system-of-record; supermemory is the derived, AI-facing read layer.

| Dimension | Detail |
|---|---|
| Complexity | **Medium** — capture hook is trivial; new work is a write-to-supermemory adapter + pointing each AI consumer at the container. SDK, schemas, and `exampilot/lib/ai/memory-client.ts` already exist. |
| Cost | **~EUR 0 infra** — `SUPERMEMORY_API_KEY` already provisioned; eng time only. Watch per-call cost at scale. |
| Timeline | Capture hook in EP-87 (Phase 0); supermemory write + first reader (Drills) in the first Drills slice. |
| Ceiling | Every current and future AI feature personalizes from one signal source; cross-session memory ("you've struggled with this for 3 weeks") becomes possible. Platform-level adaptivity. |
| Key risk | External SaaS on a personalization path: latency/availability, cost-at-scale, vendor lock-in. **Mitigation:** MongoDB remains authoritative; supermemory is a rebuildable read cache, never the source of truth. |
| Sediment contradicted | **2** (per-feature wiring) and **3** (supermemory = legacy). |

## Play 2: The deterministic mirror (zero-AI capture)

Make the deterministic distractor→misconception map the **only** capture path at launch. Do not revive the AI `StudentWorkEvaluator` (expensive, legacy, default-off). On submit, read the selected option's tagged `misconception_id` → write `misconceptions_hit`. AI is used only to *explain* (`PersonalizedInstructionalContentWorkflow`), only on demand. The felt adaptivity — Drills targeting your weak spots, the dashboard showing your misconception profile — comes from a signal that costs nothing to capture.

| Dimension | Detail |
|---|---|
| Complexity | **Low** — read selected option → write field. No AI, no new model calls on the submit path. |
| Cost | **EUR 0.** |
| Timeline | Phase 0, inside EP-87. |
| Ceiling | Misconception signal on 100% of MCQ answers across every feature; the foundation everything else reads. Modest on its own (data, not yet felt). |
| Key risk | Signal quality depends on QLP `distractor_logic` being well-tagged at seed. Thin/garbage tags = thin signal. **Mitigation:** seed QA on distractor tagging. |
| Sediment contradicted | **1** (adaptivity = engine) and **4** (capture needs AI). |

## Play 3: Readiness narrative (ERI + misconceptions as the story)

Rather than building dynamic difficulty (IRT), use what's built: ERI (readiness score) + `PERSISTENT` misconceptions to produce one student-facing narrative — "Your readiness for Pure 1 is 64%. The thing holding you back: you keep dropping the constant of integration. Here are 5 drills targeting exactly that." Not a black-box engine — a legible, AI-narrated readiness story.

| Dimension | Detail |
|---|---|
| Complexity | **Medium** — score `misconceptions_seen` into ERI weighting + one AI summary endpoint (cacheable per dashboard load). |
| Cost | **Low** — one LLM summary per dashboard load, cacheable. |
| Timeline | Phase 1, after capture + ERI scoring land. |
| Ceiling | The launch "wow": a legible, trustworthy readiness story that beats a black-box engine on trust. Drives the "this gets me" conversion moment. |
| Key risk | Needs enough seeded, misconception-tagged QLPs per topic for a credible narrative; ERI must be validated against real 9709 data first. **Mitigation:** start on the seeded Pure 1 topics only. |
| Sediment contradicted | **1** (adaptivity = engine) and **5** (adaptivity blocked on full content). |

## Sequencing recommendation

The three plays stack rather than compete, and there is a hard dependency: A is built on B (you cannot write a signal to supermemory before you capture it).

- **Now (Phase 0, fold into EP-87):** Play B — the zero-AI deterministic capture hook. Non-negotiable foundation.
- **During the first Drills slice:** Play A — write each captured hit to supermemory and point the first AI consumer (Drills explanation generator) at the `student_{userId}` container. This is the architectural keystone; do it before the second consumer is wired, or you pay the per-feature integration cost (sediment 2) and never recover it.
- **Phase 1:** Play C — the readiness narrative, once ERI scoring of misconceptions and enough seeded content exist.

If you can only make one architectural decision, make **A**: route the single committed capture signal through supermemory rather than point-to-point. It converts "one committed hook" into compounding, cross-feature, cross-session personalization — the exact "maximum leverage, minimum new dev" the frame demands. Wiring misconceptions into each feature separately pays the integration cost once per feature, forever.
