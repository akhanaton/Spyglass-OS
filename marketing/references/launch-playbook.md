# Launch Playbook

Pre-launch and launch execution framework for ExamPilot. Adapted from marketingskills launch patterns, tailored for B2C SaaS targeting 16-18 year old A-Level students.

## The ORB Framework

Structure launch marketing across three channel types. Everything leads back to owned channels.

### Owned Channels
Direct access, no algorithms. Get more effective over time.

- Email list (Brevo, once wired)
- Blog (exampilot.io/blog)
- Website/product

### Rented Channels
Visibility you don't control. Use to drive traffic to owned channels.

- Reddit (r/alevel, r/6thForm, r/CambridgeInternational, r/Edexcel)
- TikTok (P2)
- Discord study servers

### Borrowed Channels
Tap into someone else's audience.

- Tutor referrals (tutors share with their students)
- Guest posts on education blogs
- YouTube study channels
- University widening participation pages (for backlinks)

**ExamPilot priority:** Owned (email + blog) is being built. Rented (Reddit) is the immediate pre-launch channel. Borrowed (tutor referrals) is the highest-leverage channel for first 100 students.

## Five-Phase Launch

### Phase 1: Internal (current)
- Test with 2-3 friendly students (Cambridge 9709 focus)
- Collect feedback on core loop: question > answer > feedback > SRS scheduling
- Fix major usability gaps before any public mention

### Phase 2: Alpha
- Landing page live at exampilot.io with early access signup
- Announce existence in 1-2 trusted communities
- Invite individual students to test (from Reddit engagement)

### Phase 3: Beta
- Work through early access list (free accounts)
- Start Reddit value posting with occasional ExamPilot mention
- Recruit tutors to have 2-3 students try it
- "Beta" badge in UI signals active development

### Phase 4: Early Access
- Share screenshots, demo GIFs, feature previews
- Run product-market fit survey after session 3 (Sean Ellis score)
- Throttle invites in batches (monitor server load + support capacity)

### Phase 5: Full Launch
- Open self-serve signups
- Start charging (EUR29/mo, EUR69/3mo, EUR96/6mo, EUR144/yr)
- Full campaign: blog post, Reddit, email to waitlist, tutor outreach blast
- Product Hunt submission (optional, tech-savvy audience overlaps)

## Pre-Launch Checklist

- [ ] Landing page live with early access form
- [ ] Welcome email sequence ready (5 emails over 14 days, P2)
- [ ] Reddit accounts have 50+ karma and 30+ day age
- [ ] 3-5 value posts published across target subs (no ExamPilot mention)
- [ ] Blog has 3-5 SEO articles published
- [ ] Tutor outreach templates ready (see marketing/templates/tutor-outreach.md)
- [ ] Student DM templates ready (see marketing/templates/outreach-dm.md)
- [ ] Analytics wired: PostHog for product events, GA4 for marketing

## Launch Day Checklist

- [ ] Blog announcement post published
- [ ] Email sent to waitlist/early access list
- [ ] Reddit posts in r/alevel and r/CambridgeInternational
- [ ] Tutor WhatsApp messages sent (warm intros only)
- [ ] In-app banner or notification for existing beta users
- [ ] Monitor signups, errors, and support requests all day
- [ ] Respond to every Reddit comment and DM within 2 hours

## Post-Launch (First 2 Weeks)

- [ ] Onboarding email sequence firing for new signups
- [ ] Follow up with every early user who hasn't completed first session
- [ ] Publish "what's new" post for beta users
- [ ] Run PMF survey after user completes 3rd session
- [ ] Start weekly pulse ritual (/weekly-pulse)

## Ongoing Launch Strategy

Every feature update is a mini-launch opportunity.

| Update size | Marketing effort |
|---|---|
| Major (new exam board, new feature) | Full campaign: blog + email + Reddit + tutors |
| Medium (new topic coverage, UI improvement) | Targeted: email to relevant segment + Reddit post |
| Minor (bug fix, small tweak) | Changelog only. Signals active development. |

## Timing for ExamPilot

- **May/Jun 2026 exam window:** Too close for full launch. Target 15-25 students via direct outreach.
- **August 2026 Results Day:** Key trigger. Resit cohort (Oct/Nov) needs ExamPilot NOW. Content and outreach templates must be ready before this date.
- **Sep-Nov 2026 resit period:** Active acquisition window. Full launch if product is ready.
- **Jan-Mar 2027:** Mock season. Organic growth should be compounding by now.

Source: Adapted from coreyhaines31/marketingskills launch skill + ExamPilot wiki go-to-market.md
