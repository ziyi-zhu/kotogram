"""Rule definition for ～だけでなく"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～だけでなく grammar rule"""
    return GrammarRule(
        name="～だけでなく",
        patterns=[
            # Pattern for verb plain form + だけでなく
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
                    TokenPattern(value="なく"),
                ]
            ),
            # Pattern for na-adjective stem + な + だけでなく
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
                    TokenPattern(value="なく"),
                ]
            ),
            # Pattern for noun + の + だけでなく
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="の"),
                    TokenPattern(value="だけ"),
                    TokenPattern(
                        value="で",
                        alternatives=[
                            TokenPattern(value="じゃ"),
                        ],
                    ),
                    TokenPattern(value="なく"),
                ]
            ),
            # Pattern for noun + だけでなく (without の)
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
                    TokenPattern(value="なく"),
                ]
            ),
        ],
        description="動詞普通形 + だけでなく\nい形容詞普通形 + だけでなく\nな形容詞語幹+な + だけでなく\n名詞 + の + だけでなく\n名詞 + だけでなく",
        category="N3",
        index=43,
        examples=[
            "新しい携帯電話は、写真が撮れるだけじゃなくて、テレビだって見られるんだよ。",
            "あの工場は、設備だけでなく周りの環境もすばらしい。",
            "彼は英語が上手なだけでなく、フランス語もぺらぺらだ。",
        ],
    )
