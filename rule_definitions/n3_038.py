"""Rule definition for ～ずとも"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～ずとも grammar rule"""
    return GrammarRule(
        name="～ずとも",
        patterns=[
            # Pattern for verb in 未然形 + ず + とも
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(value="ず"),
                    TokenPattern(value="とも"),
                ]
            ),
        ],
        description="動詞「ない形」＋ずとも",
        category="N3",
        index=38,
        examples=[
            "嫌なら行かずともよい。",
            "この部分は書かずともよい。",
        ],
    )
