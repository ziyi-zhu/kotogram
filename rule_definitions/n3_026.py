"""Rule definition for ～ことか"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～ことか grammar rule"""
    return GrammarRule(
        name="～ことか",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="こと"),
                    TokenPattern(value="か"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.NA_ADJ_STEM_NA,
                    TokenPattern(value="こと"),
                    TokenPattern(value="か"),
                ]
            ),
            # Pattern for verb + た + ことか
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(value="た"),
                    TokenPattern(value="こと"),
                    TokenPattern(value="か"),
                ]
            ),
        ],
        description="動詞普通形/い形容詞普通形＋ことか\nな形容詞語幹＋な＋ことか\n動詞＋た＋ことか",
        category="N3",
        index=26,
        examples=[
            "自分で野菜を作ってみて、おいしい野菜を育てることがどんなに大変なことかわかりました。",
            "学生時代、奨学金がもらえてどれほど助かったことか。",
            "悪い点を注意する親が多いが、子どもにとっては、褒められたほうがどれだけうれしいことか。",
        ],
    )
