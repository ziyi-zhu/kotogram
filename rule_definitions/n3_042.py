"""Rule definition for ～たきり〜ない"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～たきり〜ない grammar rule"""
    return GrammarRule(
        name="～たきり〜ない",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_TA,
                    TokenPattern(
                        value="きり",
                        alternatives=[
                            TokenPattern(value="っきり"),
                            TokenPattern(value="ぎり"),
                        ],
                    ),
                ]
            ),
        ],
        description="動詞「た形」+きり~ない",
        category="N3",
        index=42,
        examples=[
            "彼は出かけたきり、戻ってこない。",
            "ピアノは小学生の頃習ったきりで、ほとんど忘れてしまった。",
            "彼とは3年前に一度会ったきり、その後、ずっと会っていない。",
        ],
    )
