"""Rule definition for ～みたいだ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech, POSDetailType


def create_rule() -> GrammarRule:
    """Create the ～みたいだ grammar rule"""
    return GrammarRule(
        name="～みたいだ",
        patterns=[
            # Pattern 1: 動詞普通形/い形容詞普通形 + みたいだ
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="みたい"),
                    TokenPattern(
                        value="だ",
                        alternatives=[
                            TokenPattern(value="な"),
                            TokenPattern(value="に"),
                        ],
                    ),
                ]
            ),
            # Pattern 2: な形容詞語幹/名詞 + みたいだ
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
                            TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                        ],
                    ),
                    TokenPattern(value="みたい"),
                    TokenPattern(
                        value="だ",
                        alternatives=[
                            TokenPattern(value="な"),
                            TokenPattern(value="に"),
                        ],
                    ),
                ]
            ),
            # Pattern 3: 各詞類「た形」 + みたいだ
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_TA,
                    TokenPattern(value="みたい"),
                    TokenPattern(
                        value="だ",
                        alternatives=[
                            TokenPattern(value="な"),
                            TokenPattern(value="に"),
                        ],
                    ),
                ]
            ),
        ],
        description="動詞普通形/い形容詞普通形＋みたいだ\nな形容詞語幹/名詞＋みたいだ\n各詞類「た形」＋みたいだ",
        category="N4",
        index=7,
        examples=[
            "誰か教室にいるみたいだ。電気が付いている。",
            "新しいカメラは高画質みたいだ。",
            "あの雲の形はまるで馬みたいだね。",
            "赤ちゃんはりんごみたいな顔をしている。",
            "10キロも痩せた彼女はまるで別人みたいになっている。",
            "妹は、体操の選手みたいに体が柔らかい。",
            "大きくなったら、イチローさんみたいな野球選手になりたいです。",
        ],
    )
