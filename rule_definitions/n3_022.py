"""Rule definition for ～くせに"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import InflectionForm, PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～くせに grammar rule"""
    return GrammarRule(
        name="～くせに",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="くせ"),
                    TokenPattern(value="に"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        part_of_speech=PartOfSpeech.ADJECTIVE,
                        infl_form=InflectionForm.BASIC,
                    ),
                    TokenPattern(value="くせ"),
                    TokenPattern(value="に"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA,
                    TokenPattern(value="くせ"),
                    TokenPattern(value="に"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NOUN_NO,
                    TokenPattern(value="くせ"),
                    TokenPattern(value="に"),
                ]
            ),
        ],
        description="動詞辞書形＋くせに\nい形容詞辞書形＋くせに\nな形容詞語幹＋な＋くせに\n名詞＋の＋くせに",
        category="N3",
        index=22,
        examples=[
            "姉は食事のことで文句ばかり言っているくせに、自分では何も作らない。",
            "子どものくせに、生意気だね。",
        ],
    )
