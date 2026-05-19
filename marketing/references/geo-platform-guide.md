# GEO & AI Search Platform Guide

How to get ExamPilot cited in AI-generated answers across Google AI Overviews, ChatGPT, Perplexity, Gemini, and Claude. Adapted from marketingskills ai-seo skill + platform-ranking-factors + content-patterns references.

**When to use this:** When writing any content intended to surface in AI search results. Commands `/write-article` and `/research-keywords` reference this guide.

## Google's Official Position

Google's [AI features optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) is explicit on several points that affect how we apply this guide:

- **No special markup or files are required** for AI Overviews or AI Mode — traditional SEO signals and E-E-A-T are what Google uses
- **Don't write separate content "for AI"** — writing variants targeted at AI systems risks the scaled content abuse spam policy
- **Don't chunk content for AI** — normal paragraph and heading structure is correct; don't fragment pages to be more "AI-parseable"
- **No AI-specific Search Console reporting** — standard Performance, Coverage, and Core Web Vitals reports are what you measure Google AI performance with

**What this means for ExamPilot content:**
The structural patterns in this guide (40–60 word answer blocks, FAQ schema, comparison tables, query fan-out coverage) help **non-Google AI engines** (ChatGPT, Perplexity, Claude) materially. They also don't hurt Google — they're just good content organisation. For Google AI Overviews specifically, optimise for people and core Search. For ChatGPT/Claude/Perplexity, layer on the extractable structure. Both audiences served, different reasons.

When in doubt: write for people, organise for clarity.

---

## How AI Search Differs from Traditional SEO

Traditional SEO gets you ranked. AI SEO gets you **cited**.

A well-structured page can get cited even from page 2 or 3. AI systems select sources based on content quality, structure, and relevance, not just rank position.

| Stat | Source |
|---|---|
| AI Overviews appear in ~45% of Google searches | Google |
| AI Overviews reduce clicks to websites by up to 58% | Various |
| Brands are 6.5x more likely to be cited via third-party sources than their own domains | ZipTie |
| Optimized content gets cited 3x more often than non-optimized | Princeton GEO study |
| Statistics and citations boost visibility by 40%+ across queries | Princeton GEO study |

## The Three Pillars

### 1. Structure (make it extractable)

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Rules for ExamPilot content:**
- Lead every section with a direct answer. Don't bury it.
- Keep key answer passages to 40-60 words (optimal for snippet extraction).
- Use H2/H3 headings that match how students phrase queries ("How do I revise for Cambridge 9709 Paper 1?").
- Tables beat prose for comparison content.
- Numbered lists beat paragraphs for process content.
- Each paragraph should convey one clear idea.

### 2. Authority (make it citable)

The Princeton GEO study (KDD 2024, studied across Perplexity.ai) ranked optimization methods:

| Method | Visibility Boost | ExamPilot application |
|---|---|---|
| Cite sources | +40% | Link to exam board specs, Ofqual, official syllabi |
| Add statistics | +37% | Exam pass rates, topic frequency data, revision time stats |
| Add quotations | +30% | Student testimonials (with consent), teacher/examiner quotes |
| Authoritative tone | +25% | Write with demonstrated exam expertise |
| Improve clarity | +20% | Simplify complex maths concepts for revision context |
| Technical terms | +18% | Use correct exam board terminology (CIE, IAL, WMA11) |
| Fluency optimization | +15-30% | Natural readability |
| Keyword stuffing | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost.

### 3. Presence (be where AI looks)

AI systems cite where you appear, not just your site.

| Source | Citation share | ExamPilot action |
|---|---|---|
| Reddit | 1.8% of ChatGPT citations | Active in r/alevel, r/6thForm, r/CambridgeInternational |
| YouTube | Frequently cited by AI Overviews | Future: revision tip videos |
| Review sites | Varies | App store reviews, Trustpilot |
| Forums | Varies | Student forums, The Student Room |

## Platform-Specific Optimization

### Google AI Overviews

