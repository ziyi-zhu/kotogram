"""Rule definition for ～か何か"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～か何か grammar rule"""
    return GrammarRule(
        name="～か何か",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="か"),
                    TokenPattern(value="何"),
                    TokenPattern(value="か"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="か"),
                    TokenPattern(value="何"),
                    TokenPattern(value="か"),
                ]
            ),
        ],
        description="動詞普通形＋か何か\n名詞＋か何か",
        category="N3",
        index=16,
        examples=[
            "風で紙が飛んでしまうので、本か何か重いものを載せておこう。",
            "コーヒーか何か飲みませんか。",
        ],
    )
