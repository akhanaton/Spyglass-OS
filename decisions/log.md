# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.
```

Keep it terse. Future-you will thank present-you for capturing the *why*, not just the *what*.

---

## 2026-06-23 — Free beta end policy: 14-day trial

**Decision:** Each user gets 14 days from signup before hitting the paywall. Trial-based, not fixed-date or first-N-free.

**Why:** Industry default. Fair to all users regardless of signup date. Makes conversion math predictable. Fixed date punishes late beta joiners; first-N-free creates a permanent two-tier cohort.

**Alternatives considered:** Fixed cutoff date (punishes late joiners, harder to communicate); first-N-free (permanent free cohort is a management burden).

**Owner:** Enitan. Closes EP-106. Unblocks EP-22 (Dodo checkout). Implementation: `trial_started_at` per user, paywall check compares `now - trial_started_at > 14 days`.

---

## 2026-06-23 — Marketing data modules: file-relative imports + DataForSEO seeding fix

**Decision:** Fixed three bugs in `marketing/data_sources/modules/`: (1) replaced the cwd-relative `sys.path.insert(0, "..")` in `gsc_analyzer.py` and `reddit_monitor.py` with a file-relative `Path(__file__).resolve().parent.parent` so `from config import …` resolves regardless of working directory; (2) hardened `data_aggregator._fetch_dataforseo` against DataForSEO's explicit-`null` response fields (`tasks`/`result`/`items`) with `or []` guards plus an early return when there are no keywords (skips the paid call); (3) reseeded the DataForSEO fetch from the GSC **query** dimension (real keywords) instead of GSC page URLs. Added `marketing/data_sources/cache/` to `.gitignore`.

**Why:** Surfaced when verifying the new DataForSEO password — `data_aggregator.py` errored on both sources from repo root. The cwd-relative import was a footgun: it only worked when run from inside `modules/`, but the aggregator (and its callers `/priorities`, performance agent) run from repo root. The seeding flaw was latent behind the GSC crash — once GSC worked, seeding DataForSEO with page URLs would have fired a paid SERP call returning meaningless results. Verified GSC fetch (12 pages) and real keyword seeds without any paid call.

**Alternatives considered:** Leave the seeding as-is and just flag it (rejected — would silently waste API spend on every aggregator run). Rewrite the aggregator's data model to track keywords properly (deferred — out of scope; query-seed fix is sufficient).

**Owner:** Enitan.

---

## 2026-06-23 — EP-146 Atlas credential: dev-only, no rotation required

**Decision:** The hardcoded MongoDB Atlas credential in `test_mongodb_repositories.py` is a dev credential with no prod exposure. No rotation was performed. The fix removes the hardcoded fallback and adds a clean skip — credential hygiene resolved without rotation overhead.

**Why:** Enitan confirmed the credential belongs to a dev/test Atlas cluster only. Prod was never exposed. The code fix (remove fallback, add `pytest.skip`) achieves the security goal; rotation would add overhead with no material benefit given the scope.

**Alternatives considered:** Rotate regardless (rejected — unnecessary given dev-only scope).

**Owner:** Enitan.

---

## 2026-06-23 — Combined post-654 fix branch strategy

**Decision:** All post-PR#654 code fixes (EP-146, EP-145, EP-148, EP-127, EP-163, EP-149) are stacked on a single branch `akhanaton/ep-post-654-fixes` (PR #672, merged to `main` 2026-06-23 as `f5022d52`) rather than per-ticket branches.

**Why:** The fixes are tightly related (all spawned from the same PR #654 merge) and small enough to review together. Per-ticket branches would fragment a coherent bug-fix pass into 6+ PRs with no cross-PR context. A standalone EP-146 PR (#671) was opened then closed and folded in when the combined approach was chosen.

**Alternatives considered:** Per-ticket branches (rejected — too fragmented for a batch of related post-merge fixes).

**Owner:** Enitan.

---

## 2026-06-22 — Park MSLQ cognitive profiling

**Decision:** Park MSLQ cognitive profiling — stop further investment, do not build the student-facing MSLQ onboarding gate UI, and stop positioning it as a launch feature. No code change is required to park it: it is already inert.

**Why:** Code verification (2026-06-22, two agents) confirmed MSLQ has no effect on the current or launching product — parking formalizes the de facto state. The live serving path (`GET /learning-sessions/{id}` → `QLPRuntimeService.retrieve_assessment_payload`) and session creation never read MSLQ; the MSLQ → `CardTypeSelector` → personalized-drill chain lives in `SessionPhaseAIService`, which is dormant (zero importers under `app/api/`, tests-only); the onboarding gate endpoints (`onboarding.py:137,167`) are mounted but enforced nowhere, and there is no student-facing MSLQ intake UI in `exampilot/` (only an admin read-only analytics page). Every profile consumer defaults to `profile_bucket="default"` with no NPE. The only thing forgone is future personalization — specifically the MSLQ-bias half of EP-159 (SRS card-type bias), whose launch path (`srs_batch_generation_service.py`) already runs MSLQ-free. The deterministic misconception capture (Move 37 workstream, EP-156) is the stronger, real personalization signal to invest in instead. **Revival trigger:** revisit only if we both (a) want learning-style-based card weighting and (b) have a student-facing intake that won't add onboarding friction; evidence that style-matched cards lift retention/conversion would change the mind.

**Alternatives considered:** (1) Build the MSLQ frontend onboarding gate for launch — rejected; adds onboarding friction for an unproven, unwired personalization lever. (2) Keep investing in MSLQ as the "dual-profile primary differentiator" (as the wiki framed it) — rejected; it was never wired, and deterministic misconception capture is the real signal.

**Owner:** Enitan.

---

## 2026-06-22 — Pull deterministic misconception capture hook into EP-87 scope

**Decision:** The submit-side deterministic misconception capture hook is pulled into EP-87 (first slice of the lean MCQ question engine), not deferred to post-launch. On answer submit, the engine reads the selected option's tagged `misconception_id` (already present on every served question via `QLPRuntimeService._build_options` → `distractor_logic`) and writes `misconceptions_hit`. Zero AI, zero added latency. This is the prerequisite that makes Drills (and every other adaptive consumer) have a real per-student signal at launch.

**Why:** Investigation of the live code (3 parallel agents, 2026-06-22) found that the "deterministic misconception capture in a ScoringService" the wiki described **does not exist**. The deterministic distractor→misconception map is built but write-only at generation time; nothing reads it back on submit. The only capture that runs is AI-inferred, on the legacy `/ai` conversation endpoint (gated on `extracted_work`), default-off. So no launching MCQ feature captures anything today. The hook is small because the data already sits on the served question — deferring it would leave Drills' core value proposition ("ramps as you improve") with no signal to consume. What would change the mind: if seed QLPs ship with poorly-tagged `distractor_logic`, the signal is thin and the hook's value drops until tagging QA improves.

**Alternatives considered:** (1) Keep Drills a post-launch consumer and ship it as a non-adaptive practice mode first — rejected, it guts the differentiator. (2) Revive the AI `StudentWorkEvaluator` capture path — rejected, expensive, legacy, default-off, and overkill when a deterministic lookup suffices.

**Update 2026-06-22 (reconciliation):** Full git-history trace confirmed EP-87 is correctly Done — it shipped Phase 0 **render-only** (commit `92ce2c24`, PR #624). The scoring engine (`ScoringService`/`AttemptRepository`/`question_delivery`) was always Phase 1, never built, and exists only in design docs — no hidden branch/worktree. Rather than reopen EP-87 (founder choice, AskUserQuestion), filed **EP-162 "QLP serving Phase 1"** as the real foundation; EP-156 (capture hook) is now blocked-by EP-162. `misconceptions_hit` persistence is a named line item inside Phase 1's `AttemptRepository`.

**Owner:** Enitan.

---

## 2026-06-22 — Move 37: supermemory as the personalization spine

**Decision:** Adopt "capture once, personalize everywhere" as the architecture for launch adaptivity. The committed capture hook writes each misconception hit to supermemory (`student_{userId}`) as a durable student memory; `SUPERMEMORY_ENABLED` is flipped on; every AI consumer (Drills explanation generator first, then knowledge-state one-liner, Socratic hints, future coaching) reads the same container. MongoDB stays system-of-record; supermemory is a rebuildable, AI-facing read layer. Full analysis at `references/move-37-supermemory-personalization-spine-2026-06-22.md` (status: proposed). Three stacked plays: B (zero-AI capture, now/EP-87) → A (supermemory spine, first Drills slice) → C (ERI readiness narrative, Phase 1).

**Why:** The conventional move wires misconception consumption into each feature separately — N integrations that grow with every new feature. The off-board move writes the signal once into the student-keyed memory layer already built and shelved, and lets every current and future AI feature read it for free. It turns the single committed hook into compounding, cross-session personalization — maximum leverage, minimal new dev, which was the explicit constraint. Reframes supermemory from deferred-legacy to the actual spine. What would change the mind: if supermemory's latency/cost/availability on the personalization path proves unworkable at scale, fall back to reading misconceptions directly from MongoDB per feature (the conventional path) — the capture hook and MongoDB records make that fallback always available.

**Alternatives considered:** Per-feature point-to-point wiring (the convention — rejected as non-compounding); reviving the AI evaluator as the signal source (rejected — see EP-87 entry above).

**Owner:** Enitan.

---

## 2026-06-16 — Design system sync cadence: quarterly via /tune

**Decision:** Claude Design → repo token sync is checked quarterly (March/June/September/December `/tune` cycles), not monthly or ad hoc. Added as a named check in `tune/SKILL.md` Steps 1–4. If a sync is needed and straightforward, it runs in-session; otherwise a Linear issue is filed.

**Why:** Token drift is low-risk between design iterations — the palette won't change monthly. A quarterly gate catches drift before it compounds without adding monthly overhead. The quarterly cadence matches the strategic review cadence in `references/continuous-improvement.md`.

**Alternatives considered:** Monthly (too frequent for a stable identity system); ad hoc / on demand (no enforcement, drift guaranteed).

**Owner:** Enitan.

---

## 2026-06-16 — Claude Design integration approach for ExamPilot design system

**Decision:** Claude Design (claude.ai) is the source of truth for the ExamPilot Design System. Integration follows Option B: `brand/exampilot-theme.css` in the product repo is the Claude Design output landing zone; `exampilot/app/globals.css` applies those tokens plus product-specific additions that Claude Design won't generate; one wiki article for decisions/rationale; `connections.md` entry for the Claude Design URL. No copies of token values in the wiki or OS. Full analysis at `references/design-system-integration-report-2026-06-16.md`.

**Why:** Minimises drift (Claude Design stays authoritative) while giving developers local token access. The alternative — wiki as design doc hub (Option D) — carries the highest drift risk and maintenance burden. The `brand/flight-deck-identity` branch already structures the product repo correctly for this approach.

**Alternatives considered:** Option A (URL reference only — no local tokens, developers need claude.ai access); Option C (Vercel MCP import pipeline — good enhancement but Vercel-specific, doesn't cover general branding); Option D (wiki as design hub — most duplication, most drift risk).

**Owner:** Enitan.

---

## 2026-06-15 — ExamPilot greenfield brand: "Flight Deck" identity + strategy foundation

**Decision:** Adopted a greenfield brand for ExamPilot, "Flight Deck" (your exam, on instruments). Full package committed to the product repo at `spyglass/brand/` (`BRAND-GUIDELINES.md`, `exampilot-theme.css`, `README.md`, `assets/`) on branch `brand/flight-deck-identity`. Part I (strategy): mission = "give every student sitting an international exam the precision and confidence that used to belong only to those who could afford a private tutor"; vision = "exam readiness is something you can know, not something you hope for"; values = Precision over guesswork + Evidence first; offer = 14-day no-card free trial, cancel anytime, EUR-only plans, consumer-only. Part II (expression): Ink Navy `#0B1A2D` + Signal Lime `#B8F23D` + Instrument Amber + contained Heading Cyan; Geist + Geist Mono; heading-caret-in-aperture mark; typographic, no mascot (Sparky = spark glyph); dark mode as first-class "flight deck at night". Supersedes `exampilot/DESIGN.md` (violet/rose). Token-mapped to the existing Tailwind v4 `@theme` + shadcn for a clean Claude Design handoff. Also seeded into a claude.ai/design project for execution.

**Why:** Differentiates hardest from the two category clichés (pastel "friendly learning" and purple "AI magic"), owns the shared Pilot+Spyglass navigation metaphor, and matches the locked positioning ("know exactly where you stand"). Student-first core with a parent/teacher trust layer fits the B2C2-parent model. The palette is ownable, premium-yet-energetic, and pops on social, which matters under organic-only acquisition. Grounded entirely in the wiki + voice guides; stale `raw/` wiki data (GBP pricing, school licensing, "AI tutor" language) was deliberately rejected in favour of `CLAUDE.md`/voice-guide truth.

