"""Rule definition for ～がかり"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～がかり grammar rule"""
    return GrammarRule(
        name="～がかり",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.QUANTIFIER,
                    TokenPattern(value="がかり"),
                ]
            ),
        ],
        description="名詞＋がかり",
        category="N3",
        index=14,
        examples=[
            "3年がかりの調査の結果、工場廃水に含まれている金属物質が住民に危害を及ぼしたことがわかった。",
            "その記念碑は重くて、8人がかりで運んでも動かない。",
        ],
    )
