"""Rule definition for 〜だらけ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the 〜だらけ grammar rule"""
    return GrammarRule(
        name="〜だらけ",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="だらけ"),
                ]
            ),
        ],
        description="名詞 + だらけ",
        category="N3",
        index=52,
        examples=[
            "昨日からの雨がようやく止んだが、運動場はまだ濡れていた。試合を終えたサッカー選手の顔はみんな泥だらけだ。",
            "この部屋は何年も住んでいないので、埃だらけだ。",
        ],
    )
