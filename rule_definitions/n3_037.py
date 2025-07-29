"""Rule definition for ～上"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～上 grammar rule"""
    return GrammarRule(
        name="～上",
        patterns=[
            # Pattern for noun + 上
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="上"),
                ]
            ),
            # Pattern for noun + 上の (attributive modifier)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="上"),
                    TokenPattern(value="の"),
                ]
            ),
        ],
        description="名詞＋上",
        category="N3",
        index=37,
        examples=[
            "それは法律上では許されない行為だ。",
            "生命倫理上の問題でクローン技術に反対する意見が多い。",
        ],
    )
