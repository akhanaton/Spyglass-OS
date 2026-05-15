# ExamPilot Marketing Plan: May 2026 - November 2027

**Version:** 2.0
**Owner:** Enitan & Teresa
**Review cadence:** Monthly review, quarterly recalibration
**Status:** Draft for review
**Last updated:** 2026-05-15

---

## 1. Executive Summary

This plan governs ExamPilot's marketing strategy for 18 months: from closed alpha (May 2026) through a full-scale organic growth engine (November 2027). The strategy is built on three core principles:

1. **Demand generation first, acquisition second.** Build awareness and trust with the 95% of students who aren't actively shopping before optimizing conversion for the 5% who are.
2. **One content asset, many channels.** Every piece of content is designed for repurposing across SEO, Reddit, TikTok, email, and AI search. No channel operates in isolation.
3. **Exam calendar is the metronome.** All marketing activity is timed to the A-Level exam cycle. Results Day, mock seasons, and resit windows are the highest-leverage moments in the year.

The plan is organized in four phases:

| Phase | Period | Focus | North Star |
|---|---|---|---|
| 0: Foundation | Mid-Jun-Jul 2026 | Content infrastructure, community seeding | Content Infrastructure Readiness Score (weighted composite) |
| 1: Soft Launch | Aug-Oct 2026 | Results Day campaign, first 100 students | Activated Trials (signup + first practice session) |
| 2: Growth Engine | Nov 2026-Mar 2027 | SEO compounding, email nurture, TikTok launch | Monthly Organic Signups |
| 3: Scale | Apr-Nov 2027 | Channel optimization, new markets | MRR |

**What this plan is:** The strategic framework. Channel priorities, phase gates, KPI definitions, and resource allocation.

**What this plan is not:** Daily operational playbooks. Those live in `marketing/context/` (channel-playbooks.md, content-standards.md). SEO technical architecture lives in the wiki (seo-strategy.md, content-strategy.md).

---

## 2. Strategic Foundation

### 2.1 Market Position

ExamPilot is a learning science platform for A-Level and IGCSE Maths students sitting international exam boards. At launch it covers Cambridge International 9709 Pure Mathematics 1 only. Coverage expands sequentially through the full CIE 9709 syllabus (Pure 3, Statistics 1, Statistics 2, Mechanics 1), then CIE 0580 IGCSE, and finally Edexcel International Advanced Level (IAL) across all units. CIE is the initial focus; Edexcel is sequenced after CIE coverage is substantially complete.

ExamPilot is not an "AI tutor" or content repository. The competitive moat is adaptive practice: spaced repetition (FSRS), knowledge mapping, misconception detection, and the Exam Readiness Index (ERI) that tells students exactly where they stand.

**Competitive gap we exploit:** Competitors (SaveMyExams, PapaCambridge, Physics & Maths Tutor) are static PDF repositories. They have content breadth but zero adaptive intelligence. ExamPilot is the only tool that gives a student a data-driven answer to "Where do I stand?" and "What do I do next?"

**Target geographies (in priority order, based on verified Cambridge International exam entry data):**

| Tier | Countries | Rationale |
|---|---|---|
| Tier 1 | Pakistan, UAE, India | Pakistan: 351K+ entries, 700+ schools, #3 globally, 34.5% of PapaCambridge traffic. UAE: near-universal internet, high willingness to pay, SaveMyExams's #3 market by traffic. India: 400-550+ schools, 65K+ entries (2022-23), 7-17% YoY growth. **Note: TikTok is banned in India** -- micro-funnel relies on SEO, Reddit, email, and direct outreach there. |
| Tier 2 | Malaysia, Egypt, Saudi Arabia, Bangladesh, Zimbabwe | Malaysia: 70.5K+ entries, strong November series market. Egypt: [VERIFY] historical "#1 IGCSE" claim from 2014 WES data cannot be confirmed from post-2020 Cambridge publications; Arabic primary language creates friction. Saudi Arabia: 130+ schools [2017/18 data, likely outdated], high purchasing power. Bangladesh: 23K+ entries, 150+ schools, significant payment/internet barriers. Zimbabwe: top November series country, 35% internet penetration limits reach. |
| Tier 3 | Indonesia, Singapore, Nigeria, Thailand, Vietnam, UK, Uzbekistan | Significant but smaller CIE markets. UK included for Edexcel IAL domestic demand. Uzbekistan on watch list (5.75% of PapaCambridge past papers traffic, unexplained by public Cambridge data). |

Sources: Cambridge International annual results press releases (2024, 2025), Tes Magazine, Cambridge facts and figures, SimilarWeb (PapaCambridge/SaveMyExams traffic analytics), DataReportal digital reports. Note: subject-level breakdowns by country (e.g., 9709 entries per country) are not publicly published by Cambridge; country-level total entries are the best available proxy.

