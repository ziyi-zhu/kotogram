"""Rule definition for ～せいで/せいだ/せいか"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～せいで/せいだ/せいか grammar rule"""
    return GrammarRule(
        name="～せいで/せいだ/せいか",
        patterns=[
            # Pattern for verb plain form + せい + で/だ/か
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="せい"),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="で"),
                            TokenPattern(value="だ"),
                            TokenPattern(value="か"),
                        ],
                    ),
                ]
            ),
            # Pattern for na-adjective stem + な + せい + で/だ/か
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA,
                    TokenPattern(value="せい"),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="で"),
                            TokenPattern(value="だ"),
                            TokenPattern(value="か"),
                        ],
                    ),
                ]
            ),
            # Pattern for noun + の + せい + で/だ/か
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="の"),
                    TokenPattern(value="せい"),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="で"),
                            TokenPattern(value="だ"),
                            TokenPattern(value="か"),
                        ],
                    ),
                ]
            ),
        ],
        description="動詞普通形＋せいで/せいだ/せいか\nい形容詞普通形＋せいで/せいだ/せいか\nな形容詞語幹＋な＋せいで/せいだ/せいか\n名詞＋の＋せいで/せいだ/せいか",
        category="N3",
        index=40,
        examples=[
            "今年は気温が高いせいか、冬になってもなかなか雪が降らない。",
            "原料が安いせいか、この製品は値段が安い。",
            "夜眠れないのは騒音のせいだ。",
        ],
    )
