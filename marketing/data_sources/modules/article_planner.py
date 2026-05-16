"""
Article Planner

Generates a section-by-section content plan for a blog article before writing begins.
Used by the /article command's Step 3.

Given a keyword, intent, word count target, and content gaps, produces a full
structural plan: H1 options, intro, key takeaways, H2 sections, FAQ plan, and conclusion.
"""

import argparse
import json
import math
from typing import Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

VALID_INTENTS = {
    "informational",
    "exam_prep",
    "commercial_investigation",
    "navigational",
    "how_to",
}

OUTCOME_WORDS = ["pass", "improve", "master", "understand", "practise", "score", "ace", "revise"]

INTENT_SECTION_TEMPLATES: dict[str, list[dict]] = {
    "exam_prep": [
        {"h2_template": "What Is {topic}? (Curriculum Overview)", "format": "explanation"},
        {"h2_template": "How {topic} Is Tested in {exam_code}", "format": "explanation"},
        {"h2_template": "Worked Examples: {topic} Step by Step", "format": "worked_example"},
        {"h2_template": "Common Mistakes to Avoid", "format": "explanation"},
        {"h2_template": "Practice Questions with Mark Scheme Logic", "format": "worked_example"},
    ],
    "informational": [
        {"h2_template": "What Is {topic}?", "format": "explanation"},
        {"h2_template": "Key Concepts You Need to Know", "format": "explanation"},
        {"h2_template": "Step-by-Step: {topic} in Practice", "format": "step_by_step"},
        {"h2_template": "Real Examples and How to Apply Them", "format": "worked_example"},
        {"h2_template": "Frequently Made Errors", "format": "explanation"},
    ],
    "commercial_investigation": [
        {"h2_template": "What to Look for in a {topic} Tool", "format": "comparison"},
        {"h2_template": "How ExamPilot Approaches {topic}", "format": "explanation"},
        {"h2_template": "{topic}: Free vs Paid Options Compared", "format": "comparison"},
        {"h2_template": "What Students Say", "format": "explanation"},
        {"h2_template": "Getting Started: Your Next Step", "format": "step_by_step"},
    ],
    "how_to": [
        {"h2_template": "What You Need Before You Start", "format": "explanation"},
        {"h2_template": "Step 1: {topic} — The Basics", "format": "step_by_step"},
        {"h2_template": "Step 2: Working Through Examples", "format": "worked_example"},
        {"h2_template": "Step 3: Checking Your Work", "format": "step_by_step"},
        {"h2_template": "Common Questions Answered", "format": "explanation"},
    ],
    "navigational": [
        {"h2_template": "Overview: {topic}", "format": "explanation"},
        {"h2_template": "Key Features and What They Cover", "format": "comparison"},
        {"h2_template": "How to Use {topic} Effectively", "format": "step_by_step"},
        {"h2_template": "What Students Get from {topic}", "format": "explanation"},
    ],
}

FAQ_TEMPLATES: dict[str, list[str]] = {
    "exam_prep": [
        "What does {topic} mean in A Level Maths?",
        "How do you solve {topic} questions in the exam?",
        "What are the most common {topic} mistakes at A Level?",
        "Is {topic} in Cambridge 9709 Paper 1 or Paper 3?",
        "How many marks is {topic} worth in the A Level exam?",
        "How do you revise {topic} effectively for A Level?",
    ],
    "informational": [
        "What is {topic} in simple terms?",
        "How is {topic} used in real life?",
        "What is the formula for {topic}?",
        "How do you know when to use {topic}?",
        "What level of maths do you need for {topic}?",
    ],
    "commercial_investigation": [
        "Is ExamPilot free to use?",
        "How does ExamPilot help with {topic}?",
        "What exam boards does ExamPilot support?",
        "How is ExamPilot different from other revision tools?",
        "Can I try ExamPilot before paying?",
    ],
    "how_to": [
        "How do you do {topic} step by step?",
        "What is the easiest way to learn {topic}?",
        "How long does it take to understand {topic}?",
        "What mistakes do students make with {topic}?",
        "Do you need to memorise formulas for {topic}?",
    ],
    "navigational": [
        "What topics does ExamPilot cover?",
        "How does ExamPilot's practice system work?",
        "What exam boards does ExamPilot support?",
        "Is ExamPilot suitable for Cambridge A Level?",
        "How often should I use ExamPilot to revise?",
    ],
}

