# Exam Season Intelligence Sprint — Track B

Implementation spec for a 4-week parallel execution track running alongside Phase 0 infrastructure (Track A). Starts June 2, 2026. Zero additional budget. 30 min/day per founder.

**Linear issue:** EP-77 (parent issue)
**Related issues:** EP-74 (examiner report — reprioritize), EP-60 (Facebook Groups — pull forward)

---

## Why This Exists

Phase 0's Linear issues are 100% acquisition infrastructure and 0% demand generation. Meanwhile, CIE May/June exam season is the highest-demand moment of the year. The marketing plan's Principle #1 ("demand generation first, acquisition second") is not being executed during Phase 0.

Every week of delay shrinks the compounding window before Results Day (Aug 15):
- Reddit requires 50+ karma and 30+ days account age for credibility
- Google needs 4-12 weeks to index new content
- Facebook Groups require 2-4 week observation before contributing
- Signal architecture produces zero data until engagement begins

Starting June 2 gives 74 days to Results Day. Starting mid-July gives 30 days. The difference is the difference between launching with validated intelligence and launching blind.

---

## What Track B Produces

1. **Data-validated content priority** — real engagement data tells you which topic spokes to publish first
2. **Calibrated signal weights** — PostHog geographic/behavioral data before the Results Day flood
3. **Reddit credibility** — 74 days of post history and karma by Results Day
4. **Persona validation** — real conversations reveal whether Omar/Aisha personas hold
5. **Geographic signal** — which Tier 1 country actually shows up (Pakistan at 34.5% like PapaCambridge, or different?)
6. **Build-in-public content** — authentic, data-driven X/LinkedIn material
7. **Facebook Group norms understood** — ready to contribute on Results Day, not still observing

---

## The Single Highest-Leverage Asset: Examiner Report Analysis (EP-74)

Currently Medium priority, due Jul 25. Should be **Urgent, due Jun 9** (one week from sprint start).

### Why first, not last

1. **Demonstrates ExamPilot's core value proposition.** "We tell you exactly where you're losing marks" — this article IS that thesis in content form. Topic spokes (quadratics, coordinate geometry) are educational content anyone could write.

2. **Maxes out every GEO/AI citation signal.** Princeton GEO study: statistics (+37%), cited sources (+40%), authoritative tone (+25%). Examiner report analysis uses Cambridge's OWN data with specific mark-loss statistics. Perfect AI-citable document.

3. **Not blocked by EP-53.** The article audit blocks topic spokes (EP-67-73) because new spokes must link to audited articles. The examiner report analysis is bridge content — stands alone, links to Cambridge's official reports.

4. **Perfect Reddit post during live exam season.** "I analyzed 5 years of Cambridge 9709 P1 examiner reports. These are the 5 topics where students consistently lose the most marks." Pure value. Gets indexed while the topic is hot.

5. **Becomes the Results Day anchor page.** On Aug 15, when students search "why did I fail 9709 Paper 1," this analysis is the EXACT page they need. Indexed for 10+ weeks by then.

6. **Feeds every channel.** One asset becomes: blog article (SEO), Reddit thread (community/AI seeding), X thread (build-in-public), LinkedIn post (Teresa: educator insight), WhatsApp seed post, Results Day email opener.

### How to produce it

1. Download Cambridge 9709 examiner reports (2019-2024) from Cambridge Assessment website
2. Claude analyzes for: topic-level mark-loss patterns, year-over-year trends, common examiner language, specific mark-loss percentages by topic
3. Run through `/write-article` with GEO-first structure
4. Publish on exampilot.io
5. Post to r/CambridgeInternational with UTM tracking
6. Repurpose: X thread, LinkedIn post, WhatsApp community seed

---

## Weekly Plan

### Week 1: Jun 2-8 — The Examiner Report

| Who | Action | Time |
|---|---|---|
| Enitan | Download 9709 examiner reports (2019-2024). Run analysis via Claude. Draft article via `/write-article`. | 2-3 hours total |
| Enitan | Publish article on exampilot.io. Post to r/CambridgeInternational with UTM tracking. | 1 hour |
| Enitan | X thread: "We studied 5 years of 9709 examiner reports. Here's what we found." | 30 min |
| Teresa | Join COALI Facebook Group + 1-2 CIE parent communities (EP-60, pulled forward). Observe mode. | 30 min |
| Teresa | LinkedIn post: educator angle on the examiner report data. | 30 min |

**Deliverable:** Examiner report analysis published and seeded across 4 channels. Facebook Group observation started.

### Week 2: Jun 9-15 — Seed and Listen

