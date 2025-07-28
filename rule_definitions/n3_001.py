"""Rule definition for ～間（に）"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～間（に） grammar rule"""
    return GrammarRule(
        name="～間（に）",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="間"),
                    TokenPattern(value="に", optional=True),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA,
                    TokenPattern(value="間"),
                    TokenPattern(value="に", optional=True),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NOUN_NO,
                    TokenPattern(value="間"),
                    TokenPattern(value="に", optional=True),
                ]
            ),
        ],
        description="動詞普通形/い形容詞普通形＋間（に）\nな形容詞語幹＋な＋間（に）\n名詞＋の＋間（に）",
        category="N3",
        index=1,
        examples=[
            "赤ちゃんが寝ている間に、洗濯をしました。",
            "日本に留学している間に富士山に登りたい。",
            "この機械は新しい間、使い方が難しい。",
            "山田先生の講演の間、皆熱心に話を聞いていた。",
            "私は夏休みの間、ずっと実家にいました。",
            "便利な間にやっておきましょう。",
            "静かな間に勉強を終わらせたい。",
        ],
    )
