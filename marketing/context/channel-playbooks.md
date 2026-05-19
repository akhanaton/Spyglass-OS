# Channel Playbooks

Operational rules for each active marketing channel. Strategy lives in the wiki (`wiki/marketing/growth/marketing-plan.md`). This file covers HOW to operate day-to-day.

---

## Reddit

**Primary role:** SEO/AI citation seeding engine. Threads rank on Google (#2 most visible site) and get cited by AI tools (92.8% of AI search opportunities cite Reddit). Direct student acquisition is secondary. See [[marketing-plan]] Section 3.3 for full repositioned strategy.

**Active subreddits (reprioritised):**
- r/CambridgeInternational — primary, direct CIE audience
- r/Edexcel — Edexcel IAL students directly
- r/alevel — secondary, strong Google indexing but UK domestic audience
- r/6thForm — tertiary, UK-focused

**Rules of engagement:**
- Value first, always. Answer the question before anything else.
- Never self-promote in first interaction with a community. Build karma first.
- Only mention ExamPilot when directly relevant to the question being asked.
- No link drops. If mentioning ExamPilot, describe what it does. Let them Google it.
- Read the sub rules before posting. r/alevel and r/6thForm have specific self-promo restrictions.
- If asked directly "what tools do you recommend", that is the green light.
- Account must have sufficient karma and age. Minimum: 50+ karma, 30+ days.

**Posting cadence:** 2-3 genuinely helpful contributions per week per sub (initial estimate). No flooding.

**Best posting times:** Evenings GMT (after school, 4pm-9pm UK) and weekends (initial estimate). For SEO/AI seeding, timing matters less than content quality and search-intent targeting. Posts optimised for long-tail queries ("how to solve 9709 integration by substitution") compound regardless of posting time.

**Content types by phase:**

| Phase | Content Type | Example |
|---|---|---|
| 0: Foundation | Pure value posts targeting search-intent queries | "Here's how to approach 9709 Pure 1 integration by substitution — the three patterns the examiner tests" |
| 1: Soft Launch | Value + soft mention when relevant | "I've been working on a tool that does exactly this..." |
| 2: Growth | Value + natural recommendation, authoritative voice | Full engagement as a known, trusted contributor with exam-specific expertise |
| 3: Scale | Community leadership + content seeding | Host AMAs, provide exam season guides, become the go-to authority for 9709 content |

**Reddit → SEO/AI flywheel:** Reddit threads that rank on Google are the highest-leverage content asset. The CIE student in Lahore won't browse r/alevel directly, but they will find an ExamPilot answer through Google, ChatGPT, or Perplexity. Search for existing high-ranking threads about Cambridge 9709 topics and add genuinely helpful answers. These answers get indexed by Google, cited by AI search tools, and compound into a durable authority loop.

**What gets banned/downvoted:**
- Obvious marketing language ("revolutionary", "game-changing")
- Linking to your product in every comment
- Posting the same content across multiple subs
- Not answering the actual question before mentioning your product

---

## Discord

**Status: Secondary/optional.** CIE students in target markets (Pakistan, UAE, Nigeria, Malaysia) are on WhatsApp, not Discord. Discord remains available but is deprioritised in favour of WhatsApp Communities. Maintain presence but do not prioritise over WhatsApp.

**Target servers:** A-Level study servers, Cambridge Maths groups, Edexcel revision communities.

**Norms:**
- Join and contribute before promoting anything.
- Share study tips, answer maths questions, be helpful.
- Only share ExamPilot in dedicated "resources" or "tools" channels if they exist.
- Never DM-spam server members.

---

## WhatsApp

**Three use cases:** (1) Tutor group referrals, (2) Student communities, (3) Parent outreach.

### WhatsApp — Tutor Referrals
- Only message tutors you have a warm intro to or have engaged with elsewhere.
- Keep messages brief: who you are, what ExamPilot does, what's in it for their students.
- Maximum 1 follow-up if no response. Do not chase.
- Frequency: no more than 1 message per tutor per month.

### WhatsApp — Student Communities

**Phase 0 setup (WhatsApp Business App — free):**
- Install WhatsApp Business App
- Create ExamPilot WhatsApp Channel (broadcast-only, unlimited followers, free)
- Create ExamPilot WhatsApp Community (up to 5,000 members with sub-groups, free)
- Sub-groups by exam board or topic: "9709 Pure 1", "9709 Pure 3", "Edexcel IAL"
- Seed with study tips, exam calendar reminders, new content announcements

**Phase 1+ tool evaluation (when community exceeds 256 members):**
- **Wati** (~EUR30/month Growth plan, 3 users) — automated welcome messages, broadcast segmentation by exam board, link click tracking, CRM integration (Attio, PostHog UTM params)
- **Interakt** (~EUR15/month) — budget option
- **AiSensy** (~EUR20/month) — South Asia-focused BSP

**Operating model:**
- Broadcast messages: maximum 2/week. Always educational value, not promotional.
- Content: study tips, exam calendar alerts, new content announcements, Q&A.
- Same value-first rules as Reddit: no spam, no link drops, educational content first.
- Join existing CIE student study groups in Tier 1 markets (Pakistan, UAE). Observe norms before contributing.

### WhatsApp — Parent Groups
- Identify parent WhatsApp groups through Facebook Group connections and school contacts.
- Share exam prep tips, exam calendar reminders, link to "For Parents" page when relevant.
- Voice: `references/voice-parent.md`. Professional-parental, not student casual.
- Only groups you have a warm intro to. Maximum 1 follow-up if no response. No spam.

---

## Facebook Groups (Parent Acquisition)

**Primary role:** Parent-facing discovery and trust-building. Facebook deliberately blocks automated posting to groups you don't admin — this is a manual, relationship-based channel.

**Target groups:**
- COALI (Cambridge O/A Level and IGCSE): 100,000+ members, Pakistan-dominant
- Cambridge International Education official page: 969,520+ likes
- Dubai Expat Community: 110,000+ members
- Abu Dhabi Q&A: 93,000+ members
- School-specific parent groups (discovered through existing contacts)

**Rules of engagement:**
- Join and observe norms for 2-4 weeks before contributing.
- Answer parent questions about CIE exam preparation with genuine, helpful advice.
- Voice: `references/voice-parent.md`. Knowledgeable, helpful, not salesy.
- Only mention ExamPilot when directly relevant to a parent's question.
- No link drops. Describe what ExamPilot does. Let them search.
- No cross-posting the same content across multiple groups.
- Track activity in Coda Signals table (which groups, what posted, parent inquiries generated).

**Posting cadence:** 2-3 contributions/week across groups (initial estimate — adjust via `/tune` after 30 days).

**What works:**
- Exam calendar reminders and preparation timelines
- Study approach advice that parents can share with their children
- Value framing: tutoring cost comparisons, online tool landscape
- Progress tracking tips for parents who can't help with the maths themselves
- "For Parents" page referrals when questions about safety/GDPR come up

**"For Parents" landing page design principles:**
- Trust-first: GDPR compliance badge, data safety statement, "no social features" prominent above the fold
- Value framing: EUR29/month vs. private tutoring costs in target markets. EUR144/year = one hour of tutoring for a year of daily practice.
- Progress visibility: show the parent dashboard concept (topic-level progress, ERI trend, session frequency)
- Social proof: parent testimonials (with consent, parental consent for under-18 quotes)
- Clear CTA: "Start a free trial for your child"

---

## School/Teacher Outreach

**Primary role:** B2C2B referral partner acquisition. One school recommending ExamPilot = 50-200 potential students. Teachers are referral partners, not customers. Voice: `references/voice-teacher.md`.

**Channels:**
- LinkedIn: direct outreach to CIE/Edexcel maths teachers at international schools. Content warm-up required before outreach — see `build-in-public/references/linkedin-strategy.md`. Teresa's account only.
- Teacher WhatsApp groups: professional groups, not personal
- Email: professional outreach via school contact pages
- Warm intros from existing tutor contacts

**Teacher referral program:**

What teachers get:
- Free premium access to ExamPilot for personal use in lesson prep
- Aggregate class performance dashboard (student progress by topic, with student consent)
- No cost, no contract, no obligation

What we ask:
- "Would you be open to having 2-3 of your students try it for free? I'd love your feedback."

Scaling incentives:
- 5+ students via teacher's referral link = continued free access
- 20+ students = extended free access + recognition (case study, featured partner)
- Referral tracked via UTM: `?utm_source=teacher&utm_medium=referral&utm_campaign=[teacher-id]`

**Competitive models:** SaveMyExams "Free Teacher Partnership" scheme (free teacher accounts, students pay premium). Seneca Learning (30 students + 3 teachers = 100 premium accounts). ExamPilot's model is closest to SaveMyExams: free teacher access, consumer purchase.

**Outreach pipeline by phase:**
- Phase 0: Manual outreach to 5-10 school maths departments in Tier 1 markets via LinkedIn, warm intros from tutor contacts, CIE school directories. Teresa's LinkedIn profile must show 5-10 relevant posts before any teacher DM.
- Phase 1: First school recommendations expected. Track in Attio CRM: school, teacher, status, students attributed.
- Phase 2: If validated, build self-serve teacher signup. Teacher creates account, gets free access, shares class join link.
- Phase 3: If school partnerships prove high-leverage, consider school-level partnerships (with explicit per-student consumer pricing, never licensing).

**Rules:**
- Professional voice. Address teachers as the expert.
- Lead with student outcomes, not product features.
- Low-commitment first ask: "Would you be open to having 2-3 of your students try it?"
- Maximum 1 follow-up if no response. Do not chase.
- Never cold DM teachers on personal social media.
- Never position ExamPilot as a tutor or teacher replacement.
- No B2B pricing/licensing language. Ever.
- Track all contacts in Attio CRM: school, teacher, status, students attributed.

**Outreach cadence:** 2-3 new school contacts per week in Phase 0-1 (initial estimate).

---

## Email (Brevo)

**Status:** Brevo selected. Wire in Phase 0 first two weeks. Silence after signup kills trust permanently.

**Setup checklist (in order):**
1. Create Brevo account and verify domain (exampilot.io)
2. Set up DKIM, SPF, and DMARC for deliverability
3. Create waitlist signup form and embed on landing page
4. Write and load 5-email waitlist sequence
5. Write and load 6-email onboarding sequence (fires in Phase 1)
6. Test all sequences with internal email addresses
7. Set up basic segments: waitlist vs trial vs paid (even if empty)

### Email Sequences

**Waitlist/Early Access Sequence (pre-launch, 5 emails):**
- Trigger: Signup via landing page
- Email 1 (immediate): "You're on the list" — confirmation + what ExamPilot is
- Email 2 (Day 3): Value content — a study tip relevant to their exam board
- Email 3 (Day 7): Behind the scenes — what we're building and why
- Email 4 (Day 14): Social proof — student quotes or early results
- Email 5 (on launch): "Your access is ready" — direct signup link

**Onboarding Sequence (post-signup, 6 emails):**
- Trigger: Free trial activation
- Email 1 (immediate): "Welcome. Here's how to start your first session."
- Email 2 (Day 1): "Your first session matters. Here's how to make it count."
- Email 3 (Day 3): "Here's what ExamPilot learned about your knowledge gaps."
- Email 4 (Day 7): Social proof + feature highlight (ERI, topic mapping)
- Email 5 (Day 10): Conversion prompt with pricing and value framing
- Email 6 (Day 13): Last chance before trial expires (urgency, not pressure)

**Nurture Sequence (active free/paid users):**
- Maximum 1 email/week to engaged list
- Content: exam tips, new features, study strategies, blog article highlights
- Segmented by exam board (Cambridge vs Edexcel) and status (free vs paid vs churned)

**Re-engagement Sequence (inactive users):**
- Trigger: 14 days inactive
- 3 emails maximum. If no response after 3, stop.
- Email 1 (Day 14): "We noticed you haven't practiced in a while. Here's what you're missing."
- Email 2 (Day 21): Value content (not a guilt trip)
- Email 3 (Day 28): "Is ExamPilot right for you? No hard feelings either way."

**Parent Email Sequence (4 emails):**
- Trigger: Parent email captured from "For Parents" page or Facebook Group
- Email 1 (immediate): "Here's what ExamPilot does for your child" — trust, safety, GDPR
- Email 2 (Day 3): "How it works" — product walkthrough, progress tracking emphasis
- Email 3 (Day 7): "What other parents are saying" — social proof, value framing
- Email 4 (Day 14): "Start a free trial for [exam board]" — conversion CTA

### Campaign Emails

| Campaign | Timing | Segment | Content |
|---|---|---|---|
| Results Day | August | Full list | "Whatever your result, here's your next move" |
| Resit launch | September | Waitlist + churned | Resit-specific landing page + trial offer |
| Mock season | January | Active + waitlist | "Mock prep guide" + product features |
| Pre-exam | April | All students | "Exam countdown" series (weekly for 8 weeks) |
| New feature | Ongoing | Relevant segment | Feature announcement + how it helps their revision |

### GDPR Compliance (Non-Negotiable)

- **Consent:** Every signup form includes clear consent language. Checkbox, not pre-checked.
- **Parental awareness:** For users who indicate they are under 16, request a parent/guardian email. Send a single notification explaining what data is collected and how to opt out.
- **Unsubscribe:** Every email includes a one-click unsubscribe link (GDPR-required and Brevo-enforced).
- **Data minimization:** Collect only what is needed: email, exam board, age bracket. No tracking beyond product functionality.
- **Data retention:** 24 months after last engagement. Documented in privacy policy.
- **Cookie consent:** Banner on all web properties with opt-in, not opt-out.
- **No purchased lists. Ever.**

**When to review cadences:** All cadences are initial estimates. Adjust via `/tune` after 30 days of send data.

---

## SEO / Blog

**Publishing cadence:** Maximum 3 articles per week (initial estimate). Quality over velocity.

**Review process:**
1. Draft generated via `/write-article` to `marketing/pipelines/drafts/`
2. Human reviews: resolve all [VERIFY] flags, check voice, check factual accuracy
3. Move to `marketing/pipelines/review/` when edits complete
4. Publish via `/publish-article` (P2) or manual CMS upload
5. Move to `marketing/pipelines/published/` with live URL

**URL architecture:** Follows wiki seo-strategy.md. Read it before creating any content.

---

## TikTok

**Status:** Launch Phase 2 (Nov 2026). Not yet active.

**Geographic focus:** Pakistan, UAE, Malaysia, Egypt, Saudi Arabia. TikTok is banned in India — no India-specific variant.

**Posting cadence:**
- Growing phase: 1 video/day (batch filming: 10 videos per filming session)
- Maintaining phase: 3-5 videos/week
- Best times (GST-optimised): 4pm-9pm GST (covers Pakistan + UAE after school, overlaps UK evening). Secondary: 7-9am GST (morning study).

**Content pillars (rotate weekly):**

| Pillar | % of Content | Example |
|---|---|---|
| Quick tips (15-30 sec) | 40% | "The integration trick that saves 5 minutes on 9709 P1" |
| Myth-busts (30-45 sec) | 20% | "Everyone says past papers are enough. Here's why they're not." |
| Story arcs (45-60 sec) | 15% | "I went from a D to an A in 3 months. Here's what changed." |
| Behind-the-scenes | 10% | Building ExamPilot, founder story, what we're working on |
| Trends/duets | 15% | Responding to trending sounds with exam revision angles |

**Search optimization:** Every video must include target keywords in caption text, on-screen text overlay (first 3 seconds), spoken audio (first 3 seconds), and hashtags: #alevel #cambridgemaths #9709 #revision #alevelmaths #olevel #igcse #cambridgeinternational.

**Region-specific content rules:**
- English audio (language of instruction for CIE worldwide)
- Avoid UK-specific slang (innit, mate, sixth form, UCAS). Use universally understood English.
- Examples and scenarios: reference international school contexts, not UK sixth form colleges.
- Pricing comparisons: use tutor rates in target markets (PKR 3,000-8,000/hour in Pakistan, AED 150-300/hour in UAE), not UK rates.
- Use exam paper codes (9709/12, WMA11) as universal identifiers across all markets.
- Consider Urdu subtitles for Pakistan-targeted content (Phase 2, test engagement before committing).

**TikTok-to-micro-funnel wiring:** Never put the full URL in TikTok videos. Use "Search 'ExamPilot Cambridge 9709'" or "Link in bio." This deliberately triggers the search step — generating branded search volume (Google signal), creating Reddit discussion (AI training data), and reaching students through whichever channel they trust most. All bio links use UTM: `?utm_source=tiktok&utm_medium=social&utm_campaign=[campaign-name]`.

### TikTok Exam Season Campaigns

**Campaign 1: "Revision Countdown" (March–May 2027)**
- Theme: Daily revision tips counting down to exam day
- Content: Topic-per-day revision walkthroughs, time management tips, past paper strategies, stress management
- Format: Series format with episode numbering ("Day 47: The one integration technique you must know")
- CTA: "Follow for daily tips" (building audience) + "Link in bio for your revision plan" (driving trials)
- Special: Live Q&A sessions (1/week) where students submit questions

**Campaign 2: "Results Day" (August 2026 + August 2027)**
- Theme: "Whatever your grade, here's what to do next"
- Tone: Empathetic, supportive, never condescending

| Timing | Content | Format |
|---|---|---|
| Results Day -3 days | "Whatever happens Thursday, here's what to remember" | Talking head, empathetic |
| Results Day -1 day | "The only 3 things that matter tomorrow" | Quick tip |
| Results Day (0-2 hrs) | Reaction + "here's what to do with your grade" | Talking head, raw emotion OK |
| Results Day (2-6 hrs) | Grade-specific "next steps" (one per grade bracket) | Series format |
| Results Day +1 | "The resit plan that actually works" | Value content + screen recording |
| Results Day +2-3 | "10-week countdown to October resits" | Series launch |

Pre-production note: Film multiple reaction variants in advance. Pre-write grade-specific "next steps" videos (A/A*, B/C, D/E, U) for rapid publishing.

**Campaign 3: "Resit Ready" (September–October)**
- Theme: Targeted, intensive revision content for resit students
- Content: "10-week resit plan", topic-specific gap closers, "what the examiner actually wants", motivation
- CTA: "Free trial" with resit-specific landing page
- Tone: Urgent but encouraging. "You know your grade. We know your gaps."

**Campaign 4: "Mock Season" (January–March 2027)**
- Theme: Mock exam preparation
- Content: "What to expect in your mock", topic predictions, last-minute revision techniques, "how mocks prepare you for the real thing"
- CTA: "Try ExamPilot's practice mode" (product-led)
- Note: First major campaign — use to test formats and build audience before the May/Jun exam window.

---

## Direct Outreach

**Primary purpose:** Hand-to-hand acquisition for the first 100 students. Does not scale — that is the point. Goal: prove product-market fit.

**Five channels:**

| Channel | Target Students P0-1 | Method |
|---|---|---|
| Tutor referrals (highest priority) | 15-25 | 10-15 tutor conversations, 2-3 students per converted tutor |
| Reddit direct (value-first, secondary) | 5-10 | Organic interest from value posting |
| WhatsApp communities | 10-20 | Community contribution + student study groups |
| School/teacher outreach | 10-20 | 5-10 school conversations, 2-3 converting to recommendations |
| Facebook Groups (parent) | 5-10 | Parent community engagement |
| Discord | 5-10 | Community contribution (secondary channel) |
| **Total** | **50-95** | First cohort for PMF validation |

**Tutor referral rules:**
- Target: Independent maths tutors teaching Cambridge 9709 or Edexcel IAL (LinkedIn, tutor directories, WhatsApp groups, existing network)
- Ask: "Would you be open to having 2-3 of your students try it for free?"
- Value prop for tutors: students get personalised gap analysis between sessions; tutors get insight into where students need help
- Only warm intros. Maximum 1 follow-up if no response. Never position as tutor replacement.

---

## Cross-Channel Content Engine

Every piece of content should serve at least two channels.

**Weekly content cycle:**

| Day | Primary Output | Derivatives |
|---|---|---|
| Monday | Blog article published (SEO) | — |
| Tuesday | — | Reddit value post adapted from article |
| Wednesday | — | Email tip extracted from article |
| Thursday | — | TikTok script from article's best insight |
| Friday | `/weekly-pulse` review | Plan next week's primary article |

1 article/week = 4 channel-specific pieces. At 3 articles/week, that is 12+ pieces of content per week across all channels, all from the same research and writing effort.

**Content source priority (in order of signal strength):**
1. **Reddit questions** — Search `site:reddit.com cambridge 9709 [topic]` to find real student language and pain points
2. **Keyword research** — `/research-keywords` pipeline for SEO opportunities
3. **Student feedback** — Questions and struggles from ExamPilot users (Phase 1+)
4. **Examiner reports** — Official insight into where students lose marks
5. **Competitor gaps** — Topics competitors cover poorly or don't cover at all
6. **Product data** — Aggregate performance patterns from ExamPilot usage (Phase 2+)

---

## X / Build in Public

Moved to dedicated sub-OS. See `build-in-public/context/channel-rules.md`.

---

## Quick Reference — What to Measure When

| "I want to know if..." | Look at... | Frequency |
|---|---|---|
| Our content is being found | GSC impressions, pages indexed | Weekly |
| Students trust us | Reddit upvotes, return visitors, time on site | Weekly |
| AI tools recommend us | Manual AI query checks | Monthly |
| Our funnel is working | Visitor → trial → activation → paid conversion | Monthly |
| Students are staying | D7, D30 retention, session depth | Monthly |
| We're spending efficiently | CAC by channel, blended CAC | Monthly |
| The business is growing | MRR, organic signup %, churn | Monthly |
