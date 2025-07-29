"""Rule definition for たとえ/たとい〜ても"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech, POSDetailType


def create_rule() -> GrammarRule:
    """Create the たとえ/たとい〜ても grammar rule"""
    return GrammarRule(
        name="たとえ/たとい〜ても",
        patterns=[
            # Pattern 1: たとえ/たとい + verb te-form + も
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        value="たとえ",
                        alternatives=[
                            TokenPattern(value="たとい"),
                        ],
                    ),
                    TokenPattern(
                        part_of_speech=PartOfSpeech.VERB,
                        infl_form="連用テ接続",
                    ),
                    TokenPattern(value="て"),
                    TokenPattern(value="も"),
                ]
            ),
            # Pattern 2: たとえ/たとい + i-adjective te-form + も
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        value="たとえ",
                        alternatives=[
                            TokenPattern(value="たとい"),
                        ],
                    ),
                    TokenPattern(
                        part_of_speech=PartOfSpeech.ADJECTIVE,
                        infl_form="連用テ接続",
                    ),
                    TokenPattern(value="て"),
                    TokenPattern(value="も"),
                ]
            ),
            # Pattern 3: たとえ/たとい + na-adjective stem + でも
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        value="たとえ",
                        alternatives=[
                            TokenPattern(value="たとい"),
                        ],
                    ),
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
                    TokenPattern(value="でも"),
                ]
            ),
            # Pattern 4: たとえ/たとい + noun + で + も
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        value="たとえ",
                        alternatives=[
                            TokenPattern(value="たとい"),
                        ],
                    ),
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="で"),
                    TokenPattern(value="も"),
                ]
            ),
            # Pattern 5: たとえ/たとい + [any tokens] + て + も (flexible pattern for complex structures)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        value="たとえ",
                        alternatives=[
                            TokenPattern(value="たとい"),
                        ],
                    ),
                    TokenPattern(),  # Multi wildcard that matches any number of any token
                    TokenPattern(value="て"),
                    TokenPattern(value="も"),
                ]
            ),
        ],
        description="たとえ/たとい + 動詞「て形」+ も\nたとえ/たとい + い形容詞「て形」+ も\nたとえ/たとい + な形容詞詞幹 + でも\nたとえ/たとい + 名詞 + でも\nたとえ/たとい + [任意の語] + て + も",
        category="N3",
        index=47,
        examples=[
            "たとえみんなに反対されても、わたしは絶対にこの計画を実行したい。",
            "たとえ高くても、必要なものは買わなければならない。",
            "たとえ雨でも、予定通り運動会を行う。",
        ],
    )