Pulls from Google's index. Strong E-E-A-T weighting. Only ~15% of AI Overview sources overlap with traditional Top 10 results.

**Priority for ExamPilot:**
- FAQPage schema on every blog post (30-40% visibility boost)
- Article schema with author, date, modification date
- Build topical authority through content clusters (Cambridge 9709 Paper 1 hub, Paper 3 hub, etc.)
- Target "how to" and "what is" query patterns (trigger AI Overviews most often)
- Author bios with exam teaching credentials

### ChatGPT

Uses Bing-based index. Domain authority matters more here than other platforms.

**Key signals:**
- Content-answer fit accounts for ~55% of citation likelihood (ZipTie study). Write the way ChatGPT would answer the question.
- Content updated within 30 days gets cited ~3.2x more often.
- Domain authority: sites with high referring domains average 8.4 citations per response.

**Priority for ExamPilot:**
- Update competitive content monthly
- Structure content conversationally (how ChatGPT formats its answers)
- Include verifiable statistics with named sources
- Clean heading hierarchy

### Perplexity

Always cites with clickable links. Most transparent. Uses curated authority lists and time-decay algorithm.

**Priority for ExamPilot:**
- FAQPage schema (JSON-LD) on every page with Q&A content
- Self-contained paragraphs that work as standalone answers
- Consider hosting PDF resources publicly (revision guides, topic summaries)
- Publishing velocity matters more than keyword targeting

### Microsoft Copilot

Bing-based. Embedded across Microsoft ecosystem.

**Priority for ExamPilot (lower priority overall):**
- Submit to Bing Webmaster Tools (not just GSC)
- IndexNow protocol for faster indexing
- Page speed under 2 seconds

### Claude

Uses Brave Search. Extremely selective about citations. Favors factually accurate, data-rich content.

**Priority for ExamPilot:**
- Verify content appears in Brave Search (search.brave.com)
- Allow ClaudeBot and anthropic-ai in robots.txt
- Maximize factual density: specific numbers, named sources, dated statistics

## Content Patterns for AI Citation

### Definition Block (for "What is X?" queries)

```markdown
## What is [Term]?

[Term] is [1-sentence definition]. [1-2 sentence expanded explanation]. [Why it matters for A-Level students].
```

### Step-by-Step Block (for "How to X" queries)

```markdown
## How to [Action]

[1-sentence overview]

1. **[Step]**: [Clear action in 1-2 sentences]
2. **[Step]**: [Clear action in 1-2 sentences]
3. **[Step]**: [Clear action in 1-2 sentences]
```

### Comparison Table Block (for "X vs Y" queries)

```markdown
## [A] vs [B]

| Feature | [A] | [B] |
|---|---|---|
| [Criteria] | [Value] | [Value] |

**Bottom line**: [1-2 sentence recommendation]
```

### FAQ Block (essential for FAQPage schema)

```markdown
### [Question phrased as students search]?

[Direct answer in first sentence]. [2-3 sentences of supporting context].
```

Tips: Use natural phrasing ("How do I..." not "How does one..."). Match "People Also Ask" queries. Keep answers 50-100 words.

### Self-Contained Answer Block (for AI extraction)

```markdown
**[Topic]**: [Complete answer that makes sense without surrounding context. Include specific details in 2-3 sentences.]
```

### Evidence Sandwich Block (maximum credibility)

```markdown
[Claim].

Evidence:
- [Data point with source]
- [Data point with source]
- [Data point with source]

[Concluding insight].
```

## ExamPilot-Specific GEO Tactics

### Education Content Domain Rules
- Cite official exam board specifications and syllabi
- Reference Ofqual data and exam statistics
- Include paper codes (9709/11, WMA11) for entity recognition
- Use "last updated" dates prominently
- Note exam windows and relevant dates

### Machine-Readable Files

Add to exampilot.io root:

