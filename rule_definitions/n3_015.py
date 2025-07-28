"""Rule definition for ～がたい"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～がたい grammar rule"""
    return GrammarRule(
        name="～がたい",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(value="がたい"),
                ]
            ),
        ],
        description="動詞「ます形」＋がたい",
        category="N3",
        index=15,
        examples=[
            "これだけ景気が悪いのに、税金を上げようとするのは、わたしたち国民には理解しがたい。",
            "どのコンピューターを買ったらよいか、なかなか一つには決めがたい。",
        ],
    )
