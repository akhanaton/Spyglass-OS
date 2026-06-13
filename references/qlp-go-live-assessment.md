# QLP Go-Live Assessment

**Date:** 2026-06-09
**Owner:** Enitan (assessment requested pre-launch)
**Status:** Pre-decision assessment. Pairs with the go-live workstream. Action items should become Linear issues.
**Method:** Multi-agent deep review (32 agents). Five dimension analysts (technical architecture, learning science, product/launch fit, operations, documentation forensics) read the full QLP corpus in spyglass-wiki. Every critical/high finding was then adversarially verified by an independent agent that re-fetched the cited sources and tried to refute it. 26 findings verified: 24 stood, 1 was refuted, 1 was downgraded. A completeness critic added gaps no analyst covered.
**Ground truth caveat:** The product repo was not accessible during this review. Everything here is grounded in wiki articles (most `verified_against_code: true` as of 2026-05-10) plus raw engineering docs. The verification date is now 30 days stale, straddling the exact window in which seeding was supposed to happen. Re-verify the load-bearing facts against live code first (see the acceptance checklist).

---

## Bottom line

QLP is academically credible, architecturally well-designed, and operationally unproven. The framework is a faithful knowledge-component model with misconception-grounded distractors and FSRS scheduling. The literature behind each piece is solid. The engineering shows real discipline: flag-gated rollout, approved-only retrieval, a sub-5-minute kill switch, contract-validated extraction.

But as of the last verified state, it is a theory with zero empirical contact:

- Zero seed QLPs exist. The extraction pipeline has never run on a real exam paper.
- The implemented `QLPQuestionContext` schema diverges from the spec the SRS cutover is built on.
- The wiki's own verified articles contradict each other on how a question reaches a student in production.
- Two code-level seeding blockers are documented only outside the QLP doc set (incomplete tier calculation, hardcoded exam board).
- The legal basis for ingesting Cambridge materials is recorded as unresolved.

**The single most important reframe:** QLP-seeded *content* is launch-critical. QLP-as-SRS-*substrate* is not. Gate the August launch on 50 human-vetted CIE 9709 Pure 1 QLPs retrievable in sessions, run SRS at Stage 0/1 (topic-based, fallback-safe), and explicitly defer the four-stage cutover, ERI, PMC, and Tier 3 synthesis to post-launch. Every week spent on the 12-item cutover backlog instead of seeding is a week taken from the only thing that can actually fail the launch.

The math is survivable from a ~Jun 13 infra restart, but only with zero slack and ruthless sequencing. The 6-week bootstrap plan (ingest → tier → extract → human moderation) started now lands mid-to-late July against an immovable mid-August Results Day window.

---

## What QLP is and how it is meant to be used

A Question Logic Pattern is the core pedagogical unit: a parameterized template encoding the complete logic of a maths concept. Not the topic label, but the reasoning pattern. Each QLP carries the question/solution template, misconception-linked distractor logic, prerequisite edges, real exam appearances, a predictive weight, and a tier.

- **Tier 1** "exam killers" (~60% of historical marks): 100% human-vetted, AI-origin content can never auto-approve.
- **Tier 2** core coverage: AI-generated, 10% spot-check.
- **Tier 3** A* synthesis: composes only from approved Tier 1/2 nodes ("Fidelity Lock").

Intended uses, in dependency order: seeded question content in sessions → substrate for SRS card generation (4-stage cutover from `topic_id`) → misconception feedback per wrong answer → ERI exam-readiness score → PMC forward projection → "Examiner-as-a-Service."

Only the first of these is needed for August.

---

## What is genuinely strong

- **The construct is sound.** Logic nodes are a correct application of knowledge-component theory (KLI framework). Misconception-linked distractors follow the validated distractor-driven assessment tradition (Sadler 1998; Gierl et al. 2017). FSRS is the strongest open scheduler available.
- **Safety is enforced in code, not policy.** `QLP_RETRIEVAL_REQUIRE_APPROVED=true` blocks unapproved content from serving. Tier 1 AI-origin cannot be system-approved. Tier 3 composes only from vetted nodes.
- **Rollback is designed, not improvised.** Config-only kill switch (`QLP_RETRIEVAL_ENABLED=false`), quantified triggers, RTO under 5 minutes, shadow → canary → full rollout stages.
- **The extraction pipeline design is right.** Five bounded agents, contract validation between stages, a QA feedback loop with quantified thresholds, full audit traces. Cost is trivial (~$0.11-0.14/QLP, under $15 for the seed batch).
- **Spend controls have teeth.** $50/day and $1000/month caps checked as the first action of every content/QLP task.
- **The docs are epistemically honest.** Counter-evidence sections, `verified_against_code` flags, dated verification notes. There is no self-deception to unwind, only sequencing to fix.
- **Good news from verification:** the claim that the Tier 1 moderation UI is "component stubs" was REFUTED. A working admin-qlp moderation module exists (queue, preview, approve/reject, bulk actions) per admin-ui.md, verified 2026-05-11. Teresa has a vetting surface. What is missing is a rubric, a throughput estimate, and a first real exercise of it.

