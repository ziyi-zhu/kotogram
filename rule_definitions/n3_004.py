"""Rule definition for ～いい/よい"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～いい/よい grammar rule"""
    return GrammarRule(
        name="～いい/よい",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(
                        value="いい",
                        alternatives=[
                            TokenPattern(value="よい"),
                        ],
                    ),
                ]
            ),
        ],
        description="動詞「ます形」＋いい/よい",
        category="N3",
        index=4,
        examples=[
            "この町は住みよいです。",
            "この薬は飲みいいです。",
            "この本はわかりよいです。",
        ],
    )
