---
name: outreach-draft
description: Draft a personalized outreach message for a student or tutor. Supports WhatsApp, Discord, email, and LinkedIn channels.
---

## Input

$ARGUMENTS

Expect: target type + channel + personalization details. Examples:
- "student dm discord, they asked about 9709 integration in r/alevel"
- "tutor email, found on LinkedIn, teaches Cambridge 9709 in Dubai, ~15 students"
- "resit student whatsapp, referred by tutor Sarah, sitting 9709 in November"

If target type (student/tutor) is missing, ask. If channel is missing, ask.

## Execution

### Step 1: Load context

Read these files:
- `marketing/context/audience-segments.md` — messaging angle for the target segment
- `marketing/context/channel-playbooks.md` — channel-specific rules (especially WhatsApp frequency limits, Discord norms)
- `marketing/context/content-standards.md` — positioning rules
- `references/voice-enitan.md` — personal voice for outreach (from OS root)
- `marketing/references/outreach-benchmarks.md` — personalization system, follow-up sequences, subject line data

### Step 2: Determine template

- Student (any channel) → `marketing/templates/outreach-dm.md`
- Tutor (any channel) → `marketing/templates/tutor-outreach.md`

### Step 3: Determine segment

From the input details:
- Cambridge 9709 student → cambridge-9709
- Edexcel IAL student → edexcel-ial
- Resit student → resit
- Tutor → tutor

### Step 4: Generate message

Follow the selected template. Rules:
- Student DMs: under 80 words. Personal. Single CTA.
- Tutor outreach: lead with their value. Low-commitment first ask.
- Voice matches references/voice-enitan.md
- [VERIFY] any claims about current ExamPilot features vs. planned
- No marketing language, no feature lists, no pricing in first message
- WhatsApp: only via warm intro or tutor referral (never cold to students)
- Discord: only in servers we've already contributed to

### Step 5: Output

Save with YAML frontmatter to:
- Student DMs: `marketing/pipelines/outreach/dm-[channel]-[recipient-slug]-YYYY-MM-DD.md`
- Tutor messages: `marketing/pipelines/outreach/tutor-[recipient-slug]-YYYY-MM-DD.md`

### Step 6: Review prompt

Show the draft and ask:
- "Is this personalized enough, or does it feel templated?"
- "Any claims to verify about what ExamPilot currently does?"
- "Ready to send, or want to adjust the tone?"

Never auto-send. Human review always.
