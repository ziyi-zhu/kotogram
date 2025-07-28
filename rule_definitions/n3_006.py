"""Rule definition for ～一方だ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～一方だ grammar rule"""
    return GrammarRule(
        name="～一方だ",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="一方"),
                    TokenPattern(value="だ"),
                ]
            ),
        ],
        description="動詞辞書形＋一方だ",
        category="N3",
        index=6,
        examples=[
            "ここ数年、この町の人口は減る一方だ。",
            "わが社の業績はよくなる一方だ。",
        ],
    )
