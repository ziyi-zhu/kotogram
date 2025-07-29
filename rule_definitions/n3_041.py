"""Rule definition for ～そうにない/そうもない"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～そうにない/そうもない grammar rule"""
    return GrammarRule(
        name="～そうにない/そうもない",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(value="そう"),
                    TokenPattern(
                        value="に",
                        alternatives=[
                            TokenPattern(value="も"),
                        ],
                    ),
                    TokenPattern(value="ない"),
                ]
            ),
        ],
        description="動詞「ます形」+そうにない/そうもない",
        category="N3",
        index=41,
        examples=[
            "今のわたしの給料では、何年働いても自分の家は買えそうもない。",
            "雨はまだ止みそうにない。",
        ],
    )
