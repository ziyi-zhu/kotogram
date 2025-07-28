"""Rule definition for ～上に"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～上に grammar rule"""
    return GrammarRule(
        name="～上に",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="上"),
                    TokenPattern(value="に"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA_OR_DEARU,
                    TokenPattern(value="上"),
                    TokenPattern(value="に"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NOUN_NO_OR_DEARU,
                    TokenPattern(value="上"),
                    TokenPattern(value="に"),
                ]
            ),
        ],
        description="動詞普通形/い形容詞辞書形＋上に\nな形容詞語幹＋な/である＋上に\n名詞＋の/である＋上に",
        category="N3",
        index=9,
        examples=[
            "そのスポーツクラブは入会金が要らない上に、わが家から近い。",
            "台風が近づいてきて、風が強い上に、雨も激しく降っている。",
            "この商品はデザインがユニークな上に、色もカラフルだ。",
            "彼は学生の上に、アルバイトもしている。",
        ],
    )
