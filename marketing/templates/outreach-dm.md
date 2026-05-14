# Outreach DM Template

A direct message to a prospective student. Personal, brief, single CTA. Under 80 words.

## Frontmatter

```yaml
---
type: outreach-dm
channel: ""         # whatsapp | discord | email
target_segment: ""  # cambridge-9709 | edexcel-ial | resit
funnel_stage: bofu
recipient: ""
personalization_notes: ""
status: draft
date: YYYY-MM-DD
---
```

## Structure

**Opening (1 sentence)**
Personal. Reference something specific: their post, their question, their exam board, their timeline. Never generic.

**Value prop (1-2 sentences)**
What ExamPilot does for them specifically. Not features. Outcome.
- For Cambridge 9709: "maps your weak topics across Pure 1 and builds a revision plan that adapts"
- For Edexcel IAL: "built specifically for WMA11 and WMA12, not generic maths"
- For resit: "identifies the exact gaps from your last sitting and targets them"

**CTA (1 sentence)**
Single, low-friction ask. Examples:
- "Want me to send you an invite?"
- "Happy to set you up with a free trial if you want to try it"
- "No pressure, just thought it might help with [specific thing they mentioned]"

**Sign-off**
First name only. Casual.

## Rules

- Under 80 words total
- Voice must match references/voice-enitan.md
- Never send to someone you haven't engaged with first (no cold DM-spam)
- WhatsApp: only via tutor group referral, not direct to students
- Discord: only in servers you've already contributed to
- Maximum 1 follow-up if no response
- No marketing language, no feature lists, no pricing in first message
- [VERIFY] any claims about what ExamPilot currently does vs. planned features

## Variants

**Post-helpful-comment follow-up:**
"Hey [name], saw your question about [topic] in r/[sub]. Hope the answer helped. I've been building something for exactly this - [one sentence]. Want to check it out?"

**Tutor-referred student:**
"Hey [name], [tutor name] mentioned you're sitting [paper code] in [month]. I built ExamPilot to help with exactly that - it finds your weak topics and builds a targeted plan. Want to try it for free?"

**Resit student (post-Results Day):**
"Hey [name], saw you're resitting [paper code] in Oct/Nov. ExamPilot can map what needs work based on where you are now and build a plan for the next [X] weeks. Want an invite?"

## File Output

Save to: `marketing/pipelines/outreach/dm-[channel]-[recipient-slug]-YYYY-MM-DD.md`
