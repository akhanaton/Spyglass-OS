"""
Readability Scorer

Calculates multiple readability metrics including Flesch Reading Ease,
Flesch-Kincaid Grade Level, and other readability indicators.

Target audience: 16-18 year old A-Level Maths students (international).
Target reading level: Grade 8-10, Flesch 60-70.
"""

import re
from typing import Dict, List, Any

try:
    import textstat
    TEXTSTAT_AVAILABLE = True
except ImportError:
    TEXTSTAT_AVAILABLE = False


class ReadabilityScorer:

    def __init__(self):
        self.target_reading_level = (8, 10)
        self.target_flesch_ease = (60, 70)
        self.max_avg_sentence_length = 20
        self.max_paragraph_sentences = 4

    def analyze(self, content: str) -> Dict[str, Any]:
        clean_text = self._clean_content(content)

        if not clean_text:
            return {'error': 'No readable content provided'}

        metrics = self._calculate_metrics(clean_text)
        structure = self._analyze_structure(content, clean_text)
        complexity = self._analyze_complexity(clean_text)
        overall_score = self._calculate_overall_score(metrics, structure, complexity)
        grade = self._get_grade(overall_score)
        recommendations = self._generate_recommendations(metrics, structure, complexity)

        return {
            'overall_score': overall_score,
            'grade': grade,
            'reading_level': metrics.get('flesch_kincaid_grade', 0),
            'readability_metrics': metrics,
            'structure_analysis': structure,
            'complexity_analysis': complexity,
            'recommendations': recommendations,
            'status': self._get_status(metrics, structure)
        }

    def _clean_content(self, content: str) -> str:
        text = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        text = re.sub(r'```[^`]*```', '', text)
        text = re.sub(r'\n\s*\n', '\n\n', text)
        return text.strip()

    def _calculate_metrics(self, text: str) -> Dict[str, Any]:
        if not TEXTSTAT_AVAILABLE:
            # Fallback: estimate from sentence/word stats
            words = text.split()
            sentences = re.split(r'[.!?]+', text)
            sentences = [s.strip() for s in sentences if s.strip()]
            avg_sentence_len = len(words) / max(len(sentences), 1)
            # Approximate Flesch: higher avg_sentence_len = lower score
            approx_flesch = max(0, 100 - avg_sentence_len * 2)
            return {
                'flesch_reading_ease': round(approx_flesch, 1),
                'flesch_kincaid_grade': round(avg_sentence_len / 2, 1),
                'sentence_count': len(sentences),
                'lexicon_count': len(words),
                '_note': 'textstat not installed — approximate values only'
            }

        try:
            return {
                'flesch_reading_ease': round(textstat.flesch_reading_ease(text), 1),
                'flesch_kincaid_grade': round(textstat.flesch_kincaid_grade(text), 1),
                'gunning_fog': round(textstat.gunning_fog(text), 1),
                'smog_index': round(textstat.smog_index(text), 1),
                'coleman_liau_index': round(textstat.coleman_liau_index(text), 1),
                'automated_readability_index': round(textstat.automated_readability_index(text), 1),
                'syllable_count': textstat.syllable_count(text),
                'lexicon_count': textstat.lexicon_count(text),
                'sentence_count': textstat.sentence_count(text),
                'char_count': len(text),
                'letter_count': textstat.letter_count(text),
                'polysyllable_count': textstat.polysyllabcount(text)
            }
        except Exception as e:
            return {'error': f'Metrics calculation failed: {e}', 'flesch_reading_ease': 0, 'flesch_kincaid_grade': 0}

    def _analyze_structure(self, original: str, clean_text: str) -> Dict[str, Any]:
        sentences = re.split(r'[.!?]+', clean_text)
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_lengths = [len(s.split()) for s in sentences]
        avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0

        paragraphs = [p for p in original.split('\n\n') if p.strip() and not p.strip().startswith('#')]
        paragraph_sentence_counts = []
        for para in paragraphs:
            para_sentences = re.split(r'[.!?]+', para)
            para_sentences = [s.strip() for s in para_sentences if s.strip()]
            if para_sentences:
                paragraph_sentence_counts.append(len(para_sentences))

        avg_sentences_per_paragraph = (
            sum(paragraph_sentence_counts) / len(paragraph_sentence_counts)
            if paragraph_sentence_counts else 0
        )

        words = clean_text.split()
        word_lengths = [len(word) for word in words]
        avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0

        return {
            'total_sentences': len(sentences),
            'avg_sentence_length': round(avg_sentence_length, 1),
            'shortest_sentence': min(sentence_lengths) if sentence_lengths else 0,
            'longest_sentence': max(sentence_lengths) if sentence_lengths else 0,
            'sentence_length_variance': round(self._variance(sentence_lengths), 1) if len(sentence_lengths) > 1 else 0,
            'total_paragraphs': len(paragraphs),
            'avg_sentences_per_paragraph': round(avg_sentences_per_paragraph, 1),
            'total_words': len(words),
            'avg_word_length': round(avg_word_length, 1),
            'long_sentences': len([s for s in sentence_lengths if s > 25]),
            'very_long_sentences': len([s for s in sentence_lengths if s > 35])
        }

    def _analyze_complexity(self, text: str) -> Dict[str, Any]:
        transition_words = [
            'however', 'moreover', 'therefore', 'consequently', 'additionally',
            'meanwhile', 'nevertheless', 'thus', 'hence', 'accordingly',
            'subsequently', 'for example', 'for instance', 'in addition',
            'on the other hand', 'as a result', 'in contrast'
        ]
        text_lower = text.lower()
        transition_count = sum(text_lower.count(word) for word in transition_words)

        sentences = re.split(r'[.!?]+', text)
        passive_indicators = ['was', 'were', 'been', 'being', 'is', 'are', 'am', 'be']
        passive_count = 0
        for sentence in sentences:
            sentence_lower = sentence.lower()
            if any(f' {word} ' in f' {sentence_lower} ' for word in passive_indicators):
                if re.search(r'\b\w+(ed|en)\b', sentence_lower):
                    passive_count += 1

        total_sentences = len([s for s in sentences if s.strip()])
        passive_ratio = (passive_count / total_sentences) if total_sentences > 0 else 0

        words = text.split()
        complex_word_count = sum(
            1 for word in words
            if len(re.findall(r'[aeiouy]+', re.sub(r'[^a-zA-Z]', '', word.lower()))) >= 3
        )
        complex_word_ratio = (complex_word_count / len(words)) if words else 0

        return {
            'transition_word_count': transition_count,
            'transition_words_per_100': round((transition_count / len(words)) * 100, 1) if words else 0,
            'passive_sentence_count': passive_count,
            'passive_sentence_ratio': round(passive_ratio * 100, 1),
            'complex_word_count': complex_word_count,
            'complex_word_ratio': round(complex_word_ratio * 100, 1)
        }

    def _calculate_overall_score(self, metrics: Dict, structure: Dict, complexity: Dict) -> float:
        score = 100
        flesch = metrics.get('flesch_reading_ease', 0)
        if flesch < 30:
            score -= 30
        elif flesch < 50:
            score -= 20
        elif flesch < 60:
            score -= 10
        elif flesch > 80:
            score -= 5

        grade = metrics.get('flesch_kincaid_grade', 0)
        target_min, target_max = self.target_reading_level
        if grade < target_min - 2:
            score -= 10
        elif grade > target_max + 4:
            score -= 25
        elif grade > target_max + 2:
            score -= 15
        elif grade > target_max:
            score -= 5

        avg_sentence = structure.get('avg_sentence_length', 0)
        if avg_sentence > 30:
            score -= 20
        elif avg_sentence > 25:
            score -= 10
        elif avg_sentence > 20:
            score -= 5

        very_long = structure.get('very_long_sentences', 0)
        if very_long > 0:
            score -= min(15, very_long * 3)

        avg_para_sentences = structure.get('avg_sentences_per_paragraph', 0)
        if avg_para_sentences > 6:
            score -= 10
        elif avg_para_sentences > 4:
            score -= 5

        passive_ratio = complexity.get('passive_sentence_ratio', 0)
        if passive_ratio > 30:
            score -= 10
        elif passive_ratio > 20:
            score -= 5

        transition_per_100 = complexity.get('transition_words_per_100', 0)
        if transition_per_100 < 0.5:
            score -= 5
        elif transition_per_100 > 2:
            score += 5

        return max(0, min(100, score))

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

    def _get_status(self, metrics: Dict, structure: Dict) -> Dict[str, Any]:
        grade_level = metrics.get('flesch_kincaid_grade', 0)
        flesch_ease = metrics.get('flesch_reading_ease', 0)
        avg_sentence = structure.get('avg_sentence_length', 0)
        target_min, target_max = self.target_reading_level

        grade_status = "optimal" if target_min <= grade_level <= target_max else (
            "too_simple" if grade_level < target_min else "too_complex"
        )
        ease_status = "good" if 60 <= flesch_ease <= 80 else ("difficult" if flesch_ease < 60 else "too_easy")
        sentence_status = "good" if avg_sentence <= self.max_avg_sentence_length else "too_long"

        return {
            'grade_level_status': grade_status,
            'ease_status': ease_status,
            'sentence_length_status': sentence_status,
        }

    def _generate_recommendations(self, metrics: Dict, structure: Dict, complexity: Dict) -> List[str]:
        recommendations = []
        grade = metrics.get('flesch_kincaid_grade', 0)
        target_min, target_max = self.target_reading_level
        flesch = metrics.get('flesch_reading_ease', 0)

        if grade > target_max + 2:
            recommendations.append(f"Reading level too high (Grade {grade}, target {target_min}-{target_max}). Simplify sentences.")
        elif grade < target_min - 2:
            recommendations.append(f"Reading level very simple (Grade {grade}). Add more depth.")

        if flesch < 50:
            recommendations.append(f"Content too difficult (Flesch {flesch}). Break up complex sentences.")
        elif flesch < 60:
            recommendations.append(f"Content fairly difficult (Flesch {flesch}). Aim for 60-70.")

        avg_sentence = structure.get('avg_sentence_length', 0)
        if avg_sentence > 25:
            recommendations.append(f"Avg sentence length too long ({avg_sentence:.1f} words). Target under 20.")

        very_long = structure.get('very_long_sentences', 0)
        if very_long > 0:
            recommendations.append(f"{very_long} sentences are very long (35+ words). Split them.")

        avg_para = structure.get('avg_sentences_per_paragraph', 0)
        if avg_para > 4:
            recommendations.append(f"Paragraphs too long (avg {avg_para:.1f} sentences). Target 2-4 sentences.")

        passive_ratio = complexity.get('passive_sentence_ratio', 0)
        if passive_ratio > 30:
            recommendations.append(f"Too much passive voice ({passive_ratio:.0f}%). Convert to active voice.")

        if not recommendations:
            recommendations.append("Readability is excellent.")

        return recommendations

    def _variance(self, values: List[float]) -> float:
        if len(values) < 2:
            return 0
        mean = sum(values) / len(values)
        return sum((x - mean) ** 2 for x in values) / len(values)
