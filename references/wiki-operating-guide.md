# Spyglass Wiki — Operating Guide

> This guide governs how Teresa's OS (and any AI agent) reads from and writes to the Spyglass Wiki.
> Reference this whenever you are about to perform any wiki operation.
> The canonical constitution lives at `AGENTS.md` in the wiki repo — this guide is a usage layer on top of it.

---

## 1. What the wiki is

The wiki (`github.com/akhanaton/spyglass-wiki`) is the **single source of truth** for all durable business knowledge: engineering, product, marketing, operations, and the AI OS itself.

It is **not** a code repository. Code lives in `github.com/akhanaton/spyglass`.

---

## 2. Where to find it and what to read first

Access via GitHub CLI. At the start of every wiki session, fetch in this order:

```bash
# 1. The constitution — this is the wiki's CLAUDE.md / AGENTS.md equivalent.
#    It governs how ALL AI agents must behave inside the wiki repo.
#    Read it before any wiki operation.
gh api repos/akhanaton/spyglass-wiki/contents/AGENTS.md --jq '.content' | base64 -d

# 2. Hot cache — current wiki state (article count, recent changes, last write date)
gh api repos/akhanaton/spyglass-wiki/contents/_session_context.md --jq '.content' | base64 -d

# Any article on demand
gh api repos/akhanaton/spyglass-wiki/contents/wiki/{domain}/{slug}.md --jq '.content' | base64 -d
```

**`AGENTS.md` is the wiki's behavioral constitution.** It is the equivalent of a `CLAUDE.md` file for the wiki repo. Every AI agent working in or against the wiki must read it first — it defines identity, article templates, the three core operations (ingest / query / lint), and what the wiki is not for.

Always read `_session_context.md` at session start. It is a hot cache of current wiki state — article count, recently updated knowledge areas, last write date.

---

## 3. Wiki structure

```
spyglass-wiki/
├── raw/                  ← Immutable source materials. Never edit after filing.
├── wiki/                 ← AI-synthesised, continuously maintained knowledge articles.
│   ├── engineering/
│   ├── product/
│   ├── marketing/
│   ├── operations/
│   ├── business/
│   └── ai-automation-os/
├── archive/              ← Permanently retired topics only.
├── AGENTS.md             ← The constitution. Read first.
├── INDEX.md              ← Master table of contents.
├── log.md                ← Append-only log of all writes, ingests, and lints.
└── _session_context.md   ← Hot cache. Read at session start. Update at session end.
```

---

## 4. The four wiki skills

These skills only work when the **wiki repo is your current working directory**. From the OS session, use `gh api` directly (see §2) or switch to the wiki CWD.

| Skill | When to use |
|---|---|
| `/save` | After a key decision or conversation — converts it into a filed wiki article |
| `/ingest` | A new source has been added to `raw/` — process it into wiki articles |
| `/lint` | Weekly health check, or after any write — orphans, broken links, template violations |
| `/autoresearch` | Answering a complex research question across multiple wiki articles |

---

## 5. What goes in the wiki vs other tools

**Three-tool rule:**

| Tool | Use for |
|---|---|
| **Linear** | Tasks with owners and deadlines |
| **OS skills / rituals** | Recurring execution workflows |
| **Wiki** | Durable knowledge that outlasts any single task |

**Wiki = durable knowledge.** Ask: "Would this still be useful in 6 months?" If yes, it belongs in the wiki.

Examples of what belongs in the wiki:
- Architecture decisions (ADRs)
- Product strategy and specs
- "Why we built X this way"
- Channel playbooks and SEO strategy
- How the AI OS works
- Vendor context and integration notes
- Customer research and persona findings

**What does NOT belong in the wiki:**
- Draft code (belongs in the monorepo)
- Meeting notes that will never be synthesised (file to `raw/`, then `/ingest`)
- Personal opinions without supporting sources
- In-flight technical specs still under active development (keep in monorepo until shipped)
- OS file changes, OS skill/command counts, OS task lists

---

## 6. How to decide: wiki article vs raw source vs skip

| Content type | Action |
|---|---|
| Design spec, ADR, "why we built X" | File to `raw/`, then `/ingest` |
| Meeting notes with product/arch decisions | File to `raw/`, then `/ingest` |
| External/vendor reference material | File to `raw/`, then `/ingest` |
| Feature just shipped | Read the code directly, write `wiki/` article — no raw doc needed |
| Post-implementation code docs | Read code directly |
| Coverage debt (no article exists yet) | Explore agent against code, synthesise article |
| Transient OS state (task status, issue numbers) | `decisions/log.md` or OS git history — NOT the wiki |

