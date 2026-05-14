---
name: write-reddit
description: Generate a value-first Reddit post or comment for a target subreddit. Reads audience segments, channel playbooks, and Reddit playbook for context.
---

## Input

$ARGUMENTS

Expect: subreddit name + topic or thread URL. Examples:
- "r/alevel common integration mistakes 9709"
- "r/CambridgeInternational how to revise pure 1 effectively"
- "comment on [thread URL] about past paper strategy"

If no subreddit given, ask. If no topic given, ask.

## Execution

### Step 1: Load context

Read these files:
- `marketing/context/audience-segments.md` — messaging angle for the target segment
- `marketing/context/channel-playbooks.md` — Reddit section for posting rules
- `marketing/references/reddit-playbook.md` — sub-specific norms, timing, what works
- `marketing/context/content-standards.md` — positioning rules, what NOT to say

Determine the target segment from the subreddit:
- r/alevel, r/6thForm → could be Cambridge 9709 or Edexcel IAL (check topic)
- r/CambridgeInternational → Cambridge 9709
- r/Edexcel → Edexcel IAL

### Step 2: Fetch wiki context (if needed)

If the topic requires factual grounding about ExamPilot's approach or exam board specifics:

```bash
gh api repos/akhanaton/spyglass-wiki/contents/wiki/marketing/seo/seo-strategy.md --jq '.content' | base64 -d
```

Adjust the wiki path based on what's needed. Never fabricate exam board facts.

### Step 3: Determine post type

- If input includes "comment" or a thread URL → use `marketing/templates/reddit-comment.md`
- Otherwise → use `marketing/templates/reddit-value-post.md`

### Step 4: Generate content

Write the post/comment following the selected template. Rules:
- Value first. Always.
- Match the register: casual, peer-to-peer, 16-18 year old audience
- Be specific: paper codes, topic names, mark scheme patterns
- [VERIFY] flag any exam board claim you're not 100% certain about
- No marketing language ("revolutionary", "game-changing", "AI-powered")
- ExamPilot mention only if directly relevant and natural (never in first community interaction)
- No links unless specifically relevant

### Step 5: Output

Save with YAML frontmatter to the appropriate pipeline location:
- Posts: `marketing/pipelines/outreach/reddit-[subreddit]-[topic-slug]-YYYY-MM-DD.md`
- Comments: `marketing/pipelines/outreach/reddit-comment-[subreddit]-[topic-slug]-YYYY-MM-DD.md`

### Step 6: Review prompt

Show the draft and ask:
- "Does this feel like something a real student/maths enthusiast would post?"
- "Any exam board facts to verify before posting?"
- "Should this mention ExamPilot, or is it better as a pure value post?"

Never auto-publish. Human review always.
