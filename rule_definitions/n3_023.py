"""Rule definition for ～くらい/ぐらい"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～くらい/ぐらい grammar rule"""
    return GrammarRule(
        name="～くらい/ぐらい",
        patterns=[
            # Pattern for degree expression (Meaning 1)
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(
                        value="ぐらい",
                        alternatives=[
                            TokenPattern(value="くらい"),
                        ],
                    ),
                ]
            ),
            # Pattern for verb + たい + くらい/ぐらい
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(value="たい"),
                    TokenPattern(
                        value="ぐらい",
                        alternatives=[
                            TokenPattern(value="くらい"),
                        ],
                    ),
                ]
            ),
            # Pattern for minimum degree (Meaning 2)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(
                        value="ぐらい",
                        alternatives=[
                            TokenPattern(value="くらい"),
                        ],
                    ),
                ]
            ),
            # Pattern for highest degree ~ぐらい〜はない (Meaning 3)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(
                        value="ぐらい",
                        alternatives=[
                            TokenPattern(value="くらい"),
                        ],
                    ),
                    TokenPattern(value="は"),
                    TokenPattern(value="ない"),
                ]
            ),
            # Alternative pattern for highest degree with different structure
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(
                        value="ぐらい",
                        alternatives=[
                            TokenPattern(value="くらい"),
                        ],
                    ),
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="は"),
                    TokenPattern(value="ない"),
                ]
            ),
        ],
        description="動詞普通形/い形容詞普通形＋くらい/ぐらい\n動詞＋たい＋くらい/ぐらい\n名詞＋くらい/ぐらい\n名詞＋くらい/ぐらい＋は＋ない",
        category="N3",
        index=23,
        examples=[
            "怖くて怖くて、大声で叫びたいくらいだった。",
            "今日は朝から仕事が忙しくて、食事をする時間もないくらいだ。",
            "これは新品だから、安くても5千円ぐらいはするだろう。",
            "自分のことぐらい自分でやりなさい。",
            "彼くらい努力する人はいない。",
            "戦争ぐらい残酷なものはない。",
        ],
    )
