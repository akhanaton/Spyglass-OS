---
type: x-post
channel: x
author: ""
audience: founder
post-type: ""
source: ""
status: draft
date: YYYY-MM-DD
---

## Post Types

**milestone:** "Just hit X" / "Shipped X" -- one specific number or achievement.

**decision:** "Today we decided X because Y" -- extracted from `decisions/log.md`.

**failure:** "We tried X. It didn't work. Here's why." -- transparency post.

**tip:** Educational content for the builder audience (not students).

**question:** Genuine question to the community to spark replies. Replies are 13.5x more valuable than likes.

**reply-prompt:** Designed to generate conversation -- "What's your X?" / "Unpopular opinion: Y"

## Rules

- Single tweet, max 280 characters. Shorter is better.
- No links in standalone tweets (X algorithm deprioritises them). Put links in a self-reply.
- No hashtags except #buildinpublic (once, at end, sparingly -- not in every post).
- No em dashes. No banned phrases.
- Include `[ATTACH: description]` placeholder if a screenshot or GIF would help.
- Must contain at least one specific detail: a number, a name, a date, or a concrete outcome.
- Author voice: match `references/voice-{author}.md`, NOT voice-house.md.

## Output

Save to: `build-in-public/pipelines/outreach/x-post-{author}-{slug}-YYYY-MM-DD.md`
