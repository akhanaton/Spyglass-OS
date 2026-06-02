# Tutor Distribution Flywheel — Strategic Analysis

**Status:** Pre-decision research. Not adopted.
**Version:** 1.0
**Last updated:** 2026-05-21
**Author:** AIOS session (Enitan-driven)
**Decision target date:** TBD by Enitan & Teresa. Recommended: before Phase 0 close (end July 2026) so any product build can fit Phase 0 capacity.
**Linked memory:** [project_tutor_flywheel.md](../memory/project_tutor_flywheel.md) (to be created on save)

---

## 1. Executive Summary

This document analyses a proposed strategic addition to the ExamPilot marketing plan: a Tutor Distribution Flywheel.

**The play in one paragraph.** Build a free "Tutor Mode" inside ExamPilot. A tutor sees their students' weak-spot heatmap, gets ready-made homework, and can WhatsApp-share progress digests to parents. The tutor never pays. Their students pay individually as ordinary B2C subscribers. Each tutor becomes a distribution unit of 5-20 paying students. The thesis is that in ExamPilot's Tier 1 markets (Pakistan, UAE, India), private tutoring is near-universal and tutors hold trust capital with parents that ExamPilot cannot acquire directly at the same speed or cost.

**What the data shows so far.**
- UAE: 49% of Dubai students received private tutoring in the past year; 70% among Indian curriculum students. UAE private tutoring market valued at USD 470M [(Ken Research)](https://www.kenresearch.com/uae-private-tutoring-market).
- Pakistan: 125,000+ Cambridge AS/A-Level entries in 2024 (+7% YoY); 33% of private-school students used private tuition in 2016-17; 62% of secondary students in Lahore reported relying on private tuition to pass exams [(Express Tribune)](https://tribune.com.pk/story/2580040/our-shadow-education-a-red-light-for-a-failing-institution); [(Tes)](https://www.tes.com/magazine/news/general/cambridge-international-exams-2024-results-released).
- Asia Pacific holds 60.85% of the global private tutoring market (USD 40.74B in 2025) [(Fortune Business Insights)](https://www.fortunebusinessinsights.com/private-tutoring-market-104753).
- No major exam-prep platform (Save My Exams, Physics & Maths Tutor, Sparx, MyMaths) currently runs a tutor-as-distribution model. Most either ignore tutors or offer them paid features (Save My Exams has a Test Builder for teachers/tutors as a sub-feature, not a distribution channel) [(savemyexams.com/teachers)](https://www.savemyexams.com/teachers/).
- Tutor business management SaaS (TutorCruncher, Teachworks) exists but focuses on operations (scheduling, billing, CRM), not pedagogy or student-content delivery. They are adjacent, not competitive [(TutorCruncher)](https://tutorcruncher.com/blog/tutorcruncher-vs-teachworks).

**Headline decision criteria.**
The go/no-go hinges on three questions:
1. Do tutors in Tier 1 markets actually want a free dashboard that ties them to a paid student platform? (Requires 8-12 tutor interviews to validate. Not yet done.)
2. Can ExamPilot afford the engineering work to ship a credible MVP Tutor Mode in 4-8 weeks during Phase 0-1?
3. Does the unit economics (tutor → student conversion × student LTV) clear a sensible CAC bar even at low tutor adoption rates?

This report walks through what we know, what we don't, and what would need to be true to commit.

---

## 2. The Strategic Thesis

### The conventional view in the existing plan

The current marketing plan (v3.0.1) treats tutors as **one of several P0-P1 channels**, with a tutor referral target of 15-25 students. Tutors are framed as "tutor referral partners" alongside teachers (B2C2B). The implicit model: tutors hear about ExamPilot, mention it, students sign up. Tutors are an awareness layer, not infrastructure.

This is consistent with how exam-prep edtech generally thinks about tutors: as a mention channel, not a distribution platform.

### The proposed shift

Tutors in Tier 1 international markets are not a marginal channel. They are the **primary supplementary education infrastructure** for the target student. The data points to:

- In Dubai, ~49% of all students and ~70% of Indian curriculum students use tutors [(Ken Research)](https://www.kenresearch.com/uae-private-tutoring-market).
- In Lahore (Pakistan), 62% of secondary students rely on tuition to pass exams [(Express Tribune)](https://tribune.com.pk/story/2580040/our-shadow-education-a-red-light-for-a-failing-institution).
- Asia Pacific represents 60.85% of the global tutoring market [(Fortune Business Insights)](https://www.fortunebusinessinsights.com/private-tutoring-market-104753).

If most CIE/IGCSE students in Tier 1 markets already have a tutor, then **the tutor is sitting between ExamPilot and the student.** A tutor recommendation is a high-trust signal to parents (the actual buyers in resit and first-time-sit scenarios alike — see Customer Personas).

The shift: stop trying to reach students through SEO/content/Reddit while bypassing the tutor. Instead, equip the tutor and let them become the distribution layer. One tutor brings 5-20 students. The CAC for those students drops toward zero. The conversion rate climbs because the tutor's recommendation removes the trial-period skepticism.

### Why this is strategically distinctive (Move 37 framing)

The bet is that UK-domestic-trained edtech competitors structurally cannot see this opportunity because:

1. In the UK domestic market, private tutoring is a minority phenomenon (UK supplemental education market is roughly £1.6B but with much lower per-student penetration than Tier 1 international markets — the company narrative cites this figure but does not break out tutoring vs general supplemental).
2. UK/US edtech orthodoxy treats tutors as competitors or as a free-tier user category, not as a distribution layer.
3. The "always own the customer relationship" SaaS doctrine actively discourages partnering with intermediaries.

If the thesis holds, ExamPilot can occupy this position before any competitor sees it as a strategic priority.

**Important caveat:** This Move 37 framing relies on the assumption that no current Tier 1 competitor (Tutopiya, Vedantu, Byju's, regional tutoring agencies) is already running an equivalent strategy. Validation required (see §11).

---

## 3. Market Reality Check

### What we know with confidence

| Data point | Source | Notes |
|---|---|---|
| Global private tutoring market 2024 | USD 124.5B | [imarcgroup.com](https://www.imarcgroup.com/private-tutoring-market) — IMARC Group |
| Global private tutoring market 2033 (forecast) | USD 238.5B (CAGR 7.49%) | [imarcgroup.com](https://www.imarcgroup.com/private-tutoring-market) |
| Asia Pacific share of global tutoring (2025) | 60.85% / USD 40.74B | [Fortune Business Insights](https://www.fortunebusinessinsights.com/private-tutoring-market-104753) |
| Online tutoring market 2025 | USD 10.72B | [Technavio India report](https://www.technavio.com/report/online-tutoring-services-market-in-india-industry-analysis) (referenced) |
| Online tutoring market 2033 (forecast) | USD 31B | Same |
| UAE private tutoring market | USD 470M | [Ken Research](https://www.kenresearch.com/uae-private-tutoring-market) |
| % Dubai students with tutoring | 49% overall, 70% Indian curriculum, 38% UK/American | [Discover Learning Tutors](https://www.discoverlearningtutors.com/demand-for-tutoring-in-dubai/) |
| Pakistan Cambridge AS/A-Level entries 2024 | 125,000+ (+7% YoY) | [Tes](https://www.tes.com/magazine/news/general/cambridge-international-exams-2024-results-released) |
| Pakistan Cambridge IGCSE/O-Level/A-Level total | 100,000+ at 683 schools | [The News International](https://www.thenews.com.pk/latest/1219554-cambridge-announces-oa-level-igcse-exam-results-in-pakistan) |
| Pakistan private-school tutoring rate (2016-17) | 33% | [PMC frontiersin.org](https://pmc.ncbi.nlm.nih.gov/articles/PMC9554537/) |
| Lahore secondary students reliant on private tuition | 62% | [Express Tribune](https://tribune.com.pk/story/2580040/our-shadow-education-a-red-light-for-a-failing-institution) |
| Pakistan government education spending (GDP %) | Fell from 2.0% (2018) to 0.8% (recent) | [Express Tribune](https://tribune.com.pk/story/2580040/our-shadow-education-a-red-light-for-a-failing-institution) — drives shadow education demand |

### What we don't know — research gaps

These are gaps the report cannot fill from desk research. They become validation work:

1. **Specific tutor-to-student ratio** in Tier 1 markets for CIE/IGCSE. (Anecdotal: 5-20 students per tutor commonly cited but unverified.)
2. **Tutor income per student per month** in Pakistan, UAE, India for A-Level Maths tutors. Critical for incentive design.
3. **Tutor willingness to adopt third-party platforms.** No data found on adoption rates of free SaaS tools by independent tutors in these markets.
4. **Conversion rate from tutor recommendation to paying student subscription.** No comparable case study found in this segment.
5. **India-specific Cambridge entries** for 2024. Search returned Pakistan and global figures but not granular India data.
6. **UAE Cambridge entries** specifically (CIE 9709). UAE tutoring market data is solid but not broken out by board.
7. **Whether any current Tier 1 competitor (Tutopiya, Vedantu, regional players) is already running a tutor-equipping model.** Tutopiya appears to be a tutor marketplace, Vedantu and Byju's are direct-to-student. No evidence of "free dashboard for independent tutors" approach found, but absence of evidence is not evidence of absence.

---

## 4. The Competitive Landscape

### Exam-prep content platforms (ExamPilot's direct space)

| Platform | Tutor-facing features | Distribution model |
|---|---|---|
| Save My Exams | "Save My Exams for Teachers" includes Test Builder and resources. ~430,000 educators trust the platform [(savemyexams.com)](https://www.savemyexams.com/teachers/). | Teacher/tutor use is a feature, not a strategic distribution channel. Primary growth is direct B2C subscription at ~£15/month. |
| Physics & Maths Tutor (PMT) | Free PDF resources usable by tutors and educators | Free model; expanding into paid mock papers. No tutor distribution program. |
| Sparx Maths | Teacher dashboard for setting weekly homework | UK school market focus. Sold to schools, not tutors. |
| MyMaths | 4M students/year, primary to A-Level | Subscription-based with school licenses. |
| Tutopiya | IGCSE/A-Level/IB focus, "500K students improved" | Tutor marketplace — tutors offer paid sessions through the platform. Competes for tutors, doesn't equip independent ones. |
| Vedantu | Live tutoring for grades 4-12 | Direct B2C live tutoring. Vedantu IS the tutor. |
| Byju's / Byju's Tutor | 1-on-1 live classes | Direct B2C live tutoring. Same model. |

**Reading.** Nobody in this competitive set is positioned where the proposed Tutor Mode would sit: a content + assessment platform that equips *independent* tutors as a primary distribution layer while the student pays. Vedantu/Byju's are competitors *to* tutors. Save My Exams treats tutors as a marginal user segment. Tutopiya is a marketplace.

This is the strongest piece of evidence that the position is open. It is also the weakest, because absence of competitors could mean either an unseen opportunity or a market that has been tried and failed quietly.

### Tutor management SaaS (adjacent space)

| Platform | Focus | Geography |
|---|---|---|
| TutorCruncher | Tutor business operations: scheduling, billing, CRM. API-first, founded 2013. | UK/US-centric. Larger tutoring agencies. |
| Teachworks | Tutor business operations: usage-based pricing. | UK/US-centric. SMB tutoring centres. |

These are infrastructure tools for tutoring businesses. They do not deliver content to students. They are **complementary, not competitive** to a Tutor Mode that focuses on student weak-spot detection and homework generation.

---

## 5. The Tutor Mode Product (MVP Spec Seed)

This section is a seed for a technical specification, not the spec itself.

### What the MVP must do

The product question: what would a tutor of 5-15 CIE 9709 / IGCSE students actually use, weekly, that they cannot get from a notebook + WhatsApp?

Three jobs the MVP needs to do:

1. **Show the tutor what their students don't know.**
   A heatmap view across all of the tutor's students, by topic (mapped to ExamPilot's existing knowledge graph). The tutor opens it before a session and immediately sees: "Aamir is weak on integration by parts. Priya is solid on differentiation but struggles with applications."

2. **Give the tutor a homework assignment to set.**
   One-click "set this for Aamir for next week" pulling from ExamPilot's question bank, targeted at his weak nodes. Includes a printable PDF and a shareable WhatsApp link.

3. **Generate a shareable progress digest the tutor can send to parents.**
   A one-page weekly summary per student, branded with the tutor's name (e.g., "Aamir's progress — Mr. Khan's tutoring"). Sent via WhatsApp/email. This is the *trust transfer* mechanism: parents see ExamPilot's data, attributed through the tutor they already trust.

### What the MVP must NOT do

These are scope cuts that should be defended:

- Not a tutor-to-student matching marketplace. Tutors bring their own students.
- Not a billing/scheduling system. TutorCruncher and Teachworks own that space.
- Not a separate app or codebase. Should be a role/view inside the existing ExamPilot platform.
- Not live tutoring features. ExamPilot is async by design.

### Technical assumptions to validate

These need confirmation against the actual codebase (231,544 LOC, 20+ AI agents per company narrative). I have not read the engineering wiki articles to confirm these are present:

- Multi-tenant data model that supports "tutor sees N students" without major rearchitecture
- Question Bank + Knowledge Graph already addressable by API for the homework generator
- Question DNA + Exam Readiness Index (ERI) available per student for the digest
- WhatsApp/share-link infrastructure for the progress digest
- Existing onboarding flow flexible enough to add a "tutor" role distinct from "student"

**Recommended Phase 0 task: 2-hour engineering review of these assumptions before any commitment.**

### MVP feature scope estimate

Rough estimate; needs engineering confirmation:

| Feature | Estimated effort |
|---|---|
| Tutor role + multi-student dashboard view | Medium |
| Cross-student weak-spot heatmap | Medium |
| Homework assignment generator | Medium |
| Progress digest (PDF + WhatsApp-shareable link) | Medium |
| Tutor invite / student-link-to-tutor flow | Small-Medium |
| Basic referral attribution (UTM-based) | Small |

Without engineering input, total estimate is **4-8 weeks** of focused work for an MVP that can be put in front of real tutors. This is *consistent with* the original Tutor Flywheel recommendation but should be re-estimated by engineering before commitment.

---

## 6. Economic Model and Incentive Design

This is the hardest design problem. If the incentives are wrong, the flywheel does not spin.

### The constraint

The marketing plan declares "Consumer-only pricing always." This is a structural constraint. The tutor flywheel must respect it: students pay, tutors do not. The question is what tutors *get* in return for the referral.

### Three possible incentive structures

**Option A: Free Tutor Mode in exchange for student referrals.**
Tutor gets the full Tutor Mode free indefinitely. The expectation is that any student they coach uses ExamPilot. No cash kickback. The tutor's gain is professional: better tools, better outcomes, more impressive to parents, easier prep.

- Pros: Clean. No payment infrastructure. No tax/VAT complications across jurisdictions. Aligned with consumer-only pricing.
- Cons: Maybe insufficient incentive. Tutors might use the dashboard and not push the paid student product.

**Option B: Tiered tutor access — free baseline, premium unlocked by student conversions.**
Tutor gets a basic free tier. Unlocking advanced features (e.g., predictive grading, examiner-grade marking, AI essay feedback for tutoring sessions) requires N converted paying students.

- Pros: Gamifies the referral. Aligns tutor incentive with ExamPilot revenue.
- Cons: More complex to build and explain. Tutors may resent the gating.

**Option C: Tutor-attributed extended trial for their students.**
The tutor's students get a longer free trial (e.g., 30 days vs 14) when they sign up through the tutor's referral link. This makes the tutor "the person who got you a longer trial," which is socially valuable to the tutor in front of the parent.

- Pros: Lowers student friction at the most critical conversion moment. No tutor payment needed. The tutor *and* the student both benefit from the same lever.
- Cons: Slightly delays revenue.

**Most likely correct answer: combination of A + C.** Free Tutor Mode (A) plus extended trial for tutor-referred students (C). Option B is held in reserve as a Phase 2+ refinement once base behaviour is understood.

### Why no cash kickback

In international tutoring markets, paid referral relationships have regulatory ambiguity, tax implications across jurisdictions, and can taint the tutor's recommendation in the parent's eyes ("are you recommending this because it helps me or because you get paid?"). The product-based incentive is cleaner.

### Counter-consideration

This decision should be revisited if validation interviews surface that tutors expect cash. The model can be adjusted; the assumption that "free product is enough" is just that — an assumption.

---

## 7. Financial Projections

All numbers in this section are scenario models, not forecasts. They are stated explicitly so that the assumption set can be tested.

### Inputs and assumed values

| Input | Conservative | Base | Optimistic | Notes |
|---|---|---|---|---|
| Active tutors in flywheel by Nov 2027 | 30 | 75 | 150 | Validation needed |
| Students per active tutor (avg) | 6 | 10 | 15 | Anecdotal range; needs verification per market |
| % of tutor's students who sign up for ExamPilot trial | 30% | 50% | 70% | Pure assumption — needs validation in pilot |
| % of trial signups who convert to paid | 18% | 22% | 28% | Plan baseline 15-22%; tutor-referred should convert higher |
| Blended MRR per paying user | EUR 17 | EUR 18 | EUR 19 | From marketing plan v3.0.1 |
| Monthly churn (steady state) | 8% | 6% | 5% | Plan assumes 5-7%; tutor-referred may retain better |

### Resulting steady-state MRR (illustrative)

These are illustrative outputs from the inputs above, presented as a sanity-check range, not a forecast.

**Conservative scenario.**
- Paying users: 30 × 6 × 30% × 18% ≈ 10 paying users (very low, single-cohort math)
- After 12 months of tutor onboarding with churn at 8%: ~ 50-80 paying users in steady state
- MRR: ~EUR 850-1,360

**Base scenario.**
- Paying users from tutors alone: 75 × 10 × 50% × 22% ≈ 83 paying users per cohort
- After 12 months of compounding with churn at 6%: ~250-400 paying users from the tutor channel
- MRR: ~EUR 4,500-7,200 *additive* to the rest of the marketing plan

**Optimistic scenario.**
- Paying users from tutors alone: 150 × 15 × 70% × 28% ≈ 441 paying users per cohort
- After 12 months with churn at 5%: ~800-1,400 paying users
- MRR: ~EUR 15,200-26,600 *additive*

### Critical sensitivity

The model is most sensitive to **"% of tutor's students who sign up for ExamPilot trial."** This is the unknown that validation must address first. At 30% conversion through tutor referral, the channel is solid but not transformative. At 70%, it becomes the dominant growth lever. The range is too wide to commit on without data.

### Cost side

Direct costs of running the flywheel:

| Cost | Estimate | Notes |
|---|---|---|
| Engineering (MVP build) | EUR 0 cash if internal; ~4-8 weeks of internal time | Opportunity cost real |
| Tutor outreach (organic) | EUR 0 cash; ~5-10 hours/week for first 6 months | Founders' time |
| Tutor incentive (extended trial cost) | Effectively negative-LTV-impact, modelled in conversion rate | Real but baked in |
| Tooling (CRM for tutor pipeline, e.g., Notion or Coda) | EUR 0 (existing tooling) | No new spend |
| Total cash cost | ~EUR 0-500 | Time is the real cost |

This is a low-cash-cost experiment with high time cost.

---

## 8. Tutor Acquisition Strategy

### Where the first 10 tutors come from

Highest-leverage channels for tutor outreach in Tier 1:

1. **LinkedIn (Pakistan, UAE, India).** Search "Cambridge A-Level Maths tutor" + geography. Cold DM with a specific value proposition (not "we have a product" but "I am building a tool for tutors of CIE 9709 — can I get 30 minutes of your time?"). Tied to Teresa's LinkedIn build-in-public strategy.
2. **Facebook tutor groups (Pakistan).** Closed groups for Cambridge tutors exist. Beacon Tutors, Cambridge.org.pk, and similar agencies have communities. Join, observe, contribute, then approach individuals.
3. **WhatsApp tutor networks.** Once one trusted tutor is in, they refer other tutors. This is how the tutor flywheel itself recruits *more flywheel*.
4. **University alumni networks.** A-Level Maths tutors in Pakistan are often LUMS, NUST, or IBA graduates. Alumni LinkedIn groups are reachable.
5. **Tutor-finder platforms (Beacon Tutors, Cambridge.org.pk, oleveltutors.com).** Not for poaching but for understanding who is tutoring CIE 9709 at scale.

### The pilot motion

**Phase 0 (June-July 2026): 8-12 tutor discovery interviews.**
- No product offered. Pure discovery. What do you struggle with? What tools do you use? Would you use a free dashboard? Under what conditions?
- Goal: validate the thesis before building.

**Phase 1 (Aug-Oct 2026): MVP pilot with 5 tutors.**
- After Results Day. Targeted invites to 5 tutors from the discovery cohort.
- Free Tutor Mode + extended trial for their students.
- Measured by: % of their students who sign up, % who convert.

**Phase 2 (Nov 2026 onward): scale to 30-50 active tutors.**
- Onboarding playbook codified.
- Pakistani tutors first (largest verified market, lowest cost of acquisition).
- UAE tutors second.

This phasing mirrors the existing marketing plan's structure and does not require new phase gates.

---

## 9. Validation Plan (Pre-Build)

The single most important pre-commitment step is validation. Building a Tutor Mode that no tutor wants is a 4-8 week opportunity-cost mistake.

### Minimum validation before any code commit

1. **8-12 tutor discovery interviews** (4 in Pakistan, 4 in UAE, 2-4 in India).
   - Mom-Test style. No selling. Pure discovery.
   - Questions to confirm (illustrative): How many students do you teach? What's your weekly prep flow? Do you currently use any digital tools to track them? How do you communicate progress to parents? Would a free dashboard that did X interest you?
2. **2 tutor co-design sessions** with the most engaged interview subjects.
   - Show them an early mockup or prototype. Get reaction. Get scope cuts.
3. **Pricing/incentive test in interview.** Ask directly: "If this were free for you and your students paid the normal subscription, would you recommend it? Under what condition?"

### Kill criteria

These would justify NOT proceeding even after validation:

- Fewer than 6 of 10 interviewed tutors say they would actively recommend ExamPilot to their students after seeing the product mock.
- Tutors expect cash compensation as a precondition for referral, breaking the consumer-only pricing model.
- Tutors already use a competing platform with equivalent functionality (would reframe positioning).
- Engineering effort to build MVP exceeds 12 weeks (no longer fits Phase 0-1 window).

### Confidence threshold to proceed

A go decision should require:
- ≥ 6 of ≥ 8 tutor interviews show positive intent.
- ≥ 2 tutors willing to co-design and beta test.
- Engineering MVP estimate confirmed at ≤ 8 weeks.
- One success-criteria-defined pilot plan documented for the 5 Phase 1 tutors.

---

## 10. Risk Analysis

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Tutors don't adopt — flywheel never starts | Medium | High | Validate before building. Kill criteria defined. |
| Tutors adopt the free dashboard but don't refer students | Medium | High | Incentive design (extended trial); Option B premium tiers as fallback |
| Students reject tutor's recommendation | Low | Medium | Tutor is high-trust source; risk should be empirically low |
| Tutor support burden eats founders' time | Medium | Medium | Phase 1 limit of 5 tutors caps exposure |
| Tutor brings low-quality students who churn fast | Low | Medium | Track tutor-cohort retention vs. organic in PostHog from day 1 |
| Tutors switch to a competitor that copies the model | Low (now) / Higher (year 2+) | Medium | First-mover advantage; relationship depth as moat |
| Engineering effort overruns and blocks Phase 0 content work | Medium | High | Strict timebox on MVP; Phase 0 content work must not depend on it |
| Multi-country tax/legal complications | Low | Low | Tutors are not paid; B2C billing already handles cross-border |
| Tutor uses Tutor Mode without recommending ExamPilot to students | High | Low-Medium | If pattern emerges, gating premium features behind referrals (Option B) |
| Plan ambiguity: tutor-flywheel work distracts from documented Phase 0 priorities | Medium | High | Treat as parallel workstream with defined phase gate, not a Phase 0 substitution |

---

## 11. Integration Impact on Existing Plan

If adopted, the Tutor Flywheel changes specific parts of the existing marketing plan. Captured here for the implementation-phase work, not to be done now.

### Marketing plan (wiki/marketing/growth/marketing-plan.md)

- The "Reddit repositioned as SEO/AI citation seeding" and "Tutor referrals 15-25" channels would be augmented. Tutors become a documented primary channel, not a side channel.
- The student micro-funnel adds a tutor-mediated path: Tutor → ExamPilot (via tutor's referral link / extended trial) → Trial → Paid.
- Phase 1 acquisition targets adjust: tutor-referred trial signups become a tracked sub-metric.

### Customer personas (wiki/product/research/customer-personas.md)

- A new persona is required: the Tutor as primary partner. This is not the same as the Teacher referral partner (Teresa/Mr. Rahman). Tutors are independent, paid by parents, often run their own micro-businesses.
- Voice file required: `references/voice-tutor.md` for tutor-facing communications and product copy.

### Signal registry (marketing/gtm-engineering/signal-registry.md)

- Add "Tutor referral signup" as a high-weight first-party signal (above the existing "Tutor referral click +18").
- Add "Tutor dashboard weekly active" as an engagement signal (predicts whether the tutor is genuinely using the tool).

### Product (wiki/product/strategy/)

- Tutor role/scope addition. Not currently in product vision documents; would require a new article: `wiki/product/strategy/tutor-mode.md`.

### Fundraising narrative (wiki/business/fundraising/)

- This addition strengthens the company narrative materially. "We have a Tier 1 international distribution channel through independent tutors" is a structurally different pitch than "we are doing SEO and Reddit." Update company-narrative.md if/when adopted.

### KPI framework

- Tutor-channel-specific KPIs: # of active tutors, students per tutor, conversion rate by tutor, retention by tutor-channel cohort.

---

## 12. Open Questions and Required Research

Listed as the explicit set of unknowns at time of writing. These need answers before a confident go decision.

1. What is the typical income per student for a CIE 9709 Maths tutor in Pakistan, UAE, India? (Determines whether free Tutor Mode is enough incentive.)
2. What is the average number of CIE 9709 students per active tutor in each market?
3. Are there existing platforms in any of the Tier 1 markets running this model and either succeeding or failing quietly? (Negative result narrows the strategy; positive result narrows the timing window.)
4. What does the engineering team estimate for MVP Tutor Mode build effort?
5. Does ExamPilot's existing data model support multi-student-per-tutor relationships without rearchitecture?
6. What is the regulatory/tax position on running unpaid referral relationships with international tutors? (Likely benign but should be checked.)
7. Are there published market reports on tutoring adoption rates for CIE specifically (not general K-12) that would tighten the conversion assumptions?
8. What is the actual willingness of Pakistani/UAE/Indian tutors to recommend a paid platform to families? (Cultural/professional norms may differ.)

---

## 13. Decision Framework

When the go/no-go meeting happens, evaluate against these gates.

### Must be true for GO

1. ≥ 6 of ≥ 8 tutor interviews show clear intent to use Tutor Mode and recommend ExamPilot to students.
2. Engineering MVP estimate ≤ 8 weeks of internal effort.
3. The team has capacity to onboard and support 5 tutors through Phase 1 without compromising the existing Phase 0-1 commitments (Results Day staging, Brevo wire-in, content infrastructure).
4. The incentive design has been tested in interviews and a workable shape is identified (likely free Tutor Mode + extended trial).
5. The marketing plan's "consumer-only pricing always" rule can be reaffirmed under this model.

### Indicates NO-GO

1. Tutor interviews show indifference or expectation of cash compensation.
2. Engineering effort exceeds 12 weeks or requires significant architectural change.
3. A direct competitor is already running an equivalent model and has scale.
4. The opportunity cost (what doesn't get built/published in Phase 0-1 if this is built) outweighs the projected upside even in the optimistic scenario.

### Indicates DEFER (revisit at Phase 2)

1. Validation is inconclusive — tutors are interested but not committed.
2. Engineering MVP estimate is high but reducible with scoping.
3. Phase 0 priorities are too dense to absorb additional product work.

---

## 14. Next Steps

If the analysis is accepted as a basis for decision-making, the next steps in order:

1. **Owner assignment.** Enitan or Teresa explicitly owns the validation track. (Likely Enitan, given the product/GTM intersection.)
2. **Tutor sourcing list.** Identify 15-20 named CIE 9709 tutors in Tier 1 markets to approach for discovery interviews. Prioritise Pakistan (largest verified market, easiest to reach via LinkedIn).
3. **Interview script written.** Mom-Test compliant. Avoids leading the witness.
4. **Discovery interview window scheduled.** Block 2-3 weeks in Phase 0 (target: mid-June to early-July 2026).
5. **Engineering review meeting.** Two hours with the engineer(s). Confirm MVP feasibility and effort estimate against current architecture.
6. **Go/no-go decision meeting.** After discovery interviews and engineering review complete. Decision documented in `decisions/log.md`.
7. **If GO:** Linear epic created with phased milestones (validation → MVP build → pilot with 5 tutors → scale).
8. **If NO-GO:** Document specific reasons in decisions log. Archive this analysis. Revisit at Phase 2 review.
9. **If DEFER:** Specify what additional information would change the answer and when it should be checked.

### Open questions for the decision meeting

- Is this strategically distinct enough from the current marketing plan to justify dedicated capacity, or is it a natural evolution of the existing tutor channel target?
- What happens to the existing Reddit / SEO / parent channel work if this absorbs capacity?
- Is there a smaller-scoped first step (e.g., manual tutor support without product feature build) that could test the conversion thesis cheaper?
- Should this be tied to a fundraising milestone (e.g., adopted contingent on EIC Accelerator funding) or run within current resource envelope?

---

## 15. Appendix: Sources

### Market data
- [Cambridge International exams: 2024 results released — Tes](https://www.tes.com/magazine/news/general/cambridge-international-exams-2024-results-released)
- [Cambridge announces O/A level, IGCSE exam results in Pakistan — The News International](https://www.thenews.com.pk/latest/1219554-cambridge-announces-oa-level-igcse-exam-results-in-pakistan)
- [UAE Private Tutoring Market — Ken Research](https://www.kenresearch.com/uae-private-tutoring-market)
- [The Rising Demand for Tutoring in Dubai — Discover Learning Tutors](https://www.discoverlearningtutors.com/demand-for-tutoring-in-dubai/)
- [Private Tutoring Market — Fortune Business Insights](https://www.fortunebusinessinsights.com/private-tutoring-market-104753)
- [Private Tutoring Market — IMARC Group](https://www.imarcgroup.com/private-tutoring-market)
- [India Online Tutoring Services Market — Technavio](https://www.technavio.com/report/online-tutoring-services-market-in-india-industry-analysis)

### Pakistan shadow education
- [Economic burden of private tutoring at higher secondary level in Pakistan — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9554537/)
- [Our shadow education — Express Tribune](https://tribune.com.pk/story/2580040/our-shadow-education-a-red-light-for-a-failing-institution)
- [Shadow Education ADB report (2010)](https://www.adb.org/sites/default/files/publication/29777/shadow-education.pdf)

### Competitive landscape
- [Save My Exams for Teachers](https://www.savemyexams.com/teachers/)
- [Save My Exams vs PMT comparison](https://www.savemyexams.com/learning-hub/support/physics-and-maths-tutor-alternative/)
- [Sparx Maths](https://sparxmaths.com/)
- [Tutopiya](https://www.tutopiya.com/)
- [Vedantu — Wikipedia](https://en.wikipedia.org/wiki/Vedantu)
- [Byju's — Wikipedia](https://en.wikipedia.org/wiki/Byju's)

### Tutor SaaS adjacent
- [TutorCruncher vs Teachworks](https://tutorcruncher.com/blog/tutorcruncher-vs-teachworks)

### Pakistan tutoring agencies (for outreach mapping)
- [Cambridge.org.pk — Pakistan's tutoring platform](https://cambridge.org.pk/)
- [Beacon Tutors PK](https://beacontutorspk.com/)
- [O Level Tutors Pakistan](https://oleveltutors.com/)

### Internal references
- `Spyglass-OS/marketing/gtm-engineering/signal-registry.md`
- `wiki/marketing/growth/marketing-plan.md` (v3.0.1)
- `wiki/product/research/customer-personas.md`
- `wiki/business/fundraising/company-narrative.md`
- `Spyglass-OS/marketing/context/audience-segments.md`

---

## Document changelog

- 2026-05-21 v1.0 — Initial draft. Pre-decision research. Authored in AIOS session.
