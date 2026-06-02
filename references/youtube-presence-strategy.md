# YouTube Presence Strategy — Holistic OS Integration Spec

Scoping spec for standing up a YouTube presence as a **core GEO/AI-citation channel**, and mapping every downstream effect on the OS. Deferred — gated on the production-model decision below. Created 2026-06-02.

**Linear epic:** [EP-78](https://linear.app/exampilot/issue/EP-78) (created 2026-06-02; sub-issues EP-79–EP-85). Product-repo schema work: [EP-86](https://linear.app/exampilot/issue/EP-86).
**Doctrine source:** Ahrefs 2026 AI-search findings → `wiki/marketing/growth/marketing-plan.md` v3.1, decision 19; `raw/marketing/ahrefs-ai-search-study-2026.md`
**Status:** SPEC — do not build skills until the production model is chosen

---

## Why This Exists

Ahrefs' 2026 study found **YouTube mentions are the single strongest correlate (0.737) of AI brand visibility** — ahead of backlinks, DR, and page count, across both Google and OpenAI products. That reframes YouTube from a minor distribution surface (previously only the India short-form variant in the marketing plan) into a primary AI-citation lever.

The marketing plan already absorbed the *strategy* (v3.1: KPI block + decision 19). This spec covers the *how* — which the plan does not address — because YouTube touches far more of the OS than a single KPI block: a new content artifact type, new skills, new workflow steps, new signals, a new connection, and an unresolved production-capacity question.

The point of this document is to make the full surface visible **before** we build anything, so we don't bolt video onto a text-only pipeline piecemeal.

---

## The Gating Decision: Production Model

**Nothing else gets built until this is chosen.** Neither founder produces video today. The lightweight entry point ("9709 topic explainers") can mean very different things:

| Model | What it is | Cost / effort | Pros | Cons |
|---|---|---|---|---|
| A. Faceless screencast | Screen-recorded worked solutions, voiceover (human or AI TTS), no on-camera presence | Lowest. ~30-60 min/video | Scales, no on-camera anxiety, fast | Lower trust/engagement, commodity feel |
| B. On-camera (Teresa) | Teresa presents (educator authority, ties to LinkedIn warm-up) | High. Setup + recording + editing | Highest trust, E-E-A-T, dual-use with LinkedIn | Capacity-bound to one person, slow cadence |
| C. Hybrid | Faceless explainers for volume + occasional Teresa pieces for authority anchors | Medium | Balances scale and trust | Two production tracks to maintain |
| D. Seed-only (no owned channel yet) | Get ExamPilot *mentioned* on established 9709 tutorial channels via outreach/partnership | Outreach time, no production | Captures the citation signal without production cost | No owned asset, depends on others |

**✅ DECIDED (2026-06-02):** **Model D in parallel with Model A** — seed mentions on existing 9709 channels (captures the 0.737 signal fastest, zero production) while standing up a faceless screencast channel for owned 9709 explainers to embed in blog posts. **Escalate to C** (add Teresa authority pieces) once cadence is proven. The gate is lifted; Phase 0 execution is unblocked. Logged in `decisions/log.md` 2026-06-02.

---

## OS Surface Map — Everything YouTube Touches

| # | Surface | Current state | Change required | Lives in |
|---|---|---|---|---|
| 1 | Marketing plan | ✅ v3.1 KPI block + decision 19 | None (done) | wiki |
| 2 | SEO plan (`seo-strategy`) | Touched for schema demotion | **Verify** YouTube is woven in as a GEO lever in the 90-day plan, not just referenced | wiki |
| 3 | Content pipeline | Text-article-centric | New video lifecycle: script → record → edit → thumbnail → upload → embed in blog → seed | OS |
| 4 | Frontmatter `type` enum | No video type | Add `youtube-script` / `video-explainer` to CLAUDE.md convention | OS (CLAUDE.md) |
| 5 | Skills | None for video | New `/youtube-script`; extend `/repurpose` (has TikTok placeholder); `/schema-markup` gains VideoObject | OS (.claude/skills) |
| 6 | KPIs / `/weekly-pulse` | YouTube not a tracked channel | Pull v3.1 KPI block into the Friday pulse; make YouTube a tracked channel | OS |
| 7 | GTM / signals | No YouTube source | New signals: views, comments (intent), YT→site referral, subscriber growth → signal-registry + Coda Signals | OS (gtm-engineering) |
| 8 | Connections | YouTube absent | Add channel; Phase 1 add YouTube Data API for analytics; no MCP today | OS (connections.md) |
| 9 | Channel playbooks / audience | No YouTube rules | Operational rules + per-persona video angle (9709 explainers first) | OS (marketing/context) |
| 10 | Voice / production | No on-camera model | Resolved by the gating decision above | — |
| 11 | Build-in-public boundary | X + LinkedIn sub-OS | Clarify: YouTube is **student-facing/marketing**, NOT build-in-public. Lives in `marketing/`, not `build-in-public/` | doc note |

### The two non-obvious dependencies

1. **Production capacity is the real blocker, not strategy.** See gating decision. "Seed on established channels" is also an outreach/partnership motion, not just publishing — it overlaps `/outreach-draft` and the outreach-crafter agent.
2. **Schema irony.** We are *demoting* schema as a citation lever (the parallel code-repo loop), but **VideoObject schema on a video-hosting page is one case where schema still earns its keep.** The same `/schema-markup` skill is touched by both efforts — sequence them together.

---

## Skills Required (build only after production model is chosen)

| Skill | New / extend | Purpose |
|---|---|---|
| `/youtube-script` | New | Generate a 9709/0580 explainer script from a topic or existing article. Answer-first, exam-board-specific, [VERIFY] flags on board facts |
| `/repurpose` | Extend | Replace the "TikTok script placeholder" with real YouTube + short-form output; generate a video script + blog-embed snippet from a published article |
| `/schema-markup` | Extend | Add VideoObject schema for pages that embed a video |
| `/weekly-pulse` | Extend | Add YouTube as a tracked channel with the v3.1 KPIs |
| `/signal-review` | Extend | Ingest YouTube signals (views, comments, referral) into the Coda Signals table |

---

## KPI Integration (from marketing-plan v3.1)

These already exist in the plan but are not yet wired into any ritual:

- Own explainer videos published (target: 1-2 total → 1-2/month → 2-4/month)
- Videos embedded in blog posts (where applicable → most → all topic pages)
- Videos published/week (3-5 once scaled)
- Average views/video (200-500 → 1,000-5,000)

Informational-content caveat applies: YouTube's primary value is **citation footprint + brand search**, co-equal with views. Don't read a soft view count as failure if citation share / brand search are climbing.

---

## GTM / Signal Integration

Add to `marketing/gtm-engineering/signal-registry.md` and the Coda Signals table:

| Signal | Category | Why it matters |
|---|---|---|
| Video views (per video, trend) | Engagement | Reach proxy; feeds content-priority |
| YouTube comments | Intent / community | Real student questions → content ideas + persona validation |
| YT → site referral (UTM) | Behavioral | Channel attribution; PostHog |
| Subscriber growth | Brand | Brand-build proxy |
| YouTube mentions of "ExamPilot" | Citation footprint | The 0.737 lever itself — track appearances on third-party channels |

Phase 0 = manual logging (consistent with current GTM Phase 0). Phase 1 = YouTube Data API auto-pull.

---

## Phasing

**Phase 0 (lightweight, gated on production decision):**
- Seed ExamPilot mentions on 2-3 established 9709 tutorial channels (Model D)
- Produce 1-2 faceless 9709 explainers (Model A), embed in matching published blog posts
- Add VideoObject schema to those pages
- Manual KPI + signal logging in `/weekly-pulse` and Coda

**Phase 1 (post-cadence-proof):**
- Build `/youtube-script`, extend `/repurpose`
- Wire YouTube Data API into connections + `/signal-review`
- Decide on Model C escalation (Teresa authority pieces)
- Add YouTube to the content calendar cadence

---

## Linear Epic (created 2026-06-02)

**Parent — [EP-78](https://linear.app/exampilot/issue/EP-78): YouTube presence as a core GEO/citation channel** — assignee: Enitan

Sub-issues (all assigned to Enitan):
- [EP-79](https://linear.app/exampilot/issue/EP-79) — Choose production model — ✅ **DONE**: D + A in parallel, escalate to C once cadence proven
- [EP-80](https://linear.app/exampilot/issue/EP-80) — Seed ExamPilot on 2-3 established 9709 tutorial channels (outreach) — Todo
- [EP-81](https://linear.app/exampilot/issue/EP-81) — Produce + publish 1-2 faceless 9709 explainers, embed in matching blog posts — Todo
- [EP-82](https://linear.app/exampilot/issue/EP-82) — Add VideoObject schema to video-hosting pages (product repo + `/schema-markup`) — Todo, **blocked by EP-86**
- [EP-83](https://linear.app/exampilot/issue/EP-83) — Add YouTube channel + KPIs to `/weekly-pulse` and signal-registry/Coda — Todo
- [EP-84](https://linear.app/exampilot/issue/EP-84) — (Phase 1) Build `/youtube-script` + extend `/repurpose` — Backlog
- [EP-85](https://linear.app/exampilot/issue/EP-85) — (Phase 1) Wire YouTube Data API into connections + `/signal-review` — Backlog

**Related (schema doctrine, not YouTube):** [EP-86](https://linear.app/exampilot/issue/EP-86) — Product repo: de-emphasise schema as an AI-citation signal (`JsonLd.tsx`) — Todo, blocked on product-repo access.

---

## Success Criteria (Phase 0)

- [ ] Production model chosen and logged in `decisions/log.md`
- [ ] ExamPilot mentioned on ≥2 established 9709 channels
- [ ] ≥1 owned explainer published and embedded in a matching blog post with VideoObject schema
- [ ] YouTube appears as a tracked channel in `/weekly-pulse`
- [ ] YouTube signals logged in Coda Signals table
- [ ] `seo-strategy` confirmed to carry YouTube as a GEO lever

---

## What NOT To Do

- Do not build `/youtube-script` or wire the API before the production model is chosen (EP-YT-1).
- Do not file YouTube under `build-in-public/`. It is a student-facing marketing/GEO channel, not founder build-in-public (which is X + LinkedIn only).
- Do not reintroduce schema as a citation lever — VideoObject is for the video-hosting page's rich results, consistent with the 2026-06-02 schema doctrine change.
- Do not treat view count as the primary KPI — citation footprint + brand search are co-equal for this informational channel.

---

## Cross-References

- `wiki/marketing/growth/marketing-plan.md` — v3.1, YouTube KPI block, decision 19
- `wiki/marketing/seo/seo-strategy.md` — GEO levers (verify YouTube woven in)
- `wiki/marketing/seo/llm-seo-mechanics.md` — schema demotion, answer-first lever
- `marketing/gtm-engineering/signal-registry.md` — signal additions
- `.claude/skills/schema-markup/SKILL.md` — VideoObject + 2026-06-02 doctrine note
- `references/exam-season-intelligence-sprint.md` — EP-77, the parallel-track spec pattern this mirrors
