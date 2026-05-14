# Reddit Comment Template

A reply to an existing thread. Answer the question first. ExamPilot mention only if directly relevant to the question being asked.

## Frontmatter

```yaml
---
type: reddit-comment
subreddit: ""       # r/alevel | r/6thForm | r/CambridgeInternational | r/Edexcel
target_segment: ""  # cambridge-9709 | edexcel-ial | resit
funnel_stage: mofu
thread_url: ""
thread_topic: ""
status: draft
date: YYYY-MM-DD
---
```

## Structure

**Answer (2-4 sentences)**
Directly answer the question. Be specific. Reference paper codes, topics, mark scheme patterns where relevant.

**Supporting detail (2-4 sentences)**
Expand with practical advice, a technique, or a resource. Add real value beyond the direct answer.

**ExamPilot mention (1 sentence, only if green light)**
Green light conditions:
- Thread asks "what tools/apps do you recommend?"
- Thread asks "how do I track my weak topics?"
- Thread asks about adaptive practice or spaced repetition
- Your answer naturally leads to what ExamPilot does

If green light: one sentence describing what it does (not a link, not a pitch).
If no green light: stop after the supporting detail. That's a complete, helpful comment.

## Rules

- Never start with "Great question!" or any generic opener
- No links unless specifically asked for resources
- Match the tone of the thread (casual, stressed, celebratory)
- [VERIFY] any exam board claims
- If the thread is asking about Edexcel, don't answer with Cambridge info (and vice versa)

## File Output

Save to: `marketing/pipelines/outreach/reddit-comment-[subreddit]-[topic-slug]-YYYY-MM-DD.md`
