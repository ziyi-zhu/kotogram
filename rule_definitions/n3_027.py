"""Rule definition for ～ことだ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～ことだ grammar rule"""
    return GrammarRule(
        name="～ことだ",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_NAI,
                    TokenPattern(value="こと"),
                    TokenPattern(value="だ"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="こと"),
                    TokenPattern(value="だ"),
                ]
            ),
        ],
        description="動詞「ない形」＋ことだ\n動詞辞書形＋ことだ",
        category="N3",
        index=27,
        examples=[
            "上手になりたければ、毎日短い時間でもいいから練習を続けることだ。",
            "健康でいたければ、早寝早起きをすることだ。",
        ],
    )
