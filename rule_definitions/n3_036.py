"""Rule definition for ～じゃん/じゃない/じゃないの/じゃないか"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～じゃん/じゃない/じゃないの/じゃないか grammar rule"""
    return GrammarRule(
        name="～じゃん/じゃない/じゃないの/じゃないか",
        patterns=[
            # Pattern 1: Verb plain form + ん + じゃん/じゃない/じゃないの/じゃないか
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="ん"),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="じゃん"),
                            TokenPattern(value="じゃ"),
                            TokenPattern(value="ない"),
                        ],
                    ),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="ん"),
                    TokenPattern(value="じゃ"),
                    TokenPattern(value="ない"),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="の"),
                            TokenPattern(value="か"),
                        ],
                    ),
                ]
            ),
            # Pattern 2: Na-adjective stem + なん + じゃん/じゃない/じゃないの/じゃないか
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="なん"),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="じゃん"),
                            TokenPattern(value="じゃ"),
                            TokenPattern(value="ない"),
                        ],
                    ),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="なん"),
                    TokenPattern(value="じゃ"),
                    TokenPattern(value="ない"),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="の"),
                            TokenPattern(value="か"),
                        ],
                    ),
                ]
            ),
            # Pattern 3: Noun + じゃない/じゃないの/じゃないか (for discovery/surprise)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="じゃ"),
                    TokenPattern(value="ない"),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="の"),
                            TokenPattern(value="か"),
                        ],
                    ),
                ]
            ),
            # Pattern 4: Verb volitional form + じゃないか (for suggestion/invitation)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="う"),
                            TokenPattern(value="よう"),
                        ],
                    ),
                    TokenPattern(value="じゃ"),
                    TokenPattern(value="ない"),
                    TokenPattern(value="か"),
                ]
            ),
            # Additional pattern for verb + た + じゃん (for できたじゃん)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(value="た"),
                    TokenPattern(value="じゃん"),
                ]
            ),
        ],
        description="動詞普通形(+ん)＋じゃん/じゃない/じゃないの/じゃないか\nな形容詞語幹(+なん)＋じゃん/じゃない/じゃないの/じゃないか\nい形容詞普通形(+ん)＋じゃん/じゃない/じゃないの/じゃないか\n名詞＋じゃない/じゃないの/じゃないか\n動詞意志形＋じゃないか",
        category="N3",
        index=36,
        examples=[
            "ねえ、ほら、できたじゃん。",
            "これでいいんじゃないの。",
            "本当は彼のことが好きなんじゃないの。だったら直接言えばいいじゃん。",
            "あれ、田中君じゃないか。",
            "そんなこと言い出すなんて、あいつ、ばかじゃないか。",
            "今度また一緒に遊ぼうじゃないか。",
            "皆で一緒に頑張ろうじゃないか。",
        ],
    )
