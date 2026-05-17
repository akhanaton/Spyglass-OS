# Channel Playbooks

Operational rules for each active marketing channel. Strategy lives in the wiki. This file covers HOW to operate day-to-day.

## Reddit

**Primary role:** SEO/AI citation seeding engine. Threads rank on Google (#2 most visible site) and get cited by AI tools (92.8% of AI search opportunities cite Reddit). Direct student acquisition is secondary. See marketing plan Section 3.3 for full repositioned strategy.

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

**What gets banned/downvoted:**
- Obvious marketing language ("revolutionary", "game-changing")
- Linking to your product in every comment
- Posting the same content across multiple subs
- Not answering the actual question before mentioning your product

## Discord

**Status: Secondary/optional.** CIE students in target markets (Pakistan, UAE, Nigeria, Malaysia) are on WhatsApp, not Discord. Discord remains available but is deprioritised in favour of WhatsApp Communities. Maintain presence but do not prioritise over WhatsApp.

**Target servers:** A-Level study servers, Cambridge Maths groups, Edexcel revision communities.

**Norms:**
- Join and contribute before promoting anything.
- Share study tips, answer maths questions, be helpful.
- Only share ExamPilot in dedicated "resources" or "tools" channels if they exist.
- Never DM-spam server members.

## WhatsApp

**Three use cases:** (1) Tutor group referrals, (2) Student communities, (3) Parent outreach.

### WhatsApp — Tutor Referrals
- Only message tutors you have a warm intro to or have engaged with elsewhere.
- Keep messages brief: who you are, what ExamPilot does, what's in it for their students.
- Maximum 1 follow-up if no response. Do not chase.
- Frequency: no more than 1 message per tutor per month.

### WhatsApp — Student Communities
- ExamPilot WhatsApp Community with sub-groups by exam board/topic (9709 Pure 1, 9709 Pure 3, Edexcel IAL)
- WhatsApp Business App (free) in Phase 0. Wati (~EUR30/month) in Phase 1+ for broadcasts and analytics.
- Broadcast messages: maximum 2/week. Always educational value, not promotional.
- Content: study tips, exam calendar alerts, new content announcements, Q&A.
- Same value-first rules as Reddit: no spam, no link drops, educational content first.
- Join existing CIE student study groups in Tier 1 markets (Pakistan, UAE). Observe norms before contributing.

### WhatsApp — Parent Groups
- Identify parent WhatsApp groups through Facebook Group connections and school contacts.
- Share exam prep tips, exam calendar reminders, link to "For Parents" page when relevant.
- Voice: `references/voice-parent.md`. Professional-parental, not student casual.
- Only groups you have a warm intro to. Maximum 1 follow-up if no response. No spam.

## Facebook Groups (Parent Acquisition)

**Primary role:** Parent-facing discovery and trust-building. Parents of CIE students in target markets are active in Facebook Groups. This is a manual, relationship-based channel. Facebook deliberately blocks automated posting to groups you don't admin.

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

**Posting cadence:** 2-3 contributions/week across groups (initial estimate).

**What works:**
- Exam calendar reminders and preparation timelines
- Study approach advice that parents can share with their children
- Value framing: tutoring cost comparisons, online tool landscape
- Progress tracking tips for parents who can't help with the maths themselves

## School/Teacher Outreach

**Primary role:** B2C2B referral partner acquisition. One school recommending ExamPilot = 50-200 potential students. Teachers are referral partners, not customers. Voice: `references/voice-teacher.md`.

**Channels:**
- LinkedIn: direct outreach to CIE/Edexcel maths teachers at international schools. Content warm-up required before outreach — see `build-in-public/references/linkedin-strategy.md`. Teresa's account only.
- Teacher WhatsApp groups: professional groups, not personal
- Email: professional outreach via school contact pages
- Warm intros from existing tutor contacts

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

## Email (Brevo)

**Status:** Stub until P2. Brevo selected but not yet connected.

**When wired (all cadences are initial estimates — adjust via `/tune` after 30 days of send data):**
- Welcome sequence: 5 emails over 14 days after signup
- Campaign emails: maximum 1 per week to engaged list
- Re-engagement: after 14 days inactive, maximum 3 emails
- Always include unsubscribe. GDPR compliance mandatory (under-18 audience).
- Segment by exam board (Cambridge vs Edexcel) and status (active vs churned).

## SEO / Blog

**Publishing cadence:** Maximum 3 articles per week (initial estimate). Quality over velocity.

**Review process:**
1. Draft generated via `/write-article` to `marketing/pipelines/drafts/`
2. Human reviews: resolve all [VERIFY] flags, check voice, check factual accuracy
3. Move to `marketing/pipelines/review/` when edits complete
4. Publish via `/publish-article` (P2) or manual CMS upload
5. Move to `marketing/pipelines/published/` with live URL

**URL architecture:** Follows wiki seo-strategy.md. Read it before creating any content.

## TikTok (P2)

**Status:** Planned. Not yet active.

**When active:**
- Short-form study tips (30-60 seconds)
- Search-optimized: keywords in caption, on-screen text, and spoken audio in first 3 seconds
- Focus on Cambridge 9709 and Edexcel IAL specific content
- No hard sell. Educational value first.
- 2-3 videos per week
- Posting times: 4pm-9pm GST (covers Pakistan, UAE after school; overlaps UK evening)
- Region-specific: no UK slang, universal exam identifiers (paper codes, topic names), international school contexts
- Consider Urdu subtitles for Pakistan-targeted content (Phase 2, test engagement)
- Hashtags: #alevel #cambridgemaths #9709 #revision #olevel #igcse #cambridgeinternational

## X / Build in Public

Moved to dedicated sub-OS. See `build-in-public/context/channel-rules.md`.
