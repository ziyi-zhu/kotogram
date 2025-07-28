"""Rule definition for ～おかげで / ～おかげだ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import InflectionForm, PartOfSpeech, POSDetailType


def create_rule() -> GrammarRule:
    """Create the ～おかげで / ～おかげだ grammar rule"""
    return GrammarRule(
        name="～おかげで / ～おかげだ",
        patterns=[
            # 動詞辞書形 + おかげで/おかげだ
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="おかげ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="だ"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
            # い形容詞辞書形 + おかげで/おかげだ
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        part_of_speech=PartOfSpeech.ADJECTIVE,
                        infl_form=InflectionForm.BASIC,
                    ),
                    TokenPattern(value="おかげ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="だ"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
            # な形容詞語幹 + な + おかげで/おかげだ
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA,
                    TokenPattern(value="おかげ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="だ"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
            # 名詞 + の + おかげで/おかげだ
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NOUN_NO,
                    TokenPattern(value="おかげ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="だ"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
            # 動詞た形 + おかげで/おかげだ
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_TA,
                    TokenPattern(value="おかげ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="だ"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
            # い形容詞た形 + おかげで/おかげだ
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        part_of_speech=PartOfSpeech.ADJECTIVE,
                        infl_form=InflectionForm.INFLECTED_TA,
                    ),
                    TokenPattern(value="おかげ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="だ"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
            # な形容詞た形 + おかげで/おかげだ
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
                    TokenPattern(value="だっ"),
                    TokenPattern(value="た"),
                    TokenPattern(value="おかげ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="だ"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
        ],
        description="動詞辞書形＋おかげで/おかげだ\nい形容詞辞書形＋おかげで/おかげだ\nな形容詞語幹＋な＋おかげで/おかげだ\n名詞＋の＋おかげで/おかげだ\n各词类「た」形＋おかげで/おかげだ",
        category="N3",
        index=11,
        examples=[
            "母は「風邪を引かないのは、毎朝しているジョギングのおかげだ。」とよく言っている。",
            "わたしたちが優勝できたのは、応援してくれたみんなのおかげです。",
            "彼の話を信じたおかげで、ひどい目に遭った。",
            "先生の指導のおかげで、試験に合格できました。",
            "友達が手伝ってくれたおかげで、宿題が早く終わりました。",
            "毎日練習したおかげで、ピアノが上手になりました。",
            "家族の支えのおかげで、困難を乗り越えることができた。",
        ],
    )
