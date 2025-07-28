"""Rule definition for ～こと"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～こと grammar rule"""
    return GrammarRule(
        name="～こと",
        patterns=[
            # Pattern for command/prohibition (Usage 1)
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_NAI,
                    TokenPattern(value="こと"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="こと"),
                ]
            ),
            # Pattern for exclamation/surprise (Usage 2)
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="こと"),
                ]
            ),
            # Pattern for noun + だ + こと
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="だ"),
                    TokenPattern(value="こと"),
                ]
            ),
            # Pattern for verb + た + こと
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(value="た"),
                    TokenPattern(value="こと"),
                ]
            ),
            # Pattern for polite form + こと
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(value="です"),
                    TokenPattern(value="こと"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.ADJECTIVE),
                    TokenPattern(value="です"),
                    TokenPattern(value="こと"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="です"),
                    TokenPattern(value="こと"),
                ]
            ),
        ],
        description="動詞「ない形」＋こと\n動詞辞書形＋こと\n動詞普通形/い形容詞普通形＋こと\n名詞＋だ＋こと\n動詞＋た＋こと\n動詞/い形容詞/名詞＋です＋こと",
        category="N3",
        index=25,
        examples=[
            "指定の場所以外に自転車を止めないこと。",
            "勝手に実験室に入らないこと。",
            "まあ、なんてきれいな夕焼けだこと。",
            "まあ、きれいに咲いたこと。",
            "あら、素敵な洋服ですこと。",
        ],
    )
