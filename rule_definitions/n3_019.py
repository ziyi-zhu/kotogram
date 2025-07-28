"""Rule definition for ～から～にかけて"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～から～にかけて grammar rule"""
    return GrammarRule(
        name="～から～にかけて",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="から"),
                    TokenPattern(),
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="にかけて"),
                ]
            ),
        ],
        description="名詞＋から＋名詞＋にかけて",
        category="N3",
        index=19,
        examples=[
            "あの鳥が日本で見られるのは、11月から3月にかけてです。",
            "東北地方から北海道にかけて今夜は大雪になるでしょう。",
        ],
    )