---

## Critical findings (all survived adversarial verification)

### 1. The seeding critical path consumes the entire runway, on a pipeline that has never run on real content

Seed data confirmed absent 2026-05-10. Seeding was planned "early June." It is now June 9 with no infra access until ~June 13. The wiki's own bootstrap plan is 6 weeks: ingest QP/MS/ER → tier assignment → extraction → Tier 1 human moderation → Tier 2 spot-check. Started June 13, that lands late July with zero slack before Results Day. First runs of LLM pipelines always surface issues (OCR quality, QA-loop non-convergence, contract failures). There is no buffer to absorb them.

**Do:** Make a single-paper production smoke test the first action when access returns. One real CIE 9709 Pure 1 paper + mark scheme + examiner report through all 5 agents with `QLP_EXTRACTION_USE_MOCK_DATA=false`. Measure QA pass rate, time per QLP, cost, and Teresa's moderation minutes per QLP. Multiply out to 50 and re-check the freeze date with real numbers in week one. Overlap ingestion and extraction per-topic instead of running phases sequentially. Set a hard internal gate: if approved Tier 1 coverage is below threshold by ~July 25, descope (Tier-1-only seed for the highest-weight topics) rather than slip.

### 2. QLP has no verified production delivery path

session-content-layer.md says all student questions are served exclusively through QLPRuntimeService. qlp-srs-integration.md (verified the same day) says SRS generates everything from `topic_id` and QLP is never called. The Phase 2 session-integration services are marked RESERVED and unmounted (404 in any deployed environment). The frontend has zero QLP integration (`USE_MOCKS=true`; seven expected endpoints have no backend routes). Even with 50 approved QLPs in MongoDB, it is currently unclear how one reaches a student.

**Do:** 30-minute code check: trace the real serving path from `router.py`. Then build the thin adapter endpoints (QLPRuntimeService + ImplicitFSRSRatingService) as the single engineering priority after seeding. Do NOT mount the RESERVED router as a shortcut: it carries known stubs and a concurrency bug.

### 3. Two code-level seeding blockers live outside the QLP doc set

production-readiness.md records `TierTopicRegistry._calculate_tier_for_topic()` as an incomplete TODO and the extraction workflow as having a hardcoded subject/board. Both contradict the QLP docs' "Phase 4a/7 Complete" claims. Both sit on steps 2-3 of the seeding critical path. Treat the test matrix's "NOT STARTED," not the QLP docs' "Complete," as operational truth.

**Do:** Before any seeding run, open the tier registry and confirm the tier math is implemented; grep the extraction workflow for hardcoded board/spec IDs and parameterize to CIE 9709 P1.

### 4. The legal basis for ingesting Cambridge materials is unresolved

competitive-landscape.md states this plainly as of May 2026. No QLP engineering runbook mentions it, yet the entire June plan is built on ingesting CIE 9709 papers. A takedown landing during the launch window is unrecoverable.

**Do:** Decide the posture before extraction touches real papers. The defensible line: QLPs are transformative parameterized analysis; student-facing output uses original questions exercising the same logic patterns, never verbatim Cambridge text, figures, or mark schemes. Encode that as a hard reject criterion in the moderation rubric. Scrub marketing copy of claims that imply reproduction ("questions built FROM real past papers and mark schemes" is the honest framing, not "real past paper questions"). Log the decision. One hour of real legal review is the cheapest insurance on the critical path.

### 5. Flag sequencing is the most likely day-one failure

~20 interdependent `QLP_*` flags, all defaulting OFF, with `QLP_EXTRACTION_USE_MOCK_DATA=true` by default, and no dependency matrix. Mock data left on during a real run permanently poisons predictive weights and tier assignments with random exam appearances. Docs also disagree on flag names (`MAX_QUALITY_ATTEMPTS` vs `MAX_QA_FEEDBACK_ITERATIONS`).

**Do:** Write the one-table flag matrix (valid combined states: Extraction-live, Serving-live, Kill-switch) and treat it as the deploy checklist. Add a startup assertion that fails loudly in production if mock data is on, approved-only retrieval is off, or the quality gate is off. Quarantine any QLP whose exam_appearances came from the mock generator.

