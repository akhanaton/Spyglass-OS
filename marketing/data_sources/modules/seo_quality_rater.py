"""
SEO Quality Rater

Rates content quality against SEO best practices for ExamPilot blog articles.
Provides scoring (0-100) and specific recommendations for improvement.

Target: A-Level Maths students (international). Cambridge 9709, Edexcel IAL.
"""

import re
from typing import Dict, List, Optional, Any


class SEOQualityRater:

    def __init__(self, guidelines: Optional[Dict[str, Any]] = None):
        self.guidelines = guidelines or self._default_guidelines()

    def _default_guidelines(self) -> Dict[str, Any]:
        return {
            'min_word_count': 1800,
            'optimal_word_count': 2200,
            'max_word_count': 3000,
            'primary_keyword_density_min': 1.0,
            'primary_keyword_density_max': 2.0,
            'secondary_keyword_density': 0.5,
            'min_internal_links': 3,
            'optimal_internal_links': 5,
            'min_external_links': 2,
            'optimal_external_links': 3,
            'meta_title_length_min': 50,
            'meta_title_length_max': 60,
            'meta_description_length_min': 150,
            'meta_description_length_max': 160,
            'min_h2_sections': 4,
            'optimal_h2_sections': 6,
            'h2_with_keyword_ratio': 0.33,
            'max_sentence_length': 20,
            'target_reading_level_min': 8,
            'target_reading_level_max': 10,
            'paragraph_sentence_min': 2,
            'paragraph_sentence_max': 4,
        }

    def rate(
        self,
        content: str,
        meta_title: Optional[str] = None,
        meta_description: Optional[str] = None,
        primary_keyword: Optional[str] = None,
        secondary_keywords: Optional[List[str]] = None,
        keyword_density: Optional[float] = None,
        internal_link_count: Optional[int] = None,
        external_link_count: Optional[int] = None
    ) -> Dict[str, Any]:
        structure = self._analyze_structure(content, primary_keyword)

        content_score = self._score_content(content, structure)
        keyword_score = self._score_keyword_optimization(
            content, structure, primary_keyword, secondary_keywords, keyword_density
        )
        meta_score = self._score_meta_elements(meta_title, meta_description, primary_keyword)
        structure_score = self._score_structure(structure)
        link_score = self._score_links(content, internal_link_count, external_link_count)
        readability_score = self._score_readability(content, structure)

        weights = {
            'content': 0.20,
            'keywords': 0.25,
            'meta': 0.15,
            'structure': 0.15,
            'links': 0.15,
            'readability': 0.10
        }

        overall_score = (
            content_score['score'] * weights['content'] +
            keyword_score['score'] * weights['keywords'] +
            meta_score['score'] * weights['meta'] +
            structure_score['score'] * weights['structure'] +
            link_score['score'] * weights['links'] +
            readability_score['score'] * weights['readability']
        )

        critical_issues = []
        warnings = []
        suggestions = []

        for category in [content_score, keyword_score, meta_score, structure_score, link_score, readability_score]:
            critical_issues.extend(category.get('critical', []))
            warnings.extend(category.get('warnings', []))
            suggestions.extend(category.get('suggestions', []))

        return {
            'overall_score': round(overall_score, 1),
            'grade': self._get_grade(overall_score),
            'category_scores': {
                'content': content_score['score'],
                'keyword_optimization': keyword_score['score'],
                'meta_elements': meta_score['score'],
                'structure': structure_score['score'],
                'links': link_score['score'],
                'readability': readability_score['score']
            },
            'critical_issues': critical_issues,
            'warnings': warnings,
            'suggestions': suggestions,
            'publishing_ready': overall_score >= 80 and len(critical_issues) == 0,
            'details': {
                'word_count': structure['word_count'],
                'h2_count': structure['h2_count'],
                'has_h1': structure['has_h1'],
                'keyword_in_h1': structure.get('keyword_in_h1', False),
                'keyword_in_first_100': structure.get('keyword_in_first_100', False)
            }
        }

    def _analyze_structure(self, content: str, primary_keyword: Optional[str]) -> Dict[str, Any]:
        lines = content.split('\n')

        h1_count = 0
        h2_count = 0
        h3_count = 0
        h1_text = ""
        h2_texts = []

        for line in lines:
            h1_match = re.match(r'^#\s+(.+)$', line)
            h2_match = re.match(r'^##\s+(.+)$', line)
            h3_match = re.match(r'^###\s+(.+)$', line)

            if h1_match:
                h1_count += 1
                if not h1_text:
                    h1_text = h1_match.group(1)
            elif h2_match:
                h2_count += 1
                h2_texts.append(h2_match.group(1))
            elif h3_match:
                h3_count += 1

        word_count = len(content.split())
        paragraphs = [p for p in content.split('\n\n') if p.strip() and not p.strip().startswith('#')]
        avg_paragraph_length = sum(len(p.split()) for p in paragraphs) / len(paragraphs) if paragraphs else 0

        keyword_in_h1 = False
        keyword_in_first_100 = False
        h2_with_keyword = 0

        if primary_keyword:
            keyword_lower = primary_keyword.lower()
            keyword_in_h1 = keyword_lower in h1_text.lower()
            first_100_words = ' '.join(content.split()[:100]).lower()
            keyword_in_first_100 = keyword_lower in first_100_words
            h2_with_keyword = sum(1 for h2 in h2_texts if keyword_lower in h2.lower())

        return {
            'word_count': word_count,
            'has_h1': h1_count > 0,
            'h1_count': h1_count,
            'h1_text': h1_text,
            'h2_count': h2_count,
            'h2_texts': h2_texts,
            'h3_count': h3_count,
            'paragraph_count': len(paragraphs),
            'avg_paragraph_length': avg_paragraph_length,
            'keyword_in_h1': keyword_in_h1,
            'keyword_in_first_100': keyword_in_first_100,
            'h2_with_keyword': h2_with_keyword
        }

    def _score_content(self, content: str, structure: Dict) -> Dict[str, Any]:
        score = 100
        critical = []
        warnings = []
        suggestions = []

        word_count = structure['word_count']
        min_words = self.guidelines['min_word_count']
        optimal_words = self.guidelines['optimal_word_count']
        max_words = self.guidelines['max_word_count']

        if word_count < min_words:
            score -= 30
            critical.append(f"Content too short ({word_count} words). Minimum is {min_words} words.")
        elif word_count < optimal_words:
            score -= 10
            warnings.append(f"Content could be longer ({word_count} words). Target is {optimal_words}+ words.")
        elif word_count > max_words:
            score -= 5
            suggestions.append(f"Content is very long ({word_count} words). Consider splitting if over {max_words} words.")

        avg_para = structure['avg_paragraph_length']
        if avg_para > 100:
            score -= 10
            warnings.append(f"Paragraphs are too long (avg {avg_para:.0f} words). Use 2-4 sentence paragraphs.")
        elif avg_para < 20:
            score -= 5
            suggestions.append(f"Paragraphs are very short (avg {avg_para:.0f} words). Add more depth.")

        return {'score': max(0, score), 'critical': critical, 'warnings': warnings, 'suggestions': suggestions}

    def _score_keyword_optimization(
        self,
        content: str,
        structure: Dict,
        primary_keyword: Optional[str],
        secondary_keywords: Optional[List[str]],
        keyword_density: Optional[float]
    ) -> Dict[str, Any]:
        score = 100
        critical = []
        warnings = []
        suggestions = []

        if not primary_keyword:
            return {
                'score': 50,
                'critical': ['No primary keyword specified'],
                'warnings': [],
                'suggestions': []
            }

        if not structure['keyword_in_h1']:
            score -= 20
            critical.append(f"Primary keyword '{primary_keyword}' missing from H1 heading")

        if not structure['keyword_in_first_100']:
            score -= 15
            critical.append(f"Primary keyword '{primary_keyword}' missing from first 100 words")

        h2_count = structure['h2_count']
        h2_with_kw = structure['h2_with_keyword']
        if h2_count > 0:
            ratio = h2_with_kw / h2_count
            target_ratio = self.guidelines['h2_with_keyword_ratio']
            if ratio < target_ratio:
                score -= 10
                warnings.append(
                    f"Keyword in only {h2_with_kw}/{h2_count} H2s. Target at least 2 H2s with keyword."
                )

        if keyword_density is not None:
            min_density = self.guidelines['primary_keyword_density_min']
            max_density = self.guidelines['primary_keyword_density_max']

            if keyword_density < min_density:
                score -= 15
                warnings.append(
                    f"Keyword density too low ({keyword_density}%). Target {min_density}-{max_density}%."
                )
            elif keyword_density > max_density * 1.5:
                score -= 20
                critical.append(
                    f"Keyword stuffing risk ({keyword_density}%). Target {min_density}-{max_density}%."
                )
            elif keyword_density > max_density:
                score -= 10
                warnings.append(f"Keyword density slightly high ({keyword_density}%).")

        if secondary_keywords:
            content_lower = content.lower()
            missing = [kw for kw in secondary_keywords if kw.lower() not in content_lower]
            if missing:
                score -= 5
                suggestions.append(f"Secondary keywords not found: {', '.join(missing)}")

        return {'score': max(0, score), 'critical': critical, 'warnings': warnings, 'suggestions': suggestions}

    def _score_meta_elements(
        self,
        meta_title: Optional[str],
        meta_description: Optional[str],
        primary_keyword: Optional[str]
    ) -> Dict[str, Any]:
        score = 100
        critical = []
        warnings = []
        suggestions = []

        if not meta_title:
            score -= 40
            critical.append("Meta title is missing")
        else:
            title_len = len(meta_title)
            min_len = self.guidelines['meta_title_length_min']
            max_len = self.guidelines['meta_title_length_max']

            if title_len < min_len:
                score -= 15
                warnings.append(f"Meta title too short ({title_len} chars). Target {min_len}-{max_len}.")
            elif title_len > max_len + 10:
                score -= 10
                warnings.append(f"Meta title too long ({title_len} chars). Target {min_len}-{max_len}.")

            if primary_keyword and primary_keyword.lower() not in meta_title.lower():
                score -= 15
                warnings.append(f"Primary keyword '{primary_keyword}' not in meta title")

        if not meta_description:
            score -= 40
            critical.append("Meta description is missing")
        else:
            desc_len = len(meta_description)
            min_len = self.guidelines['meta_description_length_min']
            max_len = self.guidelines['meta_description_length_max']

            if desc_len < min_len:
                score -= 15
                warnings.append(f"Meta description too short ({desc_len} chars). Target {min_len}-{max_len}.")
            elif desc_len > max_len + 10:
                score -= 10
                warnings.append(f"Meta description too long ({desc_len} chars).")

            if primary_keyword and primary_keyword.lower() not in meta_description.lower():
                score -= 10
                suggestions.append(f"Primary keyword '{primary_keyword}' not in meta description")

        return {'score': max(0, score), 'critical': critical, 'warnings': warnings, 'suggestions': suggestions}

    def _score_structure(self, structure: Dict) -> Dict[str, Any]:
        score = 100
        critical = []
        warnings = []
        suggestions = []

        if not structure['has_h1']:
            score -= 30
            critical.append("Missing H1 heading")
        elif structure['h1_count'] > 1:
            score -= 20
            critical.append(f"Multiple H1 headings ({structure['h1_count']}). Should have exactly one.")

        h2_count = structure['h2_count']
        min_h2 = self.guidelines['min_h2_sections']
        optimal_h2 = self.guidelines['optimal_h2_sections']

        if h2_count < min_h2:
            score -= 15
            warnings.append(f"Too few H2 sections ({h2_count}). Add more structure (target: {optimal_h2}).")
        elif h2_count < optimal_h2:
            score -= 5
            suggestions.append(f"Could use more H2 sections ({h2_count}). Optimal is {optimal_h2}.")

        return {'score': max(0, score), 'critical': critical, 'warnings': warnings, 'suggestions': suggestions}

    def _score_links(self, content: str, internal_count: Optional[int], external_count: Optional[int]) -> Dict[str, Any]:
        score = 100
        critical = []
        warnings = []
        suggestions = []

        if internal_count is None:
            internal_count = len(re.findall(r'\[([^\]]+)\]\((?!http)', content))

        if external_count is None:
            external_count = len(re.findall(r'\[([^\]]+)\]\(https?://', content))

        min_internal = self.guidelines['min_internal_links']
        optimal_internal = self.guidelines['optimal_internal_links']

        if internal_count < min_internal:
            score -= 20
            warnings.append(
                f"Too few internal links ({internal_count}). Add {min_internal - internal_count} more (target: {optimal_internal})."
            )
        elif internal_count < optimal_internal:
            score -= 5
            suggestions.append(f"Could add more internal links ({internal_count}). Target is {optimal_internal}.")

        min_external = self.guidelines['min_external_links']
        if external_count < min_external:
            score -= 15
            warnings.append(
                f"Too few external links ({external_count}). Add authority links (Cambridge, Pearson, Ofqual, named research)."
            )

        return {'score': max(0, score), 'critical': critical, 'warnings': warnings, 'suggestions': suggestions}

    def _score_readability(self, content: str, structure: Dict) -> Dict[str, Any]:
        score = 100
        critical = []
        warnings = []
        suggestions = []

        sentences = re.split(r'[.!?]+', content)
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_lengths = [len(s.split()) for s in sentences]
        avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0

        max_sentence = self.guidelines['max_sentence_length']
        if avg_sentence_length > max_sentence:
            score -= 10
            warnings.append(
                f"Average sentence length is {avg_sentence_length:.1f} words. "
                f"Target under {max_sentence} words (students read on phones)."
            )

        long_sentences = [s for s in sentence_lengths if s > max_sentence * 1.5]
        if len(long_sentences) > len(sentences) * 0.2:
            score -= 10
            warnings.append(
                f"{len(long_sentences)} sentences exceed {max_sentence * 1.5:.0f} words. Break them up."
            )

        lists = len(re.findall(r'^\s*[-*+]\s', content, re.MULTILINE))
        if lists == 0:
            score -= 5
            suggestions.append("No lists found. Add bullet points or numbered lists for scannability.")

        return {'score': max(0, score), 'critical': critical, 'warnings': warnings, 'suggestions': suggestions}

    def _get_grade(self, score: float) -> str:
        if score >= 90:
            return "A (Excellent)"
        elif score >= 80:
            return "B (Good)"
        elif score >= 70:
            return "C (Average)"
        elif score >= 60:
            return "D (Needs Work)"
        return "F (Poor)"


