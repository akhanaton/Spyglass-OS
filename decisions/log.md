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

## 2026-05-13 — Spyglass OS as operating layer, not a parallel track

**Decision:** Prioritise getting Spyglass OS to "significant leverage" threshold before using it to deliver other priorities (production readiness matrix, SEO/Growth planning).

**Why:** Treating it as a force multiplier means all subsequent work benefits from it. Running it as a side project means it never reaches the leverage threshold.

**Alternatives considered:** Deliver production readiness matrix first, set up AIOS in parallel.

**Owner:** Enitan

---
