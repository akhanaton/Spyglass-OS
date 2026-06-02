# Plan: EP-76 Content Pipeline Redesign — Universal Injection Endpoint

## Context

EP-76 ("Content pipeline redesign: unblock Teresa, fix Studio UX, improve image workflow") identifies three problems: Teresa cannot publish without Enitan's technical intervention, Sanity Studio UX is flat and confusing, and the image/asset workflow is disconnected.

The current EP-76 description proposes a Vercel API endpoint that "accepts `{type, document}` JSON body and calls `client.create()`". This undersells the complexity for non-blog content. The existing `scripts/create-content.mjs` pipeline does significant transformation before Sanity documents are created: 9 content-type plugins (1,132 lines), portable text builders (281 lines), asset upload with dedup (134 lines), and an orchestrator (70 lines). The API endpoint must run this same transformation, not just `client.create()`.

**Key finding from repo investigation:** The entire plugin layer is pure JavaScript data transformation with zero filesystem dependencies. Only two files touch the filesystem: `sanity-client.mjs` (reads `.env.local`) and `asset-uploader.mjs` (reads image files from disk). The plugins and helpers are already portable to Vercel serverless with zero modification.

**The design principle:** One endpoint, all content types, Teresa sees a Studio URL.

---

## Recommendation: Server-Side Transformation, Reuse Existing Plugin System

### Why this approach

1. **Zero code duplication.** The 9 plugins and helpers stay in `scripts/lib/`. The API route imports them directly (monorepo advantage). `create-content.mjs` continues to work for CLI use.

2. **Teresa's experience is invisible.** She runs a skill, approves the draft, says "inject this", gets a Sanity Studio URL. No Node.js, no tokens, no terminal commands.

3. **Not fragile.** The plugin system is battle-tested (it created all existing topic pages). The only new code is the API route handler (~100 lines) and a thin adapter (~30 lines). Everything else is reused.

4. **Handles all 9 content types.** The plugin registry (`scripts/lib/plugins/index.mjs`) routes automatically: topicPage, blogPost, hubPage, alternativePage, bestOfPage, featurePage, audienceSegmentPage, locationPage, qualificationSpoke.

### How blog posts enter the pipeline

`/write-article` produces markdown. All other skills produce content JSON via `/pre-write`. The blogPost plugin expects content JSON, not markdown.

**Solution:** The API endpoint accepts two formats:
- `format: "json"` (default) -- content JSON, passed directly to the plugin pipeline
- `format: "markdown"` -- markdown with YAML frontmatter, converted server-side to content JSON via a new `markdown-to-content.mjs` module, then routed to the blogPost plugin

This keeps `/write-article`'s human-readable markdown output unchanged. The conversion is narrow and predictable because `/write-article` follows a strict template.

---

## Architecture

```
Teresa runs skill
      |
      v
OS skill produces content
(markdown for blog, JSON for product pages)
      |
      v
Saves locally (backup + version control)
      |
      v
"Inject to Sanity?" -- user confirms
      |
      v
POST to /api/content/create
(content + base64 assets + bearer token)
      |
      v
API route:
  1. Validate auth (CONTENT_API_SECRET)
  2. Validate content type + required fields
  3. If format=markdown, convert to content JSON
  4. Upload/dedup assets via Sanity API
  5. Run plugin.parseContent() + plugin.buildDocument()
  6. Return { documentId, studioUrl }
      |
      v
Teresa opens Studio URL, reviews, publishes
```

### Code sharing (no duplication)

```
exampilot/app/api/content/create/route.ts
  imports from:
    exampilot/lib/sanity/content-pipeline.ts  (thin adapter)
      imports from:
        ../../scripts/lib/content-parser.mjs   (orchestrator)
        ../../scripts/lib/plugins/index.mjs    (plugin registry)
          imports:
            9 plugins (UNCHANGED, pure data transformers)
            sanity-helpers.mjs (UNCHANGED, pure functions)
```