US (#1 total entries) and China (#2) are excluded: US entries are primarily AICE diploma pathway in state schools (not exam-prep seekers), China has market access barriers for a consumer SaaS product.

**Currency/pricing consideration:** EUR pricing creates significant barriers in Pakistan (PKR), Egypt (EGP), Bangladesh (BDT), and Zimbabwe (ZWL). Monitor conversion data by country in Phase 2. If specific markets show high interest but low conversion, evaluate purchasing power parity pricing in Phase 3+.

### 2.2 Demand Generation vs Customer Acquisition

These two motions operate at opposite ends of the funnel and require different tactics, timelines, and KPIs.

| Dimension | Demand Generation | Customer Acquisition |
|---|---|---|
| Funnel position | Top (awareness, education) | Bottom (conversion, close) |
| Audience | 95% who don't know they need us yet | 5% actively evaluating solutions |
| Timeline | Months to years (compounds) | Days to weeks (immediate) |
| Goal | Create interest and pipeline | Convert pipeline to revenue |
| Cost profile | Lower per touchpoint, higher time investment | Higher per conversion, faster payback |
| ExamPilot tactics | SEO, TikTok, Reddit value posts, blog | Free trial, landing page, email nurture, tutor referrals |

**The critical insight:** Demand generation without acquisition wastes leads. Acquisition without demand generation caps your pipeline at the tiny fraction of students who already know they need an adaptive study tool. Both must run simultaneously but at different intensities depending on the phase.

**The allocation is not static -- it pulsates with the exam calendar.** Exam windows (Results Day, mock season, pre-exam) are always acquisition-heavy. Quiet periods (December, post-exam summer) are always demand-gen-heavy.

| Month | Demand Gen | Acquisition | Why |
|---|---|---|---|
| Jun 2026 | 60% | 40% | Building content infrastructure + tutor outreach |
| Jul 2026 | 50% | 50% | Publishing + Results Day prep |
| Aug 2026 | 30% | 70% | Results Day -- everything converts |
| Sep 2026 | 40% | 60% | Resit window -- active conversion |
| Oct 2026 | 50% | 50% | Resit winds down, SEO resumes |
| Nov 2026 | 60% | 40% | TikTok launches, SEO deepens |
| Dec 2026 | 70% | 30% | Holiday lull -- build content for mock season |
| Jan 2027 | 60% | 40% | Mock season begins |
| Feb-Mar 2027 | 50% | 50% | Mock season peak, pre-exam buildup |
| Apr-May 2027 | 30% | 70% | Exam month -- full conversion mode |
| Jun-Jul 2027 | 60% | 40% | Post-exam -- prep for August Results Day |
| Aug 2027 | 30% | 70% | Results Day 2 -- second-year campaign |
| Sep-Nov 2027 | 40% | 60% | Resit window + channel optimization |

### 2.3 The Micro-Funnel Architecture

Four discovery channels form an interlocking micro-funnel. Each channel plays a specific role and reinforces the others:

```
TikTok (emotional discovery: "oh this exists")
    ↓ triggers search
Reddit (peer validation: "is it actually good?")
    ↓ builds trust
SEO (intent capture: "how do I solve my problem?")
    ↓ feeds citations
AI Search (recommendation: "what should I use?")
    ↓ pre-sold visitor
Website → Trial → Paid
```

**How they feed each other:**
- SEO content gets cited by AI tools (Google AI Overviews, ChatGPT, Perplexity)
- Reddit threads rank on Google and feed AI training data
- TikTok drives curiosity that triggers search on Google and Reddit
- AI Search aggregates all three into recommendations

**The end goal:** A warm, pre-qualified visitor arriving at exampilot.io with high intent and pre-built trust. This is "zero-click nurturing" — the student is already sold before they click through.

### 2.4 Full B2C Funnel Mapping

The micro-funnel sits inside the broader B2C customer lifecycle:

| Stage | Consumer Mindset | Channel | Primary Goal | Success Metric |
|---|---|---|---|---|
| Awareness | "Never heard of you" | TikTok, SEO, Reddit | Reach | Impressions, new visitors |
| Consideration | "Interesting, tell me more" | Blog, comparison pages, Reddit threads | Educate and build trust | Time on site, return visits, AI citations |
| Intent | "I want this. Is it you?" | Landing page, free trial, AI Search | Remove friction | Trial signups |
| Purchase | "I'm in" | Checkout, onboarding | Smooth conversion | Trial-to-paid rate |
| Retention | "Was it worth it?" | In-app, email | Repeat behaviour | D7/D30 retention, session depth |
| Advocacy | "I love this" | Referral, reviews, word of mouth | Organic growth | NPS, referral rate |

Each channel strategy below maps to one or more of these stages.

---

## 3. Channel Strategy

### 3.1 SEO Strategy

SEO is the long-term compounding engine. It takes 3-6 months to gain traction but delivers the lowest-CAC acquisition at scale. ExamPilot's SEO strategy uses four distinct approaches, each targeting a different type of search intent.

#### 3.1.1 Pillar and Spoke (Topical Authority Clusters)

**What it is:** A hub-and-spoke content architecture where one comprehensive pillar page (4,000+ words) links to 8-12 focused spoke articles. This signals to Google that ExamPilot is the topical authority for a given exam specification.

**ExamPilot implementation:**

| Cluster | Pillar Page | Spokes | Priority |
|---|---|---|---|
| Cambridge 9709 Pure 1 | "Cambridge 9709 Pure Mathematics 1: Complete Revision Guide" | Differentiation, Integration, Functions & Graphs, Trigonometry, Coordinate Geometry, Quadratics, Series & Circular Measure + strategy spokes (How to Pass, Common Mistakes, Best Resources) | P0 (Phase 0) -- launch focus |
| Cambridge 9709 Pure 3 | "Cambridge 9709 Pure Mathematics 3: Complete Revision Guide" | Complex Numbers, Vectors in 3D, Differential Equations, Integration (Advanced), Numerical Methods, Algebra (Modulus & Polynomials), Logarithmic & Exponential Functions, Trigonometry (Advanced) | P1 (Phase 2) |
| Cambridge 9709 Statistics 1 | "Cambridge 9709 Statistics 1: Complete Revision Guide" | Representation of Data, Measures of Central Tendency & Variation, Probability, Permutations & Combinations, Discrete Random Variables, Binomial Distribution, Normal Distribution | P2 (Phase 2-3) |
| Cambridge 9709 Statistics 2 | "Cambridge 9709 Statistics 2: Complete Revision Guide" | Poisson Distribution, Linear Combinations, Continuous Random Variables, Sampling & Estimation, Hypothesis Testing | P3 (Phase 3) |
| Cambridge 9709 Mechanics 1 | "Cambridge 9709 Mechanics 1: Complete Revision Guide" | Forces, Equilibrium, Kinematics, Newton's Laws, Energy/Work/Power, Momentum | P4 (Phase 3) |
| CIE 0580 IGCSE | "IGCSE Mathematics 0580: Complete Revision Guide" | Number, Algebra, Geometry, Statistics, Probability, Functions, Trigonometry, Vectors, Mensuration | P5 (Phase 3+) |
| Edexcel IAL Pure 1 (WMA11) | "Edexcel IAL Pure Mathematics 1: Complete WMA11 Revision Guide" | (deferred until CIE 9709 + 0580 complete) | P6 |
| Edexcel IAL Pure 2-4 | WMA12, WMA13, WMA14 | (follows WMA11 cluster pattern) | P6 |
| Edexcel IAL Mechanics 1-3 | WME01, WME02, WME03 | (follows cluster pattern) | P7 |
| Edexcel IAL Statistics 1-3 | WST01, WST02, WST03 | (follows cluster pattern) | P7 |

**Exam board scope note:** At launch, ExamPilot covers CIE 9709 Pure 1 only. SEO clusters are built sequentially matching the product expansion order (see Section 10). Each cluster is substantially complete before the next begins. Edexcel IAL content follows the same cluster architecture but covers 10 units (P1-P4, M1-M3, S1-S3) and is sequenced after full CIE coverage.

**Linking architecture:**
- Every spoke links to its parent pillar
- Every pillar links to all its spokes
- Cross-cluster links where topics overlap (e.g., Integration appears in both Pure 1 and Pure 3)
- Internal links from blog articles to relevant cluster pages

**Keyword targeting by difficulty:**
- Month 1-2: KD 0-20 (paper code + topic, near-zero competition)
- Month 3-4: KD 15-25 (long-tail informational)
- Month 5-6: KD 25-35 (pillar-level head terms)
- Month 7+: KD 30-45 (competitive head terms, only if domain authority supports it)

#### 3.1.2 Product-Led SEO

**What it is:** Using ExamPilot's unique product data and capabilities to create content that only we can produce. This is the most defensible form of SEO because competitors cannot replicate the content without building the same product.

**ExamPilot implementation:**

| Content Type | Source | Example | Funnel Stage |
|---|---|---|---|
| Aggregate performance insights | Anonymized student data | "The 5 Cambridge 9709 Pure 1 Topics Where Students Lose the Most Marks" | TOFU (awareness) |
| Difficulty benchmarks | Question DNA analysis | "Cambridge 9709 Paper 1 2024: Question-by-Question Difficulty Rating" | MOFU (consideration) |
| Misconception reports | Misconception detection engine | "The 3 Most Common Integration Mistakes on Cambridge 9709 (and How to Fix Them)" | MOFU (consideration) |
| Free tools | Product capabilities, unbundled | Interactive revision timetable generator, grade boundary calculator, topic coverage checker | MOFU → BOFU (conversion) |
| Examiner report analysis | AI analysis of public examiner reports | "What the 9709 Examiner Report Actually Tells You About Paper 1 2024" | TOFU/MOFU |

**Why this works:**
- Creates genuinely unique content (not AI-generated rewrites of competitor material)
- Naturally leads to product trial (you see the data, then want the tool)
- Compounds as the user base grows (more students = better data = better content)
- Defensible: competitors cannot replicate without building the same product

**Phased deployment:**
- **Phase 0-1 (pre-data): Bridge content.** Examiner report analysis, curriculum analysis, and Question DNA applied to historical papers. This is not yet product-led in the strictest sense, but it demonstrates analytical capability, establishes content formats, and captures search queries that product-led content will later dominate.
- **Phase 2 (100+ students): Early insights.** Aggregate topic difficulty rankings, most common misconceptions detected, time allocation patterns. Combine real anonymized data with examiner report analysis for the first "State of Cambridge 9709" report.
- **Phase 3 (500+ students): Full product-led content.** Statistically meaningful difficulty benchmarks, ERI distributions by grade, Question DNA reasoning patterns, predictive content ("Based on ExamPilot data, these are the 5 topics most likely to cost you marks").

The compounding effect: more students = better data = better content = more AI citations = more students. By Phase 3, every product-led page carries a moat competitors cannot replicate without building the same platform.

**Free tools priority (build order):**

| Tool | Effort | SEO Value | Conversion Value |
|---|---|---|---|
| Revision timetable generator | Medium | High (searches: "revision timetable A-Level") | Medium |
| Grade boundary calculator | Low | Medium (searches: "9709 grade boundaries") | Low |
| Topic checklist (syllabus coverage) | Low | Medium | High (shows gaps → motivates signup) |
| Practice question sampler | Medium | High (searches: "9709 practice questions") | Very high (taste of product) |

#### 3.1.3 Programmatic SEO

**What it is:** Using templates and data to auto-generate hundreds of pages targeting long-tail keyword patterns. Each page targets a specific, low-competition query with enough unique content to avoid thin content penalties.

**ExamPilot implementation:**

**Past Paper Landing Pages (P0 priority):**
- URL pattern: `/past-papers/9709/[paper-code]/[year]/`
- Scale: 120-180 pages (Cambridge 9709), 60-90 pages (Edexcel IAL, deferred)
- Each page must include 300+ words of unique content: AI difficulty rating, topic-by-topic breakdown, common misconceptions per question type, estimated time allocation, related questions from other years
- Enrichment source: ExamPilot's Question DNA analysis and examiner report insights
- **noindex-until-enriched protocol:** Bulk-create page structures via Sanity mutation API with structural data only (paper code, year, session, topic mapping). Mark as `noindex`. Enrich 20-30 highest-priority pages first (most recent years, Pure 1 papers) with unique summaries, difficulty ratings, and misconception data. Human review before removing `noindex`. As student data accumulates, replace AI difficulty estimates with real benchmarks.

**Paper x Topic Landing Pages:**
- URL pattern: `/cambridge/9709/pure-1/[topic]/`
- Scale: 8 topics x 2+ specifications = 16+ core pages, expanding to 30-40
- Each page combines: topic overview, key formulas, exam tips, common mistakes, related practice

**Comparison Pages:**
- URL pattern: `/vs/[competitor]/`
- Targets: save-my-exams, papacambridge, physics-maths-tutor
- High commercial intent, thin competition for Cambridge 9709 specific variants
- Factual comparisons only. No FUD.

**Quality safeguard:** Every programmatic page goes through the same content review pipeline as manually written articles. No auto-publish. The enrichment data from Question DNA and examiner reports is what makes these pages valuable rather than thin.

#### 3.1.4 Location-Based SEO

**What it is:** Targeting geography-specific search queries from students in ExamPilot's priority markets. International A-Level students search with location qualifiers because their local market is underserved.

**Target markets and query patterns (aligned to verified Tier 1 and Tier 2 geographies):**

| Market | City Targets | Example Queries | CIE Entry Volume |
|---|---|---|---|
| Pakistan | Karachi, Lahore, Islamabad | "A-Level maths help Pakistan", "9709 revision Karachi", "O Level maths Pakistan" | 351K+ entries, 683 schools |
| Egypt | Cairo, Alexandria | "Cambridge 9709 Egypt", "IGCSE maths Cairo" | [VERIFY] historical top-10 IGCSE |
| India | Delhi, Mumbai, Bangalore | "Cambridge A-Level maths India", "9709 revision India" | 400-550+ schools, 65K+ entries |
| UAE | Dubai, Abu Dhabi, Sharjah | "A-Level maths tutor Dubai", "Cambridge 9709 preparation UAE" | Tier 1: high willingness to pay, ~99% internet |
| Malaysia | Kuala Lumpur, Penang | "A-Level maths tutor KL", "Cambridge 9709 Malaysia" | 70.5K+ entries |
| Saudi Arabia | Riyadh, Jeddah | "Cambridge maths Saudi Arabia", "IGCSE maths Riyadh" | 130+ schools, 44K+ entries |
| Bangladesh | Dhaka, Chittagong | "A-Level maths Bangladesh", "9709 revision Dhaka" | 23K+ entries, 150+ schools |
| Zimbabwe | Harare | "Cambridge maths Zimbabwe", "9709 revision Harare" | #3 IGCSE, November series |

**Implementation approach:**

- Create 6-8 location hub pages: `/study/[country]/` (e.g., `/study/uae/`, `/study/pakistan/`)
- Each hub includes: local exam board popularity, tutoring cost comparison (private tutor vs ExamPilot), timezone-relevant study schedule, local student testimonials (when available), regional exam centre information
- Internally link location hubs to relevant pillar/spoke pages
- Use `hreflang` tags if content is translated (future consideration)

**When to deploy:** Phase 2 onwards. Location pages need some authority before they rank. Build after pillar/spoke clusters establish domain authority.

**Volume estimate:** 8-10 country pages + 12-16 city pages = 20-26 additional indexed pages.

#### 3.1.5 SEO Publishing Cadence

| Phase | Articles/Week | Focus |
|---|---|---|
| Phase 0 (Mid-Jun-Jul 2026) | 2-3 | Complete Cambridge 9709 Pure 1 cluster (building on ~8 existing articles), first programmatic pages |
| Phase 1 (Aug-Oct 2026) | 2-3 | Results Day content, resit-focused articles, comparison pages |
| Phase 2 (Nov 2026-Mar 2027) | 3 | Pure 3 cluster, product-led content, location pages |
| Phase 3 (Apr-Nov 2027) | 2-3 | Maintenance + new clusters (Mechanics, Stats, IGCSE) |

Maximum 3 articles/week. Quality over velocity. Every article follows the low-risk AI workflow: Claude draft → human review → fact-check → personal insight → publish.

### 3.2 TikTok Strategy

TikTok is the emotional discovery engine. It puts ExamPilot on a student's radar before they know they need it. For a 16-18 year old audience, TikTok is where attention lives.

**Geographic focus:** Markets where TikTok is available -- Pakistan, UAE, Malaysia, Egypt, Saudi Arabia. India acquisition relies on SEO, Reddit, email, and direct outreach (TikTok banned since 2020).

#### 3.2.1 Regular Content (Always-On)

**Posting cadence:**
- Growing phase: 1 video/day (batch filming: 10 videos per filming session)
- Maintaining phase: 3-5 videos/week
- Best posting times (UK): 7-9 AM (before school), 12-3 PM (lunch/free periods), 7-11 PM (evening revision)

**Content pillars (rotate weekly):**

| Pillar | % of Content | Example |
|---|---|---|
| Quick tips (15-30 sec) | 40% | "The integration trick that saves 5 minutes on 9709 P1" |
| Myth-busts (30-45 sec) | 20% | "Everyone says past papers are enough. Here's why they're not." |
| Story arcs (45-60 sec) | 15% | "I went from a D to an A in 3 months. Here's what changed." |
| Behind-the-scenes | 10% | Building ExamPilot, founder story, what we're working on |
| Trends/duets | 15% | Responding to trending sounds with exam revision angles |

**Search optimization:** TikTok is a search engine for Gen Z. Every video must include target keywords in:
- Caption text
- On-screen text overlay (first 3 seconds)
- Spoken audio (first 3 seconds)
- Hashtags (#alevel #cambridgemaths #9709 #revision #alevelmaths)

#### 3.2.2 Exam Season Campaigns

These are concentrated bursts of content timed to the A-Level exam calendar. Each campaign has a theme, a content plan, and specific KPIs.

**Campaign 1: "Revision Countdown" (8-10 weeks before May/Jun exams)**
- Period: March - May 2027
- Theme: Daily revision tips counting down to exam day
- Content: Topic-per-day revision walkthroughs, time management tips, past paper strategies, stress management
- Format: Series format with episode numbering ("Day 47: The one integration technique you must know")
- CTA: "Follow for daily tips" (building audience) + "Link in bio for your revision plan" (driving trials)
- Special: Live Q&A sessions (1/week) where students submit questions

**Campaign 2: "Results Day" (August 2027)**
- Period: Results Day +/- 3 days
- Theme: "Whatever your grade, here's what to do next"
- Content: Reaction videos, "next steps" guides for each grade bracket, resit encouragement (no shame framing), "how to improve 2 grades in 10 weeks"
- CTA: "Link in bio" driving to resit landing page
- Special: Post within 2 hours of results release for maximum visibility
- Tone: Empathetic, supportive, never condescending
- **Pre-production:** Film multiple reaction variants in advance (good news framing, mixed news framing, disappointment framing). Post the one matching the day's sentiment. Pre-write grade-specific "next steps" videos (A/A*, B/C, D/E, U) for rapid publishing.

| Timing | Content | Format |
|---|---|---|
| Results Day -3 days | "Whatever happens Thursday, here's what to remember" | Talking head, empathetic |
| Results Day -1 day | "The only 3 things that matter tomorrow" | Quick tip |
| Results Day (0-2 hrs) | Reaction + "here's what to do with your grade" | Talking head, raw emotion OK |
| Results Day (2-6 hrs) | Grade-specific "next steps" (one per grade bracket) | Series format |
| Results Day +1 | "The resit plan that actually works" | Value content + screen recording |
| Results Day +2-3 | "10-week countdown to October resits" | Series launch |

**Campaign 3: "Resit Ready" (6-8 weeks before Oct/Nov resits)**
- Period: September - October 2027
- Theme: Targeted, intensive revision content for resit students
- Content: "10-week resit plan", topic-specific gap closers, "what the examiner actually wants", motivation content
- CTA: "Free trial" with resit-specific landing page
- Tone: Urgent but encouraging. "You know your grade. We know your gaps."

**Campaign 4: "Mock Season" (January - March 2027)**
- Period: January - March 2027
- Theme: Mock exam preparation
- Content: "What to expect in your mock", topic predictions, last-minute revision techniques, "how mocks prepare you for the real thing"
- CTA: "Try ExamPilot's practice mode" (product-led)
- Special: This is the first major campaign. Use it to test formats and build audience before the May/Jun exam window.

#### 3.2.3 TikTok Metrics

| Metric | What It Tells You | Target (6 months in) |
|---|---|---|
| Views per video | Reach / hook effectiveness | 1,000-5,000 average |
| Watch time % | Content quality | >50% average |
| Completion rate | Hook + delivery | >30% |
| Saves | Utility value | >2% of views |
| Profile visits | Interest in brand | >3% of views |
| Followers | Audience building | 5,000+ at 6 months |
| Link clicks (bio) | Conversion intent | Track via UTM |

#### 3.2.4 TikTok-to-Micro-Funnel Wiring

Never put the full URL in TikTok videos. Instead, use phrases like "Search 'ExamPilot Cambridge 9709'" or "Link in bio." This deliberately triggers the search step in the micro-funnel: when students search for ExamPilot on Google, Reddit, or AI tools, it generates branded search volume (Google signal), creates Reddit discussion (AI training data), and reaches students through whichever channel they trust most.

Every link-in-bio URL must use UTM parameters: `?utm_source=tiktok&utm_medium=social&utm_campaign=[campaign-name]`

### 3.3 Reddit Strategy

Reddit is the trust-building layer. Skeptical teenagers and their parents search Reddit specifically for unfiltered peer opinions. A well-placed, genuinely helpful comment can rank on Google and get cited by AI search tools.

**Active subreddits:** r/alevel (primary), r/6thForm, r/CambridgeInternational, r/Edexcel

**Operating model:**
- 2-3 genuinely helpful contributions per week per sub
- Value first, always. Answer the question before anything else.
- Only mention ExamPilot when directly relevant and only after building karma (50+ karma, 30+ day account age)
- No link drops. Describe what ExamPilot does if asked. Let them Google it.

**Content types by phase:**

| Phase | Content Type | Example |
|---|---|---|
| 0: Foundation | Pure value posts, no mention | "Here's how I'd revise differentiation for 9709 P1" |
| 1: Soft Launch | Value + soft mention when relevant | "I've been working on a tool that does exactly this..." |
| 2: Growth | Value + natural recommendation | Full engagement as a known, trusted community member |
| 3: Scale | Community leadership | Host AMAs, provide exam season guides, become the go-to resource |

**Reddit → SEO flywheel:** Reddit threads that rank on Google are golden. Search for existing high-ranking threads about Cambridge 9709 topics and add genuinely helpful answers. These answers get indexed by Google and cited by AI search tools, creating a compounding authority loop.

### 3.4 AI Search (GEO) Strategy

AI search (ChatGPT, Perplexity, Google AI Overviews) is increasingly where students begin research. **GEO is not a separate strategy -- it is a quality layer applied to all four SEO approaches and all content.** Every piece of content produced under this plan follows GEO principles by default. The tactics below are baked into the content standards and blog article template, not applied as an afterthought.

**Key tactics:**
- Answer-first structure in all SEO content (first 2-3 sentences are extractable)
- FAQPage schema on every page (AI systems crawl structured data)
- Entity optimization: always spell out full qualification names
- Cite official sources (Ofqual, Cambridge Assessment, Pearson)
- Allow AI crawlers: GPTBot, ClaudeBot, PerplexityBot, Google-Extended in robots.ts
- Seed brand mentions in Reddit/Quora to feed AI training data and RAG systems

**Measurement:** Monitor ExamPilot citations in AI-generated answers. Manual checks weekly until automated monitoring is available. Query patterns to test: "best app for Cambridge 9709 revision", "how to revise for A-Level Maths", "ExamPilot review".

### 3.5 Email Strategy

Email is the owned channel that converts warm leads into paying customers. It is the only channel where you have direct, algorithm-free access to your audience.

**Tool:** Brevo (selected, not yet connected).

**When to wire:** Phase 0, first two weeks (mid-June 2026). The waitlist email sequence must be written, loaded, and tested before any traffic arrives. Silence after signup kills trust permanently.

**Setup checklist (in order):**
1. Create Brevo account and verify domain (exampilot.io)
2. Set up DKIM, SPF, and DMARC for deliverability
3. Create waitlist signup form and embed on landing page
4. Write and load 5-email waitlist sequence
5. Write and load 6-email onboarding sequence (fires in Phase 1)
6. Test all sequences with internal email addresses
7. Set up basic segments: waitlist vs trial vs paid (even if empty)

#### 3.5.1 Email Sequences

**Waitlist/Early Access Sequence (pre-launch):**
- Trigger: Someone signs up via landing page
- Email 1 (immediate): "You're on the list" confirmation + what ExamPilot is
- Email 2 (Day 3): Value content — a study tip relevant to their exam board
- Email 3 (Day 7): Behind the scenes — what we're building and why
- Email 4 (Day 14): Social proof — student quotes or early results
- Email 5 (on launch): "Your access is ready" with direct signup link

**Onboarding Sequence (post-signup):**
- Trigger: Free trial activation
- Email 1 (immediate): "Welcome. Here's how to start your first session."
- Email 2 (Day 1): "Your first session matters. Here's how to make it count."
- Email 3 (Day 3): "Here's what ExamPilot learned about your knowledge gaps."
- Email 4 (Day 7): Social proof + feature highlight (ERI, topic mapping)
- Email 5 (Day 10): Conversion prompt with pricing and value framing
- Email 6 (Day 13): Last chance before trial expires (urgency, not pressure)

**Nurture Sequence (for active free/paid users):**
- Maximum 1 email/week to engaged list
- Content: exam tips, new features, study strategies, blog article highlights
- Segmented by exam board (Cambridge vs Edexcel) and status (free vs paid vs churned)

**Re-engagement Sequence (for inactive users):**
- Trigger: 14 days inactive
- 3 emails maximum. If no response after 3, stop.
- Email 1 (Day 14): "We noticed you haven't practiced in a while. Here's what you're missing."
- Email 2 (Day 21): Value content (not a guilt trip)
- Email 3 (Day 28): "Is ExamPilot right for you? No hard feelings either way."

#### 3.5.2 Campaign Emails

| Campaign | Timing | Segment | Content |
|---|---|---|---|
| Results Day | August | Full list | "Whatever your result, here's your next move" |
| Resit launch | September | Waitlist + churned | Resit-specific landing page + trial offer |
| Mock season | January | Active + waitlist | "Mock prep guide" + product features |
| Pre-exam | April | All students | "Exam countdown" series (weekly for 8 weeks) |
| New feature | Ongoing | Relevant segment | Feature announcement + how it helps their revision |

#### 3.5.3 GDPR Compliance (Non-Negotiable)

- **Consent:** Every signup form includes clear consent language. Checkbox, not pre-checked.
- **Parental awareness:** For users who indicate they are under 16, request a parent/guardian email. Send a single notification to the parent explaining what data is collected and how to opt out.
- **Unsubscribe:** Every email includes a one-click unsubscribe link (both GDPR-required and Brevo-enforced).
- **Data minimization:** Collect only what is needed: email, exam board, age bracket. No tracking beyond product functionality.
- **Data retention:** 24 months after last engagement. Documented in privacy policy.
- **Cookie consent:** Banner on all web properties with opt-in, not opt-out.
- **No purchased lists. Ever.**

### 3.6 Direct Outreach Strategy

Direct outreach is the highest-leverage channel for the first 100 students. It does not scale, and that is the point. The goal is hand-to-hand combat to prove product-market fit.

**Channel 1: Tutor Referrals (highest priority)**
- Target: Independent maths tutors teaching Cambridge 9709 or Edexcel IAL
- Found via: LinkedIn, tutor directories, WhatsApp groups, existing network
- Ask: "Would you be open to having 2-3 of your students try it for free?"
- Value prop for tutors: Students get personalized gap analysis between sessions. Tutors get insight into where students need help.
- Rules: Only warm intros. Maximum 1 follow-up if no response. Never position as tutor replacement.

**Channel 2: Reddit Direct (value-first)**
- Engage in target subs for 4+ weeks before any outreach
- When students post asking for revision help, offer genuine advice
- Only DM if they explicitly ask for more help or tool recommendations
- Never DM-spam

**Channel 3: Discord Study Servers**
- Join and contribute to A-Level study servers, Cambridge Maths groups
- Share study tips, answer questions
- Only share ExamPilot in dedicated "resources" channels if they exist

**Phase 0-1 targets:**

| Channel | Target Students | Method |
|---|---|---|
| Tutor referrals | 15-25 | 10-15 tutor conversations → 2-3 students per converted tutor |
| Reddit direct | 15-25 | Value posting → natural interest → DM for access |
| Discord | 10-20 | Community contribution → resource sharing |
| Total | 40-70 students | First cohort for PMF validation |

---

## 4. Phased Execution Roadmap

### Phase 0: Foundation (Mid-June - July 2026)

**Objective:** Build the content and community infrastructure. When Results Day hits in August, every channel must be ready to capture demand.

**Timeline constraint:** Content publishing restarts mid-June 2026 (home move in progress). This compresses Phase 0 to approximately 6 weeks. Prioritize ruthlessly: the Cambridge 9709 Pure 1 cluster and Results Day content are the only must-haves before August.

**Starting position (as of May 2026):**
- ~8 articles already published on exampilot.io around Cambridge 9709 Pure 1 (managed via Sanity CMS)
- 16 research briefs completed in `seomachine` repo (topic spokes for coordinate geometry, quadratics, series & circular measure; strategy spokes for how to pass, common mistakes, best resources; comparison pages vs SaveMyExams, vs Physics & Maths Tutor; international student and parent audience pages; plus keyword research with 176 keywords mapped)
- All briefs are write-ready with keyword data, SERP analysis, competitive gaps, and H2/H3 outlines
- Additional content prepared but needing editing before publish

**SEO:**
- [ ] Audit existing ~8 articles for GEO compliance, internal linking, and FAQPage schema
- [ ] Technical SEO foundation complete (CWV, schema, GSC, sitemap, robots.ts with AI crawlers)
- [ ] Publish remaining Pure 1 topic spokes from ready briefs (coordinate geometry, quadratics, series & circular measure)
- [ ] Draft and publish pillar page if not yet done (4,000+ words, FAQPage schema, links to all spokes)
- [ ] Draft and publish 3 strategy spokes from existing briefs (How to Pass, Common Mistakes, Best Resources)
- [ ] Draft and publish first examiner report analysis (product-led bridge content)
- [ ] 5-10 programmatic past paper pages enriched and indexed (noindex until enriched)
- [ ] FAQPage schema on every page from day one
- [ ] `/pricing.md` and `/llms.txt` deployed at site root
- [ ] Bing Webmaster Tools + Brave Search verified
- [ ] Link building: 3-5 referring domains (directory listings, community mentions)

**Reddit:**
- [ ] Accounts aged 30+ days with 50+ karma
- [ ] 3-5 value posts published in target subs (no ExamPilot mention)
- [ ] Active participation established in r/alevel and r/CambridgeInternational

**Email:**
- [ ] Brevo connected
- [ ] Landing page live at exampilot.io with waitlist signup
- [ ] Waitlist email sequence written and loaded
- [ ] Onboarding email sequence written

**Outreach:**
- [ ] Tutor outreach templates ready
- [ ] Student DM templates ready
- [ ] 5+ tutor conversations initiated

**Content:**
- [ ] Blog live with 15+ articles (existing ~8 + new spokes + strategy spokes + bridge content)
- [ ] Results Day content written and scheduled (to publish in August, DO NOT publish early)
- [ ] Resit landing page designed

**Phase gate (pass to enter Phase 1):** Scored gate with must-pass criteria:

| Criterion | Threshold | Weight | Must-pass? |
|---|---|---|---|
| Pages indexed (GSC) | >= 15 | 20% | Yes |
| Waitlist form live | Yes | 15% | Yes |
| Email sequences loaded and tested | Yes | 15% | Yes |
| Reddit accounts active with karma | Yes | 15% | Yes |
| Blog articles published | >= 8 | 20% | No |
| Tutor conversations initiated | >= 3 | 15% | No |

**Decision rule:** All must-pass criteria met AND weighted score >= 65%. Hard calendar override: if August arrives, enter Phase 1 regardless -- the Results Day opportunity window does not wait.

### Phase 1: Soft Launch & First 100 (August - October 2026)

**Objective:** Capitalize on Results Day. Convert the resit cohort. Prove product-market fit with the first 100 students.

**Critical moment: Results Day (August 2026)**

Results Day is the single highest-leverage marketing moment in the calendar year. Students who received disappointing results are immediately searching for solutions. The window is 48-72 hours.

Pre-Results Day checklist:
- [ ] Results Day blog post written, scheduled, ready to publish within 2 hours
- [ ] Reddit posts ready for r/alevel Results Day megathreads
- [ ] Resit landing page live with specific messaging
- [ ] Email to waitlist: "Results aren't final. Here's your next move."
- [ ] Tutor WhatsApp messages sent (warm intros only)

**SEO:**
- [ ] Results Day content published and promoted
- [ ] Resit-focused articles: "How to improve your grade by October", "Cambridge 9709 resit guide"
- [ ] Comparison pages live (/vs/save-my-exams/, /vs/papacambridge/)
- [ ] Continue Pure 1 spoke publishing
- [ ] Target: 40+ pages indexed, first keywords in top 20
- [ ] Link building: 8-15 referring domains

**Reddit:**
- [ ] Active in Results Day threads with value-first posts
- [ ] Soft ExamPilot mentions where directly relevant
- [ ] Monitor r/alevel for resit questions, answer with genuine help

**Email:**
- [ ] Waitlist contacts receive launch email
- [ ] Onboarding sequence firing for new signups
- [ ] First campaign emails (Results Day, resit encouragement)

**Outreach:**
- [ ] Tutor outreach intensifies (warm intros only)
- [ ] Target: 10-15 active tutor relationships → 40-70 students trying ExamPilot
- [ ] Follow up with every early user who hasn't completed first session

**Measurement:**
- [ ] PMF survey (Sean Ellis: "How would you feel if you could no longer use ExamPilot?") after student completes 3rd session
- [ ] Target: 40%+ "very disappointed" = PMF signal

**Phase gate (pass to enter Phase 2):**

| Criterion | Threshold | Must-pass? |
|---|---|---|
| Trial signups | >= 50 | Yes |
| PMF survey administered | Yes | Yes |
| D3/D7 retention data collected | Yes | Yes |
| Activation rate known | Yes | Yes |
| At least one keyword top 10 | Aspirational | No |

**Decision rule:** All must-pass criteria met. PMF score informs strategy but does not block Phase 2 entry -- even a low PMF score means you continue iterating, not that you stop marketing.

### Phase 2: Growth Engine (November 2026 - March 2027)

**Objective:** Organic channels start compounding. TikTok launches. Email nurture becomes a real conversion channel. Mock season is the next major exam window.

**SEO:**
- [ ] Cambridge 9709 Pure 3 cluster started (pillar + first 4 spokes) -- next in product expansion sequence
- [ ] 60-90 programmatic past paper pages live and enriched
- [ ] Product-led SEO: first data-driven content pieces (if student base supports it)
- [ ] Location pages: 3 Tier 1 markets (Pakistan, UAE, India) + 1-2 Tier 2 (Malaysia, Egypt)
- [ ] Target: 80-120 pages indexed, 5-10 keywords in top 10, 200-1,000 organic sessions/month
- [ ] Link building: 15-30 referring domains

**TikTok (LAUNCH):**
- [ ] Account created with keyword-optimized profile
- [ ] First 10 videos published (batch filmed)
- [ ] "Mock Season" campaign (Campaign 4) runs January-March 2027
- [ ] Testing: hook formulas, formats, posting times
- [ ] Target: 500+ followers by end of Phase 2

**Reddit:**
- [ ] Full engagement as a known community member
- [ ] Established contributor in r/alevel and r/CambridgeInternational
- [ ] Reddit value posts repurposed from blog articles (1-2/week)

**Email:**
- [ ] Waitlist converted or archived
- [ ] Campaign emails: mock season prep series (4 weekly emails, Jan-Feb 2027)
- [ ] Re-engagement sequence firing for inactive users
- [ ] First A/B test: subject lines for open rate optimization

**Product-Led Growth:**
- [ ] Referral mechanism: students can share their ERI/progress with friends
- [ ] NPS survey deployed in-app after session 5+
- [ ] Free tool: topic coverage checklist or revision timetable generator

**Phase gate (pass to enter Phase 3):**

| Criterion | Threshold | Must-pass? |
|---|---|---|
| Organic signups > 30% of total | Yes | Yes |
| Trial-to-paid conversion > 10% | Yes | Yes |
| Monthly organic sessions > 500 | No | No |
| TikTok account live with 10+ videos | No | No |
| Email list > 500 | No | No |

**Decision rule:** Both must-pass criteria met. Phase 3 activities (new market expansion, exam board expansion) only begin after organic channels demonstrably work.

### Phase 3: Scale (April - November 2027)

**Objective:** Organic channels dominate acquisition. CAC drops. Each channel reinforces the others. Prepare for the May/Jun 2027 exam window — the first full exam cycle with ExamPilot live.

**SEO:**
- [ ] Cambridge 9709 Pure 3 cluster complete, Statistics 1 cluster started
- [ ] Statistics 2 and Mechanics 1 clusters in progress (sequentially, matching product expansion)
- [ ] Product-led SEO at full velocity: aggregate performance data, difficulty benchmarks, misconception reports
- [ ] Location pages for all Tier 1 + Tier 2 markets (8 countries)
- [ ] Target: 200+ pages indexed, 20+ keywords in top 10, 2,000-5,000 organic sessions/month
- [ ] Domain rating: 25-40

**TikTok:**
- [ ] "Revision Countdown" campaign (Campaign 1): March-May 2027 (daily content for 8-10 weeks)
- [ ] "Results Day" campaign (Campaign 2): August 2027
- [ ] Regular content at 3-5 videos/week
- [ ] Target: 5,000+ followers, 1,000-5,000 views/video average
- [ ] Collaborate with 1-2 A-Level study TikTok accounts

**Reddit:**
- [ ] Community leadership position established
- [ ] AMA or study guide during exam season
- [ ] Reddit threads mentioning ExamPilot appearing in Google search results

**Email:**
- [ ] Pre-exam countdown series: 8 weekly emails (April-May 2027)
- [ ] Segment-specific campaigns: Cambridge vs Edexcel, free vs paid, active vs at-risk
- [ ] Email-driven conversion: 10%+ of paid conversions from email
- [ ] List size target: 2,000+ contacts

**Phase 3 success criteria:** MRR EUR5,000-9,000 by Nov 2027 (300-500 paying users). Organic acquisition > 50% of total. CAC < EUR25 blended. Monthly churn < 8%.

---

## 5. KPI Framework

### 5.1 Should KPIs Change at Different Stages?

**Yes. This is standard practice and essential for a pre-revenue startup.**

The mistake most early-stage companies make is measuring growth-stage metrics (MRR, CAC:LTV) before they have growth-stage traffic. This causes three specific failure modes:

1. **Premature optimization.** Measuring trial-to-paid conversion at Phase 0 (when there are zero trials) leads to A/B testing a landing page nobody has seen, instead of writing the SEO content that would bring traffic to it.
2. **False confidence.** High "organic sessions" at Phase 1 (when SEO has had two months) is likely bot traffic or a single viral Reddit post, not a working SEO engine. Shifting budget based on it would kill the pipeline.
3. **Demoralization.** Tracking MRR at Phase 0-1 shows EUR0 for months. For a 2-person team, staring at a zero-MRR dashboard every week is psychologically corrosive.

The right approach is **stage-based KPI evolution**: at each phase, you focus on 1-2 primary KPIs (your "north star" for that phase) and track channel-specific leading indicators that feed the north star. As the business matures, the north star shifts upstream in the funnel. Every KPI is tagged as **leading** (predictive, actionable today) or **lagging** (outcome, confirms whether activities worked). Check leading indicators weekly. Check lagging indicators monthly.

### 5.2 KPI Evolution by Phase

#### Phase 0: Foundation (Mid-Jun-Jul 2026)

**North Star: Content Infrastructure Readiness Score**

A weighted composite that quantifies how ready the system is to capture demand when Results Day hits in August. This is an input metric, not an outcome metric, and that is deliberate.

Note: Phase 0 is compressed to ~6 weeks (mid-June to end of July) due to home move. Targets are adjusted accordingly.

| KPI | Target | Weight | Leading/Lagging |
|---|---|---|---|
| Pages indexed (GSC) | 20+ | 25% | Lagging |
| Blog articles published | 8+ (including existing ~8 + new) | 25% | Leading |
| Reddit karma across target subs | 100+ | 15% | Leading |
| Waitlist signups | 50+ | 15% | Lagging |
| Tutor conversations initiated | 5+ | 10% | Leading |
| Email infrastructure complete | Yes/No | 10% | Binary gate |

**Success:** Readiness Score >= 70% (weighted sum). If you have 8+ articles published, 20+ pages indexed, Reddit active, and email infrastructure ready, you are ready for Phase 1 even if waitlist signups are below 50.

**What NOT to measure in Phase 0:** MRR, CAC, conversion rate, churn, organic traffic volume. These are literally undefined at this stage. Tracking them creates noise, not signal.

#### Phase 1: Soft Launch (Aug-Oct 2026)

**North Star: Activated Trials**

An "activated trial" is a student who signs up AND completes at least one full practice session. Raw signup count is a vanity metric. Activation proves the product delivers value.

| KPI | Target | Leading/Lagging |
|---|---|---|
| Total trial signups | 100+ | Lagging |
| Activation rate (signup → first session) | 60%+ | Lagging (but actionable via onboarding changes) |
| D7 retention (returned after 7 days) | 30%+ | Lagging |
| PMF score (Sean Ellis) | 40%+ "very disappointed" | Lagging (confirms PMF) |
| Email list size | 200+ | Leading (grows with every touchpoint) |
| Waitlist → trial conversion | 30%+ | Lagging |
| Blog articles published/week | 2-3 | Leading |
| Reddit value posts/week | 2-3 | Leading |

**Failure definition:** Fewer than 30 trials. D7 retention below 15%. PMF score below 25%. If PMF < 25%, this is a pivot signal -- the product does not solve the problem as positioned.

**What NOT to measure in Phase 1:** Revenue metrics (too early), CAC (all acquisition is manual), organic traffic volume (SEO hasn't had time to compound).

#### Phase 2: Growth Engine (Nov 2026-Mar 2027)

**North Star: Monthly Organic Signups**

The shift from manual to organic acquisition is the most important transition in the plan. When students start finding ExamPilot through Google, Reddit threads, and AI search without you pushing them there, the flywheel is working.

| KPI | Target | Leading/Lagging |
|---|---|---|
| Monthly organic signups | 30+ | Lagging |
| Organic as % of total signups | 30%+ | Lagging |
| Organic traffic (monthly sessions) | 500+ | Lagging |
| Paying users | 70-120 by end of Phase 2 | Lagging |
| MRR | EUR1,200-2,150 by Mar 2027 | Lagging |
| Trial-to-paid conversion rate | 15-20% (improving as unit coverage deepens) | Lagging |
| Monthly churn rate | <8% | Lagging |
| Email open rate | 25%+ | Lagging |
| TikTok followers | 500+ | Lagging |
| Keywords in top 10 | 5+ | Lagging |
| Articles published/week | 3 | Leading |
| TikTok videos/week | 3-5 | Leading |
| Reddit contributions/week | 2-3 per sub | Leading |

**Failure definition:** Organic signups still below 10% of total after 5 months. Conversion below 5%. No channel besides outreach working. If this persists through March 2027, the content strategy or positioning needs fundamental rethinking.

**New metrics introduced:** Trial-to-paid conversion (monetization enters the picture), churn rate (enough users to measure meaningfully), organic vs manual split (flywheel progress).

#### Phase 3: Scale (Apr-Nov 2027)

**North Star: MRR (Monthly Recurring Revenue)**

Revenue becomes the primary metric when organic channels are working and conversion is proven. Everything else becomes a supporting input.

| KPI | Target | Leading/Lagging |
|---|---|---|
| MRR | EUR5,000-9,000 by Nov 2027 | Lagging |
| Paying users | 300-500 by Nov 2027 | Lagging |
| Blended CAC | <EUR25 | Lagging |
| CAC:LTV ratio | >3:1 | Lagging |
| Monthly churn | <7% (multi-unit coverage reduces churn vs single-unit) | Lagging |
| Organic as % of total signups | >50% | Lagging |
| NPS | 40+ | Lagging |
| Referral rate | 10%+ of new signups | Lagging |
| Monthly organic sessions | 2,000-5,000 | Lagging |
| Email list | 2,000+ | Leading |
| Domain rating | 25-40 | Lagging |

**Projection model:** These targets assume full CIE 9709 coverage (P1, P3, S1, S2, M1) by Nov 2027, with 130-180+ indexed pages, 1,000-1,300 cumulative trials, 20-22% trial-to-paid conversion (improving as unit coverage deepens), and 5-7% monthly churn (lower than single-unit because students stay for their next paper). Blended MRR per user is EUR17-19 based on a tier mix weighted toward quarterly and annual plans in price-sensitive international markets.

**Failure definition:** MRR below EUR3,000 by Nov 2027. CAC rising. Still dependent on manual outreach for >50% of signups. Churn >12%.

### 5.3 Should KPIs Vary Per Channel?

**Yes. Each channel has a different role in the funnel and should be measured against the job it performs, not a single universal metric.**

Measuring TikTok by signups is like measuring a billboard by store visits. TikTok's job is awareness (reach and emotional connection). Reddit's job is trust (peer validation). SEO's job is intent capture (getting in front of students who are already looking). Email's job is conversion (turning warm leads into paying customers).

Holding every channel to the same "signups" metric would cause you to kill TikTok (low direct signups but huge awareness) and over-invest in email (high conversion rate but limited reach).

### 5.4 Channel-Specific KPIs

#### SEO

| Metric | Phase 0-1 | Phase 2 | Phase 3 | L/L |
|---|---|---|---|---|
| Articles published/week | 2-3 | 3 | 2-3 | Leading |
| Pages indexed | 20+ | 80+ | 200+ | Lagging |
| Organic sessions/month | — | 500+ | 2,000-5,000 | Lagging |
| Keywords in top 10 | — | 5+ | 20+ | Lagging |
| Domain rating (Ahrefs) | — | 15-25 | 25-40 | Lagging |
| Referring domains | 3-5 | 15-30 | 40+ | Lagging |
| AI citations (manual check) | — | Brand appears | Cited consistently | Lagging |
| Organic signups/month | — | 10+ | 50+ | Lagging |

#### TikTok

| Metric | Phase 2 (launch) | Phase 3 | L/L |
|---|---|---|---|
| Videos published/week | 3-5 | 3-5 | Leading |
| Average views/video | 200-500 | 1,000-5,000 | Lagging |
| Followers | 500+ | 5,000+ | Lagging |
| Profile visit rate | >2% of views | >3% | Lagging |
| Save rate | >1% | >2% | Lagging |
| Link clicks (bio, UTM tracked) | Track baseline | 50+/month | Lagging |
| Campaign views during exam window | — | 10,000+ per campaign | Lagging |

#### Reddit

| Metric | Phase 0-1 | Phase 2-3 |
|---|---|---|
| Karma across target subs | 100+ | 500+ |
| Value posts/week | 2-3 | 2-3 |
| Average upvotes per post | 5+ | 15+ |
| Threads ranking on Google | — | 3+ |
| DM requests (inbound) | Track any | 5+/month |
| Reddit-referred site visits | Track baseline | 100+/month |

#### Email

| Metric | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|
| List size | 200+ | 500+ | 2,000+ |
| Open rate | 30%+ | 25%+ | 25%+ |
| Click rate | 5%+ | 4%+ | 4%+ |
| Unsubscribe rate | <1% | <0.5% | <0.5% |
| Email → trial conversion | — | 5%+ | 8%+ |
| Email → paid conversion | — | — | 3%+ |

#### Direct Outreach

| Metric | Phase 0-1 | Phase 2+ |
|---|---|---|
| Tutor conversations | 10-15 | Maintenance only |
| Tutor conversion rate | 20-30% (agree to share) | — |
| Students per converted tutor | 2-3 | — |
| Response rate (outreach msgs) | 15-25% | — |
| Outreach → trial conversion | 40%+ | — |

### 5.5 KPI Approaches: Pros, Cons, and Recommendation

There are four common approaches to structuring KPIs. Here is an honest comparison:

#### Option A: North Star Metric + Input Metrics

One primary metric that everyone focuses on. Supporting metrics are tracked but secondary.

| Pros | Cons |
|---|---|
| Maximum focus and alignment | Can miss channel-specific problems |
| Easy to communicate to stakeholders | North star may be a lagging indicator |
| Prevents metric overload | Temptation to game one number |

#### Option B: AARRR Pirate Metrics

Five-stage framework: Acquisition, Activation, Retention, Revenue, Referral. Each has its own primary metric.

| Pros | Cons |
|---|---|
| Complete funnel coverage | 5+ metrics is too many for a 2-person team |
| Industry standard, well-documented | No clear priority when metrics conflict |
| Easy to identify which stage is broken | All stages measured from day 1 (premature) |

#### Option C: Stage-Based KPI Evolution

Different primary metrics at each business phase. The north star shifts as the company matures.

| Pros | Cons |
|---|---|
| Matches startup reality | Requires discipline to actually change focus |
| Prevents premature optimization | Stakeholders may want "revenue" from day 1 |
| Focuses effort where it matters most | Transition between stages can be ambiguous |

#### Option D: Leading vs Lagging Indicators

Every metric classified as either leading (predictive, actionable) or lagging (outcome, retrospective). Focus on leading indicators because you can influence them.

| Pros | Cons |
|---|---|
| Highly actionable | More complex tracking setup |
| Early warning system | Requires hypothesis about which leads cause which lags |
| Prevents "dashboard staring" at unchangeable numbers | Can over-index on activity over results |

**Recommendation: Option C (Stage-Based) + Option D (Leading/Lagging)**

Use stage-based evolution to define your 1-2 primary KPIs per phase. Within each phase, classify all supporting metrics as leading or lagging so you know what you can actually act on.

For example, in Phase 2:
- **North Star (lagging):** Monthly organic signups
- **Leading indicators:** Articles published this week, keywords gaining rank, Reddit posts made, TikTok videos posted, emails sent
- **Lagging confirmation:** Organic traffic, trial activations, conversion rate

The leading indicators tell you whether you're doing the right activities. The lagging indicators tell you whether those activities are working. Check leading indicators weekly. Check lagging indicators monthly.

### 5.6 Defining Success at Each Stage

| Phase | You've succeeded if... | You've failed if... | What failure means |
|---|---|---|---|
| 0: Foundation | Readiness Score >= 70%. 20+ pages indexed, Reddit active, email ready. | Zero articles published by end of July. No Reddit activity. No waitlist form. | Results Day arrives with nothing to capture demand. Extend Phase 0 by max 2 weeks, but August is a hard deadline. |
| 1: Soft Launch | 100+ activated trials, 30%+ D7 retention, 40%+ PMF score, first paying customers. | <30 trials. <15% D7 retention. PMF score < 25%. | **Pivot signal.** The product does not solve the problem as positioned. Re-evaluate product, messaging, or target segment before continuing to Phase 2. |
| 2: Growth Engine | Organic > 30% of total. Conversion 15-20%. 70-120 paying users. MRR EUR1,200-2,150. TikTok live. | Organic < 10% after 5 months. Conversion < 5%. Paying users < 30. | Content strategy or positioning needs fundamental rethinking. Is ExamPilot targeting the right keywords? The right audience? The right channels? |
| 3: Scale | 300-500 paying users. MRR EUR5,000-9,000. CAC < EUR25. Organic > 50%. Churn < 7%. | MRR < EUR3,000 by Nov 2027. CAC rising. Outreach still >50%. Churn > 12%. | Growth ceiling hit. Evaluate: product gaps, pricing misalignment, market saturation, or new exam board / geography expansion. |

### 5.7 KPI Dashboard Cadence

| Frequency | What to Review | Who |
|---|---|---|
| Daily (Phase 1 only) | Signups, errors, support requests | Enitan or Teresa |
| Weekly | `/weekly-pulse`: content published, channel metrics, leading indicators | Both |
| Monthly | Full KPI review: north star, channel metrics, trend analysis | Both |
| Quarterly | Strategy recalibration: are we in the right phase? Should north star shift? | Both |

### 5.8 Growth Projection Model

These projections assume full CIE 9709 expansion (P1 → P3 → S1 → S2 → M1) on schedule, with each new unit expanding the addressable keyword surface area and improving both conversion and retention.

**Key assumptions:**
- Each new 9709 unit adds ~30-40% more addressable keywords and trial volume (new student segments who need that specific unit)
- Trial-to-paid conversion improves from 15% (single unit) to 20-22% (multi-unit) because students see a platform covering all their papers
- Monthly churn drops from 8-10% (single unit) to 5-7% (multi-unit) because students stay for their next paper
- Blended MRR per user: EUR17-19 (weighted toward quarterly/annual in price-sensitive international markets)

**Monthly build-up:**

| Month | Product coverage | SEO pages (cumulative) | New trials | Conversion | New paying | Churn | Net paying |
|---|---|---|---|---|---|---|---|
| Aug 2026 | P1 | 25-35 | 80 | 15% | 12 | — | 12 |
| Sep 2026 | P1 | 35-45 | 50 | 15% | 8 | 1 | 19 |
| Oct 2026 | P1 | 45-55 | 50 | 15% | 8 | 1 | 26 |
| Nov 2026 | P1 + P3 launches | 55-70 | 60 | 18% | 11 | 2 | 35 |
| Dec 2026 | P1 + P3 | 70-85 | 50 | 18% | 9 | 2 | 42 |
| Jan 2027 | P1 + P3 + S1 launches | 85-105 | 80 | 20% | 16 | 3 | 55 |
| Feb 2027 | P1 + P3 + S1 | 100-120 | 90 | 20% | 18 | 3 | 70 |
| Mar 2027 | P1 + P3 + S1 + S2 starts | 110-135 | 100 | 22% | 22 | 4 | 88 |
| Apr 2027 | P1 + P3 + S1 + S2 | 120-150 | 120 | 22% | 26 | 5 | 109 |
| May 2027 | + M1 starts | 130-165 | 140 | 22% | 31 | 7 | 133 |
| Jun 2027 | Full 9709 building | 140-175 | 100 | 22% | 22 | 8 | 147 |
| Jul 2027 | Full 9709 | 150-180 | 100 | 22% | 22 | 9 | 160 |
| Aug 2027 | Full 9709 (Results Day 2) | 155-185 | 180 | 22% | 40 | 10 | 190 |
| Sep 2027 | Full 9709 + 0580 starts | 165-200 | 120 | 22% | 26 | 11 | 205 |
| Oct 2027 | Full 9709 + 0580 | 175-215 | 130 | 22% | 29 | 12 | 222 |
| Nov 2027 | Full 9709 + 0580 | 180-225 | 130 | 22% | 29 | 13 | 238 |

**This is the conservative scenario.** The moderate and stretch scenarios account for faster SEO compounding, referral effects, and TikTok campaign spikes:

| Scenario | Cumulative trials (Nov 2027) | Avg conversion | Avg churn | Paying users (Nov 2027) | Blended MRR/user | MRR |
|---|---|---|---|---|---|---|
| Conservative | 1,480 | 20% | 6% | ~240 | EUR 17 | **EUR 4,080** |
| Moderate | 1,800 | 21% | 5.5% | ~350 | EUR 18 | **EUR 6,300** |
| Stretch | 2,200 | 22% | 5% | ~480 | EUR 19 | **EUR 9,120** |

**What drives the difference between scenarios:**
- **Conservative:** SEO compounds at typical rates, TikTok adds modest incremental trials, referral at 5%
- **Moderate:** SEO compounds faster due to 180+ pages and 15+ months of domain aging, TikTok campaigns spike during exam windows, referral at 10%
- **Stretch:** All channels compound, second Results Day outperforms first by 2x, 0580 IGCSE content captures feeder market, referral at 15%

**MRR milestone targets:**

| Milestone | When | Paying users | MRR |
|---|---|---|---|
| First paying customers | Aug-Sep 2026 | 10-20 | EUR 170-360 |
| EUR 1,000 MRR | Jan-Feb 2027 | 55-65 | EUR 1,000 |
| EUR 2,000 MRR | Mar-Apr 2027 | 110-120 | EUR 2,000 |
| EUR 5,000 MRR | Aug-Sep 2027 | 280-300 | EUR 5,000 |
| 500 paying users | Nov 2027-Feb 2028 | 500 | EUR 8,500-9,500 |

**500 paying users is achievable but is a stretch target for Nov 2027.** More likely timeline is Q1 2028. For this plan's 18-month window, 300-500 paying users and EUR 5,000-9,000 MRR is the realistic range.

---

## 6. Exam Calendar Integration

The A-Level exam calendar is ExamPilot's metronome. All marketing activity intensifies around four annual peaks:

```
                  2026                                    2027
    May   Jun   Jul   Aug   Sep   Oct   Nov   Dec   Jan   Feb   Mar   Apr   May   Jun   Jul   Aug   Sep   Oct   Nov
    |-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
    ████████                                                                                ████████
    May/Jun exams                                                                          May/Jun exams
    (too late for us)                                                                      (FULL CAMPAIGN)
                          █████                                                                        █████
                          Results Day                                                                  Results Day
                          (CRITICAL)                                                                   (campaign 2)
                                ██████████████                                                               ██████████████
                                Resit window                                                                 Resit window
                                (campaign 3)
                                                          ██████████████████████
                                                          Mock season (campaign 4)
                                                                                ██████████████████████
                                                                                Pre-exam countdown (campaign 1)
```

**Content pre-staging rule:** All campaign content must be written, reviewed, and scheduled at least 2 weeks before the campaign window opens. No last-minute content production during campaign execution.

**Channel activation per peak:**

| Peak | SEO | TikTok | Reddit | Email |
|---|---|---|---|---|
| Results Day (Aug) | Resit guides published | Reaction + "what next" content | Active in megathreads | Waitlist conversion blast |
| Resit Window (Sep-Oct) | Resit-specific articles | "Resit Ready" campaign | Targeted value posts | Resit-specific sequence |
| Mock Season (Jan-Mar) | Mock prep content | "Mock Season" campaign | Study tips + advice | Mock prep email series |
| Pre-Exam (Mar-May) | Refresh all content, update dates | "Revision Countdown" daily | Intensive Q&A contributions | 8-week countdown series |

---

## 7. Budget and Resource Allocation

### 7.1 Tool Budget (Monthly Progression)

| Tool | Monthly Cost | Phase 0 | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|---|---|
| Google Search Console | Free | X | X | X | X |
| PostHog | Free tier | X | X | X | X |
| Brevo | Free tier (300/day) | X | X | X | Evaluate paid if list > 2,000 |
| Mangools (KWFinder) | EUR29 | X | X | X | X |
| Surfer SEO | EUR89 | Optional | X | X | Evaluate necessity |
| Claude API | ~EUR20 | X | X | X | X |
| TikTok (organic) | Free | — | — | X | X |
| AI monitoring tool | EUR0-50 | — | — | Optional | X |
| **Total** | | **EUR49-138** | **~EUR138** | **EUR138-188** | **EUR138-238** |

### 7.2 Time Allocation (2-person team)

| Activity | Hours/Week (Phase 0-1) | Hours/Week (Phase 2-3) |
|---|---|---|
| SEO content (research + write + review) | 6-8 | 4-6 |
| Reddit engagement | 2-3 | 1-2 |
| TikTok (script + film + edit + post) | 0 | 3-5 |
| Email (write + segment + send) | 1-2 | 2-3 |
| Direct outreach (tutors, students) | 4-6 | 1-2 |
| Analytics + reporting (weekly pulse) | 1 | 1-2 |
| Strategy + planning | 1 | 1 |
| **Total** | **15-21 hrs/week** | **13-21 hrs/week** |

This is shared between Enitan and Teresa. Divide by strength: whoever is stronger at content writing owns SEO and email. Whoever is stronger at community interaction owns Reddit and outreach. TikTok is a joint effort (one scripts, one films, or both).

### 7.3 Paid Advertising

No paid advertising. ExamPilot is an organic-only acquisition strategy across all phases and all channels. Growth comes from SEO compounding, community presence (Reddit), TikTok organic content, email nurture, and direct outreach. This is a deliberate, permanent decision — not a deferral.

When the growth ceiling is hit in Phase 3 or beyond, the response is product expansion (new exam boards, new geographies, new subjects) and deeper organic channel investment — not paid acquisition.

---

## 8. Cross-Channel Content Engine

Every piece of content should serve at least two channels. This is the repurposing system in practice.

### 8.1 Weekly Content Cycle

| Day | Primary Output | Derivatives |
|---|---|---|
| Monday | Blog article published (SEO) | — |
| Tuesday | — | Reddit value post adapted from article |
| Wednesday | — | Email tip extracted from article |
| Thursday | — | TikTok script from article's best insight |
| Friday | `/weekly-pulse` review | Plan next week's primary article |

**1 article/week = 4 channel-specific pieces.** At 3 articles/week maximum, that is 12+ pieces of content per week across all channels, all from the same research and writing effort.

### 8.2 Content Source Priority

Where to find content ideas, in order of signal strength:

1. **Reddit questions** — Search `site:reddit.com cambridge 9709 [topic]` to find real student language and pain points
2. **Keyword research** — `/research-keywords` pipeline for SEO opportunities
3. **Student feedback** — Questions and struggles from ExamPilot users (Phase 1+)
4. **Examiner reports** — Official insight into where students lose marks
5. **Competitor gaps** — Topics competitors cover poorly or don't cover at all
6. **Product data** — Aggregate performance patterns from ExamPilot usage (Phase 2+)

---

## 9. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| SEO takes longer than 6 months to gain traction | Medium | High | Direct outreach and Reddit are insurance channels. Don't bet everything on SEO. |
| TikTok algorithm change reduces organic reach | Medium | Medium | TikTok is an awareness channel, not the only one. SEO and email are algorithm-proof. |
| Reddit community pushback on self-promotion | Medium | Medium | Value-first approach with strict engagement rules. Never push if not welcome. |
| Google AI Overviews reduce click-through rates | High | Medium | GEO strategy ensures ExamPilot is cited in AI answers. Traffic shifts from clicks to brand mentions. |
| Competitor launches adaptive product | Low | High | Speed and niche focus are the moats. Cambridge 9709 specificity is hard to replicate quickly. |
| Under-18 data regulations tighten | Medium | Medium | GDPR compliance from day one. Parental consent recommended. No data shortcuts. |
| Content quality dips due to AI reliance | Medium | High | Mandatory human review for every piece. Low-risk AI workflow only. |
| Exam board changes syllabus | Low | Medium | Content structured by topic, not by year. Annual syllabus review during summer. |
| Team bandwidth is insufficient | High | High | Automation via AIOS marketing machine. Prioritize ruthlessly. Drop lowest-ROI channel first (Discord). |

---

## 10. Exam Board Expansion Sequencing

At launch, ExamPilot covers CIE 9709 Pure 1 only. Expansion is sequential -- each unit is completed before the next begins. CIE 9709 is fully covered first, then CIE 0580 IGCSE, then Edexcel IAL.

**CIE 9709 expansion order:**

| Step | Unit | Rationale |
|---|---|---|
| 1 (launch) | Pure Mathematics 1 (Paper 1) | Core A-Level entry point. Highest search volume. Already started. |
| 2 | Pure Mathematics 3 (Paper 3) | Completes the Pure strand. ~40% topic overlap with P1 at advanced level. Required for full A-Level. |
| 3 | Statistics 1 (Paper 5) | First applied module. Many students pair Pure + Statistics. |
| 4 | Statistics 2 (Paper 6) | Completes the Statistics strand for students taking the full Statistics pathway. |
| 5 | Mechanics 1 (Paper 4) | Second applied module. Completes the full 9709 offering. |

**Then CIE 0580 IGCSE Mathematics:**

| Step | Unit | Rationale |
|---|---|---|
| 6 | CIE 0580 IGCSE Maths | Natural feeder: 0580 students become 9709 students. 2-year LTV play. ~30-40% topic overlap with 9709 Pure 1. |

**Then Edexcel International Advanced Level (IAL) Mathematics:**

| Step | Unit | Papers | Rationale |
|---|---|---|---|
| 7 | Pure Mathematics 1-4 | WMA11, WMA12, WMA13, WMA14 | Full Pure strand. ~60-70% topic overlap with CIE 9709 Pure. Different question styles and mark schemes. |
| 8 | Mechanics 1-3 | WME01, WME02, WME03 | Applied strand. |
| 9 | Statistics 1-3 | WST01, WST02, WST03 | Applied strand. Completes full Edexcel IAL coverage. |

**Future consideration (not committed):**

| Qualification | Notes |
|---|---|
| CIE 9231 Further Mathematics | Niche but high-value prestige play. Further Maths students are serious, likely to pay, and influence peers. |
| CIE 0606 Additional Mathematics | Bridges IGCSE and A-Level. ~50% overlap with 0580 and 9709. |
| Other subjects (Sciences) | 2028+ at earliest. Only after maths coverage is comprehensive. |

**Why this order:** CIE 9709 is completed first because students taking the exam need all their units covered on one platform -- offering Pure 1 without Pure 3 means students need a second tool for half their course. CIE 0580 comes after 9709 (not interleaved) because the IGCSE-to-A-Level pipeline creates a 2-year LTV play, but only after the A-Level product is complete enough to retain those students when they progress. Edexcel IAL comes last because it is a parallel market (different exam board) rather than a vertical pipeline extension.

---

## 11. Competitive Positioning

**Positioning statements vs each competitor:**

| Competitor | Their strength | ExamPilot's advantage | Positioning |
|---|---|---|---|
| SaveMyExams | Comprehensive revision notes, multiple exam boards | Zero adaptive intelligence, static content | "They tell you WHAT to study. We tell you WHERE you're weak and WHAT to do next." |
| PapaCambridge | Free, complete past paper archive, high DA | Zero analysis, no feedback, no practice loop | "They give you the papers. We give you the practice loop: question, feedback, adaptation, and a map of what you know." |
| Physics & Maths Tutor | Good worked solutions, clean content, high UK rankings | UK-domestic focus, limited Cambridge International | "PMT is built for UK A-Levels. ExamPilot is built for Cambridge International 9709 specifically -- different syllabus, different papers, different exam strategy." |
| Private tutoring | Personalized 1:1 attention | EUR40-80/hour vs EUR12/month. Tutor sees you weekly; ExamPilot tracks daily. | "One hour of tutoring buys a year of daily practice." |

**Content rules for competitor mentions:** Factual comparisons only. No FUD. Acknowledge competitor strengths honestly. On Reddit, never badmouth competitors. In outreach, never mention competitors by name.

**SERP gaps to exploit:** Misconception-specific content, exam strategy articles (not just topic notes), revision plan generators, location-specific queries, "best Cambridge 9709 app" queries, examiner report analysis.

---

## 12. Decision Log

Decisions made in this plan that should be logged:

1. **Stage-based KPI evolution adopted** over AARRR or universal metrics. Rationale: 2-person team, pre-revenue, premature optimization is the bigger risk than metric gaps.
2. **Sequential expansion: 9709 P1 → P3 → S1 → S2 → M1 → 0580 → Edexcel IAL.** Rationale: complete each unit before starting the next. Full CIE 9709 coverage first (students need all their units on one platform), then 0580 (IGCSE-to-A-Level pipeline), then Edexcel IAL (parallel market, 10 units: P1-P4, M1-M3, S1-S3).
3. **No paid advertising.** Organic-only acquisition across all phases. Growth ceiling response is product and geography expansion, not paid spend.
4. **TikTok launch deferred** to Phase 2 (November 2026). Rationale: building content foundation and proving product-market fit with direct channels first.
5. **TikTok geographic focus** on markets where available (Pakistan, UAE, Malaysia, Egypt, Saudi Arabia). No India-specific short-form variant.
6. **Location-based SEO deferred** to Phase 2. Rationale: requires domain authority to rank; build after pillar/spoke clusters.
7. **Product-led SEO bridge content** starts Phase 0-1 with examiner report analysis and curriculum analysis. Full product-led content (student data) deferred to Phase 2.
8. **UAE promoted to Tier 1, Egypt demoted to Tier 2.** Rationale: UAE has verified high willingness to pay, near-universal internet, and is SaveMyExams's #3 market. Egypt's "#1 IGCSE" claim cannot be verified from post-2020 data.
9. **Monthly demand gen/acquisition pulsing** adopted over static phase-based allocation. Rationale: exam calendar creates natural acquisition peaks and demand-gen valleys regardless of phase.
10. **Formal phase gate scoring** with must-pass criteria and weighted thresholds. Rationale: checklists are ambiguous; scored gates force explicit decisions.
11. **Programmatic SEO uses noindex-until-enriched** protocol. Rationale: prevents thin content penalties while building URL structure early.
12. **Brevo wiring in Phase 0 first two weeks** (not vague "before Phase 1"). Rationale: silence after signup kills trust permanently.

---

## Appendix A: Glossary

| Term | Definition |
|---|---|
| TOFU | Top of funnel (awareness) |
| MOFU | Middle of funnel (consideration) |
| BOFU | Bottom of funnel (conversion) |
| CAC | Customer acquisition cost |
| LTV | Lifetime value of a customer |
| MRR | Monthly recurring revenue |
| PMF | Product-market fit |
| GEO | Generative Engine Optimization (optimizing for AI search) |
| ERI | Exam Readiness Index (ExamPilot's predictive grade metric) |
| FSRS | Free Spaced Repetition Scheduler (ExamPilot's retention algorithm) |
| CWV | Core Web Vitals (Google's page experience metrics) |
| DR | Domain Rating (Ahrefs authority metric) |
| KD | Keyword Difficulty (Ahrefs competition metric) |
| NPS | Net Promoter Score |
| Sean Ellis Score | "How would you feel if you could no longer use [product]?" — 40%+ "very disappointed" = PMF |
| ICE | Impact, Confidence, Ease (experiment prioritization framework) |
| ORB | Owned, Rented, Borrowed channels framework |

## Appendix B: Channel Dependency Map

```
                    ┌─────────────┐
                    │   CONTENT   │
                    │  (1 article)│
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
         ┌────▼────┐  ┌───▼────┐  ┌───▼────┐
         │   SEO   │  │ Reddit │  │ TikTok │
         │  (blog) │  │ (post) │  │(script)│
         └────┬────┘  └───┬────┘  └───┬────┘
              │            │            │
              └────────────┼────────────┘
                           │
                    ┌──────▼──────┐
                    │  AI Search  │
                    │ (citations) │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Website   │
                    │  (convert)  │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │    Email    │
                    │  (nurture)  │
                    └─────────────┘
```

## Appendix C: Quick Reference — What to Measure When

| "I want to know if..." | Look at... | Frequency |
|---|---|---|
| Our content is being found | GSC impressions, pages indexed | Weekly |
| Students trust us | Reddit upvotes, return visitors, time on site | Weekly |
| AI tools recommend us | Manual AI query checks | Monthly |
| Our funnel is working | Visitor → trial → activation → paid conversion | Monthly |
| Students are staying | D7, D30 retention, session depth | Monthly |
| We're spending efficiently | CAC by channel, blended CAC | Monthly |
| The business is growing | MRR, organic signup %, churn | Monthly |
| Students love the product | NPS, PMF score, referral rate | Quarterly |