**`/pricing.md`** — so AI agents can parse pricing without rendering JavaScript:
```markdown
# Pricing — ExamPilot

## Monthly
- Price: EUR29/month
- Features: All features, all exam boards

## Quarterly
- Price: EUR69/quarter (EUR23/month)
- Savings: 21% vs monthly

## Semi-Annual
- Price: EUR96/6 months (EUR16/month)
- Savings: 45% vs monthly

## Annual
- Price: EUR144/year (EUR12/month)
- Savings: 59% vs monthly
```

**`/llms.txt`** — context file for AI systems (see llmstxt.org) — Google doesn't require this for AI Overviews, but ChatGPT, Claude, and Perplexity actively use it

### AI Bot Access (robots.txt)

Allow these user agents:
```
User-agent: GPTBot
User-agent: ChatGPT-User
User-agent: PerplexityBot
User-agent: ClaudeBot
User-agent: anthropic-ai
User-agent: Google-Extended
User-agent: Bingbot
Allow: /
```

Block CCBot (Common Crawl) if you want. It's training-only, not search.

## Content Types That Get Cited Most

| Content Type | Citation Share | ExamPilot application |
|---|---|---|
| Comparison articles | ~33% | "ExamPilot vs tutoring", "Cambridge vs Edexcel" |
| Definitive guides | ~15% | "Complete guide to Cambridge 9709 P1" |
| Original research/data | ~12% | Exam topic frequency analysis, pass rate data |
| Best-of/listicles | ~10% | "Best A-Level maths revision tools" |
| How-to guides | ~8% | "How to revise for P3 mechanics" |

**Underperformers:** Generic posts without structure, marketing fluff, gated content, undated content, PDF-only content.

## Monitoring AI Visibility

### Manual Monthly Check (pre-tool)

1. Pick top 20 target queries
2. Run each through ChatGPT, Perplexity, and Google
3. Record: Are we cited? Who is? What page?
4. Track month-over-month in experiment log

### Tools (when budget allows)

| Tool | Coverage |
|---|---|
| Otterly AI | ChatGPT, Perplexity, Google AI Overviews |
| Peec AI | ChatGPT, Gemini, Perplexity, Claude, Copilot |
| ZipTie | Google AI Overviews, ChatGPT, Perplexity |

## AI Visibility Audit Checklist

For each priority page:

- [ ] Clear definition in first paragraph?
- [ ] Self-contained answer blocks?
- [ ] Statistics with sources cited?
- [ ] Comparison tables for "X vs Y" queries?
- [ ] FAQ section with natural-language questions?
- [ ] Schema markup (FAQPage, Article)?
- [ ] Recently updated (within 6 months)?
- [ ] Heading structure matches query patterns?
- [ ] AI bots allowed in robots.txt?

## Agentic Experiences

Autonomous AI agents are starting to access sites directly — reading, comparing, and acting on behalf of users without a human click. Google's AI optimization guide flags this as an emerging category.

**How agents access your site:**
- **Visual rendering** — screenshot/read the page as a user would
- **DOM inspection** — parse the page's HTML structure
- **Accessibility tree** — rely on semantic information assistive tech uses (labels, roles, landmarks, headings)

**What to do now:**
- Render meaningful content without heavy JS — if the page is blank until multiple frameworks finish loading, agents see blank
- Use semantic HTML: `<main>`, `<nav>`, `<article>`, `<button>`, proper heading hierarchy, `alt` text on all images
- Clean accessibility tree — every interactive element labelled; ARIA used correctly or not at all
- Visible pricing, specs, contact info on public indexable pages — anything an agent needs to make a recommendation should not be gated or JS-only
- This is where `/pricing.md` earns its keep: agents parsing pricing on behalf of a user comparing exam prep tools will cite whoever has readable pricing

**Forthcoming — Universal Commerce Protocol (UCP):** Google references UCP as a standardised protocol for commerce interactions (catalog discovery, pricing, checkout) that agents will use. No action needed yet — the structural work above is the right precursor.

---

Source: Adapted from coreyhaines31/marketingskills ai-seo skill v2.0.1 + content-patterns + platform-ranking-factors references. Google's official AI optimization guide (developers.google.com/search/docs/fundamentals/ai-optimization-guide).