### 6. ERI "exam readiness" is an uncalibrated heuristic; readiness claims must not ship

The "90% predictive confidence" line in the ideation doc is an assertion, not a derived property. The formula multiplies three quantities on different scales with no calibration against actual exam outcomes. FSRS stability is also tracked per topic, not per node, so the formula's F_stability term is computed at the wrong granularity. Telling a 17-year-old they are "exam ready" off an unvalidated index is the single biggest validity risk in the product, aimed at exactly the persona (resit students) most likely to punish overclaim.

**Do:** For launch, frame student-facing analytics as coverage, not readiness ("secure recall on X of the high-frequency question patterns for Pure 1"). Never "ready" or "predicted grade." Strike "90% predictive confidence" from all docs and copy. Pre-register a calibration plan: collect outcomes from the Oct/Nov 2026 sitting, regress against ERI, and introduce predictive language only when a validated mapping exists.

### 7. The QLPQuestionContext contract is a fork that blocks everything downstream

Two competing specs exist. The raw impact report (2026-02-28) requires only `qlp_id`/`qlp_version`/deterministic seed. The wiki article presents a rich payload contract (template_body, distractor_logic, evaluation_steps, prerequisites, exam_appearances) and marks the implemented schema "Different." The implemented schema may actually satisfy the original spec. There are also two different 12-item backlogs and two different "Stage 1-4" sequences with contradictory migration philosophies (hard cutover vs silent fallback).

**Do:** One-day decision before any seeding or SRS code: open `qlp_phase3_contracts.py`, pick the canonical contract (likely a merge: keep traceability fields, add the payload fields the card composer needs), verify the extraction pipeline emits that format so seed data does not need re-extraction later, collapse the wiki to one contract and one backlog, and log the decision.

---

## High findings, condensed

- **Plan the launch explicitly on topic-only SRS and say so.** Stage 2+ before August adds risk for zero first-100-trials benefit. Pre-launch, do only the two cheap forward-compatible items: optional `qlp_id` on DrillCardResponse and `fallback_reason` telemetry. (Technical, verified)
- **Misconception inventory is unvalidated and the QA gate tolerates 40% ungrounded distractors.** Ingest examiner reports FIRST, build the canonical misconception inventory for Pure 1 Algebra before extracting QLPs, raise `distractor_grounding` to ≥0.8 for Tier 1, and require Teresa's checklist to trace each distractor to an examiner-report span. Wrong misconception attribution is worse than no diagnosis. (Pedagogy, verified)
- **FSRS granularity mismatch.** Memory parameters exist per topic; node-level claims need per-QLP grain. Decide the target grain now, before seed data shapes the migration. If staying topic-level for launch, ERI-style analytics must use observed per-node accuracy, not topic stability. (Pedagogy, verified)
- **No alerting; key observability defaults are OFF.** The documented rollback triggers cannot be observed. Set `QLP_RETRIEVAL_TRACE_ENABLED=true`, tracing flags on, point `OTEL_EXPORTER_OTLP_ENDPOINT` at a free-tier backend, and build exactly two phone-reaching alerts: fallback rate >50%/hour and health-check failure. (Ops, verified)
- **Single-founder bus factor in a 48-72h window.** Freeze code and flags one week before Results Day. Extend the incident playbook with 4 QLP-specific scenarios. Give Teresa a break-glass card: check /api/health, flip `QLP_RETRIEVAL_ENABLED=false` in Railway. (Ops, verified)
- **No executable production seeding runbook.** The procedure is fragmented across three articles with no verification steps, and its examples still point at Edexcel folder paths and possibly the wrong storage backend. Write the one-page "CIE 9709 Pure 1 Seeding Runbook" with exact commands, a verification query after each step, and abort criteria. Rehearse once in staging. (Ops, verified)
- **Edexcel-era remnants throughout.** No node count, tier split, or seed parameters exist for CIE 9709 P1 (only Edexcel estimates). path-to-revenue's seed topic list includes Statistics, which is not a P1 topic. Run a one-day re-parameterization pass before seeding. (Consistency, verified)
- **Product/strategy docs are five months stale on QLP.** product-current-state and path-to-revenue list "remaining work" that shipped in March, and omit the work that actually remains. Rewrite both to match the verified engineering state so planning happens against reality. (Consistency, verified)
- **Marketing claims must be trimmed to Stage 0/1 truth.** Claim freely: adaptive practice, spaced review, topic-level gap analysis, "questions built from real CIE 9709 past papers and mark schemes." Do not claim: misconception-level precision, exam readiness, predicted grades, examiner-grounded SRS. The resit persona (Omar) is the audience most likely to detect the gap between promise and product in week one. (Product, verified)
- **50 Algebra-only QLPs is thin for a 50+ cohort.** An engaged trialist can exhaust one topic in days, and the Phase 1 D7 retention gate would then misread content starvation as PMF failure. If Teresa's measured throughput allows, extract a second exam-killer topic (Differentiation or Integration) before freeze. Either way, set coverage expectations in onboarding and instrument a content-exhaustion event in PostHog. (Product)
- **Hide every dead-end surface before trial users arrive.** ExamLens "Start" navigates to a page that does not exist. Module test, leaderboard, score predictor, Sparx store: audit student-reachable nav and feature-gate everything without a working backend. One day of work, independent of QLP. (Product)
- **Synthesizer model decision before the seed run.** The terminal extraction stage runs on the weakest math model in the stack (DeepSeek V3.2, flagged P1-upgrade). Re-extracting 50 QLPs after a model swap doubles cost and re-triggers moderation. Decide first. Also execute the P0 Gemini Flash-Lite deprecation check and pre-stage the fallback. (Ops)