INTERNAL_LINK_OPPORTUNITIES = [
    "/blog/a-level-maths-revision-tips",
    "/cambridge/9709/paper-1",
    "/cambridge/9709/paper-3",
    "/pricing",
    "/features",
    "/blog/how-to-use-mark-schemes",
    "/cambridge/9709/statistics",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _extract_topic(keyword: str) -> str:
    """Extract the core topic from a keyword, stripping exam codes and noise words."""
    noise = ["cambridge", "9709", "a level", "a-level", "alevel", "edexcel", "wma11",
             "revision", "notes", "guide", "how to", "what is", "maths", "math"]
    topic = keyword.lower()
    for n in noise:
        topic = topic.replace(n, "")
    topic = " ".join(topic.split()).strip()
    return topic or keyword


def _extract_exam_code(keyword: str) -> str:
    """Extract exam paper code from keyword if present."""
    import re
    match = re.search(r'\b(9709|wma\d+|wst\d+|9MA\d+)[/\d]*\b', keyword, re.IGNORECASE)
    return match.group(0).upper() if match else "Cambridge A Level"


def _build_h1_options(keyword: str, topic: str, intent: str) -> list[str]:
    """Generate 3 H1 variations using benefit, specificity, and question formulas."""
    exam_code = _extract_exam_code(keyword)
    topic_cap = topic.title()

    benefit = f"How to Master {topic_cap} — {exam_code} Complete Guide"
    specific = f"{exam_code} {topic_cap}: Worked Examples and Mark Scheme Logic"
    question = f"What Is {topic_cap} and How Is It Tested in {exam_code}?"

    if intent == "commercial_investigation":
        benefit = f"How ExamPilot Helps You Practise {topic_cap} for {exam_code}"
        specific = f"{topic_cap} Revision Tools: What Actually Works for {exam_code}"
        question = f"What Is the Best Way to Practise {topic_cap} Before Your {exam_code} Exam?"
    elif intent == "how_to":
        benefit = f"How to Do {topic_cap}: Step-by-Step for {exam_code} Students"
        specific = f"{topic_cap} in {exam_code}: Complete Worked Guide"
        question = f"How Do You Solve {topic_cap} in {exam_code}?"

    return [benefit, specific, question]


def _distribute_words(word_count_target: int, num_sections: int) -> list[int]:
    """Distribute word count across H2 sections. Intro fixed at 175, conclusion at 150."""
    intro_words = 175
    conclusion_words = 150
    faq_words = 250  # Approximate allocation for FAQ
    body_words = word_count_target - intro_words - conclusion_words - faq_words
    per_section = max(200, body_words // num_sections)

    # Adjust last section to absorb rounding
    allocations = [per_section] * num_sections
    total_allocated = sum(allocations) + intro_words + conclusion_words + faq_words
    allocations[-1] += word_count_target - total_allocated
    allocations[-1] = max(200, allocations[-1])
    return allocations


def _build_sections(keyword: str, intent: str, content_gaps: list[str], word_count_target: int) -> list[dict]:
    """Build section plan from intent template, incorporating content gaps."""
    topic = _extract_topic(keyword)
    exam_code = _extract_exam_code(keyword)
    templates = INTENT_SECTION_TEMPLATES.get(intent, INTENT_SECTION_TEMPLATES["informational"])

    sections = []
    for i, tmpl in enumerate(templates):
        h2 = tmpl["h2_template"].format(topic=topic.title(), exam_code=exam_code)
        gap = content_gaps[i] if i < len(content_gaps) else f"General coverage of {topic}"
        link_opp = INTERNAL_LINK_OPPORTUNITIES[i % len(INTERNAL_LINK_OPPORTUNITIES)]
        sections.append({
            "h2": h2,
            "content_gap_addressed": gap,
            "format": tmpl["format"],
            "target_words": 0,  # filled below
            "internal_link_opportunity": link_opp,
        })

    # Add extra sections if more gaps than templates
    for i in range(len(templates), len(content_gaps)):
        sections.append({
            "h2": f"More on {content_gaps[i][:50]}",
            "content_gap_addressed": content_gaps[i],
            "format": "explanation",
            "target_words": 0,
            "internal_link_opportunity": INTERNAL_LINK_OPPORTUNITIES[i % len(INTERNAL_LINK_OPPORTUNITIES)],
        })

    word_allocations = _distribute_words(word_count_target, len(sections))
    for section, words in zip(sections, word_allocations):
        section["target_words"] = words

    return sections


def _build_faq(keyword: str, intent: str) -> list[dict]:
    """Generate FAQ Q&A stubs from intent templates."""
    topic = _extract_topic(keyword)
    templates = FAQ_TEMPLATES.get(intent, FAQ_TEMPLATES["informational"])

    faq = []
    for q_tmpl in templates[:5]:
        question = q_tmpl.format(topic=topic)
        faq.append({
            "question": question,
            "answer_placeholder": f"[Write 2-3 sentence answer addressing '{question}' directly. Include specific examples where possible. Add [VERIFY] to any statistics.]",
        })
    return faq


# ---------------------------------------------------------------------------
# Core function
# ---------------------------------------------------------------------------

def plan_article(
    keyword: str,
    intent: str,
    word_count_target: int,
    content_gaps: list[str],
) -> dict:
    """Generate a structured section-by-section plan for an article."""
    if intent not in VALID_INTENTS:
        intent = "informational"

    word_count_target = max(1800, min(5000, word_count_target))
    topic = _extract_topic(keyword)

    h1_options = _build_h1_options(keyword, topic, intent)
    sections = _build_sections(keyword, intent, content_gaps, word_count_target)
    faq = _build_faq(keyword, intent)

    total = 175 + sum(s["target_words"] for s in sections) + 150 + 250

    return {
        "keyword": keyword,
        "intent": intent,
        "h1_options": h1_options,
        "intro": {
            "target_words": 175,
            "structure": (
                "Sentence 1-2: Direct answer — state what {topic} is or how to do it. "
                "Sentence 3-5: Why this matters for their exam (paper, mark weighting, frequency). "
                "Final sentence: Preview of what this article covers."
            ).format(topic=topic),
        },
        "key_takeaways": [
            f"{topic.title()} is a core {intent.replace('_', ' ')} concept in this exam unit.",
            "The most common errors involve [specific mistake — fill during writing].",
            "The mark scheme rewards [approach — fill from past papers].",
            "ExamPilot provides structured practice questions and instant feedback for this topic.",
            "Use this guide alongside past paper practice for best results.",
        ],
        "sections": sections,
        "faq": faq,
        "conclusion": {
            "target_words": 150,
            "structure": (
                "Summarise each Key Takeaway in one sentence. "
                "Transition: 'The best way to consolidate {topic} is through practice.' "
                "CTA: 'Try ExamPilot's adaptive {topic} questions — [Start Practising Free](/pricing).'"
            ).format(topic=topic),
        },
        "total_target_words": total,
    }


# ---------------------------------------------------------------------------
# Markdown output
# ---------------------------------------------------------------------------

def format_plan_as_markdown(plan: dict) -> str:
    """Render an article plan dict as formatted markdown."""
    lines = []
    lines.append(f"# Article Plan: `{plan['keyword']}`")
    lines.append(f"\n**Intent:** {plan['intent']}  |  **Target words:** {plan['total_target_words']}\n")

    lines.append("## H1 Options\n")
    for i, h1 in enumerate(plan["h1_options"], 1):
        lines.append(f"{i}. {h1}")

    lines.append("\n## Intro Structure\n")
    lines.append(f"Target: {plan['intro']['target_words']} words\n")
    lines.append(plan["intro"]["structure"])

    lines.append("\n## Key Takeaways\n")
    for kt in plan["key_takeaways"]:
        lines.append(f"- {kt}")

    lines.append("\n## Sections\n")
    for i, sec in enumerate(plan["sections"], 1):
        lines.append(f"### {i}. {sec['h2']}")
        lines.append(f"- **Format:** {sec['format']}")
        lines.append(f"- **Addresses gap:** {sec['content_gap_addressed']}")
        lines.append(f"- **Target words:** {sec['target_words']}")
        lines.append(f"- **Internal link:** {sec['internal_link_opportunity']}\n")

    lines.append("## FAQ Plan\n")
    for qa in plan["faq"]:
        lines.append(f"**Q: {qa['question']}**")
        lines.append(f"A: {qa['answer_placeholder']}\n")

    lines.append("## Conclusion Structure\n")
    lines.append(f"Target: {plan['conclusion']['target_words']} words\n")
    lines.append(plan["conclusion"]["structure"])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a section-by-section article plan")
    parser.add_argument("--keyword", required=True, help="Primary keyword (e.g. 'integration by parts 9709')")
    parser.add_argument(
        "--intent",
        default="exam_prep",
        choices=list(VALID_INTENTS),
        help="Search intent (default: exam_prep)",
    )
    parser.add_argument("--words", type=int, default=2400, help="Word count target (default: 2400)")
    parser.add_argument(
        "--gaps",
        nargs="*",
        default=[],
        help="Content gaps to address (space-separated quoted strings)",
    )
    parser.add_argument("--json", action="store_true", dest="json_out", help="Output raw JSON instead of markdown")
    args = parser.parse_args()

    plan = plan_article(
        keyword=args.keyword,
        intent=args.intent,
        word_count_target=args.words,
        content_gaps=args.gaps,
    )

    if args.json_out:
        print(json.dumps(plan, indent=2))
    else:
        print(format_plan_as_markdown(plan))
