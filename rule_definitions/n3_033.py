"""Rule definition for ～最中に"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～最中に grammar rule"""
    return GrammarRule(
        name="～最中に",
        patterns=[
            # Pattern for noun + の + 最中に
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="の"),
                    TokenPattern(value="最中"),
                    TokenPattern(value="に"),
                ]
            ),
            # Pattern for verb te-iru form + 最中に
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(value="て"),
                    TokenPattern(value="いる"),
                    TokenPattern(value="最中"),
                    TokenPattern(value="に"),
                ]
            ),
        ],
        description="名詞＋の＋最中に\n動詞「ている形」＋最中に",
        category="N3",
        index=33,
        examples=[
            "電話している最中に、誰かが玄関に来た。",
            "食事の最中に、お客さんが来た。",
        ],
    )
