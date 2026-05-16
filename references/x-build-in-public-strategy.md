# Build in Public on X -- Strategy Reference

ExamPilot's build-in-public strategy for X (Twitter). Enitan and Teresa post from personal accounts. This file covers the WHY and WHAT. For operational rules (HOW), see `marketing/context/channel-playbooks.md` (X section).

## Why we build in public

X serves a fundamentally different audience than the student micro-funnel. Students are on TikTok, Reddit, and SEO. X targets founders, indie hackers, edtech builders, and potential advisors.

Build-in-public:
- Builds founder credibility that makes everything else easier (press, partnerships, tutor referrals from the edtech community)
- Creates a launch-day audience that amplifies student-facing channels
- Generates word-of-mouth among people who tell other people about ExamPilot
- Opens doors to advisors, investors (if ever needed), and collaborators

It does NOT directly convert students. This distinction must stay sharp to prevent scope creep.

## Audience

Founders, indie hackers, solo developers, edtech builders. Age 25-45. Building their own products.

They care about: authentic progress, real numbers, decisions with reasoning, failures and what was learned. They are allergic to polish and marketing speak.

They do NOT care about: A-Level Maths tips, exam board specifics, or student-facing content. When repurposing blog articles for X, extract the BUILD process, not the exam content.

## Content pillars (with target ratios)

**These ratios are initial estimates.** Adjust based on engagement data after 30 days via `/tune`. See `references/continuous-improvement.md`.

| Pillar | % (initial estimate) | Examples |
|---|---|---|
| Progress and milestones | 40% | "Shipped X", "Just hit Y sessions", "Published our 10th article" |
| Decisions and reasoning | 25% | "Today we decided X because Y" -- sourced from `decisions/log.md` |
| Failures and learnings | 20% | "We tried X. It didn't work. Here's why." |
| Questions and engagement | 15% | Genuine asks to the community to spark replies |

The decisions log is the richest content source. Most entries are tweetable with minimal adaptation.

## Posting cadence

**First 60 days (building habits):**
- 1-2 original tweets/day + 2-3 quality replies to other accounts
- 1 weekly thread (highest-performing format on X)
- 70% replies, 30% original content
- The reply ratio matters because a reply is worth 13.5x a like on X's algorithm

**After 500 followers:**
- Shift to 50% replies, 50% original
- Increase thread frequency if weekly threads are performing
- Begin cross-channel repurposing (blog articles > X threads via `/repurpose`)

**Best posting times (initial, test and adjust):**
- 8-9 AM GMT (US East Coast morning)
- 5-6 PM GMT (UK evening, US afternoon overlap)

## Content differentiation between founders

Enitan and Teresa do NOT tweet the same things.

| Enitan | Teresa |
|---|---|
| Engineering decisions | Marketing experiments |
| Product architecture | Content strategy |
| Data and metrics | Community building |
| Technical build-in-public | Educational insights |
| Spyglass OS itself | What's working in student engagement |

Both share: milestone celebrations, failures/learnings (each from their own perspective).

## Anti-AI rules for X

The X audience is hypersensitive to AI-generated content. Getting caught destroys credibility permanently.

1. Never publish raw AI output. Treat `/write-x` output as a draft generator, not a publisher.
2. Every draft goes through the voice file for the author (`references/voice-{name}.md`).
3. Add personal context, specific stories, and exact numbers in the edit pass. AI can't add what you actually experienced.
4. Banned phrases: no em dashes, no "game-changer", no "revolutionary", no "let's dive in", no "comprehensive", no "robust", no "cutting-edge", no "seamless", no "I'm excited to share".
5. The test: "Would I type this on my phone at 11pm?" If no, rewrite.
6. Shorter is always better. 200 characters beats 280.

## Content sources from the OS

| Source | Type | Frequency |
|---|---|---|
| `decisions/log.md` | Decisions with reasoning | After any new decision |
| Linear issues (via MCP) | Shipped features, in-progress work | When something ships |
| PostHog metrics (via MCP) | Session counts, signups, feature adoption | Weekly milestones |
| Git commits (product repo) | Lines shipped, areas of focus | Weekly recap |
| Wiki articles | Synthesized knowledge, architecture | Occasional deep-dive threads |
| `/signal-review` output | Signal architecture insights | When interesting patterns emerge |
| Marketing experiments | What worked, what didn't | After any experiment concludes |
| Tool evaluations | "We tried X, here's what we found" | When evaluating new tools |

## Reply strategy

Replies are 13.5x more valuable than likes on X's algorithm. A retweet is 20x. Replies also build relationships.

- Find 5-10 accounts in #buildinpublic, edtech, or SaaS indie hacker space
- Consistently engage with genuine, substantive replies (not "great post!")
- Quality over volume. One thoughtful reply beats ten "nice!" comments.
- Turn on notifications for 5-10 established builders
- Engage within the first hour of their posts (algorithm favours early engagement)

## Analytics

- **Postiz dashboard:** impressions, engagement rate, follower growth per post
- **UTM tracking:** all links shared on X use `?utm_source=x&utm_medium=social&utm_campaign=bip` -- tracked in PostHog
- **Primary metric:** engagement rate (engagements / impressions). Target: 3-6% for small accounts.
- **Reviewed in:** `/weekly-pulse` (Step 6.5, added for X)

## Timeline

This is a slow burn, not a hockey stick.

- Months 1-2: 100-500 followers. Building habits. Finding your voice.
- Months 3-4: 500-2,000 followers. Content starts compounding. Replies generate inbound.
- Months 5-8: 2,000-5,000+ followers. Launch-ready audience.
- Typical SaaS conversion from engaged X audience: 15-25% at launch.

## Account setup checklist

Before first post, both founders should have:
- [ ] Professional headshot (not a logo)
- [ ] Bio: "Building @exampilot" + personal angle (parent, engineer, educator)
- [ ] Pinned thread: the ExamPilot story (why we're building this, what we've learned so far)
- [ ] Header image: product screenshot or the team
- [ ] Location set (builds trust with international audience)

## Scheduling

All scheduling via Postiz (Standard plan, $29/mo). This is the same plan used for TikTok (Phase 2). Incremental cost of X: $0. Postiz absorbs X API costs via OAuth.

Phase 0: Copy approved drafts to Postiz dashboard manually.
Phase 1 (after n8n wired): n8n pushes approved drafts to Postiz API.
Phase 2 (3+ months): Evaluate Postiz MCP integration if copy-paste friction is real.
