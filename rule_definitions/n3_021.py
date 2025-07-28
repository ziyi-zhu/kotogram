"""Rule definition for ～きる/きれる/きれない"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import InflectionForm, PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～きる/きれる/きれない grammar rule"""
    return GrammarRule(
        name="～きる/きれる/きれない",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(
                        value="きる",
                        alternatives=[
                            TokenPattern(value="きれる"),
                            TokenPattern(value="きれない"),
                        ],
                    ),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        part_of_speech=PartOfSpeech.VERB,
                        alternatives=[
                            TokenPattern(
                                part_of_speech=PartOfSpeech.VERB,
                                infl_form=InflectionForm.INFLECTED,
                            ),
                        ],
                    ),
                    TokenPattern(
                        value="きる",
                        alternatives=[
                            TokenPattern(value="きれる"),
                            TokenPattern(value="きれない"),
                        ],
                    ),
                ]
            ),
        ],
        description="動詞「ます形」＋きる/きれる/きれない\n動詞＋きる/きれる/きれない",
        category="N3",
        index=21,
        examples=[
            "こんなに長い小説は、1日では読みきれない。",
            "お小遣いを使いきってしまった。",
            "彼のことを信じきっています。",
            "今日は忙しくて、もう疲れきってしまった。",
            "この問題は複雑すぎて、私には理解しきれない。",
        ],
    )
