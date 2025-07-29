"""Rule definition for 〜たら/ったら"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the 〜たら/ったら grammar rule"""
    return GrammarRule(
        name="〜たら/ったら",
        patterns=[
            # Pattern 1: noun + たら
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="たら"),
                ]
            ),
            # Pattern 2: noun + っ + たら (for cases like 李さんったら)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="っ"),
                    TokenPattern(value="たら"),
                ]
            ),
        ],
        description="名詞 + たら/ったら",
        category="N3",
        index=51,
        examples=[
            "李さんったら、また遅刻した。",
            "この時間たら、どこも込んでるよ。",
        ],
    )
