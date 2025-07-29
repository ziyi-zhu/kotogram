"""Rule definition for ～たって/だって"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech, POSDetailType


def create_rule() -> GrammarRule:
    """Create the ～たって/だって grammar rule"""
    return GrammarRule(
        name="～たって/だって",
        patterns=[
            # Pattern 1: Concessive condition - verb masu form + たって
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(value="たっ"),
                    TokenPattern(value="て"),
                ]
            ),
            # Pattern 2: Concessive condition - i-adjective + たって
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        part_of_speech=PartOfSpeech.ADJECTIVE,
                        infl_form="連用テ接続",
                    ),
                    TokenPattern(value="たっ"),
                    TokenPattern(value="て"),
                ]
            ),
            # Pattern 3: Concessive condition - na-adjective stem + だって
            GrammarRulePattern(
                patterns=[
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
                    TokenPattern(value="だって"),
                ]
            ),
            # Pattern 4: Concessive condition - noun + だって
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="だって"),
                ]
            ),
            # Pattern 5: "No matter what" - interrogative + だって
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        part_of_speech=PartOfSpeech.NOUN,
                        pos_detail=POSDetailType.NOUN_PRONOUN,
                        alternatives=[
                            TokenPattern(
                                part_of_speech=PartOfSpeech.NOUN,
                                pos_detail=POSDetailType.NOUN_ADVERBIAL,
                            ),
                        ],
                    ),
                    TokenPattern(value="だって"),
                ]
            ),
        ],
        description="動詞「ます形」+たって\nい形容詞語幹+く+たって\nな形容詞語幹+だって\n名詞+だって\n疑問詞+だって",
        category="N3",
        index=46,
        examples=[
            "今さら謝りたって許してもらえない。",
            "難しくたって、この仕事に挑戦したい。",
            "野菜が嫌いだって、健康のために食べるべきだ。",
            "最近は仕事が忙しくて、日曜日だって休めない。",
            "わたしの応援が力になるならいくらだって応援します。",
            "あの二人が結婚したと聞けば、誰だってびっくりするよ。",
        ],
    )
