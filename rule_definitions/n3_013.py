"""Rule definition for ～恐れがある"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～恐れがある grammar rule"""
    return GrammarRule(
        name="～恐れがある",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NOUN_NO,
                    TokenPattern(value="恐れ"),
                    TokenPattern(value="が"),
                    TokenPattern(value="ある"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="恐れ"),
                    TokenPattern(value="が"),
                    TokenPattern(value="ある"),
                ]
            ),
        ],
        description="名詞＋の＋恐れがある\n動詞辞書形＋恐れがある",
        category="N3",
        index=13,
        examples=[
            "今晚、大型の台風がこの地方へ近づく恐れがあります。",
            "この欠陥を直さないと、重大な事故が起こる恐れがある。",
        ],
    )
