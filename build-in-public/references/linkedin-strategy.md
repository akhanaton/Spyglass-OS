# Build in Public on LinkedIn — Strategy Reference

ExamPilot's LinkedIn strategy. Teresa posts from her personal account. This file covers the WHY and WHAT. For operational rules (HOW), see `build-in-public/context/channel-rules.md` (LinkedIn section).

## Why LinkedIn

LinkedIn serves a different audience than X and a different purpose than student-facing channels. The people ExamPilot needs to reach for B2C2B growth — maths teachers at international schools, school administrators, parents in professional roles — are active on LinkedIn.

LinkedIn does two things simultaneously:
- **Content warm-up:** A teacher who has read 10 of Teresa's posts on exam prep and learning science before receiving a DM is already half-sold. Content does the trust-building so the outreach doesn't have to.
- **Professional credibility:** Press, edtech partnerships, and advisor relationships come from people who found Teresa through LinkedIn content, not from cold approaches.

It does NOT directly convert students. That is not the goal.

## Why Teresa

Teresa's educational background gives her natural authority with the LinkedIn audience. Teachers want to hear from someone who understands the classroom — not an engineer. Parents want to hear from another parent who also understands the exam system. Teresa is both.

Enitan may join LinkedIn later with a product/engineering angle. For now: Teresa is the voice.

## Audience

**Primary:** CIE and Edexcel maths teachers at international schools. Ages 28-55. Teaching A-Level or IGCSE maths. Aware of student exam pressure. Frustrated by the gap between what students need and what's available.

**Secondary:** Parents of international school students in professional roles. Ages 35-55. LinkedIn-active. Making decisions about their child's exam preparation.

**Tertiary:** EdTech professionals, school administrators, curriculum coordinators.

They care about: student outcomes, what actually works in exam prep, the gap between traditional tutoring and modern tools, the learning science behind maths mastery. They are allergic to corporate marketing speak but respond to genuine professional insight.

They do NOT care about: the indie hacker journey, MRR targets, or how we're building in public. The X build-in-public frame is wrong for this audience. Adapt the source material, not the frame.

## Content pillars (with target ratios)

**These ratios are initial estimates.** Adjust based on engagement data after 30 days via `/tune`.

| Pillar | % (initial estimate) | Examples |
|---|---|---|
| Educational insights | 35% | "What CIE Paper 1 actually tests (and what most students miss)" / "Why rote practice fails for 9709 integration" |
| Behind the scenes — educator angle | 25% | "What building ExamPilot taught me about how students actually learn maths" — sourced from decisions/log.md, adapted to professional frame |
| Teacher/educator recognition | 20% | Celebrate what excellent CIE maths teachers do. Build goodwill with the audience you need. |
| Milestones and product updates | 20% | "We just launched topic X — here's what went into getting the worked examples right" — professional framing, not founder raw |

The decisions log is the richest content source. Most entries are reframeable as professional insights with minimal adaptation.

## The angle adaptation rule

Same source material. Different frame.

| Source | X frame (Enitan/Teresa) | LinkedIn frame (Teresa) |
|---|---|---|
| decisions/log.md entry | "We decided X because Y. Here's what almost made us choose Z." | "3 things choosing our content approach taught me about how students learn" |
| Shipped feature | "Just shipped X. Took Y hours. Here's what broke." | "We just added [feature]. Here's the problem it solves for students working through 9709." |
| Content creation process | "Just wrote our 10th article. Python scorer gave it a 72. Tweaking structure." | "What writing 10 articles on CIE maths revision taught me about exam-ready explanations" |
| PostHog metric | "1,000 sessions. Here's the feature students use most." | "Students spent 3x more time on worked examples than practice questions. Here's what that tells us." |

The X post is a confession. The LinkedIn post is an insight.

## Format guide

LinkedIn's algorithm rewards:
- Text posts with line breaks (no links in body — put in first comment)
- Native documents/carousels (PDFs with 6-10 slides — highest engagement format on LinkedIn)
- Consistency over frequency

| Format | When to use | Optimal length |
|---|---|---|
| Text post | Daily observations, milestones, quick insights | 1,000-1,500 characters |
| Carousel (PDF) | Structured guides, frameworks, "X things" posts | 6-10 slides, no wall of text per slide |
| Native article | Deep educational content, thought leadership | 800-1,500 words |

## Posting cadence

**2-3 original posts per week.** Quality over frequency. LinkedIn's algorithm penalises inconsistency more than low volume — a missed week is better than a bad post.