---

## 7. The mandatory wiki write protocol

**After EVERY wiki write — no exceptions:**

1. Run targeted `/lint` on all new or modified articles. Fix every issue before recording state.
2. Append a one-line entry to `log.md` under today's date. Include the lint result.
3. Update `_session_context.md` — wiki state only (see §8).

Skipping this protocol is what causes wiki state to drift. The lint step catches template violations and broken cross-references before they compound.

---

## 8. What goes in `_session_context.md`

`_session_context.md` is a **wiki-state-only** hot cache. It is not a general OS journal.

**Write this:**
- Which articles were added or modified (wiki paths only)
- Current total wiki article count
- What key knowledge areas are now current
- Last updated date and the triggering wiki change

**Never write this:**
- OS file changes, OS command/skill counts, OS infrastructure state
- Linear issue numbers or task lists
- OS pending items or OS decisions
- Anything that belongs in `decisions/log.md` or the OS git history

**The routing rule:**
- OS decisions → `decisions/log.md`
- OS state → OS git history
- Wiki state → `_session_context.md`

---

## 9. Article template

Every `wiki/` article must contain all of these sections:

```markdown
---
title:
domain:
last_updated:
---

## Summary
<!-- 2-3 sentences. What is this? Why does it matter to Spyglass? -->

## Key Facts
<!-- Bullet list of the most important, durable facts. -->

## Detail
<!-- The full synthesised content. -->

## Counter-Evidence
<!-- What this doesn't support. Open questions. Known gaps. -->

## Cross-References
<!-- Use [[slug]] format where slug = filename without .md extension.
     Example: [[qlp-system]] — brief description of the relationship
     Do NOT use relative markdown paths. -->

## Sources
<!-- Links to raw/ documents this article is based on. -->
```

Cross-references use `[[slug]]` format — not relative markdown links. The only exceptions are `AGENTS.md`, `INDEX.md`, `log.md`, and `_session_context.md`, which keep relative links.

---

## 10. Archive rules

- `archive/` is for **permanently retired topics only**: a feature shut down, a vendor relationship ended, a channel abandoned.
- If a topic continues but the approach evolved, **update the article in place**. Git history preserves the old version.
- Agents **ignore `archive/`** unless explicitly asked to search it.

---

## 11. Two modes for keeping the wiki current

**Mode 1 — Feature just shipped:**
Read the relevant code directly and write the wiki article from the code. No raw doc needed. Set `verified_against_code: true`.

**Mode 2 — Coverage debt:**
Use INDEX.md as a backlog. Find topics with no article. Run an Explore agent against the relevant code directory, synthesise the article from the findings.

---

## 12. How to install this guide in Teresa's OS CLAUDE.md

Add the following block to Teresa's `CLAUDE.md`, inside or immediately after the knowledge base / wiki section:

```
## Wiki operating guide

The Spyglass Wiki lives at `github.com/akhanaton/spyglass-wiki`.

Before performing any wiki operation (read, write, ingest, lint, save, or session-end update):

1. Fetch and read AGENTS.md — this is the wiki's behavioral constitution (its CLAUDE.md):
   gh api repos/akhanaton/spyglass-wiki/contents/AGENTS.md --jq '.content' | base64 -d

2. Fetch and read _session_context.md — current wiki state hot cache:
   gh api repos/akhanaton/spyglass-wiki/contents/_session_context.md --jq '.content' | base64 -d

3. Read the full wiki operating guide (covers skills, what-goes-where, write protocol,
   article template, and _session_context.md rules):
   [Coda link — paste URL here once published]

Critical rules:
- Never update _session_context.md with OS state (only wiki state — see guide §8)
- Never skip the lint → log.md → _session_context.md sequence after any write
- OS decisions → decisions/log.md | OS state → OS git history | Wiki state → _session_context.md
```

---

## 13. Quick reference card

| Question | Answer |
|---|---|
| Where is the wiki? | `github.com/akhanaton/spyglass-wiki` |
| What to read first? | `AGENTS.md` (constitution) + `_session_context.md` (current state) |
| Just wrote something — what next? | `/lint` → `log.md` entry → `_session_context.md` update |
| New source to add? | File to `raw/[domain]/` → `/ingest` |
| Key decision just made? | Log to `decisions/log.md` in the OS, then `/save` to wiki if durable |
| Something permanently retired? | Move to `archive/` — never delete |
| Article cross-references? | Use `[[slug]]` format — not relative paths |
| OS state in `_session_context.md`? | Never. Wiki state only. |
| Skills work from OS session? | No — switch to wiki CWD, or use `gh api` directly |