Notable mediums: ack-early Celery tasks can silently drop seed jobs on worker restart (verify `acks_late` on `generate_single_qlp`; run a dispatched-vs-created reconciliation query after every batch). Cost metering is structurally inaccurate (measure real $/QLP from generation_traces during the first run). Three incompatible difficulty constructs need a one-page unification note before SRS Stage 1. The AI-generated "pedagogical validation" doc with a fictional professor and fabricated effect sizes must never leak into external copy; add that rule to content-standards.md and commission one real external review of the Tier 1 seed batch (fits the B2C2B teacher strategy).

Downgraded by verification: PMC is a roadmap guardrail, not a launch blocker (it cannot mechanically ship by August anyway). Keep the rule: no PMC, no enriched ERI, until post-launch response data exists.

---

## Gaps no analyst covered (completeness critic)

1. **GDPR / children's data.** The wiki's own audit rates the platform HIGH RISK: no DPIA (mandatory for AI profiling of minors), no age verification, privacy/terms/cookie pages 404, PII in logs, student data flowing to DeepSeek (no EU adequacy). QLP makes it worse: node-level misconception tracking is automated cognitive profiling of minors. Add a compliance gate to the launch checklist: publish the legal pages, capture age at signup, minimal DPIA covering QLP telemetry, remove DeepSeek from student-data paths or document SCCs.
2. **Security of the admin/moderation/seeding surface.** Verify every QLP admin endpoint requires founder-level auth in production, the moderation UI is not publicly routable, and extraction prompts treat OCR text as data, not instructions. Run /security-review against the product repo when access returns.
3. **Cost blowout scenarios.** Make the launch window generation-free by policy: serve only pre-vetted bank + topic fallback, real-time generation flag-disabled, provider-side spend caps tested.
4. **The moat is the data, not the framework.** The schema and pipeline are replicable; the durable assets are the human-vetted misconception bank and outcome-calibration data, both of which accrue only after launch. This is an argument for launching the flywheel sooner at smaller scope, not for more pre-launch sophistication. Align fundraising language accordingly.
5. **Content-defect loop.** One wrong answer will surface in week one, in front of the audience that screenshots to Reddit. Ship a minimal "report a problem" affordance and a same-day unapprove runbook (approved-only retrieval makes pulling a bad QLP cheap).
6. **Teresa's moderation capacity is the real seeding clock.** At a plausible 30-40% rejection rate, 50 approved QLPs means reviewing 70-85 plus re-reviews. At 20 min/item that is 25-30 hours of expert review nobody has scheduled, in the same weeks as EP-77 and the content sprint. Write the rubric, pilot-vet 5, measure, re-derive the schedule, block the calendar.
7. **Backup and restore of the vetted corpus.** The 50 approved QLPs plus moderation provenance will embody weeks of irreplaceable founder time. Confirm backups cover QLP/moderation tables, run one restore drill, and export the approved batch to versioned files in git after each moderation session.

---

## Recommended sequence from June 13

**Week of Jun 13 (prove + decide):**
1. Re-verify ground truth: count `question_logic_patterns` documents, check flag state, confirm tier-calc and hardcoded-board status in code.
2. IP posture decision + log it. No real-paper extraction before this.
3. Contract reconciliation (one day): canonical QLPQuestionContext, one backlog, verify extraction output format matches.
4. Single-paper smoke test with mock data off. Measure everything.
5. Flag matrix + startup assertions. Synthesizer model decision.
6. Teresa: vetting rubric + pilot-vet 5 candidates, measure minutes/item.

