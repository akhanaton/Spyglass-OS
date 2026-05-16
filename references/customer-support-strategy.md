# Customer Support Strategy — Infrastructure Assessment

**Date:** 2026-05-16  
**Owner:** Teresa (operations), Enitan (tooling)  
**Stage:** Pre-launch → Alpha (100 students)  
**Linear issue:** EP-48

---

## Current state

Nothing exists in the OS for customer support. Teresa owns it but has no tooling — no templates, no commands, no connected channels. Gmail, Discord, and Loom are all listed in `connections.md` as "not connected." Attio (CRM) isn't wired either.

---

## Stage reality

At alpha, "customer support" is not a support function. It's user research wearing a support costume. Every message a student sends is a product signal. The risk at this stage isn't operational overwhelm — it's **losing the insight** from those early conversations.

Support volume at 100 users will be low: 3–8 contacts per week. No ticketing infrastructure needed. The goal is making sure Teresa can respond fast and that neither person loses what those conversations are telling you about the product.

The second reality: students will primarily reach you on **Discord**, not email. Discord is synchronous and community-based — students will ask questions publicly, which means one good answer serves many. That channel has zero OS wiring right now.

---

## Decision

Build a **thin but purposeful layer** — not as thin as product, slightly thicker — because Teresa needs to operate this independently and support conversations have a direct product feedback loop that needs to be structured.

Target: 1 Coda table, 1 templates folder, 1 command, 2 connection entries. No new Python modules. No new agents.

---

## Tier 1 — Build now

### Discord → `connections.md`
- Primary student channel. Students will judge the product partly by how responsive and human you feel.
- Slow or robotic Discord responses damage trust before they've even tried the product properly.
- **Action:** Add Discord to `connections.md`. Teresa needs response templates accessible quickly.

### `templates/support/` folder
Common alpha scenarios to pre-draft:
1. `getting-started.md` — onboarding, how to navigate the product
2. `session-issue.md` — practice session not loading or behaving unexpectedly
3. `syllabus-question.md` — exam board / topic coverage questions
4. `billing.md` — pricing, cancellation (Phase 1, when payments are live)
5. `feedback-thanks.md` — acknowledging feature requests or bug reports
6. `discord-welcome.md` — standard welcome message for new server members

No skill needed. Simple markdown files Teresa grabs and adapts.

### Coda support log table
- Already have Coda connected — 20 minutes to build.
- Columns: student name/handle, channel, date, issue type, resolution, product insight
- The "product insight" field is the critical one — forces Teresa to ask "what does this tell us about the product?" for every contact
- Searchable record of everything alpha users struggled with; feeds directly into product prioritisation

### `/feedback-digest` command
- Weekly, Teresa or Enitan runs it
- Pulls from Coda support log + any Discord threads worth flagging
- Output: top 3 recurring issues, top 3 feature requests, top 3 moments of delight
- That output feeds the weekly `/product-review` (EP-47 Tier 2)
- This is the lever: turns support from a cost into a product intelligence function

---

## Tier 2 — Wire at Phase 1 (launch → first 100 users)

### PostHog in-app feedback survey
- A simple "something wrong?" or "rate this question" survey at key moments: after completing a topic, after a wrong-answer streak
- PostHog supports this natively — one afternoon to implement
- Generates passive signal at scale that Discord never will
- **Why Phase 1:** need users in the product first; no signal to capture pre-launch

### Attio CRM
- Once you're at 30–40 users and need to track individual user context across conversations: who they are, what they've tried, where they dropped off
- At sub-30 users you can hold this in the Coda support log
- Attio becomes worth the setup cost when conversations are too numerous to track manually
- Activation chain: PostHog behavioral signal → Attio contact enrichment → Brevo sequences (already planned in GTM Engineering)

---

## Tier 3 — Don't build

| Item | Why not |
|---|---|
| Zendesk / Intercom / Freshdesk | Designed for 500+ users with volume that exceeds what two people can handle conversationally. Overkill. |
| NPS surveys | Meaningless at alpha. Students don't have enough product experience to give reliable scores. One direct Discord conversation > 50 NPS responses. |
| Knowledge base / FAQ | Write this only once users keep asking the same 3 questions. Let the Coda support log tell you what those questions are first. |
| Ticketing system | Coda table is enough. Tickets imply a queue you're managing; at 3–8 contacts/week you're having conversations, not processing tickets. |

---

## Integration status

| Integration | Status | Action |
|---|---|---|
| Discord | Not connected | Add to `connections.md`, create `templates/support/discord-welcome.md` |
| Gmail | Not connected | Phase 1 — low volume pre-launch, Discord is the primary channel |
| Coda | Connected | Build support log table now |
| PostHog | Connected (GTM scope) | Extend to in-app feedback surveys at Phase 1 |
| Attio | Not connected | Phase 1 — contact enrichment + conversation tracking |
| Loom | Not connected | Phase 2 — async video support (useful for showing students how to use a feature) |

---

## Acceptance criteria

**Tier 1 (do now):**
- [ ] Discord added to `connections.md`
- [ ] `templates/support/` folder created with 6 templates (getting-started, session-issue, syllabus-question, billing, feedback-thanks, discord-welcome)
- [ ] Coda support log table created (student, channel, date, issue type, resolution, product insight)
- [ ] `/feedback-digest` command created (Coda support log + Discord → top 3 issues / requests / delights)

**Tier 2 (Phase 1 — at launch):**
- [ ] PostHog in-app feedback survey implemented (post-topic completion, post-wrong-answer streak)
- [ ] Attio wired for contact enrichment + conversation tracking (30–40 user threshold)
- [ ] Gmail added to `connections.md` and wired for support routing

**Tier 3 (don't build):**
- [ ] ~~Help desk (Zendesk, Intercom)~~
- [ ] ~~NPS automation~~
- [ ] ~~Knowledge base / FAQ~~
- [ ] ~~Ticketing system~~

---

## Key principle

At alpha, every support conversation is a research conversation. The infrastructure should be optimised for **insight capture**, not ticket resolution. If every support touchpoint flows into a weekly `/feedback-digest` that informs the product sprint, you've turned a cost centre into a competitive advantage — which matters when you're trying to out-serve incumbents who have large teams but terrible feedback loops.
