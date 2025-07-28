"""Rule definition for ～からすると/からすれば"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～からすると/からすれば grammar rule"""
    return GrammarRule(
        name="～からすると/からすれば",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="から"),
                    TokenPattern(
                        value="する",
                        alternatives=[
                            TokenPattern(value="すれ"),
                        ],
                    ),
                    TokenPattern(
                        value="と",
                        alternatives=[
                            TokenPattern(value="ば"),
                        ],
                    ),
                ]
            ),
        ],
        description="名詞＋からすると/からすれば",
        category="N3",
        index=18,
        examples=[
            "プロからすると、わたしの技術はまだ未熟です。",
            "あの言い方からすれば、彼はこの仕事が好きではないようだ。",
            "彼女の表情からすると、何かうれしいことがあったらしい。",
        ],
    )
