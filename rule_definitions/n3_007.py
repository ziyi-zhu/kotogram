"""Rule definition for ～上で（の）"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～上で（の） grammar rule"""
    return GrammarRule(
        name="～上で（の）",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_TA,
                    TokenPattern(value="上"),
                    TokenPattern(value="で"),
                    TokenPattern(value="の", optional=True),
                ]
            ),
        ],
        description="動詞「た形」＋上で（の）",
        category="N3",
        index=7,
        examples=[
            "私が皆様のご意見を伺った上で、来週ご報告いたします。",
            "それぞれの説明をよく聞いた上で、旅行のコースを選びたいと思います。",
        ],
    )
