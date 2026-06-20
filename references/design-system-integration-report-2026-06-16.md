# Design System Integration Report — 2026-06-16

**Topic:** Integrating ExamPilot Design System (Claude Design) into the OS, wiki, and product repo.
**Status:** Analysis complete. Integration approach decided. Migration partially in-flight.

---

## What we have

**Claude Design project:** "ExamPilot Design System" on claude.ai. Source of truth for the Flight Deck visual identity. Design work continues here. URL not yet registered in connections.md.

**Product repo branch:** `brand/flight-deck-identity` (local only, not pushed to remote as of 2026-06-16). Contains:
- `brand/BRAND-GUIDELINES.md` — supersedes `exampilot/DESIGN.md`; the full brand strategy + expression spec written to be executed by Claude Design
- `brand/exampilot-theme.css` — portable `@theme` + `.dark` token block; this is the Claude Design output landing zone
- `brand/assets/mark.svg`, `brand/assets/app-icon.svg` — starter logo geometry
- Updated `exampilot/app/globals.css` — Flight Deck tokens applied with legacy aliases for migration safety
- Updated `exampilot/components/ui/button.tsx` — CTA variant updated to use `--color-on-cta` (navy text on lime)
- Updated `exampilot/components/ui/icon.tsx`

**Current `exampilot/DESIGN.md`:** Still says "Source of truth" but is superseded by `brand/BRAND-GUIDELINES.md`. Needs a deprecation notice before the branch merges.

---

## Integration decision

**Approach: Option B — Claude Design as source of truth; portable tokens in product repo; one wiki article; connections.md entry.**

- **Claude Design:** source of truth (always). No copies of token values elsewhere.
- **`brand/exampilot-theme.css`:** the integration point — Claude Design output pastes here.
- **`exampilot/app/globals.css`:** applies those tokens plus product-specific additions (nav dimensions, KaTeX overrides, z-index fixes, keyframes) that Claude Design will never generate.
- **Wiki:** one article — design decisions, rationale, links to both Claude Design and `brand/exampilot-theme.css`. Does NOT copy token values.
- **OS `connections.md`:** add Claude Design URL (mechanism: `claude.ai design tool`).
- **`/tune` cadence:** add a quarterly check that `brand/exampilot-theme.css` is still in sync with Claude Design.

Claude Design → `brand/exampilot-theme.css` → diff against `globals.css @theme` → merge carefully preserving product-specific tokens → commit.

---

## What the Flight Deck migration has already solved

- Semantic token names preserved (same names, different values — no codebase-wide rename)
- Legacy aliases bridge old references: `--color-brand-violet → navy`, `--color-brand-rose → signal (lime)`, etc.
- `--color-on-cta: #0B1A2D` prevents white text on lime CTA (already in `button.tsx`)
- `brand/exampilot-theme.css` exists as the portable handoff file
- Dark mode strategy unchanged (`.dark` class)

---

## Remaining friction / what's not done

### 1. Hardcoded Tailwind color utilities (highest risk)
Legacy aliases fix CSS custom property references only. Any component using direct Tailwind utilities (`bg-violet-500`, `text-rose-400`, `border-violet-200`) will stay violet/rose. Run this before merging:
```bash
grep -r "violet\|rose\|purple" exampilot/app exampilot/components exampilot/features --include="*.tsx" -l
```

### 2. Only `button.tsx` and `icon.tsx` are updated
All other shadcn components in `components/ui/` are untouched. They'll pick up new semantic token values automatically — but any that hardcode Tailwind color classes or pass `text-white` on a CTA override will break visually.

### 3. Marketing pages (`(marketing)` route group) — not audited
Almost certainly has violet heroes and rose CTAs using Tailwind utilities directly. Most visible regression risk.

### 4. `exampilot/DESIGN.md` is a liability
Still says "Source of truth". Needs a deprecation notice pointing to `brand/BRAND-GUIDELINES.md` before the branch merges.

### 5. Claude Design → repo sync loop is not wired
No ritual or skill enforces the sync. Without one, Claude Design and the repo will drift. Need a skill or `/tune` ritual item.

### 6. Font decision unresolved
`--font-sans: 'Geist', 'Satoshi', system-ui` — if Geist is the intent, `layout.tsx` needs `next/font` loading for it. Confirm whether `layout.tsx` on the branch handles this.

---

## Recommended next steps (in order)

1. ~~Register Claude Design URL in OS `connections.md`~~ — done 2026-06-16 (row 27)
2. Run the Tailwind utility grep; fix any violet/rose hardcodes in the branch — **EP-128** (grep done: 2 false positives, blog aliases acceptable)
3. Add deprecation notice to `exampilot/DESIGN.md` — **EP-129**
4. Audit `(marketing)` route group visually in a browser on the branch — **EP-130**
5. Confirm `layout.tsx` loads Geist via `next/font` or explicitly fall back to Satoshi — **EP-131**
6. ~~Write wiki article: `design-system.md`~~ — done 2026-06-16 (`wiki/engineering/frontend/design-system.md`, article 158)
7. Push `brand/flight-deck-identity` and merge when visual audit passes — **EP-132** (gated on EP-128–131)
8. ~~Add quarterly design sync ritual to `/tune`~~ — done 2026-06-16 (tune/SKILL.md updated; runs March/June/September/December cycles)
