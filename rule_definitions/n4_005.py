"""Rule definition for ～ようだ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～ようだ grammar rule"""
    return GrammarRule(
        name="～ようだ",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="よう"),
                    TokenPattern(
                        value="だ",
                        alternatives=[
                            TokenPattern(value="に"),
                            TokenPattern(value="な"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA,
                    TokenPattern(value="よう"),
                    TokenPattern(
                        value="だ",
                        alternatives=[
                            TokenPattern(value="に"),
                            TokenPattern(value="な"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NOUN_NO,
                    TokenPattern(value="よう"),
                    TokenPattern(
                        value="だ",
                        alternatives=[
                            TokenPattern(value="に"),
                            TokenPattern(value="な"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.ADNOMINAL),
                    TokenPattern(value="よう"),
                    TokenPattern(
                        value="だ",
                        alternatives=[
                            TokenPattern(value="に"),
                            TokenPattern(value="な"),
                            TokenPattern(value="です"),
                        ],
                    ),
                ]
            ),
        ],
        description="動詞普通形＋ようだ/ように/ような/ようです\nい形容詞普通形＋ようだ/ように/ような/ようです\nな形容詞詞干＋な＋ようだ/ように/ような/ようです\n名詞＋の＋ようだ/ように/ような/ようです\n連体詞＋ようだ/ように/ような/ようです",
        category="N4",
        index=5,
        examples=[
            "母ははじめて飛行機に乗って、子どものように喜んだ。",
            "彼女の笑顔は太陽のように明るく輝いている。",
            "わたしは田中さんのような優しい人が好きです。",
            "このように操作すれば、ロボットが起動します。",
            "あの時はしかたなかったのだが、彼を怒らせるようなことを言ってしまって悪かったと思った。",
            "外は寒いようですね。",
        ],
    )
