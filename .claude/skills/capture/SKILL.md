---
name: capture
description: Use when you want to save something — a document, research finding, decision, URL, or conversation excerpt — to either Spyglass OS or spyglass-wiki. Handles classification, templating, drafting, commit, and lint in one command. Trigger on "capture this", "save this to the wiki", "ingest this", "where does this go", or any request to preserve a piece of knowledge. One run = one saved artifact.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
  The Three Ms of AI™ is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*

## What this skill does

Collapses the 4-step OS↔wiki capture pipeline (classify → template → draft → ingest + lint) into one command. You identify something worth keeping; `/capture` handles where it goes and how it gets there. You review the draft before anything commits.

**Bike Method Phase 1:** Run manually and review every draft. Do not advance to Phase 2 until you've run this 5+ times and trust the classification and draft quality.

## When `/capture` runs

Any time you want to preserve a piece of knowledge:
- A document, research finding, or article you've been reading
- A decision just made (offers to write a `decisions/log.md` entry)
- A conversation excerpt worth keeping
- A URL pointing to reference material
- Any "I should remember this" moment

## Execution — six steps

### Step 0 — Read wiki conventions

Before anything else, fetch AGENTS.md from the wiki:

```bash
gh api repos/akhanaton/spyglass-wiki/contents/AGENTS.md --jq '.content' | base64 -d
```

Hold the article templates and conventions in context for the full run. Do not re-fetch.

### Step 1 — Receive content

The user provides one of:
- Pasted text or a document
- A local file path (read with Read tool)
- A URL (fetch with WebFetch)
- A description of what to capture

If nothing is provided alongside the command, ask: *"What do you want to capture? Paste the content, give me a file path, or describe it."*

### Step 2 — Classify destination

Answer two questions and show the answer before proceeding.

**Q1 — OS or wiki?**

| Goes to OS (`Spyglass-OS`) | Goes to wiki (`spyglass-wiki`) |
|---|---|
| Identity, voice, per-machine config | Business knowledge, architecture |
| Connection registry, env vars | Decisions and the reasoning behind them |
| Priorities, role, personal context | How systems work, specs, research findings |
| Operational runbooks for Enitan/Teresa | Anything a future team member needs |

**Q2 — If wiki → which article type?** (per AGENTS.md template list — read in Step 0)

Show the user: *"I'll save this as [type] → [OS path or wiki article slug]. Reason: [one sentence]. Confirm?"*

Do not proceed to Step 3 until confirmed. If the user redirects the destination, update and re-confirm.

### Step 3 — Draft the artifact

**If OS file:** Write to the confirmed path using the Write tool. Show the content first and get confirmation. Skip to Step 5.

**If wiki article:** Draft using the correct template from AGENTS.md. Requirements:
- Correct frontmatter (all required fields per template)
- Correct heading structure
- No placeholder text — fill every section, or omit with a `<!-- TODO: -->` comment
- `[VERIFY]` flags on any factual claim not directly sourced from the input content
- Internal links to related articles using wiki slug conventions

Show the full draft. Ask: *"Does this look right? Any corrections before I commit?"*

Do not commit until explicitly approved.

### Step 4 — Commit to wiki

On approval, commit via gh api. Check for existing file first (to get SHA for update vs. create):

```bash
# Get SHA if file exists (fails silently if new)
SHA=$(gh api repos/akhanaton/spyglass-wiki/contents/{path} --jq '.sha' 2>/dev/null || echo "")

# Commit (omit sha field if empty — creates new file)
gh api repos/akhanaton/spyglass-wiki/contents/{path} \
  -X PUT \
  -f message="docs: add {article-title}" \
  -f content="$(printf '%s' '{content}' | base64)" \
  ${SHA:+-f sha="$SHA"}
```

Report: "Committed `{path}` to spyglass-wiki."

### Step 5 — Lint

Do not rely on a local wiki clone. Run lint entirely via `gh api` — this works for any operator (Enitan or Teresa) on any machine.

**Fetch the committed article back:**
```bash
gh api repos/akhanaton/spyglass-wiki/contents/{path} --jq '.content' | base64 -d
```

**Fetch the articles index to check for orphan / inbound-link status:**
```bash
gh api repos/akhanaton/spyglass-wiki/git/trees/main?recursive=1 --jq '[.tree[].path | select(endswith(".md"))]'
```

**Run lint checks inline** against the AGENTS.md rules already in context:
- All required frontmatter fields present and non-empty?
- Heading structure matches the template?
- Internal links resolve to real slugs in the index?
- Any `[VERIFY]` flags left unresolved?
- At least one inbound link from another article (or is this orphaned)?

Categorize issues:
- **Auto-fixable** (broken link to an existing article with a known slug, missing frontmatter field with an obvious deterministic value): fix via a second `gh api` PUT, report as "fixed N issues"
- **Needs your eyes** (orphan article with no inbound links, ambiguous `[VERIFY]` flag, missing required section with no clear fill): surface as a numbered list

If lint is clean, report: "Lint clean."

### Step 6 — Close

Output a one-screen summary:
- What was saved and where
- Lint result (clean / N auto-fixed / N need review)
- Ask: *"Log this as a decision in `decisions/log.md`?"* — only if the content is a decision or strategic choice
- Ask: *"Update `_session_context.md`?"* — always prompt this; the wiki state changed

## What this skill does NOT do

- Does not commit without explicit approval at Step 3
- Does not auto-advance to Phase 2 — edit `bike-method-phase` yourself when you're ready
- Does not modify existing wiki articles unless you explicitly direct it to update one

## Phase advancement guide

| Phase | What changes |
|---|---|
| **1 (now)** | Review every draft. Confirm every commit. |
| **2** | Auto-commit high-confidence article types (decisions, reference entries). Review only complex articles. |
| **3** | Auto-classify + auto-commit + async lint report. One-line capture, review batch weekly. |

Advance by editing `bike-method-phase` in this file and updating the execution steps above.
