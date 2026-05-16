# Product Owner OS Layer — Infrastructure Assessment

**Date:** 2026-05-16  
**Owner:** Enitan  
**Stage:** Pre-launch → Alpha (100 students)  
**Linear issue:** EP-47

---

## Current state

The OS has a fully mature marketing + GTM brain — 29 skills, 21 Python modules, signal architecture, an 18-month strategy. That investment was right because marketing is Teresa's domain and it's execution-heavy. Product is different: at this stage, product is mostly making fast decisions, not running repeatable processes.

The OS currently has zero dedicated product infrastructure beyond what's implicit in the marketing plan and CLAUDE.md. That's not necessarily wrong — it means operating from instinct.

---

## Stage reality

Marketing runs continuously, in parallel, and needs Teresa to operate semi-independently. That justifies deep infrastructure. Product decisions at pre-launch are serial, low-frequency, and owned by one person (Enitan). Over-engineering this adds overhead with zero ROI until there are paying users generating real feedback.

The biggest product risk right now isn't missing infrastructure — it's not having a fast, structured way to go from **signal → decision → shipped**.

---

## Decision

Build a **thin, high-leverage layer** — approximately 15% the size of the marketing infrastructure. 2–3 commands, no new Python modules, no new agents.

The difference: marketing is a machine that runs continuously. Product at this stage is a *judgment layer* — the OS should help surface the right information fast and log decisions well, not automate the decisions themselves.

---

## Tier 1 — Wire immediately (integrations already exist)

### Linear MCP
- MCP is available in the harness but not in `connections.md` and has no commands
- Issues sitting in Linear are inaccessible to the OS — the most glaring gap
- **Action:** Add a `/backlog-review` command that pulls open issues, groups by priority, and sequences the week
- No skill needed — one command, Linear MCP calls

### PostHog (extend scope)
- Connected but scoped only to GTM signals
- **Action:** Add a thin `/product-pulse` command — weekly, 5 minutes — queries feature adoption rates, session depth, trial-to-return rates, and drop-off points
- No new integration needed — data infrastructure already exists

---

## Tier 2 — Build at Phase 1 (launch → first 100 users)

### `templates/prd.md`
- One PRD template — becomes critical when juggling 10+ ideas simultaneously
- Costs nothing to add pre-launch; pays off immediately at Phase 1

### `/spec` command
- Takes a feature idea and structures it as a Linear issue
- Must include: context, acceptance criteria, and a PostHog success metric baked in
- This is the handoff artifact between thinking and building

### `/product-review` ritual
- Weekly, runs after `/signal-review`
- Combines: Linear velocity (what shipped) + PostHog adoption (what got used) + one decision logged to `decisions/log.md`
- Keeps product and growth mode from bleeding into each other

### Coda Product Board view
- A Coda "Product Board" view (backlog + roadmap) so Teresa can see product state without needing Linear access
- Low lift — Coda MCP already connected

---

## Tier 3 — Don't build yet (useful at 200+ users)

| Item | Why not |
|---|---|
| Roadmap visualisation | Theatre at this stage — decisions happen in Linear and `decisions/log.md` |
| NPS automation | Meaningless at alpha; no reliable baseline until 200+ consistent users |
| Release notes automation | Useful at Phase 2+ when shipping frequency justifies it |
| Competitive product feature matrix | Premature until you know what features actually drive conversion |

---

## Integration status

| Integration | Status | Action |
|---|---|---|
| Linear | MCP available, not wired | Wire now — highest value product integration |
| PostHog | Connected (GTM scope only) | Extend to product queries, no new integration needed |
| Coda | Connected | Add Product Board view for Teresa visibility |
| Attio | Not connected | Phase 1 — first real user feedback loop |
| Dodo Payments | Not connected | Phase 1 — revenue signal feeds product decisions (which tier converts, at what price) |

---

## Acceptance criteria

**Tier 1 (do now):**
- [ ] Linear added to `connections.md`
- [ ] `/backlog-review` command created (pulls open issues, groups by priority, sequences the week)
- [ ] `/product-pulse` command created (PostHog queries: adoption, session depth, trial return rate, drop-off)

**Tier 2 (Phase 1 — at launch):**
- [ ] `templates/prd.md` created
- [ ] `/spec` command created (feature idea → structured Linear issue with context, AC, PostHog success metric)
- [ ] `/product-review` ritual command created (Linear velocity + PostHog adoption + decision log entry)
- [ ] Coda Product Board view created (backlog + roadmap, Teresa-accessible)

**Tier 3 (don't build):**
- [ ] ~~Roadmap visualisation~~
- [ ] ~~NPS survey automation~~
- [ ] ~~Release notes automation~~
- [ ] ~~Competitive product feature matrix~~

---

## Key principle

The OS should help surface the right information fast and log decisions well — not automate product decisions themselves. Wire Linear to close the gap between intent and execution. Extend PostHog to add one feedback loop. One weekly ritual to keep product and growth from bleeding into each other. That's it for now.