**First 60 days:**
- 2 text posts/week + 1 carousel/week
- 5-10 quality comments/week on other educators' and edtech professionals' posts
- Target: teachers posting about CIE/Edexcel, edtech founders, education researchers

**After 500 followers:**
- Begin native articles quarterly (SEO-indexed, longer shelf life)
- Increase carousel frequency if they're outperforming text posts
- Review pillar ratios via `/tune`

**Best posting times (initial — test and adjust):**
- Tuesday-Thursday, 8-10am GMT (professionals browsing before work)
- Avoid Mondays (low engagement) and Fridays after 12pm

## Algorithm rules

- Reply to all comments within 2 hours of posting. The algorithm scores your response rate.
- Engage with comments in the first 30-60 minutes — early engagement juices reach.
- No links in post body. LinkedIn deprioritises external links. Put the link in the first comment and reference it at the end of the post ("link in comments").
- 3 hashtags max. Relevant ones: #cambridgeinternational #alevel #mathseducation #examprep #edtech
- Do not cross-post from X. LinkedIn detects it and penalises reach. Adapt or rewrite.

## Anti-AI rules for LinkedIn

The professional audience includes educators who can spot AI content instantly. LinkedIn has stricter AI-detection norms than X because the stakes are professional credibility.

1. Never publish raw AI output. Treat `/write-linkedin` output as a draft generator.
2. Every draft reviewed and personally edited by Teresa before posting.
3. Add specific classroom observations, student stories (anonymised), and personal context. AI cannot add what Teresa has actually experienced.
4. Banned phrases: "game-changer", "revolutionary", "in today's digital landscape", "it's worth noting", "moreover", "furthermore", "in conclusion", "I'm excited to share", "proud to announce" (overused on LinkedIn), "thrilled".
5. Em dashes: allowed sparingly on LinkedIn (they're more accepted here than on X), but no more than one per post.
6. The test: "Would a teacher I respect read this and think it was genuine?" If not, rewrite.

## Teacher outreach integration

LinkedIn content is the warm-up layer for school/teacher outreach. Before sending any DM:
- Teresa's profile must show at least 5-10 posts relevant to CIE/Edexcel maths teaching
- Content must be visible and public
- Profile must be complete: headshot, professional bio referencing teaching background, ExamPilot, and the mission

Outreach sequence (after content warm-up is established):
1. Connect with personalised note referencing a specific pain point ("I work with CIE maths students and noticed your work at [school]")
2. Wait for acceptance. Do not pitch in connection request.
3. First message: genuine observation or question. No pitch.
4. If interested: share 1 piece of relevant content. Offer free access.
5. If no response: one follow-up after 2 weeks. Then stop.

Full outreach rules in `marketing/context/channel-playbooks.md` (School/Teacher Outreach section).

## Scheduling

All scheduling via Postiz (Standard plan, $29/mo — same plan as X). Incremental cost: $0.

Phase 0: Teresa copies approved drafts to Postiz dashboard manually.
Phase 1 (after n8n): n8n pushes approved drafts to Postiz API.

## Analytics

- **Postiz dashboard:** impressions, engagement rate, follower growth per post
- **LinkedIn native analytics:** post reach, profile views, connection growth
- **UTM tracking:** all links shared on LinkedIn use `?utm_source=linkedin&utm_medium=social&utm_campaign=bip` — tracked in PostHog
- **Primary metrics:** engagement rate (target 3-5% for professional accounts), connection acceptance rate for teacher outreach
- **Reviewed in:** `/weekly-pulse` (add LinkedIn as Step 6.6)

## Timeline

Professional audiences build more slowly than indie hacker communities but are higher-value per connection.

- Months 1-2: 100-300 followers. Establishing consistency. Finding what resonates with teachers vs parents.
- Months 3-4: 300-800 followers. Inbound teacher connections starting. Outreach acceptance rate improving.
- Months 5-8: 800-2,000+ followers. Warm outreach viable. School referrals beginning.
- First meaningful B2C2B conversion from LinkedIn: expect Month 4-6.

## Account setup checklist (Teresa)

Before first post:
- [ ] Professional headshot
- [ ] Headline: "Co-founder at ExamPilot | Helping CIE maths students pass with confidence" (or similar — must include teaching/education angle)
- [ ] About section: personal story — parent, saw the exam prep gap, building the solution. Under 300 words. First person.
- [ ] Featured section: pin one carousel or article once content exists
- [ ] Experience: ExamPilot co-founder + any relevant education/tutoring background
- [ ] Location: current city (builds local trust)
- [ ] Open to: collaborations, partnerships (not job opportunities)
