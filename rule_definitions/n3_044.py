"""Rule definition for ～だけでは"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～だけでは grammar rule"""
    return GrammarRule(
        name="～だけでは",
        patterns=[
            # Pattern for verb plain form + だけでは
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="だけ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="じゃ"),
                        ],
                    ),
                    TokenPattern(value="は"),
                ]
            ),
            # Pattern for na-adjective stem + な + だけでは
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA,
                    TokenPattern(value="だけ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="じゃ"),
                        ],
                    ),
                    TokenPattern(value="は"),
                ]
            ),
            # Pattern for noun + だけでは
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="だけ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="じゃ"),
                        ],
                    ),
                    TokenPattern(value="は"),
                ]
            ),
        ],
        description="動詞普通形 + だけでは\nい形容詞普通形 + だけでは\nな形容詞語幹+な + だけでは\n名詞 + だけでは",
        category="N3",
        index=44,
        examples=[
            "スポーツはただ見るだけではつまらない。",
            "行動せずに口先だけでは成功できない。",
        ],
    )