**Alternatives considered:** Concept territories "Calm Clarity" (minimal/trust-led, risked feeling under-powered to teens) and "Kinetic Momentum" (gamified, risked undercutting parent/teacher trust). Audience weighting: balanced or parent-first core (rejected; student-first is the winning B2C2-parent pattern). Character: light or full mascot (rejected; typographic protects learning-science credibility). Type: keep Satoshi/JetBrains (retained as fallback) vs Geist (chosen primary). Colour: electric azure/aqua instead of Signal Lime (offered as a swap if lime reads too hot).

**Owner:** Enitan.

---

## 2026-06-14 — QLP synthesizer model: Opus 4.8 for seed, Kimi K2.5 A/B for scale (closes OPEN decision #5, EP-90)

**Decision:** The Pattern Synthesizer (agent 4 of the 5-agent QLP extraction pipeline) runs on **Claude Opus 4.8** for the CIE 9709 Pure 1 seed run, replacing DeepSeek V3.2. **Kimi K2.5** is the designated value-model to A/B against Opus on a held-out set of 9709 templates *before* scaling extraction beyond the seed. Flash-Lite deprecation check (the ticket's P0 sub-task): Gemini 2.5 Flash-Lite is deprecated, hard shutdown 2026-10-16; replacement is `gemini-3.1-flash-lite`.

**Why:** Live research (6 parallel agents, model landscape as of 2026-06-14) established that Pure 1 math is *saturated* across every current reasoning model (all score 80–99% on AIME, far above Pure 1 difficulty), so raw math ceiling is not a discriminator. The synthesizer's real job — reverse-engineering a parameterizable template, encoding mark-scheme logic, grounding distractors in misconceptions, emitting schema-valid JSON — is gated by structured-output reliability, instruction-following, and low hallucination. Opus 4.8 leads on the best proxy for that (GPQA Diamond 93.6%, highest verified) and on structured-output reliability. Seed-run cost is trivial (~$19 for all 50 QLPs at standard rates; cheapest-to-priciest candidate spread is only ~$17), so the foundation is bought on quality, not price. Cost only compounds at scaled extraction (≈10x ratio Opus→Kimi across hundreds–thousands of QLPs) — which is exactly what the Kimi A/B de-risks.

**DeepSeek rejected on merit, not geography:** its JSON mode has a documented "occasionally returns empty content" defect — disqualifying for a schema-bound foundational pipeline. (China hosting and provider-integration lift were both explicitly ruled non-issues by the founder.)

**Alternatives considered:** Gemini 3.5 Flash (stable, ~$7/run — best balanced/cheap pick, but Flash-tier with unconfirmed GPQA and "verbose" output; its eye-catching AIME ~99.7% is the *3 Flash preview* SKU, not 3.5 Flash); Gemini 3.1 Pro (GPQA ~94.3%, ~$9/run — Gemini quality-max, but still preview); Kimi K2.5 as the *primary* (near-frontier, 8x cheaper, exposes `reasoning_content` for the moderator — assigned to the scale A/B instead of the seed); Kimi K2.7 (ruled out — it is K2.7 *Code*, coding-specialized, no math benchmarks, forced always-on verbose thinking).

**Consequences / follow-ups (Linear):** (1) implementation ticket — swap agent 4 (DeepSeek V3.2 → Opus 4.8) + build the Kimi K2.5 A/B harness; (2) migration ticket — move Gemini 2.5 Pro (pipeline agents 1 & 2: Question Parser + Mark Scheme Analyzer) and any Gemini 2.5 Flash-Lite usage off the 2026-10-16 deprecation *before* the seed run (locate Flash-Lite usage in code; pre-stage `gemini-3.1-flash-lite`).

**Owner:** Enitan. EP-90 closed.

---

## 2026-06-14 — Canonical QLPQuestionContext contract: code is canonical (closes OPEN decision #3)

**Decision:** Adopt the implemented `qlp_phase3_contracts.py` `QLPQuestionContext` as the canonical contract, unchanged. It is a thin post-retrieval identity/traceability envelope: `qlp_id`, `qlp_version`, `instance_id`, `reproducibility_seed`, `trace_id`, plus retrieval context (`topic_id`, `subject_code`, `qualification_level`, `exam_board`, `specification_id`, `tier`) plus `targeted_misconceptions`, `evaluation_logic`, `estimated_seconds`. The wiki "fat" contract (template_body, distractor_logic, evaluation_steps, prerequisites, exam_appearances, difficulty_hint, predictive_weight) is rejected — those are QLP *document* fields, not context-envelope fields.

**Why:** A direct code trace of every producer and consumer of `QLPQuestionContext` in `akhanaton/spyglass` settled it. The origin spec (impact report) and the code agree on a thin envelope; only the synthesized wiki article drifted into a content-bearing envelope by pulling fields out of the QLP document schema. Code is ground truth and is already deployed; the runtime composes QLP content separately. Adopting code = zero re-extraction risk for the seed run.

**Contested fields, resolved by the trace:**
- `topic_id` stays Optional. The sole producer (`qlp_runtime_service.build_qlp_question_context`) always sets it, because `retrieve_assessment_payload` already gates on a present topic_id upstream. The only consumer that reads it (promotion lineage) tolerates None. Making it required buys nothing and would break deserialization of already-persisted `qlp_context` blobs.
- Course-context fields (`qualification_code`/`qualification_title`) NOT added. The course-context injection convention is real but lives in the prompt/resolver layer (sourced from the curriculum spec), not on this runtime envelope. Nothing reads them off `QLPQuestionContext`.
- Field names: keep code names (`instance_id`, `targeted_misconceptions`), not the spec variants.

**Consequences:**
- Wiki Spec A (`engineering/backend/qlp-srs-integration.md`) corrected to the canonical contract (done this session).
- Two follow-ups filed in Linear: tier typing hardening (`Optional[str]`→`Literal`); promotion path sets `exam_board` but not `qualification_code`/`title` on promoted ContentItems (retrieval-parity gap).
- Product repo: no code change required to the contract itself. EP-87 (whether a *promoted* QLP renders richly via the live `topic_id` path) remains open — needs a content-render-layer trace, separate ticket.

**Alternatives considered:** Merge the spec's content fields into the contract (rejected — duplicates the QLP document, no consumer needs them inline); make `topic_id` required (rejected — see above).

**Owner:** Enitan. EP-89 closed.

---

## 2026-06-14 — Cambridge IP posture for QLPs adopted (closes OPEN decision #2)

**Decision:** QLPs are transformative parameterised analysis. Student-facing output exercises the same logic patterns with original questions — never verbatim Cambridge text, figures, or mark schemes. This line is adopted as the canonical IP posture.

**Why:** The entire June plan ingests CIE papers. No runbook stated a posture before this. Transformative-use is the defensible line: ExamPilot's output parameterises the underlying mathematical structure, it does not reproduce Cambridge IP. The hard constraint (no verbatim reproduction) also maps cleanly to a moderation criterion.

**Consequences adopted with this decision:**
- Hard reject criterion for Tier-1 moderation rubric: reject any QLP output containing verbatim Cambridge text, figures, or mark-scheme language.
- Marketing copy rule: "built FROM past papers and mark schemes", not "real past paper questions". `marketing/templates/reddit-value-post.md` line 36 flagged for scrub.
- Moderation rubric lives in the product repo (`akhanaton/spyglass`) — criterion must be encoded there before the first real extraction run.

**What would change it:** Legal advice that explicitly contradicts the transformative-use rationale, or a C&D from Cambridge Assessment.

**Alternatives considered:** Full licensing (rejected — cost and timeline incompatible with August launch); abstain from ingesting past papers entirely (rejected — the content layer is the product; abstaining kills the launch).

**Owner:** Enitan. EP-88 closed.

---

## 2026-06-14 — PMC (Projected Mastery Coverage) deferred to post-launch

**Decision:** PMC is deferred to post-launch (Phase 8+). Not in the August MVP. Tracked as Linear EP-121 (Post-MVP). The 593-line spec is kept; implementation waits.

**Why:** PMC forward-projects mastery of unseen QLPs from accumulated per-QLP mastery data + a prerequisite graph. Neither exists in sufficient volume before launch, so any projection would be meaningless. Closes the "open decision" left in the 2026-06-10 QLP go-live entry. Depends on EP-120 (per-QLP mastery tracking, also Post-MVP).

**What would change it:** enough real student interaction data post-launch to make projections meaningful, plus EP-120 shipped.

**Owner:** Enitan

---

## 2026-06-14 — Work-tracking rationalization: Linear is the single actionable surface

**Decision:** Reverse the 2026-06-10 "matrix-stays-tracker, Linear not mirrored" stance. Linear is now the single source of truth for actionable work; the Production Readiness matrix is a status dashboard (flow PASS/FAIL, launch readiness); the Coda mirror is retired. This realigns practice with the three-tool execution model already adopted 2026-05-17 (`references/execution-model.md`).

**Why:** A catch-up audit found work fragmented across four surfaces with no coherent view. 27 of 72 active Linear issues had no project; ~12 P0/P1 launch-blocking *code* items lived ONLY in the matrix with no Linear issue (so invisible from the task board); Coda was a one-way script mirror of the matrix that nobody reads. The matrix's "these blockers live only here, by decision" section had become a visibility hole on the critical path to an immovable August launch.

**Actions taken (all executed, verified):**
- Created Linear **Post-MVP** project; created **EP-94–EP-105** (the matrix-only P0/P1 blockers, Engineering) + **EP-106** (free-beta-end policy decision → blocks EP-22). EP-101/EP-102 = the two QLP code blockers, linked to EP-87/EP-90 as seed-run gates; EP-99→EP-100 sequenced.
- Reassigned all 27 projectless issues (Engineering / Alpha Launch / Post-MVP / Content & Growth + new "YouTube / GEO" milestone). **0 projectless active issues remain** (Alpha Launch 38, Engineering 29, Content & Growth 11, Post-MVP 7).
- Product repo PR `akhanaton/spyglass#618`: matrix "Open Flags / Awareness" section now maps each blocker to its Linear issue; matrix header notes Coda retired; `scripts/coda-sync-test-matrix.mjs` marked DEPRECATED. Coda doc `hWFDV3mysB` left as a frozen snapshot (not deleted).
- Updated memory `project-launch-readiness-flags`; added `project-linear-rationalization`.

**Alternatives considered:** (1) Umbrella Linear issues pointing back to the matrix (rejected — keeps detail in markdown, defeats single-surface goal); (2) keep blockers matrix-only (rejected — the visibility hole was the original problem); (3) keep Coda as a maintained read-view (rejected — no reader; pure sync overhead). YouTube cluster placed in Content & Growth rather than Post-MVP (it is an active GEO channel, gated only on the already-decided production model).

**Owner:** Enitan

---

## 2026-06-13 — Informational pages measured by citation share, not CTR (AI-era); AIO check baked in

**Decision:** Informational content is judged by citation share and brand-search lift, not clicks/CTR — reaffirming `wiki/marketing/seo/seo-strategy.md` GEO point 13. AI Overview presence is the per-query determinant of which KPI applies: AIO present → citation share + GEO optimisation; AIO absent → CTR/title work and clicks (navigational, comparison, niche long-tail). AIO presence is now checked live in two places: `/research-serp` (per-keyword, pre-writing) and `/signal-review` Step 3b (weekly, on top ranking queries).

**Why:** The 2026-06-13 GSC site analysis first benchmarked our 0.8% CTR against a pre-AI 2-4% standard and recommended title rewrites for a 3.8x gain. That ignored AI-Overview suppression (Ahrefs: ~58% click loss to #1; Seer: ~61% on informational queries) and cut against our own re-baselined doctrine. Per-query AIO measurement (DataForSEO SERP) showed presence is mixed and geography-varying: our biggest pages (trigonometry, functions, differentiation) are AIO-suppressed in the UK, while integration, "9709 syllabus", past papers, the paper-code tail, and brand are AIO-free. Pakistan shows fewer AIOs than the UK, so our international audience faces milder suppression than UK-centric studies imply.

**Actions taken:** Corrected the GSC site-analysis report (CTR section + AIO-presence table + revision note). Built `serp_analyzer.py` (DataForSEO SERP: live AIO presence, SERP features, PAA, who-ranks) — resolves the phantom-module gap. Wired it into `/research-serp` Step 2 (measured AIO, not estimated) and `/signal-review` Step 3b (weekly AIO monitoring; flags KPI flips and the "ranking held but clicks fell" pattern). Added the keyword-selection principle to `target-keywords.md` (never gate on ad-volume; a `0` = below planner floor; a Move 37 distribution-arbitrage instance). Updated `connections.md` row 12.

**Still open:** Sibling-skill pointers (`/research-gaps`, `/cluster`, `/priorities`) to the keyword-selection principle, and logging the Move 37 outcome — both deferred pending decision.

**Owner:** Enitan

---

## 2026-06-13 — Keyword research is OS-native; seomachine stays superseded

**Decision:** All keyword research lives in Spyglass OS, not the seomachine repo. This reaffirms the 2026-05-16 supersession ("seomachine is now superseded by Spyglass OS for all ExamPilot marketing work") against an ambiguity that surfaced today. `keyword_volume.py` is the canonical OS keyword-research tool — two modes: lookup (volume + difficulty for a known list) and seed expansion (seed → related-keyword cluster). The never-built `keyword_researcher.py` name is retired.

**Why:** While wiring DataForSEO I inferred the unbuilt keyword-expansion capability "lived in seomachine" and proposed leaving OS tooling lookup-only. The decision log and wiki refute that: seomachine was consolidated into the OS specifically so Teresa can access the flow (she couldn't reach the separate repo; commands were CWD-dependent). Leaving expansion out would have reopened the split-brain the consolidation closed. Building it in the OS completes the job. Standing geography rule baked into the tool: pull worldwide first — CIE 9709 / Edexcel IAL are international exams and a UK lens understates demand ~100x+; cross-reference GSC impressions for the long tail the keyword planner can't see.

**Actions taken:** Built `keyword_volume.py` (lookup + `--seed` expansion via DataForSEO Labs). Repointed `/research-keywords`, `/optimize`, `/landing-research` off the phantom `keyword_researcher.py` to the real module. Fixed the GSC OAuth-rewrite fallout in `signal_processor.py` + `data_aggregator.py` (both gated GSC on the removed `GSC_CREDENTIALS_PATH`). Updated `connections.md` (GWS CLI, GSC OAuth, DataForSEO now live), `seo-analytics-stack.md`, `target-keywords.md`.

**Still open (deferred, not done):** Stale seomachine pointers — `wiki/marketing/growth/marketing-plan.md` still lists seomachine as a live connection; Linear EP-67–73 reference research briefs that physically sit in the old repo (tracked as EP-93). [Update 2026-06-13: the `serp_analyzer.py` phantom is now built — see the CTR/AIO entry above.]

**Alternatives considered:** (1) Keep expansion in seomachine, OS tooling lookup-only (rejected — refuted by the supersession decision and breaks Teresa's access); (2) rename the new module `keyword_researcher.py` to match old references (rejected — it does lookup + expansion, not the full original spec; accurate name avoids overclaiming).

**Owner:** Enitan

---

## 2026-06-10 — Payments processor = Dodo (Stripe references superseded)

**Decision:** Dodo Payments is the processor of record (confirmed; originally selected 2026-05-11). All "Stripe" references across the stack are stale and superseded.

**Actions taken:** Linear EP-22 repurposed from the empty "Stripe Payment" stub → "Dodo Payments — checkout + webhook + subscription integration" (High, engineering). Production Readiness matrix §H5 annotated: processor = Dodo, and flagged that H5 actually covers *Sparx credit-pack* purchases (distinct from the €29/mo subscription model in EP-22), and that EP-41 proposes removing Sparx top-up purchasing — resolve before building.

**Open sub-decision:** Free-beta-end policy (fixed date / 14-day trial / first-N-free) — shapes Dodo checkout urgency.

**Owner:** Enitan

---

## 2026-06-10 — QLP go-live: six decisions from the go-live assessment

Source: `references/qlp-go-live-assessment.md` (2026-06-09, 32-agent assessment) + code trace of `github.com/akhanaton/spyglass` @ commit 2026-04-23 (2026-06-10). Canonical current-state article: `wiki/engineering/backend/qlp-current-state.md`. Two of the six are DECIDED; four are OPEN (recommendation captured, decision pending the named owner).

**1. Launch scope — DECIDED.** August launch gates on Phase 10 exit + 50 moderated CIE 9709 Pure 1 (Algebra) QLPs *retrievable in a live session*; SRS ships at Stage 0/1 (topic-based). SRS Stages 2–4, PMC, per-QLP mastery tracking, Tier 3 synthesis, cache-key migration, and Examiner-as-a-Service taxonomy are explicitly deferred to post-Phase-1-gate.

> **Correction (2026-06-10):** ERI is NOT deferred. The Production Readiness matrix (the canonical launch plan, `docs/operations/PRODUCTION_READINESS_TEST_MATRIX.md`) lists ERI as **P1.5 — Must Verify & Complete Before MVP**: expose the API endpoint (`GET /exam-readiness/...`), surface it on the dashboard/exam-lens page, and validate the formula against real 9709 data. ERI is in MVP scope. What's genuinely deferred is **PMC** (matrix: open decision — likely insufficient data by August) and **per-QLP mastery tracking** (matrix P3). The copy guardrail in decision #6 still applies: surface the score, don't overclaim predictive confidence.
- *Why:* QLP-seeded content is launch-critical; QLP-as-SRS-substrate is not. Every week on the cutover backlog is stolen from the only thing that can fail the launch (seeded, vetted content) against an immovable August Results Day window. Now reflected as canonical wiki state (product-current-state, path-to-revenue, qlp-current-state).
- *What would change it:* serving-path wiring proves larger than the content lift, or seeding slips far enough that there's no content to gate on.
- *Owner:* Enitan.

**2. IP posture for Cambridge-derived QLPs — OPEN (decide before any real-paper extraction).** Recommended line: QLPs are transformative parameterized analysis; student-facing output exercises the same logic patterns with original questions, never verbatim Cambridge text, figures, or mark schemes. Encode as a hard reject criterion in the moderation rubric; scrub marketing copy that implies reproduction ("built FROM past papers and mark schemes", not "real past paper questions").
- *Why:* The entire June plan ingests CIE papers; no runbook currently states a posture. One hour of real legal review is the cheapest insurance on the critical path.
- *Owner:* Enitan + one hour of legal review. **Blocks the first real extraction run.**

**3. Canonical QLPQuestionContext contract — OPEN (one-day decision before SRS/seeding code).** The spec contract and the implemented `qlp_phase3_contracts.py` schema have forked. Recommended: pick one canonical contract (likely a merge — keep traceability fields, add the payload fields the card composer needs), verify the extraction pipeline emits that format so seed data needs no re-extraction, then collapse the wiki to one contract + one backlog.
- *Why:* Seeding against the wrong contract means re-extracting 50 QLPs later. Cheaper to settle the shape first.
- *Owner:* Enitan (eng). Prerequisite: dump the actual model from code and diff against both wiki specs.

**4. FSRS grain — OPEN.** Target is per-QLP FSRS signals; FSRS currently operates at topic level. Decision needed: commit to the per-QLP target and define interim handling if launch ships topic-level (which it will, per #1).
- *Why:* PMC and per-QLP ERI need per-QLP grain (a `spaced_repetition_reviews` schema migration). Not launch-critical, but the target should be recorded so interim choices don't harden into the wrong default.
- *Owner:* Enitan (eng). Can be decided post-launch, but log the target now.

**5. Synthesizer model for the seed run — OPEN (decide before the seed run).** The terminal extraction stage (Pattern Synthesizer) runs on DeepSeek V3.2, the weakest math model in the stack (flagged for P1 upgrade). Decide the model before extracting 50 QLPs.
- *Why:* Re-extracting after a model swap doubles cost and re-triggers Tier 1 moderation. Also run the P0 Gemini Flash-Lite deprecation check and pre-stage the fallback.
- *Owner:* Enitan (eng). **Blocks the seed run.**

**6. No readiness/predicted-grade language until calibration — DECIDED (guardrail adopted).** No "exam readiness", predicted-grade, or "90% predictive confidence" claims in any user-facing or marketing copy until the Oct/Nov 2026 calibration study validates ERI against real exam outcomes. "90% predictive confidence" struck from all copy now. This guardrail bans *overclaiming* (predicted-grade / "90% predictive confidence"), **not** surfacing ERI itself — the Production Readiness matrix requires ERI surfaced in MVP (P1.5). Surface the readiness score with honest framing; withhold the predictive-confidence claim until the calibration study.
- *Why:* ERI's predictive confidence is an unvalidated assertion with zero calibration against actual outcomes. Shipping a grade claim we can't stand behind is both a churn risk and a trust/compliance risk.
- *Owner:* Enitan + Teresa (copy audit pending).

**Alternatives considered (set-level):** Logging all six as ratified (rejected — four aren't decided yet; recording them as decisions would be false). Holding the log until all six resolve (rejected — the two settled ones and the four owners/deadlines are worth capturing now so nothing stalls silently).

---

## 2026-05-21 — Tutor Distribution Flywheel analysis filed (pre-decision)

**Decision:** Comprehensive strategic analysis of a Tutor Distribution Flywheel addition to the marketing plan filed at `references/tutor-flywheel-analysis.md`. No commitment yet. Document is the basis for a future go/no-go decision and seed for a technical specification.

**Why:** International-market tutoring data (Pakistan, UAE, India) suggests tutors are a primary supplementary education infrastructure that competitors structurally cannot see from a UK-domestic vantage point. Worth a real analysis before any plan change. Filing now so the research is durable and the decision can be made with full context later without re-running the work.

**Alternatives considered:** Treating this as a side-channel within existing tutor referral target (status quo). Skipping analysis and committing directly (rejected — too much engineering opportunity cost without validation).

**Owner:** Enitan (per AIOS context). Decision meeting target: close of Phase 0 (end July 2026) after tutor discovery interviews and engineering review.

---

## 2026-05-13 — GitHub MCP over git submodule for second brain

**Decision:** Connect the second brain GitHub repo via GitHub MCP server, not as a git submodule inside Spyglass-OS.

**Why:** Multiple writers (other apps, repos, Enitan, Teresa) and multiple readers. A submodule makes Spyglass-OS manage sync state across machines and tools — overhead that compounds. MCP means Claude queries live content; the sync problem disappears entirely. Submodule is a viable fallback if offline access becomes a requirement.

**Alternatives considered:** Git submodule with post-merge hook; symlink to separate local clone.

**Owner:** Enitan

---

## 2026-05-13 — OS is the desk, wiki is the library

**Decision:** Clear separation between Spyglass OS and spyglass-wiki. OS owns identity, voice, connections, and local config. Wiki owns all business, product, engineering, and operational knowledge. OS reads wiki at session start via `_session_context.md`. No duplication of knowledge between the two systems. OS CLAUDE.md "Knowledge base" section replaced with a live wiki read instruction.

**Why:** Both systems had overlapping control planes — two CLAUDE.md files, two decision logs, two session context concepts. The OS's static Knowledge base paragraph was a stale snapshot of what the wiki maintains dynamically at 117+ articles.

**Alternatives considered:** Merge OS into wiki (rejected — personal identity, voice samples, and per-machine connection config don't belong in a shared knowledge base); add `.claude/context/` distillation layer inside the wiki (rejected — wiki/ is already the distillation of raw/; the OS is already the distillation layer for non-coding sessions).

**Owner:** Enitan

---

## 2026-05-13 — Skills Library / Processes split in Coda

**Decision:** Two separate Coda pages in Spyglass HQ. Skills Library = AI/automation skills only (executable by Claude). Processes = human-followed SOPs. Hard boundary: if a human follows it, it's a process; if Claude runs it, it's a skill. Never mix.

**Why:** Without a home for SOPs, the Skills Library absorbs them and becomes a junk drawer within weeks. A named boundary forces the discipline at input time, not cleanup time.

**Alternatives considered:** Single unified table with a "type" column (rejected — mixing makes filtered views unreliable and blurs the AI-executable contract); SOPs in wiki (rejected — wiki is engineering/product knowledge, not operational runbooks for the team).

**Owner:** Enitan

---

## 2026-05-13 — Spyglass OS as operating layer, not a parallel track

**Decision:** Prioritise getting Spyglass OS to "significant leverage" threshold before using it to deliver other priorities (production readiness matrix, SEO/Growth planning).

**Why:** Treating it as a force multiplier means all subsequent work benefits from it. Running it as a side project means it never reaches the leverage threshold.

**Alternatives considered:** Deliver production readiness matrix first, set up AIOS in parallel.

**Owner:** Enitan

---

## 2026-05-14 — Marketing machine integrated into Spyglass OS

**Decision:** Build the ExamPilot marketing machine as an integrated part of Spyglass OS (commands at `.claude/commands/`, agents at `.claude/agents/`, data in `marketing/`). Not a sub-OS folder, not a separate repo.

**Why:** If marketing lives outside the OS, `/audit` and `/level-up` can't see marketing capabilities, breaking the force multiplier concept. The OS philosophy is that everything flows through the operating layer. Commands at root means they activate from the project CWD. Strategy lives in the wiki; operational rules and templates live in `marketing/context/` and `marketing/templates/`.

**Alternatives considered:** (1) Sub-OS folder with its own CLAUDE.md and skills (rejected: loses skill discoverability, /audit can't see it); (2) Separate repo like seomachine (rejected: fragments the operating layer, duplicates context, requires repo switching).

**Owner:** Enitan

---

## 2026-05-14 — 18-month marketing plan: stage-based KPIs + micro-funnel architecture

**Decision:** Adopted stage-based KPI evolution (Phase 0-3) combined with leading/lagging indicators over AARRR pirate metrics or a single universal north star. Each phase has 1-2 primary KPIs that shift as the business matures. Channel-specific KPIs measured independently against each channel's funnel role. Six additional decisions documented in the plan: Edexcel deferred, no paid ads (permanent), TikTok Phase 2, location SEO Phase 2, product-led SEO Phase 2, pillar+spoke as SEO foundation.

**Why:** 2-person team at pre-revenue stage. Premature optimization (measuring CAC before there are customers) creates noise. Stage gates force discipline: you prove activation before measuring revenue, you prove organic before scaling paid. The micro-funnel (TikTok → Reddit → SEO → AI Search → Website) is the discovery architecture; the B2C macro-funnel (awareness → advocacy) is the lifecycle.

**Alternatives considered:** (1) AARRR pirate metrics from day 1 (rejected: 5+ metrics is too many for early stage, no clear priority when they conflict); (2) Single north star metric throughout (rejected: "MRR" is meaningless at Phase 0, "signups" is meaningless at Phase 3); (3) Channel-agnostic KPIs only (rejected: each channel has a different funnel job, single metric distorts resource allocation).

**Owner:** Enitan & Teresa

---

## 2026-05-15 — Marketing plan v2: operational precision upgrade

**Decision:** Updated marketing plan from v1.0 to v2.0 in place (not a separate document). Key changes: (1) UAE promoted to Tier 1, Egypt demoted to Tier 2 based on verified data and traffic analysis. (2) Monthly demand gen/acquisition pulsing tied to exam calendar replaces static 70/30 phase split. (3) Formal phase gate scoring with weighted must-pass criteria replaces checklists. (4) Leading/lagging tags on every KPI. (5) Explicit failure definitions per phase. (6) Product-led SEO "bridge content" (examiner reports, curriculum analysis) starts Phase 0-1 instead of waiting for student data. (7) Programmatic SEO noindex-until-enriched protocol. (8) TikTok campaigns detailed with weekly themes, Results Day pre-production strategy. (9) Brevo wiring specified as Phase 0 first two weeks. (10) Exam board expansion sequencing formalized (CIE 0580 before Edexcel IAL for IGCSE-to-A-Level pipeline). (11) Competitive positioning section added. (12) Existing ~8 published articles factored into Phase 0 baseline.

**Why:** V1 was strategically sound but operationally vague in places. Phase gates were checklists without decision rules. Demand gen/acquisition split was static when the exam calendar naturally creates monthly pulsation. Geography data had unverified claims (Egypt "#1 IGCSE" from 2014). KPIs lacked leading/lagging classification, making it unclear what to act on daily vs review monthly. V2 is the same strategy with sharper instrumentation.

**Alternatives considered:** (1) Write v2 as a separate document and compare (rejected: creates two competing sources of truth); (2) Selective cherry-picking from v2 research (rejected: the improvements are interconnected -- phase gates depend on KPI tags, which depend on failure definitions).

**Owner:** Enitan

---

## 2026-05-15 — MRR projections revised upward with full 9709 expansion model

**Decision:** Replaced the EUR 1,500 Phase 3 MRR target with EUR 5,000-9,000 (300-500 paying users). Added a month-by-month growth projection model (Section 5.8) that accounts for each CIE 9709 unit launch expanding the addressable keyword surface, improving trial-to-paid conversion (15% single-unit → 22% multi-unit), and reducing churn (8-10% → 5-7%). Blended MRR per user is EUR 17-19 based on tier mix weighted toward quarterly/annual in price-sensitive international markets.

**Why:** The original EUR 1,500 target implicitly assumed ~75-100 paying users (from 500 total trials at 15% conversion). It did not account for the multiplicative effect of covering five 9709 units: each unit is a new acquisition channel (new keywords, new student segments, new Reddit questions), and multi-unit coverage improves both conversion and retention. With 130-180+ indexed pages by Nov 2027, the SEO footprint is 3-4x larger than a Pure-1-only model. 500 paying users is a stretch for Nov 2027 (more likely Q1 2028) but 300-350 is realistic at the moderate scenario.

**Alternatives considered:** Keeping EUR 1,500 as a conservative floor (rejected: it's so far below what the pricing math actually produces that it would give false comfort at Phase 3 if hit but still far below potential).

**Owner:** Enitan

---

## 2026-05-15 — No paid advertising, ever

**Decision:** ExamPilot will not run paid ads of any kind across any phase. This is a permanent strategic decision, not a deferral. All acquisition is organic: SEO, Reddit, TikTok organic content, email, and direct outreach. If a growth ceiling is hit in Phase 3+, the response is product expansion (new exam boards, geographies, subjects) and deeper organic channel investment.

**Why:** Organic acquisition builds compounding assets (content, community authority, email list, brand reputation). Paid acquisition stops the moment you stop paying. For a 2-person team with limited budget and a long-horizon content strategy, organic is the only channel that scales without linear cost increases.

**Alternatives considered:** Paid ads deferred to Phase 3 conditional on organic benchmarks (rejected: a conditional deferral creates ambiguity and temptation; a clean no removes the decision from the table permanently).

**Owner:** Enitan

---

## 2026-05-15 — SEO analytics stack: DataForSEO as core programmatic layer

**Decision:** Build the SEO intelligence loop on DataForSEO API + GSC API + GA4 + PostHog, synthesized by Claude via a `/strategy-review` command. Reject SEO-Stack.io. Deprecate Ubersuggest (redundant). Keep Mangools until DataForSEO `keyword_researcher.py` module is built and validated (Phase 2). Add Ahrefs Webmaster Tools (free) immediately for site audit coverage.

**Why:** DataForSEO is pay-per-call ($12-28/mo at startup scale) and covers everything Ahrefs Lite ($129/mo) and SEMrush Pro ($140/mo) provide programmatically — rank tracking, keyword research, competitor SERP data, backlink data, on-page NLP analysis. The AI querying layer SEO-Stack sells is what Claude in the OS already does, with full business context. The virtuous loop (DataForSEO → GSC → GA4 → PostHog → Claude → action) closes the feedback chain from keyword opportunity through to trial conversion and retention by source. Each layer answers a different question; together they surface decisions, not just reports.

**Alternatives considered:** SEO-Stack.io (rejected: first-party data only, redundant with DataForSEO, founder listing business for sale — continuity risk, MCP server unconfirmed); Ahrefs Lite (rejected: 4x cost, no features needed until Phase 3); SEMrush Pro (rejected: same cost issue, stronger on PPC which is not a Phase 0-2 priority); Mangools kept short-term as the human-facing keyword research UI until programmatic layer is validated.

**Owner:** Enitan

---

## 2026-05-15 — GTM Engineering signal architecture adopted

**Decision:** Added GTM Engineering as Enitan's formal function within Spyglass OS. Built a B2C-adapted signal architecture covering first-party (PostHog behavioral), second-party (Reddit community), and third-party (GSC/DataForSEO SEO + exam calendar) signals. Activation chain: PostHog → scored signal → Coda Signals table (operational) + Attio CRM (contact enrichment) → Brevo sequences. Phase 0 is command-driven (`/signal-review`); Phase 1 automates Attio enrichment and Brevo sequence triggers once those APIs are connected.

**Why:** The Marketing Machine (content, community execution) generates demand but has no intelligence layer to track who is paying attention, how engaged they are, or when they're ready to convert. A signal architecture closes the loop: every piece of content we produce, every Reddit post we answer, every blog article we publish — the behavioral response feeds back into a score that routes the right action to the right person at the right time. Adapted from B2B intent-signal architecture (workflows.io) for a B2C edtech context — no CRM deals, no SDR sequences, student behavioral signals instead of firmographic data.

**Alternatives considered:** (1) Integrate signals into the Marketing Machine only (rejected: Marketing Machine is Teresa's content/community domain; signal scoring and CRM enrichment are engineering concerns — clean separation avoids coordination friction); (2) Start fully automated from day 1 (rejected: no conversion data yet to validate scoring weights; premature automation fires wrong triggers automatically — worse than manual).

**Owner:** Enitan

---

## 2026-05-15 — Reddit tool stack: Syften + RedShip

**Decision:** Adopt Syften (€40/mo Standard) for brand/competitor monitoring and RedShip ($19/mo Starter) for Google-ranking thread discovery and reply drafting. Combined ~EUR 57/month. Activate F5bot (free) in Phase 0 to validate subreddit volume before spending. Add RedShip in Phase 1 ahead of Results Day.

**Why:** No single tool covers all requirements (subreddit monitoring + Google-rank detection + brand monitoring + reply drafting + manual-post-only workflow) at under EUR 80/mo. Syften is the strongest standalone monitoring tool with confirmed Reddit API compliance. RedShip is the only tool in this price range with an explicit weekly Google-ranking scan — finding threads that already rank on page 1 and staying in them compounds far longer than chasing new viral posts.

**Alternatives considered:** ReplyAgent (rejected: proxy accounts, incompatible with karma-building strategy); Redreach (rejected: DM automation creates ban risk, pricing opaque); ReplyDaddy (close but BYOK API costs push effective price to $69-99/mo, early-stage longevity risk); Brand24 (overkill, worse Reddit granularity at higher cost); SubHunt (watch list — similar Google-rank feature to RedShip at $12/mo but insufficient third-party validation). GummySearch is dead (shut down Nov 2025).

**Owner:** Enitan

---

## 2026-05-15 — /capture skill: OS↔wiki ingest pipeline automation

**Decision:** Built `/capture` as an AI-assisted skill (L2 autonomy, Bike Method Phase 1) that collapses the 4-step OS↔wiki capture pipeline — classify destination, draft in correct template, commit via gh api, lint + surface issues — into one command with a human review gate before every commit.

**Scoped via 3Ms Method interview:**
- Trigger: Enitan runs `/capture` with content (paste, file path, URL, or description)
- Data sources: input content + AGENTS.md (wiki conventions) + wiki templates
- Transformations: content → classified destination → drafted article → committed file → lint report
- Decision points: OS vs wiki? / which template? / lint issues auto-fixable or needs human?
- Destination: wiki article or OS file + optional `decisions/log.md` entry + `_session_context.md` update prompt
- Autonomy: L2 — AI drafts, human reviews and approves before any commit
- KPI: Time from "I want to capture this" to "lint-clean and committed" — target under 5 min (from ~15-30 min)

**Why:** The capture pipeline was a repeating attention tax on every useful piece of information encountered. At 3+ occurrences per week, the friction was real enough to cause skipped captures. The wiki cannot grow as a living knowledge system if ingestion is expensive.

**Alternatives considered:** Sub-agent for full pipeline (rejected: L4 too high for first build, no validation baseline yet); prompt template only (rejected: doesn't solve CWD-switching friction or lint parsing); local wiki clone for lint (rejected: machine-specific path, breaks for Teresa). All operations run via `gh api` — no local clone dependency. Phase 2 (auto-commit high-confidence types) available as an explicit edit to `bike-method-phase` once Phase 1 is validated.

**Owner:** Enitan

---

## 2026-05-16 — SEO write pipeline ported from seomachine into Spyglass OS

**Decision:** Ported the full blog article write pipeline from the seomachine repo into Spyglass OS, replacing the stub `/write-article` command with a proper skill and 4 sub-agents. Updated `references/voice-house.md` from a placeholder to the full ExamPilot brand voice guide.

**What was built:**
- `.claude/skills/write-article/SKILL.md` — 6-step write skill: pre-write confirmation, full article structure (GEO-first, APP formula, Key Takeaways, mini-stories, contextual CTAs, FAQ, conclusion), guardrails scrub pass, 4 post-write agents, quality gate, save + report
- `agents/seo-optimizer.md` — keyword density, heading structure, GEO compliance audit
- `agents/meta-creator.md` — 3 meta title + 3 meta description options with scoring patterns
- `agents/internal-linker.md` — passage-level link insertion with anchor text rules
- `agents/content-quality.md` — 5-dimension inline scorer (Voice 30%, Specificity 25%, Structure 20%, SEO 15%, GEO 10%), threshold routing
- `references/voice-house.md` — full ExamPilot brand voice: 5 pillars, tone by content type, messaging framework, terminology table, formatting standards, CTAs, what we never do

**Why:** The seomachine repo had the full execution layer; Spyglass OS had context files but no runnable write pipeline. Porting gives the OS the ability to go from research brief to reviewed draft in one command, with quality scoring built in.

**Alternatives considered:** Keep write pipeline in seomachine and call cross-repo (rejected: CWD friction, breaks Teresa's access); rebuild from scratch (rejected: seomachine's agent architecture was already validated).

**Owner:** Enitan

---

## 2026-05-16 — Python quality scorer and /pre-write skill added

**Decision:** Ported the 3-module Python quality scorer from seomachine and created a new `/pre-write` skill for Sanity CMS content scaffolding.

**Python scorer (`marketing/data_sources/modules/`):**
- `readability_scorer.py` — Flesch/Kincaid + structure analysis; targets Grade 8-10 / Flesch 60-70; graceful fallback if `textstat` not installed
- `seo_quality_rater.py` — 6-dimension SEO rating with ExamPilot defaults (1800-word min, 20-word sentence target, Cambridge/Pearson authority links)
- `content_scorer.py` — 5-dimension composite scorer; ExamPilot additions: banned brand phrases in Humanity scoring; exam codes (9709/12, WMA11, syllabus topic numbers) boosting Specificity; YAML frontmatter parsing in `main()`
- `requirements.txt` updated: added `textstat>=0.7.3`
- `write-article/SKILL.md` Step 5 updated: Python scorer is now primary; inline content-quality agent is fallback

**`/pre-write` skill (`.claude/skills/pre-write/SKILL.md`):**
- 5-step flow: classify content type → plan structure → build Sanity JSON scaffold → anti-regression checklist → save to product repo
- Reads `integration.json` as gold standard before every scaffold
- 10-type content taxonomy with folder mappings; full Sanity block type reference
- Writes to `/Users/enitan/Documents/Projects/spyglass/scripts/content/[folder]/[slug].json`

**Why:** The inline content-quality agent can't do Flesch scoring. The Python scorer gives real readability data. The /pre-write skill fills the gap for product content (topic pages, hub pages, feature pages) which previously required manual JSON construction.

**Alternatives considered:** Keep only inline scoring (rejected: loses Flesch accuracy, rhythm analysis); build Python scorer as external CI step only (rejected: more valuable in-session where Claude can act on results immediately).

**Owner:** Enitan

---

---

## 2026-05-16 — Full seomachine feature set ported into Spyglass OS

**Decision:** Ported every applicable feature from `akhanaton/seomachine` into Spyglass OS across three commits (`7e0af12`, `b50e66e`, `d61fadb`). 63 new files, ~15,500 lines. seomachine is now superseded by Spyglass OS for all ExamPilot marketing work.

**What was ported (summary):**

*Commands (14 new → 24 total):* /article, /rewrite, /optimize, /analyze-existing, /scrub, /research-serp, /research-gaps, /research-trending, /research-topics, /research-ai-citations, /priorities, /repurpose, /content-calendar, /cluster, /landing-research, /landing-write, /landing-audit, /landing-competitor

*Post-write agents (9 new → 12 total):* content-analyzer, editor, headline-generator, keyword-mapper, performance, cluster-strategist, cro-analyst, landing-page-optimizer

*Python modules (15 new → 21 total):* content_scrubber, keyword_analyzer, search_intent_analyzer, content_length_comparator, opportunity_scorer, competitor_gap_analyzer, diagram_generator, google_analytics, data_aggregator, article_planner, landing_page_scorer, above_fold_analyzer, cta_analyzer, trust_signal_analyzer, cro_checker

*Skills (17 new → 25 total):* seo-audit, copywriting, email-sequence, schema-markup, marketing-psychology, analytics-tracking, copy-editing, ab-test-setup, signup-flow-cro, onboarding-cro, paywall-upgrade-cro, free-tool-strategy, page-cro, form-cro, popup-cro, launch-strategy

*Context files (4 new):* target-keywords.md, internal-links-map.md, competitor-analysis.md, ai-citation-targets.md

**What was deliberately excluded:**
- `wordpress_publisher.py` + /publish-draft + /landing-publish — ExamPilot uses Sanity CMS, not WordPress
- `engagement_analyzer.py` — requires GA4 custom events; ExamPilot's GA4 is pageview-only
- `landing_performance.py` — requires conversion tracking not yet implemented
- `/paid-ads` skill — permanent no-paid-ads decision (logged 2026-05-15)
- Podcast-specific content (Castos references) — not applicable

**Why:** seomachine was built for ExamPilot but maintained as a separate repo, creating a split-brain problem — Teresa couldn't access it, commands were CWD-dependent, and the AIOS had no awareness of the full capability set. Consolidating into Spyglass OS gives both users access to the full marketing machine under one roof.

**Owner:** Enitan

---

## 2026-05-16 — Continuous improvement adopted as core OS principle

**Decision:** Adopted continuous improvement as a core operating principle of Spyglass OS. Every repeatable function follows a three-step loop: Capture (inputs + outcomes), Review (at defined cadence), Adjust (change parameters, log with data). Created `references/continuous-improvement.md` (philosophy reference) and `/tune` skill (monthly review ritual). Added to CLAUDE.md as a foundational section alongside the 3Ms framework. All initial parameters across the OS are now explicitly labeled as estimates subject to data-backed adjustment. Linear: EP-51.

**Why:** The GTM Engineering signal architecture already embeds this pattern (weights are "initial estimates, adjust after 8-12 weeks"). Extending it to every OS function -- content, SEO, support, product, X -- creates a system that gets measurably better each month. Without this, parameter settings fossilize and drift from reality. With it, each monthly `/tune` cycle narrows the gap between what we assume and what the data shows.

**Alternatives considered:** Ad hoc improvements as needed (rejected: leads to inconsistent attention, some functions improve while others stagnate); quarterly reviews only (rejected: too slow for early-stage where conditions change weekly); automated parameter adjustment (rejected: premature, Phase 1 is human-approved adjustments only).

**Owner:** Enitan

---

## 2026-05-16 — Build-in-public on X integrated into Spyglass OS

**Decision:** Added X (Twitter) build-in-public as a new channel in Spyglass OS. Created `/write-x` skill (pulls from decisions log, Linear, PostHog, git, or freeform input), strategy reference, two templates (x-post, x-thread), and updated 7 existing files (channel playbooks, audience segments, funnel strategy, repurposing playbook, `/repurpose` command, `/weekly-pulse` command, connections.md). Postiz Standard ($29/mo, already planned for TikTok) handles scheduling. Incremental cost: $0. Enitan starts posting; Teresa joins when `voice-teresa.md` is populated with real writing samples. Full strategy in `references/x-build-in-public-strategy.md`. Linear: EP-50.

**Why:** Build-in-public on X serves a different audience (founders, indie hackers, edtech builders) than the student micro-funnel. It builds founder credibility, creates a launch-day amplification audience, and opens doors to advisors and partnerships. Research shows: 15-25% conversion from engaged X followers at SaaS launch, 6-month timeline to build launch-ready audience. Starting now (6 months before Phase 1 soft launch) is correctly timed. X is a parallel credibility channel, not a replacement for any student-facing channel.

**Alternatives considered:** Brand account only (rejected: personal accounts get 5-10x more engagement); delay until Phase 2 with TikTok (rejected: 6-month audience-building lead time means starting now is optimal); full automation pipeline (rejected: Phase 0 is manual copy-paste to Postiz, automation comes after n8n is wired in EP-49).

**Owner:** Enitan (infrastructure + posting), Teresa (posting, after voice file populated)

---

## 2026-05-16 — Spyglass OS full coverage assessment: gaps identified and prioritised

**Decision:** Completed a research-backed audit of Spyglass OS coverage across all functions. Two critical gaps identified that must be fixed before the first paid user: (1) involuntary churn is undocumented in wiring — ChurnWard ($29/mo, Dodo Payments integration confirmed) to be added; (2) no production observability — Sentry Team ($26/mo) to be added. Three strategic additions with outsized returns: WhatsApp via AiSensy for Tier 1 markets (UAE 85.8% penetration, India 500M+ users), student outcome data collection (the product moat — must collect from the first exam cohort), and n8n for event-driven activation chain (trial → Attio → Brevo → Discord). Full assessment in `references/os-coverage-assessment.md`. Linear: EP-49.

**Why:** Marketing machine is strong. Revenue operations and production observability have no wiring. Student outcome data is the single most defensible competitive advantage and has a one-year collection window tied to the exam calendar — missing the first cohort means waiting 12 months. WhatsApp is not optional for Pakistan/UAE/India markets; it is the primary communication channel in those geographies.

**Alternatives considered:** Add more marketing tooling (rejected: already deep coverage); full help desk / NPS infrastructure (rejected: overkill at 100 users, confirmed by external benchmarks); Zapier over n8n (rejected: per-operation pricing compounds at scale, n8n is flat).

**Owner:** Enitan

---

## 2026-05-16 — Product owner OS layer: thin infrastructure, not a marketing-scale build

**Decision:** Build a minimal product owner layer in Spyglass OS — ~15% the size of the marketing infrastructure. Two Tier 1 items now (Linear MCP wiring + `/backlog-review` command; PostHog extended to `/product-pulse`). Four Tier 2 items at Phase 1 (`templates/prd.md`, `/spec` command, `/product-review` ritual, Coda Product Board view). Nothing in Tier 3 until 200+ users. Full assessment in `references/product-owner-strategy.md`. Linear: EP-47.

**Why:** Marketing runs continuously and in parallel — deep infrastructure pays. Product decisions at pre-launch are serial, low-frequency, and owned by one person. The risk isn't missing tooling; it's not having a fast path from signal → decision → shipped. Over-engineering creates overhead with no ROI until paying users generate real feedback.

**Alternatives considered:** Full product OS parity with marketing machine (rejected: wrong stage, wrong cadence, wrong size team); no product infrastructure at all (rejected: Linear is invisible to the OS today — that gap has a real cost).

**Owner:** Enitan

---

## 2026-05-16 — Customer support: thin insight-capture layer, not a support operation

**Decision:** Build a purposeful-but-thin customer support layer: Discord added to `connections.md`, `templates/support/` folder (6 templates), Coda support log table, and a `/feedback-digest` command. Phase 1 adds PostHog in-app feedback surveys and Attio wiring. No help desk, no NPS, no FAQ, no ticketing system. Full assessment in `references/customer-support-strategy.md`. Linear: EP-48.

**Why:** At alpha (100 students), support volume will be 3–8 contacts/week. The risk isn't operational overwhelm — it's losing the insight from early conversations. Framing support as user research determines the right infrastructure: optimise for insight capture, not ticket resolution. The `/feedback-digest` command is the lever — it turns every support touchpoint into a product intelligence input.

**Alternatives considered:** Help desk tooling (Intercom/Zendesk — rejected: overkill until 500+ users with volume exceeding what two people can handle conversationally); NPS surveys (rejected: meaningless at alpha, no reliable baseline); FAQ pre-built (rejected: let the Coda log tell you what to write, don't guess).

**Owner:** Teresa (operations), Enitan (tooling)

---

## 2026-05-16 — OS structural audit: skills promoted to canonical layer, duplicates resolved

**Decision:** Ran a full coherence audit of Spyglass OS after the seomachine port. Four issues identified and fixed in commit `f6ab25c`:

1. **Skills are now the canonical execution layer.** 7 commands that existed only in `.claude/commands/` (scrub, content-calendar, research-topics, research-gaps, research-keywords, research-serp, landing-competitor) were promoted to proper `.claude/skills/{name}/SKILL.md` files with bike-method-phase frontmatter and 3Ms attribution. The `write-article` command was deleted — the skill was already a strict superset (adds APP formula, Python scorer, editor agent). 16 commands remain, all genuinely command-only with no skill twin.

2. **3 agents relocated.** `content-analyzer`, `cro-analyst`, and `landing-page-optimizer` were incorrectly nested under `.claude/skills/write-article/agents/` during the seomachine port. All three run after `/landing-write`, not `/write-article`. Moved to `.claude/agents/` (top-level).

3. **Hardcoded machine path fixed.** `/pre-write` skill hardcoded `/Users/enitan/Documents/Projects/spyglass/scripts/content/` in 4 places, breaking Teresa's access entirely. Replaced with `$SPYGLASS_PRODUCT_REPO` env var with a setup block at the top of the skill.

4. **connections.md row 8 corrected.** Entry said "Shared skills | Coda | mcp" — skills never moved to Coda. Updated to reflect reality: shared via `akhanaton/spyglass-os` GitHub repo via git clone / gh cli.

**Why:** The seomachine port added 63 files in 3 commits without a structural review pass. The command/skill duplication created maintenance drift risk (update the skill, command stays stale) and ambiguity about which implementation runs. Skills are the right canonical layer: they have discoverability metadata, phase tracking, and work regardless of CWD — the exact properties that make them shareable with Teresa.

**Alternatives considered:** Commands as canonical, delete duplicate skills (rejected: commands are the seomachine pattern we moved away from; loses bike-method-phase metadata and trigger-word discoverability); split commands/skills by role — commands for operational pipelines, skills for advisory (rejected: introduces new abstraction the OS doesn't support, most capabilities are operational anyway).

**Owner:** Enitan

---

## 2026-05-16 — Premium positioning validated: market large enough, pricing confirmed, channel gaps identified

**Decision:** Confirmed ExamPilot's premium positioning (single EUR price, no regional adjustment, targeting the segment that can afford it in every market). The addressable market is verified as large enough. Marketing channel mix has identified gaps that need addressing in a future session.

**Key findings:**
- TAM: 250,000-350,000 CIE + Edexcel IAL maths students/year (EUR36M-50M at annual pricing)
- ~95% of CIE students globally attend private/international schools — CIE IS the premium segment
- EUR29/month = 0.5-17% of annual school fees across all target markets; equivalent to 1-2 hours of tutoring
- Dodo Payments confirms support for all target markets (Nigeria, Pakistan, UAE, Malaysia, Singapore, etc.)
- No regional pricing adjustment needed — even Pakistan/Nigeria's top private school families can afford it

**Channel misalignments identified (modifications pending):**
1. Reddit should be repositioned as SEO/AI citation engine (not direct acquisition for premium international segment)
2. No parent-facing acquisition path exists (parent is the economic buyer in most target markets)
3. No school/teacher partnership model (one school = 50-200 students)
4. Discord should be deprioritized in favour of WhatsApp Communities (dominant in South Asia, Middle East, West Africa)
5. TikTok needs region-specific content (not UK-focused) — verified as THE platform for 16-18s in all target markets
6. Dual voice strategy needed (student-facing casual + parent-facing trust-building)
7. Postiz covers TikTok/X but NOT WhatsApp/Facebook Groups — WhatsApp Business App (free) covers Phase 0; Wati (~$30/month) for Phase 1

**What was NOT decided:** How and when to modify the marketing plan. Research saved to wiki (`wiki/marketing/target-market-analysis.md`) for future implementation session.

**Why:** Needed to verify the strategic assumption that a premium-only position wouldn't limit growth. Data confirms the market is large enough. The finding that CIE ≈ private school globally means we are not excluding anyone by pricing — we're just naming our natural audience.

**Alternatives considered:** Regional pricing (rejected by strategic preference — complexity, brand dilution, and the target segment can afford it); broader subject coverage to increase TAM (not rejected, but sequenced after 9709 is proven); lower price to capture expanding middle-class CIE segment in Pakistan/Nigeria (rejected — focus on who can afford it now, revisit only if premium segment proves insufficient).

**Owner:** Enitan

---

## 2026-05-16 — Build-in-public extracted to dedicated sub-OS

**Decision:** Extracted the build-in-public on X workstream from `marketing/` into a new top-level sub-OS `build-in-public/`. Previously, X infrastructure was spread across `references/x-build-in-public-strategy.md`, `marketing/templates/x-post.md`, `marketing/templates/x-thread.md`, and X sections inside three `marketing/context/` files (`channel-playbooks.md`, `audience-segments.md`, `funnel-strategy.md`).

New structure:
- `build-in-public/references/x-strategy.md` (moved from `references/x-build-in-public-strategy.md`)
- `build-in-public/templates/x-post.md`, `x-thread.md` (moved from `marketing/templates/`, save paths updated)
- `build-in-public/context/channel-rules.md`, `audience.md`, `funnel.md`, `repurposing-rules.md` (extracted from `marketing/context/` files, which now have one-line pointer stubs)
- `build-in-public/pipelines/outreach/` (new output folder — X drafts no longer go to `marketing/pipelines/outreach/`)

Skills/commands updated: `write-x/SKILL.md` (8 path edits), `repurpose.md` (3 edits), `tune/SKILL.md` (2 edits), `weekly-pulse.md` (pipeline scan fix), `CLAUDE.md` (`build-in-public/` added to "Where things live"). `marketing/` is now purely ExamPilot student-facing.

**Why:** Build-in-public on X was placed inside `marketing/` by path-of-least-resistance when the feature was first built. But by a 5-criteria workstream test (different goal, different audience, different KPIs, different voice, different cadence) it qualifies as a second workstream. The X strategy doc itself states: "It does NOT directly convert students." Keeping it in `marketing/` causes: `/weekly-pulse` conflating student funnel and builder metrics; `channel-playbooks.md` mixing incompatible audiences; future `/tune` parameter drift between workstreams. The workstream test that identified this is now documented in `EXPANSIONS.md`.

**Alternatives considered:** Leave in `marketing/`, add a comment (rejected: cost compounds as X content grows; a half-committed structure is worse than a clean one); partial extract — move only leaf files, leave context sections in `marketing/context/` (rejected: still requires reading two locations to understand the X channel, defeating the purpose).

**Owner:** Enitan

---

## 2026-05-17 — Marketing plan v3.0: channel realignment from target market analysis

**Decision:** Updated marketing plan from v2.0 to v3.0 based on target market analysis (`wiki/marketing/target-market-analysis.md`). The analysis validated premium positioning (CIE = 95%+ private school overlap, EUR29/month = 0.5-7% of school fees) but identified 7 channel misalignments. Six sub-decisions documented below.

**Sub-decisions:**

1. **Reddit repositioned from direct acquisition to SEO/AI citation seeding engine.** P0-P1 direct acquisition target reduced from 15-25 to 5-10 students. Primary role is now indexable content that ranks on Google and gets cited by AI tools. Subreddit priority reordered: r/CambridgeInternational (primary), r/alevel (secondary), r/6thForm (tertiary).

2. **Parent acquisition added as primary channel.** Facebook Groups (COALI 100K+ members, CIE parent communities), parent WhatsApp groups, "For Parents" landing page, parent email sequence in Brevo. Parent is the economic buyer in Tier 1 markets (Pakistan, UAE, Nigeria, Malaysia). New voice guide: `references/voice-parent.md`.

3. **School/teacher B2C2B partnership model added.** Teachers get free access and progress dashboard. They recommend to students/parents. Students purchase individually at consumer price. Not B2B -- no school licensing or institution pricing. New voice guide: `references/voice-teacher.md`. B2B prohibition in voice-house.md amended to: "No B2B school licensing or institution pricing. Consumer-only purchase model. School/teacher content uses referral-partner framing (B2C2B)."

4. **Discord demoted to secondary; WhatsApp Communities promoted.** CIE students in South Asia, Middle East, and West Africa are on WhatsApp, not Discord. WhatsApp has 100+ active student study groups in Pakistan alone. WhatsApp Business App (free) at Phase 0, Wati (~EUR30/month) evaluated at Phase 1.

5. **TikTok updated for region-specific content.** GST-optimized posting times (4pm-9pm GST for Pakistan/UAE after school). No UK slang. Universal exam identifiers (paper codes, topic names). Urdu subtitle consideration for Pakistan content (P2). Regional hashtags added.

6. **Growth projections not revised upward.** School partnerships are not modeled in projections until Phase 2 review when real conversion data exists. Follows OS principle that initial parameters are estimates requiring data-backed adjustment.

**Structural decisions:**

- Parent acquisition and school partnerships stay inside `marketing/` as channels, not sub-OSes. Both fail the EXPANSIONS.md workstream test (1/5 criteria -- only "different voice"). Creating sub-OSes for channels that share the same goal, KPIs, and cadence adds overhead without benefit for a 2-person team.
- Three new voice guides: voice-parent.md (parent-facing), voice-teacher.md (teacher/school-facing), voice-house.md amended for multi-audience awareness.
- P0-P1 student acquisition target increased from 40-70 to 50-95 through new channels.
- Five new GTM signals added: WhatsApp community join, WhatsApp broadcast click, Facebook Group mention, teacher referral click, school cohort signup.

**Why:** The marketing plan v2.0 was built before the target market analysis confirmed that CIE is essentially a private/international school product. Channel mix was optimized for UK domestic students (Reddit, Discord) rather than international private school students and their parents (WhatsApp, Facebook Groups, school partnerships). The micro-funnel architecture (TikTok -> Reddit -> SEO -> AI Search -> Website) remains correct for students; a parallel parent funnel is added alongside it.

**Alternatives considered:** (1) Create sub-OSes for parent acquisition and school partnerships (rejected: fails workstream test, adds management overhead); (2) Revise growth projections upward immediately (rejected: no conversion data for new channels yet); (3) Remove Reddit entirely from P0-P1 targets (rejected: overcorrection, Reddit still generates some organic direct interest); (4) Remove B2B prohibition entirely (rejected: B2C2B is not B2B, the prohibition protects against scope creep into enterprise sales).

**Execution completed:** All 6 waves implemented across 2 sessions. 19 OS files updated/created, 10 wiki articles updated, targeted lint PASS (4 minor issues fixed). Stale reference sweep confirmed zero remaining old targets, old B2B language, or Discord-as-primary references.

**Files touched (OS):** decisions/log.md, references/voice-parent.md (new), references/voice-teacher.md (new), references/voice-house.md, marketing/strategy/marketing-plan-2026-2027.md, marketing/context/audience-segments.md, marketing/context/content-standards.md, marketing/context/channel-playbooks.md, marketing/context/funnel-strategy.md, marketing/gtm-engineering/signal-registry.md, marketing/gtm-engineering/scoring-model.md, marketing/gtm-engineering/trigger-playbook.md, connections.md, CLAUDE.md, references/continuous-improvement.md, .claude/skills/launch-strategy/SKILL.md, .claude/agents/outreach-crafter.md, .claude/commands/landing-write.md, .claude/skills/free-tool-strategy/SKILL.md, .claude/skills/write-article/SKILL.md, marketing/templates/blog-article.md, marketing/references/launch-playbook.md, references/os-coverage-assessment.md.

**Wiki articles touched:** marketing/growth/marketing-plan.md, marketing/growth/gtm-engineering.md, marketing/growth/marketing-machine.md, marketing/INDEX.md, business/competitive/go-to-market.md, business/INDEX.md, product/strategy/beta-acquisition.md, product/INDEX.md, ai-automation-os/marketing-os/marketing-os-overview.md, _session_context.md.

**Skills identified (spec only, build via `/level-up`):** /write-whatsapp, /write-parent, /school-outreach.

---

## 2026-05-17 — LinkedIn added to build-in-public sub-OS, Teresa as primary voice

**Decision:** Added LinkedIn as a second channel inside `build-in-public/`, with Teresa as the primary (and currently only) author. LinkedIn is not a mirror of X — it is the same source material with a different frame: X = founder confession (peer-to-peer), LinkedIn = educator insight (professional authority). Incremental cost: $0 (Postiz Standard already covers LinkedIn).

**Why:** LinkedIn serves the B2C2B acquisition model directly. The teacher outreach already planned (channel-playbooks.md) is cold without a content warm-up layer. A teacher who has read 10 of Teresa's posts on CIE exam prep before receiving a DM is already half-sold. Teresa's educational background gives her natural authority with the teacher/parent audience on LinkedIn — the same authority that Enitan has with the indie hacker audience on X.

**Structural rationale:** LinkedIn sits inside `build-in-public/` (not `marketing/`) because the content source is the same as X — decisions log, milestones, product progress — just reframed. The student-facing content in `marketing/` is structurally incompatible. LinkedIn fails the sub-OS workstream test (only 2/5 criteria: different audience, different voice) so it stays as a second channel within the existing sub-OS.

**What was built:**
- `build-in-public/references/linkedin-strategy.md` — Full strategy: WHY, audience profiles, content pillars, angle adaptation rule, outreach integration, format guide, algorithm rules, anti-AI rules, timeline
- `build-in-public/templates/linkedin-post.md` — Post template with 5 post types, format rules, hook patterns
- `build-in-public/templates/linkedin-article.md` — Native article template for quarterly thought leadership
- `.claude/skills/write-linkedin/SKILL.md` — 7-step skill: source extraction, angle adaptation, format generation (post/article/carousel-outline), LinkedIn-specific scrub pass, human review gate, save
- `build-in-public/context/audience.md` — LinkedIn audience profile added (professional educator/parent)
- `build-in-public/context/channel-rules.md` — LinkedIn channel rules section added
- `build-in-public/context/funnel.md` — LinkedIn funnel added (content warm-up → outreach → B2C2B referral)
- `build-in-public/context/repurposing-rules.md` — LinkedIn repurposing rules and [LINKEDIN CANDIDATE] flag added
- `marketing/context/channel-playbooks.md` — LinkedIn outreach entry updated to reference build-in-public strategy

**Alternatives considered:** (1) LinkedIn as pure outreach channel only, no content (rejected: cold outreach without content warm-up is visibly cold — teacher clicks profile and sees nothing); (2) LinkedIn as a separate sub-OS (rejected: fails workstream test at 2/5 criteria — shares source material and cadence with X); (3) Enitan as primary LinkedIn voice (rejected: his authority with teachers/parents is lower than Teresa's; engineering frame is wrong for the professional educator audience).

**Owner:** Teresa (content + posting), Enitan (infrastructure).

---

## 2026-05-17 — OS execution model: Linear for tasks, OS for execution, wiki for knowledge

**Decision:** Established a three-tool execution model for operationalizing strategic plans in Spyglass OS. Linear handles one-time tasks with owners and deadlines. OS skills and rituals handle recurring execution and cadence-driven review. Wiki holds durable knowledge. No work should live in more than one place. Decision framework codified in `references/execution-model.md`.

**Why:** The marketing plan needed to be turned from a strategic document into actionable items. The initial instinct was to wire everything through OS rituals (`/weekly-pulse` phase gate scoring, `/tune` phase tracking). But Phase 0 is primarily one-time setup work — setup tasks don't fit rituals, which are designed for steady-state recurring execution. Forcing setup tasks into rituals means they either disappear between sessions or generate noise in the weekly review. Linear already exists, is MCP-connected, is used by Enitan for product (EP-XX issues), and Teresa can see it without running the OS. The right tool for the job.

**The framework:**
- One-time task, specific owner, deadline, dependencies → Linear
- Recurring execution, cadence-driven, data-triggered → OS skill or ritual
- Durable knowledge, reasoning, reference material → wiki
- Phase transitions → `decisions/log.md` via `/phase-gate` skill (to build)

**What would change this:** If Linear stops being used consistently by both founders, the task tracking layer collapses and everything migrates back to ritual-driven. The model only works if Linear is maintained.

**Alternatives considered:** (1) Ritual-only approach — all phase execution wired through `/weekly-pulse` and `/tune` (rejected: rituals are designed for steady-state recurring execution, not one-time project setup; forcing gate criteria into a weekly review creates noise and loses tasks between sessions); (2) Wiki-based tracker — a `phase-0-tracker.md` wiki article updated manually (rejected: wikis go stale fast, no owner accountability, no dependency tracking); (3) New OS infrastructure — a `/task` command or Coda task table (rejected: Linear already exists and is MCP-connected — adding new infrastructure for the same job is the wrong move).

**Owner:** Enitan

---

## 2026-05-17 — Phase 0 Foundation: Linear milestone + 24 issues + /weekly-pulse gate scoring

**Decision:** Operationalised the marketing plan Phase 0 by creating a Linear milestone ("Phase 0 — Foundation", target July 31 2026) with 24 issues (EP-52 to EP-75) and updating `/weekly-pulse` Step 7 to score the Phase 0 gate every Friday.

**What was built:**

*Linear milestone:* Phase 0 — Foundation (Alpha Launch project, target 2026-07-31). Gate: all 4 must-pass criteria met AND weighted score ≥ 65%. Hard override: August arrival triggers Phase 1 regardless.

*24 issues (EP-52 → EP-75):*
- EP-52: Wire Brevo (Enitan, Urgent, Jun 21) — blocks EP-55, EP-62, EP-63, EP-64
- EP-53: Audit existing ~8 articles (Teresa, Urgent, Jun 28) — blocks EP-67 through EP-73
- EP-54: Technical SEO foundation — CWV, GSC, robots.ts, /pricing.md, /llms.txt (Enitan, Urgent, Jun 21)
- EP-55: Landing page + waitlist signup (Enitan, Urgent, Jun 28)
- EP-56: 5-10 programmatic past paper pages (Enitan, High, Jul 20)
- EP-57: Bing + Brave Search verified (Enitan, Medium, Jul 5)
- EP-58: School/teacher outreach list — 5-10 schools Tier 1 (Enitan, High, Jul 15)
- EP-59: Teresa's LinkedIn profile complete (Teresa, Urgent, Jun 21)
- EP-60: Join + observe 2-3 Facebook parent groups (Teresa, High, Jun 21)
- EP-61: WhatsApp Business App + ExamPilot community (Teresa, Medium, Jul 5)
- EP-62: Waitlist email sequence 5 emails (Teresa, Urgent, Jul 5)
- EP-63: Student onboarding email sequence 6 emails (Teresa, High, Jul 10)
- EP-64: Parent email sequence 4 emails (Teresa, High, Jul 10)
- EP-65: "For Parents" landing page (Teresa, High, Jul 15)
- EP-66: Results Day content — staged, DO NOT publish early (Teresa, Urgent, Jul 20)
- EP-67: Pillar page Cambridge 9709 Pure Mathematics 1 (Teresa, Urgent, Jul 10)
- EP-68–70: Topic spokes — Coordinate Geometry, Quadratics, Series & Circular Measure (Teresa, High, Jul 15)
- EP-71–73: Strategy spokes — How to Pass, Common Mistakes, Best Resources (Teresa, High, Jul 20)
- EP-74: Examiner report analysis bridge content (Teresa, Medium, Jul 25)
- EP-75: Link building 3-5 referring domains (Enitan, Medium, Jul 28)

*`/weekly-pulse` Step 7 updated:* Queries Linear for EP-55, EP-62, EP-60, EP-61, EP-65 status; scores 9 gate criteria (4 must-pass + 5 weighted); outputs scorecard with ON TRACK / AT RISK / BLOCKED; surfaces single blocking item. Phase-aware — adapts to Phase 1+ once Phase 0 is passed.

**Why:** Applied the execution model (see 2026-05-17 execution model entry): Phase 0 is one-time setup work → Linear. Recurring gate check → ritual. Both wired.

**Key dependency chain:** EP-52 (Brevo) unblocks EP-55/62/63/64. EP-53 (article audit) unblocks EP-67–73. EP-59 (Teresa LinkedIn profile) must be done before Enitan acts on EP-58.

**Owner:** Enitan

---

## 2026-05-18 — /growth-review skill: deferred until post-launch data exists

**Decision:** Decided to build a `/growth-review` skill (quarterly McKinsey-style strategic review) but deferred it until 8-12 weeks post-launch, when real data exists to analyze.

**What the skill will do:** Reads all connected data sources (PostHog, Linear, GSC, Coda Signals, channel metrics from the last 90 days), structures the analysis as Situation / Complication / Recommendation, and outputs a quarterly strategic assessment with one action recommendation. Pairs with `/tune` (tactical parameter changes) as the strategic counterpart — `/tune` asks "how do we execute better?", `/growth-review` asks "are we executing the right things?".

**Why deferred:** Pre-launch with minimal data, a "strategic review" defaults to frameworks applied to assumptions — which feels rigorous but isn't. The skill is only as good as the signal it analyzes. Building it now means it would produce generic SaaS growth advice rather than ExamPilot-specific insight. The real value kicks in when PostHog, conversion, and channel metrics give it something real to analyze.

**What the skill is NOT:** Not an always-on consultant persona. Not a replacement for `/launch-strategy` (launch decisions), `/tune` (tactical monthly review), or `/signal-review` (GTM signals). A quarterly skill invoked when you need strategic direction review, not execution guidance.

**Trigger to build:** 8-12 weeks after Phase 1 soft launch, when you have at least one cohort of PostHog funnel data and channel-to-conversion signal. Parked in `EXPANSIONS.md` with the trigger condition.

**Alternatives considered:** Build now with placeholder data (rejected: frameworks on assumptions is strategy theatre); never build, rely on ad-hoc strategic thinking (rejected: no structured challenge to the strategy direction creates drift risk over time).

**Owner:** Enitan

---

## 2026-05-18 — SEO Brothers knowledge pipeline: staged evaluation before integration

**Decision:** Adopted a staged approach to ingesting the SEO Brothers YouTube channel (https://www.youtube.com/@OfficialSEOBrothers/videos) as an SEO execution resource. Phase 0 fetches a 5-10 video sample, evaluates content style (tactics vs. frameworks, niche applicability, signal density), and produces a written integration decision before touching any active execution layer.

**Integration model (if Phase 0 green-lights):**
- Wiki ingest is a staging step, not the end goal
- Final active destinations: `content-standards.md` updates, skill instruction updates, new `/seo-quality-check` skill as a publishing gate
- Wiki articles (`wiki/marketing/seo/`) remain as the reference/source layer
- Topic-consolidated articles (multiple videos on same topic → one article)

**Build:** New Python module `marketing/data_sources/modules/yt_transcript_fetcher.py` — uses `yt-dlp` + `youtube-transcript-api`, outputs wiki-compliant `raw/marketing/seo-brothers/` files. No API keys needed.

**Why staged:** We don't yet know if the content is tactics (embeds cleanly into checklists) or frameworks (harder to operationalize). Integrating into active skills before that's clear risks baking in guidance that doesn't apply to ExamPilot's niche or silently overriding approaches that are already working.

**Alternatives considered:** (1) Wiki-only destination (rejected: passive reference gets underused — low leverage); (2) Immediate active layer integration without evaluation (rejected: wrong until we know what kind of knowledge it is); (3) One article per video instead of topic-consolidated (rejected: produces a video index rather than a coherent knowledge base).

**Plan file:** `/Users/enitan/.claude/plans/jazzy-spinning-snail.md`

**Owner:** Enitan

---

## 2026-05-18 — SEO and marketing synthesis overview: wiki over OS duplication

**Decision:** Created a synthesised SEO + marketing strategy overview as a wiki article (`wiki/marketing/seo-and-marketing-overview.md`) rather than a standalone OS file. Added a lightweight pointer at `marketing/references/seo-marketing-overview.md` in the OS for quick access.

**Why wiki:** The OS has an explicit rule against duplicating strategy into local files — the wiki is the source of truth for "what the strategy is" and the OS is for "how to execute." The synthesis article draws entirely from existing wiki articles. Storing it locally would create two sources of truth that drift apart as the strategy evolves.

**Why not OS:** An OS-local strategy file would need manual updates every time the underlying wiki articles change (seo-strategy, marketing-plan, llm-seo-mechanics, etc.). The wiki pointer pattern keeps one canonical home that stays in sync automatically.

**Outcome:** Article marked "Start here" in `wiki/marketing/INDEX.md`. Covers micro-funnel, 4-phase plan, flywheel, GTM measurement, channel-to-stage mapping, all SEO tactical frameworks — 13 cross-references to underlying articles.

**Owner:** Enitan

---

## 2026-05-19 — EP-76 content pipeline: two competing plans to evaluate

**Decision:** PENDING. Two plans exist for EP-76 (content pipeline redesign). Neither has been approved. Both must be compared before implementation begins.

**Plan A (original, in Linear EP-76 description):** Six sequential phases. Phase 4 ("injection bridge") creates a Vercel POST endpoint that "accepts {type, document} JSON body and calls `client.create()`". Treats the endpoint as a simple passthrough. Updates `/write-article` and `/pre-write` to POST to it.

**Plan B (alternate, in `references/content-pipeline-redesign-alt.md`):** Server-side transformation via the same Vercel endpoint, but recognises that `client.create()` is not enough. The existing `scripts/lib/` plugin system (9 plugins, 1,756 lines) must run inside the endpoint to transform content JSON into Sanity portable text. Key additions:
- Imports `scripts/lib/` directly into the API route (monorepo advantage, zero code duplication)
- Handles all 9 content types through the existing plugin registry
- Adds a markdown-to-content-JSON converter for blog posts (`/write-article` outputs markdown, not JSON)
- Assets arrive as base64 in POST body, decoded and uploaded server-side
- Reorders EP-76 phases: API endpoint first, then OS skill integration, then Studio UX

**Why two plans:** Investigation of the spyglass repo revealed that `create-content.mjs` does significant transformation (content JSON -> portable text, asset upload with dedup, parent hub linking, plugin-based routing) that Plan A's "calls `client.create()`" does not account for. Plan B addresses this but is a larger scope change.

**What to compare:** (1) Is the plugin import from `scripts/lib/` into a Vercel serverless function reliable, or will build/tracing issues make it fragile? (2) Is the markdown-to-content converter (Plan B Phase 3) worth the complexity, or should `/write-article` just output content JSON directly? (3) Phase ordering: Plan A does Studio UX before injection bridge; Plan B does injection first.

**Files:**
- Plan A: Linear EP-76 description (https://linear.app/exampilot/issue/EP-76)
- Plan B: `references/content-pipeline-redesign-alt.md`

**Owner:** Enitan

---

## 2026-05-21 — Added /move-37 skill for off-board strategic thinking

**Decision:** Built `/move-37` as a Spyglass OS skill. Forces the AlphaGo Move 37 thinking pattern — name the cultural sediment in a space, map what it makes invisible, then generate 3 plays that explicitly contradict named assumptions. Stress test (complexity / cost / timeline / ceiling / risk) is mandatory per play.

**Why:** Strategic conversations were producing good off-board ideas but inconsistently — sometimes by accident. The skill captures the discipline: refuse to generate plays until sediment is named. Avoids the failure mode of brainstorming on the same axis as competitors.

**Design choices:**
- Altitude-invariant (one skill for whole-business strategy down to single artifact angle) — altitude is a question in the interview, not a mode flag.
- Output to `marketing/pipelines/strategy/` with YAML frontmatter (`status`, `outcome: TBD`) so `/tune` can review historical plays monthly.
- Auto-consumes wiki marketing strategy + audience segments to ground sediment scan in real ExamPilot context, not generic edtech defaults.
- Refuses pre-committed answers ("just give me the tutor flywheel plan") — offers to stress-test instead, doesn't pretend to discover what the user already named.

**Continuous improvement hook:** Each Move 37 artifact carries `outcome: TBD`. `/tune` reads these monthly and asks user to mark Won / Lost / Inconclusive. After 6+ outcomes, surfaces patterns about which kinds of sediment-breaks work in ExamPilot's specific context.

**Files:**
- `.claude/skills/move-37/SKILL.md`
- `marketing/pipelines/strategy/` (new folder for artifacts)

**Owner:** Enitan

---

## 2026-05-21 — /tune updated to capture Move 37 outcomes monthly

**Decision:** Extended `/tune` to include Move 37 as a tracked function. Each monthly cycle now scans `marketing/pipelines/strategy/` for artifacts with `outcome: TBD`, prompts user to mark them Won / Lost / Inconclusive / Still-running / Retired with a one-sentence reason, then writes the result back into the artifact frontmatter and a `## Outcome` section.

**Why:** Move 37 is the only function in the OS that produces *outcomes*, not parameters. The `/tune` framework was built for parameter adjustment ("change weight X from 0.4 to 0.6"). Move 37 needed a parallel track for outcome capture and pattern surfacing. Without this, the `outcome: TBD` field in Move 37 artifacts would never get filled and the continuous-improvement loop would silently break.

**Shape difference made explicit in the skill:** Other functions adjust parameters from data; Move 37 captures outcomes and surfaces patterns about which sediment-breaks work in this business. Pattern analysis is gated at ≥6 closed outcomes — below that, the skill says so and skips pattern summary to avoid false signal.

**Files:**
- `.claude/skills/tune/SKILL.md` (function table + Steps 2, 3, 4, 5, 6 all extended)

**Owner:** Enitan

---

## 2026-06-02 — Aligned schema skills with the v3.1 schema-demotion doctrine (pipeline catch-up)

**Decision:** Reframed the OS-side schema rationale to match the wiki's 2026-06-02 doctrine change. Schema is now documented as a lever for traditional rich results, featured snippets, and agent-readability — **not** an AI-citation driver. The AI-citation lever is answer-first extractable prose plus entity/YouTube signals.

**Why:** Ahrefs' 2026 controlled study found schema markup has no measurable effect on AI citations. The wiki was updated 2026-06-02 (marketing-plan v3.1 decision 20; llm-seo-mechanics; seo-strategy) but the pipeline still encoded the retired "schema drives citations" rationale — the wiki was ahead of the code.

**Important scope correction:** The wiki's open-action wording ("schema-markup skill + composite scorer in github.com/akhanaton/spyglass") was inaccurate on two counts:
1. The `schema-markup` skill and the content scorers live in **this OS repo** (`akhanaton/Spyglass-OS`), not the product repo.
2. The composite scorer (`marketing/data_sources/modules/content_scorer.py` + `seo_quality_rater.py`) does **not** weight schema at all — its SEO sub-score is keyword/meta/H1/word-count. There was no schema weight to re-weight. The retired rationale lived only in the `schema-markup` skill text and one `seo-quality-check` checklist row.

**Files changed (OS):**
- `.claude/skills/schema-markup/SKILL.md` — description + "What this skill does" reframed; FAQ 200-char rule reframed from "AI Overview inclusion" to "featured-snippet display"; added a dated doctrine note
- `.claude/skills/seo-quality-check/SKILL.md` — section F renamed "GEO Technical" → "Rich Results & Technical"; FAQPage row reframed; note added that the citation lever is answer-first (section B) + entity (section D); optional video-embed/VideoObject check added

**Still open (product repo, separate session):** Whatever JSON-LD injection and quality scoring exist in the exampilot.io app (`$SPYGLASS_PRODUCT_REPO` / `github.com/akhanaton/spyglass`) — de-emphasise schema as a citation signal there too. Doctrine is de-emphasise, **not remove**: schema still ships for rich results.

**Owner:** Enitan

---

## 2026-06-02 — Deferred YouTube presence as a scoped initiative (spec + Linear epic), not piecemeal

**Decision:** YouTube presence is being treated as a cross-cutting initiative with its own spec (`references/youtube-presence-strategy.md`) and a Linear epic (EP-YT, to create once Linear is authed), mirroring the EP-77 pattern — not absorbed piecemeal into existing skills. Execution is **gated on a production-model decision** (faceless screencast / on-camera Teresa / hybrid / seed-only) that Enitan + Teresa must make before any skill is built.

**Why:** Ahrefs 2026 found YouTube mentions are the strongest measured correlate of AI brand visibility (0.737). The marketing plan absorbed the strategy (v3.1, decision 19) but YouTube touches 11 OS surfaces — content pipeline, frontmatter type enum, 5 skills, weekly-pulse KPIs, GTM signals, connections, channel playbooks, and the build-in-public boundary. Bolting it on without a spec would create drift. The real blocker is production capacity, not strategy — neither founder produces video today.

**Recommended starting model (to confirm):** Seed-only (D) in parallel with faceless screencast (A) — capture the citation signal fast at zero production cost while standing up owned 9709 explainers to embed in blog posts. Escalate to hybrid (C, add Teresa authority pieces) once cadence is proven.

**Boundary clarified:** YouTube is a student-facing marketing/GEO channel → lives in `marketing/`, NOT in the `build-in-public/` sub-OS (which is X + LinkedIn, founder-facing, only).

**Files:**
- `references/youtube-presence-strategy.md` (new spec — 11-surface map, skills list, KPI/signal integration, phasing, Linear epic shell, success criteria)

**Owner:** Enitan + Teresa (production-model decision); Enitan (execution)

---

## 2026-06-16 — Canonical host for ExamPilot set to non-www (exampilot.io)

**Decision:** `https://exampilot.io` (non-www) is the canonical host. `www.exampilot.io` redirects via a 301 at Vercel. All code references aligned.

**Why:** Three files disagreed on the canonical host, splitting Google ranking signals. Non-www was already the majority in the codebase and is the modern standard. The Vercel www→non-www redirect was already configured, so the change carries no redirect risk.

**Alternatives considered:** Canonicalise on www instead — rejected; minority usage in the codebase, no SEO advantage, more files to change.

**Owner:** Enitan (deploy) / Teresa (GSC + Sanity + OAuth verification)

---

## 2026-06-16 — Bucket 1 SEO content applied to Cambridge 9709 Pure 1 cluster

**Decision:** Custom meta descriptions and Key Takeaways blocks added to all 7 Cambridge 9709 Pure 1 pages in Sanity Studio. Meta titles corrected on trigonometry, binomial-series, and functions.

**Why:** Meta descriptions were the top audit gap — the fallback (`definition.slice(0, 160)`) was not keyword-optimised and had no CTA. Key Takeaways blocks are the primary GEO lever: answer-first, extractable prose for AI citations. Highest-ROI changes from the 76.7/100 batch audit.

**Alternatives considered:** Defer Sanity edits until a content template was formalised — rejected; the audit spec is sufficient, and waiting blocks measurable score improvement.

**Owner:** Teresa

---

## 2026-06-16 — SEO audit run on Cambridge 9709 Pure 1 cluster

**Decision:** Run a structured 6-dimension SEO audit across all 7 published Cambridge 9709 Pure 1 pages. Batch score: 76.7/100 (Good). Priority gaps: missing meta descriptions, no external authority links on 5 of 7 pages, hub missing two topic cards.

**Why:** Phase 0 is building the SEO foundation that Phase 2 compounds. Auditing before building more spoke pages is correct sequencing — it anchors the improvement backlog against a measurable score rather than ad hoc intuition.

**Alternatives considered:** Defer audit until more pages exist — rejected; fixing the first 7 well is cheaper than fixing 30 later, and the scoring baseline is more useful early.

**Owner:** Teresa

---

## 2026-06-16 — Three repo-side SEO fixes applied (Bucket 3 of audit)

**Decision:** Applied three code/config fixes to `akhanaton/spyglass`: updated `llms.txt` with Cambridge 9709 Pure 1 content and corrected board references, added AI bot crawl rules to `robots.ts`, added a temporary 307 redirect `/past-papers` → `/cambridge/9709/pure-1`.

**Why:** These are the audit action items that live in the repo rather than Sanity. Shipping them separately keeps content edits (Teresa, Sanity) and code changes (Enitan, deploy) on independent tracks with no cross-dependency.

**Alternatives considered:** Bundle repo fixes with Bucket 1 Sanity edits into one deploy — rejected; different owners and deploy cycles, decoupling reduces coordination cost.

**Owner:** Enitan (deploy) / Teresa (Sanity edits remain Bucket 1)

---

## 2026-06-02 — YouTube production model chosen: seed-only + faceless screencast (gate lifted)

**Decision:** Production model = **D (seed-only) in parallel with A (faceless screencast)**, escalating to **C (hybrid — add Teresa on-camera authority pieces)** once cadence is proven. This lifts the gate on `references/youtube-presence-strategy.md`; Phase 0 execution (EP-YT-2 onward) is unblocked. EP-YT-1 (the decision sub-issue) is resolved.

**Why:** Captures the 0.737 AI-visibility signal fastest at zero production cost (seed mentions on established 9709 channels) while building an owned, scalable explainer library (faceless screencasts) to embed in blog posts. Defers the high-cost on-camera track until volume/trust justify it.

**Files:**
- `references/youtube-presence-strategy.md` (gating section + EP-YT-1 marked DECIDED)

**Owner:** Enitan + Teresa

---

## 2026-06-02 — YouTube epic + schema-repo task created in Linear (all assigned to Enitan)

**Decision:** Created the YouTube initiative in Linear under team Exampilot, and converted every production/gh follow-up into a Linear issue assigned to Enitan (per request: "make any production gh task a Linear issue for now and assign to me").

**Issues created:**
- **EP-78** (parent) — YouTube presence as a core GEO/citation channel
- EP-79 — Choose production model (✅ Done: D+A, escalate to C)
- EP-80 — Seed mentions on 9709 tutorial channels (Todo)
- EP-81 — Produce + embed faceless 9709 explainers (Todo)
- EP-82 — VideoObject schema on video-hosting pages (Todo, **blocked by EP-86**)
- EP-83 — YouTube channel + KPIs into /weekly-pulse + signals (Todo)
- EP-84 — [Phase 1] Build /youtube-script + extend /repurpose (Backlog)
- EP-85 — [Phase 1] Wire YouTube Data API into connections + /signal-review (Backlog)
- **EP-86** (standalone) — Product repo: de-emphasise schema as an AI-citation signal in `JsonLd.tsx` (Todo, blocked on product-repo access)

`references/youtube-presence-strategy.md` updated with the real issue numbers.

**Owner:** Enitan

