"""Rule definition for ～あがる"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～あがる grammar rule"""
    return GrammarRule(
        name="～あがる",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(
                        value="あがる",
                        alternatives=[
                            TokenPattern(value="上がる"),
                        ],
                    ),
                ]
            ),
        ],
        description="動詞「ます形」＋あがる",
        category="N3",
        index=3,
        examples=[
            "最新の企画書が出来あがったので、どうぞご覧ください。",
            "彼氏へのマフラーが編みあがった。",
        ],
    )
