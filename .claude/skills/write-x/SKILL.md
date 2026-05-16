---
name: write-x
description: Draft a tweet or thread for X (build in public). Pulls from OS data sources (decisions log, Linear, PostHog, git) or accepts freeform input. Drafts in the author's personal voice with anti-AI scrub. Human review gate before publishing. Trigger on "write a tweet", "draft a thread", "write-x", or any request to create X/Twitter content for build-in-public. One run = one draft saved to build-in-public/pipelines/outreach/.
bike-method-phase: 1
three-ms-attribution: |
  Adapted from The Three Ms of AI(TM) (c) 2026 Nate Herk. All rights reserved.
  The Three Ms of AI(TM) is a trademark of Nate Herk.
---

> *Adapted from The Three Ms of AI(TM) (c) 2026 Nate Herk. All rights reserved.*

## What this skill does

Drafts X (Twitter) content for ExamPilot's build-in-public presence. Generates standalone tweets or threads from OS data sources or freeform ideas, in the author's personal voice. Every draft goes through a human review gate before posting.

**Bike Method Phase 1:** Every draft requires human review. No auto-publishing. Copy approved drafts to Postiz dashboard manually.

**Audience:** Founders, indie hackers, edtech builders. NOT students. This channel builds founder credibility and generates word-of-mouth among people who amplify student-facing channels.

## Flags

- `--author enitan|teresa` -- defaults to reading `context/.whoami`
- `--source decisions|linear|posthog|git|manual` -- defaults to `manual` (freeform input)
- `--type thread|post` -- defaults to `post`

If called with no flags and freeform text, treat as: `--source manual --type post --author [from .whoami]`

Examples:
```
/write-x "We tried X and it didn't work"
/write-x --source decisions
/write-x --type thread --source linear EP-47
/write-x --source posthog --author enitan
/write-x --type thread "our first week building in public"
```

## Context files -- read before drafting

```bash
# 1. Author's personal voice (NOT voice-house.md)
cat references/voice-{author}.md

# 2. Author's role and priorities
cat context/{author}.md

# 3. X channel rules
cat build-in-public/context/channel-rules.md

# 4. Content standards and banned phrases
cat marketing/context/content-standards.md

# 5. Build-in-public strategy (for content pillars and anti-AI rules)
cat build-in-public/references/x-strategy.md
```

Do not skip the voice file. The draft must sound like the author typed it on their phone.

## Execution -- seven steps

### Step 1 -- Determine source and extract content

Based on the `--source` flag:

**`decisions` (scan decisions/log.md):**
Read `decisions/log.md`. Show the 3 most recent entries. Ask the author which one to tweet about, or auto-select if one is clearly more tweetable (contrarian, has specific numbers, or tells a story).

Extract: the decision, the reasoning (why), and one alternative that was rejected.

**`linear EP-XX` (fetch a Linear issue):**
Use Linear MCP to fetch the specified issue. Extract: title, description summary, what was built, why it matters, current status.

**`posthog` (pull metrics):**
Use PostHog MCP to query key product metrics: total sessions, signups, feature adoption, retention. Pick the most interesting metric (biggest change, milestone crossed, or surprising finding).

Extract: the metric, the number, the trend, and one sentence of interpretation.

**`git` (recent commits):**
```bash
git -C $SPYGLASS_PRODUCT_REPO log --oneline -10 --since="7 days ago"
```
If `$SPYGLASS_PRODUCT_REPO` is not set, ask for the product repo path.

Extract: what was shipped, how many commits/lines, and one sentence of what it means.

**`manual` (freeform input / default):**
Take the user's input directly. Expand the raw idea into a properly formatted draft.

### Step 2 -- Determine format

If `--type` was specified, use it. Otherwise:

- Default to `post` (standalone tweet)
- Upgrade to `thread` if: the content has 3+ distinct points, tells a multi-step story, or the user's input is longer than 2 sentences

### Step 3 -- Generate draft

**For standalone tweets (`post`):**

Load `build-in-public/templates/x-post.md`. Generate a single tweet, max 280 characters.

Rules:
- Determine post-type: milestone, decision, failure, tip, question, or reply-prompt
- No links in the main tweet (X algorithm deprioritises them). If a link is needed, note: "[Link goes in self-reply]"
- No hashtags except #buildinpublic (once, at end, sparingly -- not in every post)
- Include a `[ATTACH: description]` placeholder if a screenshot or GIF would strengthen the post
- Must contain at least one specific detail: a number, a name, a date, or a concrete outcome

**For threads (`thread`):**

Load `build-in-public/templates/x-thread.md`. Generate 5-7 tweets.

Rules:
- Tweet 1 (hook): the single most compelling insight, number, or decision. Must stop scrolling. No hashtags.
- Tweets 2-5 (body): one point per tweet. Each must read standalone. Specific details -- numbers, screenshots, decisions, what failed.
- Final tweet (close): takeaway + soft CTA ("follow for more" or "building this at @exampilot"). Never "check out our product."
- Include `[ATTACH: description]` placeholders where screenshots/GIFs would help
- Every thread must contain at least one specific number

### Step 4 -- Scrub pass

Check the draft against these rules:
- No em dashes (replace with commas, periods, or colons)
- No banned phrases: "game-changer", "revolutionary", "let's dive in", "in today's world", "without further ado", "it's worth noting", "at the end of the day", "leverage" (as a verb in marketing context), "deep dive"
- No AI tells: "I'm excited to", "I'm thrilled to", "comprehensive", "robust", "cutting-edge", "seamless"
- Each tweet is under 280 characters
- Thread tweets are numbered (1/N format)
- Voice matches the author's voice file (check sentence length, formality level, opening patterns)

If any rule is violated, fix it before showing the draft.

### Step 5 -- Content differentiation check

Based on the author:
- **Enitan:** engineering decisions, product architecture, data/metrics, technical build-in-public, Spyglass OS itself
- **Teresa:** marketing experiments, content strategy, community building, educational insights

If the content doesn't match the author's natural domain, flag it: "This topic might be more natural coming from [other author]. Want to switch, or keep it?"

### Step 6 -- Human review

Show the draft inline. Then ask:

1. "Does this sound like {author} wrote it on their phone?"
2. "Any specific numbers, details, or personal context to add?"
3. "Screenshot or GIF to attach?" (if no `[ATTACH:]` placeholder exists)

Wait for edits. Apply any changes the author requests.

### Step 7 -- Save

Save the approved draft to:
- Posts: `build-in-public/pipelines/outreach/x-post-{author}-{slug}-YYYY-MM-DD.md`
- Threads: `build-in-public/pipelines/outreach/x-thread-{author}-{slug}-YYYY-MM-DD.md`

Apply YAML frontmatter from the appropriate template.

Remind: "Draft saved. Copy to Postiz to schedule. No auto-publish."
