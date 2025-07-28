"""Rule definition for ～から見ると/から見れば/から見て"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～から見ると/から見れば/から見て grammar rule"""
    return GrammarRule(
        name="～から見ると/から見れば/から見て",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="から"),
                    TokenPattern(
                        value="見る",
                        alternatives=[
                            TokenPattern(value="見れ"),
                            TokenPattern(value="見"),
                        ],
                    ),
                    TokenPattern(
                        value="と",
                        alternatives=[
                            TokenPattern(value="ば"),
                            TokenPattern(value="て"),
                        ],
                    ),
                ]
            ),
        ],
        description="名詞＋から見ると/から見れば/から見て",
        category="N3",
        index=20,
        examples=[
            "平凡なわたしから見ると、彼女はあらゆる才能に恵まれているように思える。",
            "外国人のわたしから見れば、日本は住みよい国だと思う。",
            "彼の症状から見て、食中毒の可能性が高い。",
        ],
    )
