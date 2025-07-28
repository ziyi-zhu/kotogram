"""Rule definition for ～こそ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～こそ grammar rule"""
    return GrammarRule(
        name="～こそ",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="こそ"),
                ]
            ),
        ],
        description="名詞＋こそ",
        category="N3",
        index=24,
        examples=[
            "いいえ、こちらこそ。",
            "これこそ本場の日本料理です。",
            "今年こそ試験に合格できるよう、頑張る。",
        ],
    )
