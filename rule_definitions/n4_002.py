"""Rule definition for 〜たがる"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the 〜たがる grammar rule"""
    return GrammarRule(
        name="〜たがる",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(
                        value="た",
                    ),
                    TokenPattern(
                        value="がる",
                    ),
                ]
            ),
        ],
        description="動詞「ます形」＋たがる",
        category="N3",
        index=25,
        examples=[
            "うちの子どもは怖い話を聞きたがる。",
            "このアパートに住みたがっている学生が多い。",
        ],
    )
