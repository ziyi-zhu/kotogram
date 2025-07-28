"""Rule definition for ～上で(は)/上での"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～上で(は)/上での grammar rule"""
    return GrammarRule(
        name="～上で(は)/上での",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NOUN_NO,
                    TokenPattern(value="上"),
                    TokenPattern(value="で"),
                    TokenPattern(value="は", optional=True),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="上"),
                    TokenPattern(value="で"),
                    TokenPattern(value="は", optional=True),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NOUN_NO,
                    TokenPattern(value="上"),
                    TokenPattern(value="で"),
                    TokenPattern(value="の"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="上"),
                    TokenPattern(value="で"),
                    TokenPattern(value="の"),
                ]
            ),
        ],
        description="名詞＋の＋上で(は)/上での\n動詞辞書形＋上で(は)/上での",
        category="N3",
        index=8,
        examples=[
            "仕事の上では別に問題はない。",
            "外国語を勉強する上で、単語を覚えるのはとても大事なことだ。",
            "この仕事の上での注意点を説明します。",
            "勉強する上でのコツを教えてください。",
        ],
    )
