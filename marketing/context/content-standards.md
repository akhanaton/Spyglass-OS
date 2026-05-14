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
- [ ] No B2B school licensing messaging
- [ ] Internal links included (minimum 3 for blog articles)
- [ ] CTA present and appropriate for funnel stage
- [ ] Factually accurate for the specific exam board (Cambridge 9709 vs Edexcel IAL)
- [ ] No generic filler phrases ("in today's world", "it's no secret that", "at the end of the day")

## GEO Checklist (AI Search Optimization)

For all blog articles and landing pages:

- [ ] Answer-first structure: first 2-3 sentences after each H2 are a complete, extractable answer
- [ ] FAQPage schema: minimum 4 self-contained Q&A pairs per article
- [ ] Entity naming: spell out full names. "Cambridge International AS & A Level Mathematics 9709", "Edexcel International Advanced Level Pure Mathematics WMA11/WMA12"
- [ ] Cite official sources: link to Ofqual, Cambridge Assessment, Pearson exam board sites
- [ ] Conversational long-tail in FAQ: "what's the best app for Cambridge 9709 revision?"
- [ ] AI crawlers permitted: GPTBot, ClaudeBot, PerplexityBot, Google-Extended in robots.ts
- [ ] Key Takeaways block immediately after introduction (3-5 bullet points, standalone claims)

## Positioning Rules

**ExamPilot is:**
- A learning science tool built on spaced repetition, active recall, and knowledge mapping
- An exam readiness platform that tells students where they stand and what to do next
- Built specifically for Cambridge 9709 and Edexcel IAL A-Level Maths (at launch)

**ExamPilot is NOT:**
- An "AI tutor" or "AI wrapper"
- A generic study app
- A school/institution tool (no B2B messaging at this stage)
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
