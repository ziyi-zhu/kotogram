"""Rule definition for 〜がる"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import InflectionType, PartOfSpeech, POSDetailType


def create_rule() -> GrammarRule:
    """Create the 〜がる grammar rule"""
    return GrammarRule(
        name="〜がる",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        part_of_speech=PartOfSpeech.ADJECTIVE,
                        infl_type=InflectionType.ADJECTIVE_ISTEM,
                        alternatives=[
                            TokenPattern(
                                part_of_speech=PartOfSpeech.NOUN,
                                pos_detail=POSDetailType.NOUN_ADJECTIVE_VERBAL_STEM,
                                alternatives=[
                                    TokenPattern(
                                        part_of_speech=PartOfSpeech.NOUN,
                                        pos_detail=POSDetailType.NOUN_NAI_ADJECTIVE_STEM,
                                    ),
                                ],
                            ),
                        ],
                    ),
                    TokenPattern(
                        value="がる",
                    ),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        part_of_speech=PartOfSpeech.VERB,
                        value="怖がる",
                        alternatives=[
                            TokenPattern(value="可愛がる"),
                        ],
                    ),
                ]
            ),
        ],
        description="い形容詞語幹/な形容詞語幹＋がる",
        category="N4",
        index=3,
        examples=[
            "急に大きな音がしたので、その子どもは怖がって泣いてしまった。",
            "猫を可愛がる女の子が多いです。",
        ],
    )