| Who | Action | Time |
|---|---|---|
| Enitan | 2-3 genuine Reddit contributions in r/CambridgeInternational. Answer real 9709 questions using examiner report data. Not promoting — helping. | 30 min/day |
| Enitan | Monitor PostHog: anonymous traffic from Reddit UTMs. Log geographic distribution, article engagement, top pages. | 15 min/day |
| Teresa | Continue Facebook Group observation. Note: What do parents ask about? What language do they use? Do they ask about revision tools or school admissions? | 15 min/day |
| Teresa | WhatsApp: explore 2-3 existing CIE student study groups (don't create ExamPilot community yet — listen first). | 15 min/day |

**Deliverable:** Reddit engagement baseline established. Facebook Group norms documented. First PostHog geographic data.

### Week 3: Jun 16-22 — Deepen and Validate

| Who | Action | Time |
|---|---|---|
| Enitan | Continue Reddit contributions (now with established post history). Track which topics get most engagement. | 30 min/day |
| Enitan | Log all signals manually in Coda Signals table (Reddit engagement, traffic sources, geographic data). | 15 min |
| Teresa | Facebook Group: first value-add contribution if norms are clear and observation period is sufficient. | 15 min/day |
| Both | Persona validation check: does Omar's shame-coded behavior appear in real conversations? Does Aisha's "I don't know what I don't know" show up? Do parents match the Sarah/Fatima persona? | 30 min session |

**Deliverable:** Validated persona insights. Content priority data (which 9709 topics drive most engagement).

### Week 4: Jun 23-29 — Extract and Calibrate

| Who | Action | Time |
|---|---|---|
| Enitan | Compile 4-week data: Reddit engagement by topic, PostHog geographic distribution, Coda Signals summary. | 1 hour |
| Enitan | Feed findings into content priority: reorder EP-68-70 (topic spokes) based on engagement data, not assumptions. | 30 min |
| Enitan | Set initial signal weight adjustments based on proxy data. | 30 min |
| Teresa | Write Facebook Group observation summary: parent language patterns, concerns, trust signals. Feed into EP-65 ("For Parents" page) brief. | 30 min |
| Both | Results Day messaging split decision: based on persona validation, confirm or revise the two-track approach (Omar resit vs. new Year 12 students). | 30 min session |

**Deliverable:** Data-informed content priority order. Calibrated signal weights. Persona validation report. Results Day messaging split confirmed.

---

## The Results Day Messaging Split (Bonus Insight)

The customer personas doc states: "Resit and first-time sitter messaging is MUTUALLY EXCLUSIVE."

On August 15, Results Day creates two simultaneous audiences:
- **Omar (resit):** "I failed. What do I do now?" High urgency, shame-coded, buys himself. Precision/failure framing.
- **Year 12 students starting A-Levels in September:** "I'm about to start 9709." Low urgency, planning mode, parent co-buys. Certainty/readiness framing.

EP-66 (Results Day content) should produce **two sets of staged content**, not one:

| Track | Audience | Emotional register | Channel emphasis | CTA |
|---|---|---|---|---|
| Resit Track | Omar (failed, resitting Oct/Nov) | Precision, no shame, "close the gap" | Reddit, direct search, email | Direct trial signup |
| New Starter Track | Year 12 beginning A-Levels | Certainty, readiness, "start strong" | Facebook Groups (parents), WhatsApp, school/teacher | Parent co-purchase via "For Parents" page |

The examiner report analysis serves BOTH tracks (it's factual, not emotional). But Reddit posts, email sequences, and landing page CTAs need separate versions.

Sprint Week 4 persona validation data informs which emotional register actually resonates before committing the messaging.

---

## Interaction with Existing Phase 0 Issues

| Issue | Current state | Suggested change |
|---|---|---|
| EP-74 (examiner report) | Medium, due Jul 25 | **Urgent, due Jun 9** — first content published, not last |
| EP-60 (Facebook Groups) | High, due Jun 21 | **Pull forward to Jun 2** — observation period starts immediately |
| EP-66 (Results Day content) | Urgent, due Jul 20 | **Split into two messaging tracks** (add note to issue) |
| EP-53 (article audit) | Urgent, due Jun 28 | Unchanged — Track B content (examiner report) is not blocked by this |
| EP-52 (Brevo) | Urgent, due Jun 21 | Unchanged — Track A infrastructure continues as planned |

No other Phase 0 issues change. Track B runs in parallel, not instead of.

---

## Success Criteria (measured at end of Week 4)

- [ ] Examiner report analysis published and indexed in GSC
- [ ] Reddit: 10+ genuine contributions, 50+ karma earned
- [ ] PostHog: geographic distribution data from 3+ weeks of traffic
- [ ] Facebook Group: norms documented, parent language patterns captured
- [ ] Persona validation: written summary confirming or revising Omar/Aisha/Sarah personas
- [ ] Content priority: EP-68-70 reordered based on engagement data
- [ ] Signal architecture: initial weight adjustments logged in Coda Signals table
- [ ] Results Day messaging: two-track split confirmed with supporting data

---

## What NOT To Do

- Do not promote ExamPilot on Reddit during the sprint. Value only. The product mention comes in Phase 1.
- Do not create the WhatsApp community yet (EP-61). Listen to existing groups first.
- Do not skip Track A infrastructure work. Both tracks run in parallel.
- Do not publish topic spokes before EP-53 (article audit). Only the examiner report analysis bypasses the audit dependency.