The adapter (`content-pipeline.ts`) replaces the two filesystem-dependent modules:
- Creates a write-capable Sanity client from `process.env.SANITY_EDIT_TOKEN` (replaces `sanity-client.mjs`'s `.env.local` reading)
- Accepts base64 assets and decodes to Buffer (replaces `asset-uploader.mjs`'s `readFileSync`)

### Authentication

Bearer token (`CONTENT_API_SECRET`). Same pattern as the existing `SANITY_REVALIDATE_SECRET` webhook auth. The token lives in:
- Vercel env vars (server-side)
- Teresa's and Enitan's shell profiles (for Claude Code skills to read via `$CONTENT_API_SECRET`)

Teresa never sees or manages the token. Claude Code reads it from the environment and includes it in the HTTP call.

### Asset handling

Assets arrive as base64 strings in the POST body. The API decodes to Buffer, dedup-checks against Sanity (same GROQ query as existing CLI), uploads new assets, returns asset ID map to the plugin pipeline.

Size budget: Vercel body limit 4.5MB. Typical content JSON + 5 SVGs at 50KB each = ~500KB raw, ~665KB with base64 overhead. Well within limits.

---

## Implementation Phases

### Phase 1: API Endpoint + Adapter (~6h)

**New files:**

| File | Purpose | Lines (est.) |
|------|---------|-------------|
| `exampilot/lib/sanity/content-pipeline.ts` | Adapter: write client + re-exports from scripts/lib/ | ~40 |
| `exampilot/lib/sanity/asset-handler.ts` | Base64 decode + Sanity upload with dedup | ~60 |
| `exampilot/app/api/content/create/route.ts` | API route handler | ~120 |

**Modified files:**

| File | Change |
|------|--------|
| `exampilot/lib/env.ts` | Add optional `SANITY_EDIT_TOKEN` and `CONTENT_API_SECRET` to server schema |
| `exampilot/.env.local` | Add the two new tokens |
| `exampilot/next.config.ts` | Change `outputFileTracingRoot` from `__dirname` to `path.resolve(__dirname, '..')` so Vercel traces `scripts/lib/` imports |

**Unchanged (single source of truth):**
- `scripts/lib/content-parser.mjs`
- `scripts/lib/plugins/*.mjs` (all 9)
- `scripts/lib/core/sanity-helpers.mjs`
- `scripts/lib/plugins/index.mjs`
- `scripts/create-content.mjs` (CLI continues to work)

**Verification:** `curl` POST with an existing content JSON file (e.g., `scripts/content/topics/cambridge-9709-pure-1/integration.json`) creates a Sanity draft. Confirm document appears in Studio.

### Phase 2: OS Skill Integration for Product Pages (~2h)

**Modified files (Spyglass-OS repo):**

| File | Change |
|------|--------|
| `.claude/skills/pre-write/SKILL.md` | Add Step 6: "Inject to Sanity" (optional, on user instruction). Reads saved JSON, base64-encodes referenced assets, POSTs via curl, reports Studio URL. |

**Environment setup:**
- Add `EXAMPILOT_URL` and `CONTENT_API_SECRET` to Enitan's and Teresa's shell profiles (one-time)

**Verification:** Teresa runs `/pre-write topicPage "differentiation"` -> reviews scaffold -> says "inject this" -> sees Sanity Studio URL -> opens Studio, document is there as draft.

### Phase 3: Blog Post Markdown Support (~3h)

**New files:**

| File | Purpose |
|------|---------|
| `scripts/lib/core/markdown-to-content.mjs` | Converts /write-article markdown to blogPost content JSON |

**Modified files:**

| File | Change |
|------|--------|
| `exampilot/app/api/content/create/route.ts` | Add `format: "markdown"` handling (5-10 lines in the route) |
| `exampilot/lib/sanity/content-pipeline.ts` | Import and re-export markdown converter |
| `.claude/skills/write-article/SKILL.md` | Add Step 7: "Inject to Sanity" (optional, same pattern as pre-write) |

**Scope of markdown converter:** Only handles the patterns `/write-article` produces: `##`/`###` headings, paragraphs, bullet/numbered lists, blockquotes, callout blocks (bold-prefixed blockquotes), image references, LaTeX math blocks, FAQ sections. Not a general-purpose markdown parser.

**Verification:** Teresa runs `/write-article "cambridge 9709 quadratics"` -> reviews draft -> says "inject this" -> blog post appears in Sanity Studio as draft.

### Phase 4: Studio UX (~6-8h, from original EP-76 Phase 1)

| File | Change |
|------|--------|
| `studio-spyglass/sanity.config.ts` | Custom Structure tool: group into Blog Posts / Topic Pages / Hub Pages / Landing Pages / Settings. Hide dev-only types. |
| `studio-spyglass/schemaTypes/post.ts` | Add preview with status badge, move status field to top, add field groups (content / seo) |
| `studio-spyglass/schemaTypes/topicPage.ts` | Add preview config |
| `studio-spyglass/schemaTypes/objects/seo.ts` | Add character count validation (65 metaTitle, 160 metaDescription) |

**Verification:** Open Studio as Teresa. Confirm grouped navigation, status badges visible in document list, SEO field validation works.

### Phase 5: Sanity Growth Plan + Presentation Tool (~5h, from original EP-76 Phases 2-3)

- Upgrade to Growth plan ($30/month) for Scheduled Drafts, Comments, AI Assist
- Add `presentationTool` plugin for live preview
- Create draft mode API routes (`/api/draft-mode/enable`, `/api/draft-mode/disable`)

### Phase 6: Desmos Embeds + Diagram Checklist (~6h, from original EP-76 Phases 5-6)

- New `desmosBlock` schema type + React component
- Update `/pre-write` to output desmosBlock for function graphs
- Add `## Required Assets` checklist to `/pre-write` output

---

## Risks and Mitigations

| Risk | Mitigation |
|------|-----------|
| Vercel file tracing doesn't follow `../scripts/lib/` imports | Change `outputFileTracingRoot` to repo root. If still fails, add `experimental.outputFileTracingIncludes` in next.config.ts. Test on preview deployment before merging. |
| `.mjs` imports cause TypeScript issues | Next.js bundler handles .mjs natively. If type errors arise, add `scripts/lib/content-pipeline.d.ts` with exported function signatures. |
| `keyCounter` in sanity-helpers.mjs is module-level mutable state | Keys are document-scoped in Sanity, not global. Concurrent requests generating same keys in separate documents is safe. Add `resetKeyCounter()` export if needed. |
| Markdown converter is fragile for edge cases | Scope narrowly to /write-article patterns only. Not a general-purpose parser. Document the coupling. |
| Base64 assets exceed Vercel body limit | Current assets are SVGs (<100KB). If future content needs large images, add a separate `/api/content/assets` endpoint for pre-upload. Not needed now. |
| Teresa's env vars not configured | `/pre-write` and `/write-article` check for `$CONTENT_API_SECRET` and `$EXAMPILOT_URL` before attempting injection. Clear error message with setup instructions if missing. |

---

## Critical Files

**Spyglass product repo (to modify/create):**
- `exampilot/app/api/content/create/route.ts` -- CREATE
- `exampilot/lib/sanity/content-pipeline.ts` -- CREATE
- `exampilot/lib/sanity/asset-handler.ts` -- CREATE
- `exampilot/lib/env.ts` -- MODIFY (add 2 env vars)
- `exampilot/next.config.ts` -- MODIFY (outputFileTracingRoot)
- `scripts/lib/core/markdown-to-content.mjs` -- CREATE (Phase 3)
- `studio-spyglass/sanity.config.ts` -- MODIFY (Phase 4)

**Spyglass-OS repo (to modify):**
- `.claude/skills/pre-write/SKILL.md` -- MODIFY (add Step 6)
- `.claude/skills/write-article/SKILL.md` -- MODIFY (add Step 7)

**Unchanged (imported as-is):**
- `scripts/lib/content-parser.mjs`
- `scripts/lib/plugins/index.mjs` + all 9 plugin files
- `scripts/lib/core/sanity-helpers.mjs`
- `scripts/create-content.mjs`

---

## Verification (end-to-end)

1. **Product page (topic):** `/pre-write topicPage "differentiation"` -> scaffold saved -> "inject this" -> curl POST succeeds -> topic page draft in Sanity Studio with all fields populated, assets uploaded
2. **Product page (hub):** Same flow with hubPage type -> hub document with keyTopics linked
3. **Blog post:** `/write-article "cambridge 9709 integration by parts"` -> markdown draft saved -> "inject this" -> POST with `format: "markdown"` -> blog post draft in Sanity Studio with portable text body
4. **Asset dedup:** Inject a topic page twice -> second injection reuses existing Sanity asset IDs, no duplicates
5. **Error recovery:** Kill network mid-POST -> skill reports error with retry instructions -> `/inject` retries successfully
6. **Teresa walkthrough:** Teresa runs full flow on her machine with no Enitan intervention
