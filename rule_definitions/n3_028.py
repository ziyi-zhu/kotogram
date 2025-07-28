"""Rule definition for ～ことに"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～ことに grammar rule"""
    return GrammarRule(
        name="～ことに",
        patterns=[
            # Pattern for verb た-form + ことに
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(value="た"),
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                ]
            ),
            # Pattern for i-adjective dictionary form + ことに
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.ADJECTIVE),
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                ]
            ),
            # Pattern for na-adjective stem + な + ことに
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA,
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                ]
            ),
        ],
        description="動詞「た形」＋ことに\nい形容詞辞書形＋ことに\nな形容詞語幹＋な＋ことに",
        category="N3",
        index=28,
        examples=[
            "興味深いことに、昔のおもちゃが再び流行しているそうだ。",
            "困ったことに、相手の名前がどうしても思い出せなかった。",
            "不思議なことに、会社をやめたら、よく眠れるようになった。",
        ],
    )
