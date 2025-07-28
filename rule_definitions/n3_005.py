"""Rule definition for ～一方（で）"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～一方（で） grammar rule"""
    return GrammarRule(
        name="～一方（で）",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="一方"),
                    TokenPattern(value="で", optional=True),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA_OR_DEARU,
                    TokenPattern(value="一方"),
                    TokenPattern(value="で", optional=True),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NOUN_NO_OR_DEARU,
                    TokenPattern(value="一方"),
                    TokenPattern(value="で", optional=True),
                ]
            ),
        ],
        description="動詞普通形/い形容詞辞書形＋一方（で）\nな形容詞語幹＋な/である＋一方（で）\n名詞＋である＋一方（で）",
        category="N3",
        index=5,
        examples=[
            "彼は自分は何もしていない一方で、他人のすることによく文句を言う。",
            "田中さんは医科大学の教授である一方、小説家としても有名だ。",
            "娘ならきっと合格できるだろうと信じる一方で、ちょっと不安なところもある。",
            "この機械は新しい一方で、使い方が難しい。",
            "収入が減る一方で、教育費などの支出は増えていくのだから、節約するしかない。",
            "姉は明るい一方で、妹は無口だ。",
            "彼は真面目な一方で、冗談もよく言う。",
            "この部屋は静かな一方で、少し暗いです。",
            "彼女は有名である一方、謙虚な人です。",
            "田中さんは医科大学の教授である一方、小説家としても有名だ。",
            "この制度は学生のための一方、教員にもメリットがある。",
        ],
    )
