"""Rule definition for ～ことにする"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～ことにする grammar rule"""
    return GrammarRule(
        name="～ことにする",
        patterns=[
            # Pattern for verb dictionary form + ことにする
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(value="する"),
                ]
            ),
            # Pattern for verb nai-form + ことにする
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_NAI,
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(value="する"),
                ]
            ),
        ],
        description="動詞辞書形＋ことにする\n動詞「ない形」＋ことにする",
        category="N3",
        index=29,
        examples=[
            "小学校に入学して字を書く機会が増えるだろうと思い、孫に文房具をあげることにした。",
            "アルコールはもう飲まないことにする。",
            "毎日6時に起きることにしています。",
        ],
    )
