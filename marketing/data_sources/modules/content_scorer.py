"""
Content Scorer

Multi-dimensional content quality scoring system that evaluates:
- Humanity/Voice (30%): Human tone, personality, conversational devices
- Specificity (25%): Concrete examples vs vague generalizations
- Structure Balance (20%): Prose-to-list ratio (target 40-70%)
- SEO Compliance (15%): Keyword density, meta, structure
- Readability (10%): Flesch score, sentence rhythm, paragraph length

Target audience: 16-18 year old A-Level Maths students (international).
Target reading level: Grade 8-10, Flesch 60-70.

Composite score must be >= 70 to pass quality threshold.
"""

import re
import sys
from typing import Dict, List, Optional, Any
from pathlib import Path

try:
    from .readability_scorer import ReadabilityScorer
    from .seo_quality_rater import SEOQualityRater
except ImportError:
    from readability_scorer import ReadabilityScorer
    from seo_quality_rater import SEOQualityRater


class ContentScorer:

    WEIGHTS = {
        'humanity': 0.30,
        'specificity': 0.25,
        'structure_balance': 0.20,
        'seo': 0.15,
        'readability': 0.10
    }

    PASS_THRESHOLD = 70

    AI_PHRASES = [
        # Generic AI tells
        r'\bin today\'s (?:digital|modern|fast-paced)\b',
        r'\bwhen it comes to\b',
        r'\bit\'s (?:worth noting|important to note)\b',
        r'\blet\'s dive (?:in|into)\b',
        r'\bin the world of\b',
        r'\bfurthermore\b',
        r'\bmoreover\b',
        r'\badditionally\b',
        r'\bin order to\b',
        r'\bdue to the fact that\b',
        r'\bat the end of the day\b',
        r'\bgoing forward\b',
        r'\butilize\b',
        r'\bsynergy\b',
        r'\bholistic\b',
        r'\brobust\b',
        r'\bseamless(?:ly)?\b',
        r'\bparadigm\b',
        r'\bfacilitate\b',
        r'\bdelve (?:in|into)\b',
        r'\bnavigate\b',
        r'\btapestry\b',
        r'\bin conclusion,? it is clear\b',
        # ExamPilot-banned phrases (brand violation, not just AI tell)
        r'\bai.?tutor\b',
        r'\bai.?wrapper\b',
        r'\bai.?powered\b',
        r'\bai.?driven\b',
        r'\brevolutionary\b',
        r'\bgame.?changer\b',
        r'\bgame.?changing\b',
        r'\bunlock(?:ing)? (?:the )?(?:your )?potential\b',
    ]

    VAGUE_WORDS = [
        r'\bmany\b',
        r'\bsome\b',
        r'\bvarious\b',
        r'\bnumerous\b',
        r'\bseveral\b',
        r'\boften\b',
        r'\bsometimes\b',
        r'\busually\b',
        r'\bgenerally\b',
        r'\btypically\b',
        r'\bsignificant(?:ly)?\b',
        r'\bsubstantial(?:ly)?\b',
        r'\bconsiderable\b',
        r'\bvery\b',
        r'\breally\b',
        r'\bquite\b',
        r'\brather\b',
        r'\brelatively\b',
        r'\brecently\b',
        r'\bcurrently\b',
        r'\beffective(?:ly)?\b',
        r'\bimportant\b',
    ]

    SPECIFICITY_PATTERNS = [
        r'\b\d{1,3}%\b',
        r'\b\d{4}\b',
        r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}',
        r'(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+(?:said|says|explained|noted|mentioned)',
        r'\"[^\"]{10,}\"',
        # ExamPilot specifics: exam codes and paper references
        r'\b9709/\d{2}\b',
        r'\bWMA1[123]\b',
        r'\bWMA2[123]\b',
        r'\b(?:Pure|Statistics|Mechanics)\s+[12]\b',
        r'\b\d+\.\d+\.\d+\b',  # Syllabus topic numbers like 1.8.1
        r'\b\d+\s*(?:marks?|out of \d+)\b',
    ]

    CONVERSATIONAL_PATTERNS = [
        r'\([^)]{5,50}\)',
        r'\?(?:\s|$)',
        r'\bdon\'t\b',
        r'\bcan\'t\b',
        r'\bwon\'t\b',
        r'\byou\'re\b',
        r'\byou\'ve\b',
        r'\bit\'s\b',
        r'\bthat\'s\b',
        r'\bhere\'s\b',
        r'\blet\'s\b',
        r'\bI\'ve\b',
        r'\bI\'m\b',
        r'\bwe\'ve\b',
        r'\bwe\'re\b',
        r'(?:^|\.\s+)(?:Look|Here\'s the thing|The truth is|Sound familiar|Trust me)',
    ]

    def __init__(self):
        self.readability_scorer = ReadabilityScorer()
        self.seo_rater = SEOQualityRater()

    def score(self, content: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        metadata = metadata or {}

        clean_content = self._clean_for_analysis(content)

        humanity = self._score_humanity(clean_content)
        specificity = self._score_specificity(clean_content)
        structure = self._score_structure_balance(content)
        seo = self._score_seo(content, metadata)
        readability = self._score_readability(clean_content)

        composite = (
            humanity['score'] * self.WEIGHTS['humanity'] +
            specificity['score'] * self.WEIGHTS['specificity'] +
            structure['score'] * self.WEIGHTS['structure_balance'] +
            seo['score'] * self.WEIGHTS['seo'] +
            readability['score'] * self.WEIGHTS['readability']
        )
        composite = round(composite, 1)

        all_issues = []
        for dim_name, dim_data in [
            ('humanity', humanity),
            ('specificity', specificity),
            ('structure_balance', structure),
            ('seo', seo),
            ('readability', readability)
        ]:
            for issue in dim_data.get('issues', []):
                issue['dimension'] = dim_name
                issue['dimension_score'] = dim_data['score']
                all_issues.append(issue)

        for issue in all_issues:
            weight = self.WEIGHTS[issue['dimension']]
            deficit = 100 - issue['dimension_score']
            issue['impact'] = weight * deficit

        priority_fixes = sorted(all_issues, key=lambda x: -x['impact'])[:5]

        return {
            'composite_score': composite,
            'passed': composite >= self.PASS_THRESHOLD,
            'threshold': self.PASS_THRESHOLD,
            'dimensions': {
                'humanity': {
                    'score': humanity['score'],
                    'weight': self.WEIGHTS['humanity'],
                    'issues': humanity.get('issues', []),
                    'details': humanity.get('details', {})
                },
                'specificity': {
                    'score': specificity['score'],
                    'weight': self.WEIGHTS['specificity'],
                    'issues': specificity.get('issues', []),
                    'details': specificity.get('details', {})
                },
                'structure_balance': {
                    'score': structure['score'],
                    'weight': self.WEIGHTS['structure_balance'],
                    'prose_ratio': structure.get('prose_ratio', 0),
                    'issues': structure.get('issues', []),
                    'details': structure.get('details', {})
                },
                'seo': {
                    'score': seo['score'],
                    'weight': self.WEIGHTS['seo'],
                    'issues': seo.get('issues', []),
                    'details': seo.get('details', {})
                },
                'readability': {
                    'score': readability['score'],
                    'weight': self.WEIGHTS['readability'],
                    'flesch': readability.get('flesch', 0),
                    'issues': readability.get('issues', []),
                    'details': readability.get('details', {})
                }
            },
            'priority_fixes': priority_fixes
        }

    def _clean_for_analysis(self, content: str) -> str:
        text = content
        # Strip YAML frontmatter
        text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
        text = re.sub(r'^---+\s*$', '', text, flags=re.MULTILINE)
        text = re.sub(r'```[^`]*```', '', text)
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
        text = re.sub(r'\*([^*]+)\*', r'\1', text)
        text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
        return text.strip()

    def _score_humanity(self, content: str) -> Dict[str, Any]:
        issues = []
        details = {}

        content_lower = content.lower()
        word_count = len(content.split())

        ai_phrase_count = 0
        ai_phrases_found = []
        for pattern in self.AI_PHRASES:
            matches = re.findall(pattern, content_lower)
            ai_phrase_count += len(matches)
            if matches:
                ai_phrases_found.extend(matches[:2])

        ai_density = (ai_phrase_count / max(word_count, 1)) * 1000
        details['ai_phrases_per_1000'] = round(ai_density, 1)
        details['ai_phrases_found'] = ai_phrases_found[:5]

        conversational_count = 0
        for pattern in self.CONVERSATIONAL_PATTERNS:
            conversational_count += len(re.findall(pattern, content, re.IGNORECASE))

        conv_density = (conversational_count / max(word_count, 1)) * 1000
        details['conversational_per_1000'] = round(conv_density, 1)

        passive_indicators = len(re.findall(r'\b(?:is|are|was|were|been|being)\s+\w+ed\b', content_lower))
        passive_ratio = passive_indicators / max(word_count / 100, 1)
        details['passive_voice_ratio'] = round(passive_ratio, 2)

        contractions = len(re.findall(r"'(?:t|s|re|ve|ll|d|m)\b", content))
        contraction_density = (contractions / max(word_count, 1)) * 100
        details['contractions_per_100'] = round(contraction_density, 1)

        score = 100

        if ai_density > 5:
            penalty = min(30, (ai_density - 5) * 3)
            score -= penalty
            issues.append({
                'issue': f'AI/banned phrases detected ({ai_phrase_count} instances)',
                'fix': f'Remove or rephrase: {", ".join(ai_phrases_found[:3])}',
                'severity': 'high' if ai_density > 10 else 'medium'
            })

        if passive_ratio > 2:
            penalty = min(15, (passive_ratio - 2) * 5)
            score -= penalty
            issues.append({
                'issue': 'High passive voice usage',
                'fix': 'Convert passive sentences to active voice',
                'severity': 'medium'
            })

        if conv_density > 3:
            bonus = min(15, (conv_density - 3) * 2)
            score = min(100, score + bonus)

        if contraction_density < 1:
            score -= 10
            issues.append({
                'issue': 'Lacks contractions (sounds formal)',
                'fix': "Use contractions like don't, can't, you're, it's",
                'severity': 'low'
            })

        return {
            'score': max(0, min(100, round(score))),
            'issues': issues,
            'details': details
        }

    def _score_specificity(self, content: str) -> Dict[str, Any]:
        issues = []
        details = {}

        content_lower = content.lower()
        word_count = len(content.split())

        vague_count = 0
        vague_found = []
        for pattern in self.VAGUE_WORDS:
            matches = re.findall(pattern, content_lower)
            vague_count += len(matches)
            if matches and len(vague_found) < 5:
                vague_found.extend(matches[:2])

        vague_density = (vague_count / max(word_count, 1)) * 1000
        details['vague_words_per_1000'] = round(vague_density, 1)
        details['vague_words_found'] = list(set(vague_found))[:5]

        specific_count = 0
        for pattern in self.SPECIFICITY_PATTERNS:
            specific_count += len(re.findall(pattern, content))

        specific_density = (specific_count / max(word_count, 1)) * 1000
        details['specifics_per_1000'] = round(specific_density, 1)

        numbers = re.findall(r'\b\d+(?:,\d{3})*(?:\.\d+)?\b', content)
        number_density = (len(numbers) / max(word_count, 1)) * 1000
        details['numbers_per_1000'] = round(number_density, 1)

        score = 70

        if vague_density > 15:
            penalty = min(25, (vague_density - 15) * 1.5)
            score -= penalty
            issues.append({
                'issue': f'Too many vague words ({vague_count} instances)',
                'fix': f'Replace vague words with specifics: {", ".join(vague_found[:3])}',
                'severity': 'high' if vague_density > 25 else 'medium'
            })

        if specific_density > 2:
            bonus = min(30, specific_density * 5)
            score += bonus

        if number_density < 3:
            penalty = min(15, (3 - number_density) * 5)
            score -= penalty
            issues.append({
                'issue': 'Lacks specific numbers and data',
                'fix': 'Add exam mark allocations, percentages, paper codes (9709/12), or syllabus topic numbers',
                'severity': 'medium'
            })

        return {
            'score': max(0, min(100, round(score))),
            'issues': issues,
            'details': details
        }

    def _score_structure_balance(self, content: str) -> Dict[str, Any]:
        issues = []
        details = {}

        content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
        content = re.sub(r'^---+\s*$', '', content, flags=re.MULTILINE)

        lines = content.split('\n')

        list_chars = 0
        table_chars = 0
        header_chars = 0
        total_chars = 0

        for line in lines:
            line_stripped = line.strip()
            if not line_stripped:
                continue

            char_count = len(line_stripped)
            total_chars += char_count

            if re.match(r'^[-*+]\s', line_stripped) or re.match(r'^\d+\.\s', line_stripped):
                list_chars += char_count
            elif '|' in line_stripped:
                table_chars += char_count
            elif re.match(r'^#+\s', line_stripped):
                header_chars += char_count

        structured_chars = list_chars + table_chars
        prose_chars = total_chars - structured_chars - header_chars
        prose_ratio = prose_chars / max(total_chars - header_chars, 1)

        details['prose_ratio'] = round(prose_ratio, 2)
        details['list_ratio'] = round(list_chars / max(total_chars, 1), 2)
        details['table_ratio'] = round(table_chars / max(total_chars, 1), 2)

        # Target: 40-70% prose (content-quality agent uses same range)
        if 0.40 <= prose_ratio <= 0.70:
            score = 100
        elif prose_ratio < 0.40:
            deficit = 0.40 - prose_ratio
            score = max(0, 100 - (deficit * 150))
            issues.append({
                'issue': f'Too much structure ({round(prose_ratio * 100)}% prose, target 40-70%)',
                'fix': 'Convert some bullet lists to prose paragraphs',
                'severity': 'high' if prose_ratio < 0.25 else 'medium'
            })
        else:
            excess = prose_ratio - 0.70
            score = max(0, 100 - (excess * 100))
            issues.append({
                'issue': f'Too much prose ({round(prose_ratio * 100)}% prose, target 40-70%)',
                'fix': 'Add tables for comparisons, lists for steps, or worked examples',
                'severity': 'medium' if prose_ratio < 0.90 else 'high'
            })

        return {
            'score': round(score),
            'prose_ratio': round(prose_ratio, 2),
            'issues': issues,
            'details': details
        }

    def _score_seo(self, content: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
        issues = []
        details = {}

        meta_title = metadata.get('meta_title', '')
        meta_description = metadata.get('meta_description', '')
        primary_keyword = metadata.get('primary_keyword', '') or metadata.get('keyword', '')

        # Extract from YAML frontmatter if not passed directly
        if not meta_title:
            match = re.search(r'^meta_title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
            if match:
                meta_title = match.group(1).strip()

        if not meta_description:
            match = re.search(r'^meta_description:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
            if match:
                meta_description = match.group(1).strip()

        if not primary_keyword:
            match = re.search(r'^keyword:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
            if match:
                primary_keyword = match.group(1).strip()

        details['meta_title'] = meta_title
        details['meta_title_length'] = len(meta_title)
        details['meta_description_length'] = len(meta_description)
        details['primary_keyword'] = primary_keyword

        score = 100

        if not meta_title:
            score -= 15
            issues.append({
                'issue': 'Missing meta title',
                'fix': 'Add meta_title to YAML frontmatter (50-60 characters)',
                'severity': 'high'
            })
        elif len(meta_title) < 50:
            score -= 5
            issues.append({
                'issue': f'Meta title too short ({len(meta_title)} chars)',
                'fix': 'Expand meta title to 50-60 characters',
                'severity': 'low'
            })
        elif len(meta_title) > 60:
            score -= 5
            issues.append({
                'issue': f'Meta title too long ({len(meta_title)} chars)',
                'fix': 'Shorten meta title to 50-60 characters',
                'severity': 'low'
            })

        if not meta_description:
            score -= 15
            issues.append({
                'issue': 'Missing meta description',
                'fix': 'Add meta_description to YAML frontmatter (150-160 characters)',
                'severity': 'high'
            })
        elif len(meta_description) < 150:
            score -= 5
        elif len(meta_description) > 160:
            score -= 5

        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            h1 = h1_match.group(1).lower()
            details['h1'] = h1_match.group(1)
            if primary_keyword and primary_keyword.lower() not in h1:
                score -= 10
                issues.append({
                    'issue': 'Primary keyword not in H1',
                    'fix': f'Include "{primary_keyword}" in the H1 headline',
                    'severity': 'medium'
                })
        else:
            score -= 10
            issues.append({
                'issue': 'Missing H1 headline',
                'fix': 'Add an H1 headline with primary keyword',
                'severity': 'high'
            })

        clean_content = self._clean_for_analysis(content)
        first_100 = ' '.join(clean_content.split()[:100]).lower()
        if primary_keyword and primary_keyword.lower() not in first_100:
            score -= 10
            issues.append({
                'issue': 'Primary keyword not in first 100 words',
                'fix': f'Include "{primary_keyword}" in the introduction',
                'severity': 'medium'
            })

        word_count = len(clean_content.split())
        details['word_count'] = word_count
        if word_count < 1800:
            score -= 15
            issues.append({
                'issue': f'Content too short ({word_count} words)',
                'fix': 'Expand to at least 1,800 words (target 2,000-2,500)',
                'severity': 'high'
            })

        return {
            'score': max(0, min(100, round(score))),
            'issues': issues,
            'details': details
        }

    def _score_readability(self, content: str) -> Dict[str, Any]:
        issues = []
        details = {}

        try:
            analysis = self.readability_scorer.analyze(content)
            flesch = analysis.get('readability_metrics', {}).get('flesch_reading_ease', 50)
            grade = analysis.get('reading_level', 12)
        except Exception:
            flesch = 60
            grade = 10

        details['flesch_reading_ease'] = flesch
        details['grade_level'] = grade

        score = 100

        if flesch < 50:
            penalty = min(30, (50 - flesch) * 1.5)
            score -= penalty
            issues.append({
                'issue': f'Content too difficult for 16-18 yr olds (Flesch: {flesch})',
                'fix': 'Simplify sentences and use shorter words. Target Flesch 60-70.',
                'severity': 'high' if flesch < 40 else 'medium'
            })
        elif flesch < 60:
            score -= 10
            issues.append({
                'issue': f'Content slightly difficult (Flesch: {flesch})',
                'fix': 'Simplify some complex sentences. Target Flesch 60-70.',
                'severity': 'low'
            })
        elif flesch > 80:
            score -= 5

        if grade > 12:
            score -= 10
            issues.append({
                'issue': f'Reading level too high (Grade {grade}, target 8-10)',
                'fix': 'Shorten sentences and replace multi-syllable words',
                'severity': 'medium'
            })

        paragraph_issues = self._check_paragraph_length(content)
        details['long_paragraphs'] = paragraph_issues['count']
        details['longest_paragraph_sentences'] = paragraph_issues['longest']

        if paragraph_issues['count'] > 0:
            penalty = min(15, paragraph_issues['count'] * 3)
            score -= penalty
            issues.append({
                'issue': f'{paragraph_issues["count"]} paragraphs exceed 4 sentences (longest: {paragraph_issues["longest"]})',
                'fix': 'Break long paragraphs into 2-4 sentence chunks',
                'severity': 'medium' if paragraph_issues['count'] < 5 else 'high'
            })

        rhythm_issues = self._check_sentence_rhythm(content)
        details['rhythm_score'] = rhythm_issues['rhythm_score']
        details['monotonous_sections'] = rhythm_issues['monotonous_count']

        if rhythm_issues['rhythm_score'] < 60:
            penalty = min(10, (60 - rhythm_issues['rhythm_score']) / 4)
            score -= penalty
            issues.append({
                'issue': f'Monotonous sentence rhythm ({rhythm_issues["monotonous_count"]} uniform sections)',
                'fix': 'Vary sentence length: mix short punchy (5-10 words) with longer flowing (15-25 words)',
                'severity': 'medium' if rhythm_issues['rhythm_score'] > 40 else 'high'
            })

        return {
            'score': max(0, min(100, round(score))),
            'flesch': flesch,
            'issues': issues,
            'details': details
        }

    def _check_paragraph_length(self, content: str) -> Dict[str, Any]:
        paragraphs = re.split(r'\n\s*\n', content)
        long_paragraphs = 0
        longest = 0

        for para in paragraphs:
            para = para.strip()
            if not para or para.startswith('#') or para.startswith('-') or para.startswith('*') or para.startswith('|'):
                continue

            sentences = re.split(r'[.!?]+(?:\s|$)', para)
            sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 10]
            sentence_count = len(sentences)

            if sentence_count > 4:
                long_paragraphs += 1
                longest = max(longest, sentence_count)

        return {'count': long_paragraphs, 'longest': longest}

    def _check_sentence_rhythm(self, content: str) -> Dict[str, Any]:
        sentences = re.split(r'[.!?]+(?:\s|$)', content)
        sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 5]

        if len(sentences) < 10:
            return {'rhythm_score': 70, 'monotonous_count': 0}

        word_counts = [len(s.split()) for s in sentences]
        monotonous_sections = 0
        window_size = 5

        for i in range(len(word_counts) - window_size + 1):
            window = word_counts[i:i + window_size]
            avg = sum(window) / len(window)
            if all(abs(wc - avg) <= 5 for wc in window):
                monotonous_sections += 1

        mean = sum(word_counts) / len(word_counts)
        std_dev = (sum((wc - mean) ** 2 for wc in word_counts) / len(word_counts)) ** 0.5

        if std_dev < 5:
            rhythm_score = 40 + (std_dev * 6)
        elif std_dev <= 15:
            rhythm_score = 100 - abs(10 - std_dev) * 2
        else:
            rhythm_score = 80

        rhythm_score -= monotonous_sections * 3
        rhythm_score = max(0, min(100, rhythm_score))

        return {
            'rhythm_score': round(rhythm_score),
            'monotonous_count': monotonous_sections,
            'std_dev': round(std_dev, 1)
        }

    def format_report(self, result: Dict[str, Any]) -> str:
        lines = []
        lines.append("=" * 50)
        lines.append("CONTENT QUALITY SCORE — ExamPilot")
        lines.append("=" * 50)
        lines.append("")

        status = "PASSED" if result['passed'] else "BELOW THRESHOLD"
        lines.append(f"Composite Score: {result['composite_score']}/100 ({status})")
        lines.append(f"Threshold: {result['threshold']}")
        lines.append("")

        lines.append("Dimensions:")
        for dim_name, dim_data in result['dimensions'].items():
            score = dim_data['score']
            weight = dim_data['weight']
            check = "OK" if score >= 70 else "NEEDS WORK"
            extra = ""
            if dim_name == 'structure_balance':
                extra = f" ({round(dim_data.get('prose_ratio', 0) * 100)}% prose)"
            elif dim_name == 'readability':
                flesch = dim_data.get('flesch', 0)
                det = dim_data.get('details', {})
                extra = f" (Flesch: {flesch}, Rhythm: {det.get('rhythm_score', 'N/A')}, Long¶: {det.get('long_paragraphs', 0)})"

            lines.append(f"  {dim_name:20} {score:3}/100 (weight: {int(weight*100)}%) [{check}]{extra}")

        lines.append("")

        if result['priority_fixes']:
            lines.append("Priority Fixes:")
            for i, fix in enumerate(result['priority_fixes'][:5], 1):
                dim = fix.get('dimension', 'unknown')
                issue = fix.get('issue', 'Unknown issue')
                suggestion = fix.get('fix', 'No suggestion')
                lines.append(f"  {i}. [{dim}] {issue}")
                lines.append(f"     Fix: {suggestion}")

        lines.append("")
        lines.append("=" * 50)

        return "\n".join(lines)


def _parse_yaml_frontmatter(content: str) -> Dict[str, Any]:
    """Extract key/value pairs from YAML frontmatter block."""
    metadata = {}
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        return metadata

    for line in match.group(1).split('\n'):
        kv = re.match(r'^(\w[\w_-]*):\s*["\']?(.+?)["\']?\s*$', line)
        if kv:
            metadata[kv.group(1)] = kv.group(2)

    return metadata


def main():
    if len(sys.argv) < 2:
        print("Usage: python content_scorer.py <draft_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    metadata = _parse_yaml_frontmatter(content)

    scorer = ContentScorer()
    result = scorer.score(content, metadata)

    print(scorer.format_report(result))


if __name__ == '__main__':
    main()
