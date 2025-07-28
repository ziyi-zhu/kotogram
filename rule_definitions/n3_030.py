"""Rule definition for ～ことになっている/こととなっている"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～ことになっている/こととなっている grammar rule"""
    return GrammarRule(
        name="～ことになっている/こととなっている",
        patterns=[
            # Pattern for verb dictionary form + ことになっている
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(value="なっ"),
                    TokenPattern(value="て"),
                    TokenPattern(value="いる"),
                ]
            ),
            # Pattern for verb nai-form + ことになっている
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_NAI,
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(value="なっ"),
                    TokenPattern(value="て"),
                    TokenPattern(value="いる"),
                ]
            ),
            # Pattern for verb dictionary form + こととなっている
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="こと"),
                    TokenPattern(value="と"),
                    TokenPattern(value="なっ"),
                    TokenPattern(value="て"),
                    TokenPattern(value="いる"),
                ]
            ),
            # Pattern for verb nai-form + こととなっている
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_NAI,
                    TokenPattern(value="こと"),
                    TokenPattern(value="と"),
                    TokenPattern(value="なっ"),
                    TokenPattern(value="て"),
                    TokenPattern(value="いる"),
                ]
            ),
        ],
        description="動詞辞書形＋ことになっている/こととなっている\n動詞「ない形」＋ことになっている/こととなっている",
        category="N3",
        index=30,
        examples=[
            "今日は7時東京駅で友だちと会うことになっているので、6時半に会社を出ます。",
            "この部屋には、関係者以外入ってはいけないことになっている。",
            "日本では車は左側を走ることとなっている。",
        ],
    )
