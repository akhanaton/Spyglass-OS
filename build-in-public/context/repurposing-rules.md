# X Repurposing Rules

How to extract build-in-public content from ExamPilot articles. For the full repurposing playbook (Reddit, email, TikTok), see `marketing/references/repurposing-playbook.md`.

## The Core Principle

Different audience (founders, not students). Extract the BUILD process, not the exam content.

"We just published our 10th article on Cambridge 9709 revision" (HOW we're building)
NOT "Here's how to revise for 9709 Paper 1" (WHAT the article says).

## X Formats from a Blog Article

| Format | Adaptation |
|---|---|
| Thread (5-7 tweets) | One point per tweet. Hook in tweet 1. Extract the build process, not exam content. |
| Standalone tweet | Single insight or milestone from the article's creation. 280 chars max. Screenshot if visual. |

## Rules

- Never cross-post Reddit content to X. The registers are incompatible.
- Builder audience is allergic to polish and marketing speak.
- Always extract the process insight, not the exam content.
- No links in main tweets (X algorithm deprioritises them). Links go in self-reply.
- Author voice: match `references/voice-{author}.md`, NOT voice-house.md.
- See `build-in-public/context/channel-rules.md` for full posting rules.
- See `build-in-public/references/x-strategy.md` for full strategy and content pillars.

## Good vs. Bad Examples

**Good (process insight):**
- "Just published our 10th article on Cambridge 9709 revision. The internal linking alone took 2 hours. Here's what we learned about topical authority."
- "Wrote 3,000 words on integration techniques today. The Python content scorer gave it a 72. Tweaking the structure until it hits 80."

**Bad (exam content):**
- "Here's how to revise for 9709 Paper 1" — student content, not builder content
- "Check out our latest article!" — marketing, not build-in-public

## Thread Flag

If the article's creation involved an interesting multi-step process, decision, or failure, flag it:

`[THREAD CANDIDATE] This article's creation story could make a good weekly thread. Run /write-x --type thread to expand.`

---

## LinkedIn Repurposing Rules

Same source material as X. Fundamentally different frame.

### The Angle Adaptation Rule

| Source | X frame | LinkedIn frame |
|---|---|---|
| decisions/log.md | "We decided X because Y" (peer founder) | "What choosing X taught me about how students learn" (educator insight) |
| Shipped feature | "Just shipped X. Took Y hours. Here's what broke." | "We added [feature] because students were doing this instead" |
| Blog article creation | "10th article. Python scorer gave it 72." | "Writing about integration techniques revealed something about how students approach unfamiliar problems" |
| PostHog metric | "1,000 sessions. Here's our top feature." | "Students spent 3x longer on worked examples than practice. Here's what that tells us." |

The X post is a confession. The LinkedIn post is an insight.

### LinkedIn Formats from a Blog Article

| Format | Adaptation |
|---|---|
| Text post (1,000-1,500 chars) | Extract one educational insight from the article. Frame as "what this topic reveals about how students learn." Not a summary. |
| Carousel (6-10 slides) | Structure the key points of the article as a visual guide. "The 5 things students get wrong about [topic]" — teachers will share this. |
| Native article (800-1,500 words) | Deep-dive on the teaching challenge the blog article addresses. Different angle — not the student how-to, but the educator's perspective on why students struggle. |

### Rules

- Never cross-post from X to LinkedIn. The registers are incompatible and the algorithm detects it.
- Never copy-paste blog article content directly. Adapt the angle — educator perspective, not SEO article.
- No links in LinkedIn post body. Put links in the first comment.
- Author voice: Teresa only (until Enitan joins with product/engineering angle).
- Always apply the angle adaptation rule before drafting. State it explicitly.
- See `build-in-public/context/channel-rules.md` for full LinkedIn posting rules.
- See `build-in-public/references/linkedin-strategy.md` for full strategy.

### LinkedIn Flag

If an article's topic reveals something about how students learn or fail that would be genuinely useful to a CIE maths teacher, flag it:

`[LINKEDIN CANDIDATE] This article's core insight could make a strong LinkedIn post for Teresa. Run /write-linkedin --source manual to expand the educator angle.`
