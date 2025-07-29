"""Rule definition for 〜たまえ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the 〜たまえ grammar rule"""
    return GrammarRule(
        name="〜たまえ",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(value="た"),
                    TokenPattern(value="ま"),
                    TokenPattern(value="え"),
                ]
            ),
        ],
        description="動詞「ます形」+ たまえ",
        category="N3",
        index=50,
        examples=[
            "上田君、この方案を説明したまえ。",
            "明日は朝7時に来たまえ。",
        ],
    )
