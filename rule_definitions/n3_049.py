"""Rule definition for 〜たび(に)"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the 〜たび(に) grammar rule"""
    return GrammarRule(
        name="〜たび(に)",
        patterns=[
            # Pattern 1: noun + の + たび(に)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="の"),
                    TokenPattern(value="たび"),
                    TokenPattern(value="に", optional=True),
                ]
            ),
            # Pattern 2: verb dictionary form + たび(に)
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="たび"),
                    TokenPattern(value="に", optional=True),
                ]
            ),
        ],
        description="名詞 + の + たび(に)\n動詞辞書形 + たび(に)",
        category="N3",
        index=49,
        examples=[
            "わたしは山田さんに会うたびに素敵な人だといつも思う。",
            "この写真を見るたび、故郷のことを思い出す。",
            "木村さんは旅行のたびに、お土産を買ってきてくれる。",
        ],
    )