**Jun 20 – Jul 11 (seed):**
7. Ingest examiner reports first, build the Pure 1 Algebra misconception inventory, then batch extraction. Teresa moderates daily in parallel.
8. Enitan in parallel: thin adapter endpoints so vetted QLPs reach sessions; hide dead-end surfaces; alerting + tracing on.

**Jul 11 – 25 (harden):**
9. Load-test sessions with seeded content. Rollback rehearsal in staging (flip the kill switch, time it). Seeding runbook finalized. Optional second topic if throughput allows.
10. Content freeze Jul 25. Code/flag freeze ~Aug 1. Anything not seeded ships post-launch.

**Explicitly post-launch:** SRS Stages 2-4, ERI, PMC, Tier 3 synthesis, cache-key migration, Examiner-as-a-Service taxonomy, node-map work. Log this de-scope as a decision.

---

## Acceptance checklist: "works as advertised"

Run these against the live system when infra access returns. Each is pass/fail.

1. **Schema ground truth.** Dump the actual QLPQuestionContext model from code and diff against both wiki specs. Record which is canonical in decisions/log.md before any SRS code.
2. **Real-paper extraction smoke test.** One real CIE 9709 P1 paper end-to-end in staging, mock flags off. Pass = QLP instance lands in DB with exam_board=CIE (proves the hardcoded-board fix), complete tier calculation, contract validation passing. Record wall-clock and cost.
3. **Delivery-path proof.** As a test student, start a session and trace one served question to the producing service. Pass = a vetted QLP reaches a student through a mounted production route.
4. **Moderation gate integrity.** Generate one QLP, confirm it is NOT retrievable while unapproved; approve it, confirm it serves; unapprove it, confirm it stops within minutes. Time the cycle (first real throughput number).
5. **Production flag audit.** Dump every QLP_* flag's production value. Pass = mock data OFF, approved-only ON, all Stage 2-4 / ERI / PMC / real-time-generation flags OFF. Commit the table as the flag matrix.
6. **Kill-switch rehearsal.** Flip `QLP_RETRIEVAL_ENABLED=false` mid-session in staging. Pass = next request serves topic fallback, no 5xx, within 5 minutes.
7. **Worker durability.** Kill the Celery worker mid-seeding-task, restart. Pass = task redelivered (ack-late), and a real failure surfaces as a failure, not a success-shaped dict. If it fails: never run seeding unattended.
8. **Spend-cap test.** Set a deliberately low cap, exceed it with a small batch. Pass = generation halts AND recorded token costs roughly match the provider dashboard.
9. **Alerting fires.** Force a fallback-rate spike in staging. Pass = a human-visible alert arrives without anyone watching logs.
10. **GDPR spot-checks.** No student data to DeepSeek; no PII in production logs (including the known auth.py offender); /privacy, /terms, /cookies resolve; signup captures age and gates profiling for under-16s.
11. **Backup restore drill.** Restore latest backup to a scratch DB; approved seed batch + approval metadata survive. Export the corpus to versioned files in git.
12. **Launch-surface sweep.** As a trial-tier account in production, attempt to reach ExamLens and every QLP-adjacent unfinished surface. Pass = all unreachable or cleanly hidden. Confirm SRS runs topic-only with no cutover flags partially enabled.

---

## Decisions this report recommends logging

1. August launch gates on Phase 10 exit + 50 moderated Pure 1 Algebra QLPs retrievable; SRS ships at Stage 0/1; Stages 2-4, ERI, PMC, Tier 3 deferred to post-Phase-1-gate.
2. IP posture for Cambridge-derived QLPs (transformative templates, no verbatim text, hard reject criterion in moderation).
3. Canonical QLPQuestionContext contract (and the single backlog/stage taxonomy that follows).
4. FSRS grain decision (per-QLP target; interim handling if topic-level at launch).
5. Synthesizer model for the seed run.
6. No readiness/predicted-grade language until the Oct/Nov 2026 calibration study; "90% predictive confidence" struck from all copy.

## Wiki corrections needed (separate session, wiki repo)

- Resolve the session-content-layer vs qlp-srs-integration serving-path contradiction after the code trace.
- Rewrite product-current-state and path-to-revenue Phase 10 sections to the verified state; fix the P1 topic list (no Statistics).
- Collapse to one QLPQuestionContext contract, one 12-item backlog; rename one of the two Stage 1-4 sequences.
- Fix Edexcel remnants in runbook paths and frontend badge examples; confirm R2 vs Supabase for exam-document storage.
- Fix exam-lens.md's inverted tier semantics (Tier 1 is not "Easy").
- Re-verify and re-date the three load-bearing articles once seeding state is known.
