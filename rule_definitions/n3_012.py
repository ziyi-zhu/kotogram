"""Rule definition for ～おきに"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～おきに grammar rule"""
    return GrammarRule(
        name="～おきに",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.QUANTIFIER,
                    TokenPattern(value="おき"),
                    TokenPattern(value="に"),
                ]
            ),
        ],
        description="数量詞＋おきに",
        category="N3",
        index=12,
        examples=[
            "この道には5メートルおきに木が植えてある。",
            "新宿へ向かう電車は3分おきに出ている。",
        ],
    )
