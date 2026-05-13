# AIS-OS Intake — Enitan

This is Enitan's source-of-truth file. Fill it in by typing, voice-pasting (Wispr Flow / OS dictation), or running `/onboard` for a guided conversation. When filled, run `/onboard` and the wizard will scaffold your Day-1 file set.

**Hard cap: 7 questions.** Each answerable in under 60 seconds. Don't overthink — you can edit and re-run `/onboard` any time.

---

## Q1 — Who are you, what do you sell, who do you sell it to?

Identity, offer, ICP. One paragraph each is fine.

```
Who are you?

ExamPilot (built by Spyglass) is an AI-powered exam readiness platform grounded in learning science — specifically spaced repetition (FSRS) and active recall. It was founded by parents who experienced first-hand the gap in high-quality, syllabus-aligned revision materials for international UK exams. The core philosophy is that preparation shouldn't be random practice; it should be diagnostic, adaptive, and driven by evidence of what you actually know and don't know. The product is currently in closed alpha.

What do you sell?

You sell exam confidence — operationalized as a measurable, data-backed prediction of a student's grade and a personalized path to improve it. The mechanism is a closed loop: assess knowledge gaps using "Question DNA" and a PRISM diagnostic architecture, diagnose underlying misconceptions (not just wrong answers), close gaps through adaptive Socratic practice, reinforce retention via FSRS-scheduled spaced repetition, and predict exam performance through an Exam Readiness Index (ERI). The pitch isn't "more practice" — it's purposeful practice: no wasted effort, every session targeted to your specific gaps.

Who do you sell it to?

Students sitting Cambridge (CIE) and Edexcel International exams at GCSE and A-Level — with an initial focus on Maths. The current beachhead is international students in markets where quality syllabus-aligned revision material is especially scarce (think students outside the UK sitting Cambridge papers who can't walk into a WH Smith and grab a CGP book). The buyer is often the parent; the user is the student. The emotional trigger is exam-calendar anxiety: students 8–12 weeks out from a high-stakes sitting who know they have gaps but don't know where to start.
```

---

## Q2 — Paste 1-2 things you've written recently. Don't edit them.

An email, a LinkedIn post, a DM, a doc — anything that sounds like you when you're not trying. **Paste verbatim.** Do not type these mid-conversation with Claude — chat-shaped samples are worse than no samples (voice contamination).

```
Sample 1 — Email (personal, Apr 21)

Enitan Williams <akhanaton@gmail.com>
Tue, Apr 21, 10:56 AM
to Angela

Hello Angela,

How are you and your family doing? Teresa and I will be in Mojacar from May 4th to May 7th and we were hoping to get your help with our padron then if that works for you? We will of course bring the letter from Dad as you mentioned.

Un abrazo,

Enitan
```

```
Sample 2 — Email (vendor, Apr 5)

Enitan Williams <akhanaton@gmail.com>
Sun, Apr 5, 4:44 PM
to Digitek

Hello Tamara

Thank you for the quote. I assume this includes servicing the other 3 units?

Regards,

Enitan
```

```
Sample 3 — Email (school, formal)

Dear Mr. Short,

I would like to meet with you regarding Tayo at your earliest convenience please. Can you please let me know when it is convenient for you? I would appreciate your discretion in this matter, Tayo is not aware of this and I would like to keep it that way until our discussion.

Kind regards,

Enitan Williams
```

---

## Q3 — What are your 2-3 biggest priorities for the next 90 days?

Quarterly priorities. Not yearly aspirations. Things that, if not done by July, would make you say "I wasted Q2."

```
1. Launch ExamPilot beta by completing the production readiness matrix
2. Complete setup and start using Spyglass OS (in progress)
3. Work with Teresa to plan and implement SEO and Growth strategies including relevant KPIs, goals, strategy, and milestones
```

---

## Q4 — Where does revenue actually land, and where is it tracked?

Multiple answers OK. Stripe? Skool? GoHighLevel? QuickBooks? A spreadsheet?

```
Pre-revenue until ~end of August 2026. Payment processor will be Dodo Payments (not Stripe). Until then, success is measured by traffic, waitlist sign-ups, and newsletter sign-ups. Tracking location TBD.
```

---

## Q5 — Where do you talk to customers, your team, and the outside world day-to-day?

Email (which one — Gmail / Outlook)? Slack? Teams? DMs (Skool / Discord / iMessage)? Phone?

```
Customers: Reddit, TikTok (planned), email (Gmail), Loom
Internal (Enitan & Teresa): Coda, Discord
```

---

## Q6 — Where do meeting recordings, notes, and important docs live?

Granola? Otter? Fireflies? Google Drive? Notion? Dropbox? A folder on your desktop you keep meaning to organize?

```
Google Workspace (Drive/Docs), Coda, second brain (external GitHub context repo)
```

---

## Q7 — What's the one task that eats your week, and where do you currently track work?

The single biggest time-suck or recurring drudgery. Plus where tasks/projects live (ClickUp / Asana / Linear / Notion / a notebook).

```
Tasks live in Coda. Top time-suck to be reviewed later — revisit at first /level-up session.
```

---

When this file is filled, run `/onboard` (or re-run it) and the wizard will scaffold your Day-1 file set: `context/enitan.md`, `references/voice-enitan.md`, populated `connections.md`, and a filled `CLAUDE.md`.
