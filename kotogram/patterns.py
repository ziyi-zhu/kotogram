"""Commonly used token patterns for Japanese grammar rules"""

from kotogram.grammar import TokenPattern
from kotogram.types import InflectionForm, InflectionType, PartOfSpeech, POSDetailType


class CommonPatterns:
    """Collection of commonly used token patterns"""

    # 動詞普通形/い形容詞普通形
    VERB_OR_I_ADJ_PLAIN = [
        TokenPattern(
            part_of_speech=PartOfSpeech.VERB,
            alternatives=[
                TokenPattern(
                    part_of_speech=PartOfSpeech.ADJECTIVE,
                    infl_type=InflectionType.ADJECTIVE_ISTEM,
                    alternatives=[
                        TokenPattern(
                            part_of_speech=PartOfSpeech.ADJECTIVE,
                            infl_type=InflectionType.ADJECTIVE_AUO,
                        ),
                    ],
                ),
            ],
        ),
        TokenPattern(value="ない", optional=True),
    ]

    # な形容詞語幹 + な
    NA_ADJ_STEM_NA = [
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
        TokenPattern(value="な"),
    ]

    # な形容詞語幹 + な/である
    NA_ADJ_STEM_NA_OR_DEARU = [
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
        TokenPattern(
            value="な",
            alternatives=[
                TokenPattern(value="で"),
            ],
        ),
        TokenPattern(value="ある", optional=True),
    ]

    # 名詞 + の
    NOUN_NO = [
        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
        TokenPattern(value="の"),
    ]

    # 名詞 + の/である
    NOUN_NO_OR_DEARU = [
        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
        TokenPattern(
            value="の",
            alternatives=[
                TokenPattern(value="で"),
            ],
        ),
        TokenPattern(value="ある", optional=True),
    ]

    # 動詞辞書形
    VERB_BASIC = [
        TokenPattern(part_of_speech=PartOfSpeech.VERB, infl_form=InflectionForm.BASIC),
    ]

    # 動詞 + た
    VERB_TA = [
        TokenPattern(part_of_speech=PartOfSpeech.VERB),
        TokenPattern(value="た"),
    ]

    # 動詞 + ない
    VERB_NAI = [
        TokenPattern(part_of_speech=PartOfSpeech.VERB),
        TokenPattern(value="ない"),
    ]

    # 動詞「ます形」
    VERB_MASU = [
        TokenPattern(
            part_of_speech=PartOfSpeech.VERB, infl_form=InflectionForm.INFLECTED
        ),
    ]

    # 数量詞
    QUANTIFIER = [
        TokenPattern(
            part_of_speech=PartOfSpeech.NOUN, pos_detail=POSDetailType.NOUN_NUMERAL
        ),
        TokenPattern(
            part_of_speech=PartOfSpeech.NOUN, pos_detail=POSDetailType.NOUN_COUNTER
        ),
    ]
