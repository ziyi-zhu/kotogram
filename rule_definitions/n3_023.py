"""Rule definition for ～くらい／ぐらい"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～くらい／ぐらい grammar rule"""
    return GrammarRule(
        name="～くらい／ぐらい",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(
                        value="ぐらい",
                        alternatives=[
                            TokenPattern(value="くらい"),
                        ],
                    ),
                    TokenPattern(),
                    TokenPattern(value="は"),
                    TokenPattern(value="い", optional=True),
                    TokenPattern(value="ない"),
                ]
            ),
        ],
        description="～ぐらい～はない",
        category="N3",
        index=23,
        examples=[
            "戦争ぐらい残酷なものはない。",
            "彼くらい努力する人はいない。",
        ],
    )
