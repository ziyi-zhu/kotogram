"""Rule definition for ～たことにする"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern


def create_rule() -> GrammarRule:
    """Create the ～たことにする grammar rule"""
    return GrammarRule(
        name="～たことにする",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(value="た"),
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(
                        value="する",
                        alternatives=[
                            TokenPattern(value="し"),
                        ],
                    ),
                ]
            ),
        ],
        description="動詞「た形」+ことにする",
        category="N3",
        index=45,
        examples=[
            "その話は聞かなかったことにします。",
            "今までのことはなかったことにしましょう。",
        ],
    )
