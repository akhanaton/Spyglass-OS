# Content Standards

Quality bar, review checklists, and positioning rules for all marketing content.

## AI Content Risk Matrix

| Workflow | Risk Level | Notes |
|---|---|---|
| Claude draft -> human review -> fact-check -> personal insight -> publish | Low | Standard workflow |
| Claude draft -> light edit -> publish | Medium | Helpful Content demotion risk |
| Bulk AI output -> auto-publish | High | Scaled Content Abuse policy violation |

Default: always use the low-risk workflow. Every draft gets human review.

## Review Checklist

Before any content moves from `drafts/` to `review/`:

- [ ] All [VERIFY] flags resolved with confirmed facts
- [ ] Voice matches `references/voice-house.md` (or voice-enitan.md for personal outreach)
- [ ] No "AI tutor", "AI wrapper", "AI-powered" language. Use "learning science", "spaced repetition", "active recall", "exam readiness"
- [ ] Pricing is correct: EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr. EUR only.
- [ ] No B2B school licensing messaging. School/teacher content uses referral-partner framing (B2C2B). See `references/voice-teacher.md`.
- [ ] If parent-facing: voice matches `references/voice-parent.md`
- [ ] If teacher/school-facing: voice matches `references/voice-teacher.md`. No B2B pricing/licensing language.
- [ ] If Facebook/WhatsApp: platform-appropriate formatting (shorter paragraphs, no markdown headers)
- [ ] Internal links included (minimum 3 for blog articles — initial estimate, adjust via `/tune`)
- [ ] CTA present and appropriate for funnel stage
- [ ] Factually accurate for the specific exam board (Cambridge 9709 vs Edexcel IAL)
- [ ] No generic filler phrases ("in today's world", "it's no secret that", "at the end of the day")

## GEO Checklist (AI Search Optimization)

For all blog articles and landing pages. Deep detail in `marketing/references/geo-platform-guide.md`.

### Structure (make content extractable)

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

- [ ] Answer-first structure: first 2-3 sentences after each H2 are a complete, extractable answer
- [ ] Key answer passages are 40-60 words (initial estimate — optimal for snippet extraction)
- [ ] H2/H3 headings match how students phrase queries ("How do I revise for Cambridge 9709 Paper 1?")
- [ ] Tables for comparisons, numbered lists for processes
- [ ] Key Takeaways block immediately after introduction (3-5 bullet points, standalone claims)
- [ ] FAQPage schema: minimum 4 self-contained Q&A pairs per article (initial estimate), conversational phrasing
- [ ] Use content patterns from geo-platform-guide.md: definition blocks, step-by-step blocks, comparison tables, evidence sandwich blocks

### Authority (make content citable)

Princeton GEO study visibility boosts (apply these to every article):

| Method | Boost | ExamPilot application |
|---|---|---|
| Cite sources | +40% | Link to exam board specs, Ofqual, official syllabi |
| Add statistics | +37% | Exam pass rates, topic frequency data |
| Add quotations | +30% | Student testimonials (with consent), teacher quotes |
| Authoritative tone | +25% | Demonstrated exam expertise |
| Keyword stuffing | **-10%** | **Never do this** |

- [ ] Entity naming: spell out full names. "Cambridge International AS & A Level Mathematics 9709", "Edexcel International Advanced Level Pure Mathematics WMA11/WMA12"
- [ ] Cite official sources: link to Ofqual, Cambridge Assessment, Pearson exam board sites
- [ ] Include specific statistics with named sources and dates
- [ ] Author bios with exam teaching credentials on blog posts
- [ ] "Last updated" date prominently displayed

### LLM Chunk Optimization (apply to every article)

Google and other AI systems do not read a page as a whole — they chunk it and attach ancestor heading context to each chunk. A poorly named heading makes that chunk invisible.

- [ ] **Ancestor headings rule**: Every H2 and H3 must be descriptive enough to stand alone. "Conclusion" → "Conclusion: Best Integration Techniques for 9709 P1". "Step 1" → "Step 1: Identify the Integration Method". Test: can a reader with no surrounding context understand the topic from this heading alone?
- [ ] **Conversational long-tail headers**: AI queries average 23 words. Include at least 2–3 H2s phrased as natural student questions ("How do I know which integration method to use in 9709 Paper 1?")
- [ ] **Explicit logical connectors for AI parsing**: Where relevant, use "Because X, Y happens." and "Unlike method A, method B does not require C." — these feed cross-attention models that handle causal relationships
- [ ] **Query fan-out coverage**: Each article should link out to related subtopic pages that would answer adjacent subqueries (e.g., integration article links to: by-parts page, definite integrals page, common mistakes page, past paper examples page)

### Technical

- [ ] AI crawlers permitted: GPTBot, ClaudeBot, PerplexityBot, Google-Extended in robots.ts
- [ ] FAQPage and Article schema markup on every blog post
- [ ] `/llms.txt` file on exampilot.io root (scope: key landing pages only, exclude /app, /dashboard, /docs) — note: Google doesn't require this for AI Overviews; it benefits ChatGPT, Claude, and Perplexity
- [ ] Page load time under 2 seconds
- [ ] Bing Webmaster Tools sitemap submitted — ChatGPT browses Bing; not indexed on Bing = invisible to ChatGPT (EP-57)

### GEO Don'ts (Google's official guardrails)

These are explicitly called out in Google's AI optimization guide as harmful to both traditional Search and AI features:

- [ ] No AI-specific content variants — same content serves people and AI; writing separate AI-targeted versions risks scaled content abuse policy
- [ ] No content chunked into AI-bait fragments — use normal paragraph + heading structure, not fragmented AI-optimised snippets
- [ ] No bulk AI-generated thin variations for ranking manipulation — AI-generated content is fine if it meets quality standards; mass-producing variants does not
- [ ] No inauthentic third-party mentions — real Reddit/Quora participation only; don't fabricate citations or spam communities for AI visibility
- [ ] AI crawlers not blocked — GPTBot, PerplexityBot, ClaudeBot, Google-Extended must remain unblocked if you want citation (block CCBot only if needed)
- [ ] Main content visible without JS — agents and AI crawlers see blank if content renders only after heavy JS; content must be in the HTML

## Positioning Rules

**ExamPilot is:**
- A learning science tool built on spaced repetition, active recall, and knowledge mapping
- An exam readiness platform that tells students where they stand and what to do next
- Built specifically for Cambridge 9709 and Edexcel IAL A-Level Maths (at launch)

**ExamPilot is NOT:**
- An "AI tutor" or "AI wrapper"
- A generic study app
- A school/institution tool (no B2B licensing or pricing -- ExamPilot is always consumer-purchased)
- A tutoring replacement (it complements tutoring, doesn't replace it)

**Competitor mentions:**
- Factual comparisons only. Never FUD (fear, uncertainty, doubt).
- Reference SaveMyExams, PapaCambridge, Physics & Maths Tutor as content-only (no adaptive learning).
- Highlight the unique combination: AI + knowledge graphs + misconception detection + spaced repetition + Socratic method + exam-board specific.

## Legal

- Target audience includes 16-18 year olds. GDPR/PECR compliance is mandatory.
- Testimonials require explicit consent. For under-18s, parental consent is recommended.
- Cookie consent banner required on all web properties.
- Recording consent (for Loom/interviews) requires explicit opt-in, not casual mention.