def rate_seo_quality(
    content: str,
    meta_title: Optional[str] = None,
    meta_description: Optional[str] = None,
    primary_keyword: Optional[str] = None,
    secondary_keywords: Optional[List[str]] = None,
    keyword_density: Optional[float] = None,
    internal_link_count: Optional[int] = None,
    external_link_count: Optional[int] = None,
    custom_guidelines: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    rater = SEOQualityRater(custom_guidelines)
    return rater.rate(
        content, meta_title, meta_description, primary_keyword,
        secondary_keywords, keyword_density, internal_link_count, external_link_count
    )


if __name__ == "__main__":
    sample_content = """
# Cambridge 9709 Pure 1 Integration: Complete Guide

Cambridge 9709 Pure 1 integration is the reverse of differentiation.
This 9709 Pure 1 guide covers every technique you need for Paper 1.

## The Power Rule for Integration

Add one to the power, divide by the new power.

## The Reverse Chain Rule

Only works when the expression inside the brackets is linear.

## Definite Integrals

Evaluate between limits — no +C needed.

## Area Under a Curve

Set up the integral with limits from the intersection points.

## Common Mistakes on 9709 Paper 1

Integration carries 15-20 marks out of 75 on Paper 1.
    """

    result = rate_seo_quality(
        content=sample_content,
        meta_title="Cambridge 9709 Pure 1 Integration Guide | ExamPilot",
        meta_description="Master A Level Maths integration for Cambridge 9709 Pure 1. Power rule, reverse chain rule, definite integrals, and area under curves with worked examples.",
        primary_keyword="9709 Pure 1 integration",
        keyword_density=1.5,
        internal_link_count=3,
        external_link_count=2
    )

    print(f"Overall Score: {result['overall_score']}/100")
    print(f"Grade: {result['grade']}")

    if result['critical_issues']:
        print("\nCritical Issues:")
        for issue in result['critical_issues']:
            print(f"  - {issue}")
