# Reddit Value Post Template

A value-first post for target subreddits. The goal is to be genuinely helpful. ExamPilot mention is optional and must never be the point of the post.

## Frontmatter

```yaml
---
type: reddit-value-post
subreddit: ""       # r/alevel | r/6thForm | r/CambridgeInternational | r/Edexcel
target_segment: ""  # cambridge-9709 | edexcel-ial | resit
funnel_stage: tofu
topic: ""
status: draft
date: YYYY-MM-DD
---
```

## Structure

### Title

- Specific to the sub's audience (16-18 year olds)
- Describes the value clearly (not clickbait)
- Examples: "How I went from D to A in 9709 Pure 1 in 8 weeks", "The 4 topics that come up every single year in WMA11"

### Body

**Hook (1-2 sentences)**
Start with a relatable student pain point or observation. No preamble.

**Value section (bulk of the post)**
The actual helpful content. This is the whole point. Be specific:
- Name exact topics, paper codes, mark scheme patterns
- Give actionable steps, not vague advice
- Reference real past paper questions where possible
- [VERIFY] any exam board claims

**Soft mention (optional, last paragraph only)**
Only include if ExamPilot is directly relevant to what was discussed. Never force it.

If including:
- Describe what it does, don't just name-drop
- No link. Let them search for it
- Frame as "I've been using..." or "there's a tool that does..."
- Never in first interaction with a community

If not including: end with the value. That's fine. Building karma is the goal.

## Rules

Read channel-playbooks.md Reddit section before posting.

- Value first, always. Answer before anything else.
- Casual register. Peer-to-peer. Not teacher-to-student.
- No marketing language ("revolutionary", "game-changing", "AI-powered")
- No link drops
- Don't cross-post the same content to multiple subs
- Check sub rules before posting
- Account needs 50+ karma and 30+ days age
- Post during peak hours: evenings GMT (4pm-9pm UK), weekends

## File Output

Save to: `marketing/pipelines/outreach/reddit-[subreddit]-[topic-slug]-YYYY-MM-DD.md`
