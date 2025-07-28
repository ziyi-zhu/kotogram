"""Rule definition for ～らしい"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech, POSDetailType


def create_rule() -> GrammarRule:
    """Create the ～らしい grammar rule"""
    return GrammarRule(
        name="～らしい",
        patterns=[
            # Usage 1: Inference/Judgment - Verb plain form + らしい
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="らしい"),
                ]
            ),
            # Usage 1: Inference/Judgment - Na-adjective stem + らしい
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
                    TokenPattern(value="らしい"),
                ]
            ),
            # Usage 1: Inference/Judgment - Noun + らしい
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="らしい"),
                ]
            ),
            # Usage 1: Inference/Judgment - Ta-form + らしい
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_TA,
                    TokenPattern(value="らしい"),
                ]
            ),
            # Usage 2: Resembling/Authentic - Noun + らしい
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="らしい"),
                ]
            ),
        ],
        description="動詞普通形＋らしい\nい形容詞普通形＋らしい\nな形容詞語幹＋らしい\n名詞＋らしい\n各詞類「た形」＋らしい",
        category="N4",
        index=6,
        examples=[
            # Usage 1: Inference/Judgment examples
            "二人は来年結婚するらしいです。",
            "明日はいい天気らしい。",
            "この家には誰もいないらしく、いつ行っても静かだ。",
            # Usage 2: Resembling/Authentic examples
            "学生らしくもっと勉強しなさい。",
            "日本語らしい日本語を身につけたい。",
            "今日は涼しくて、秋らしい天気です。",
        ],
    )
