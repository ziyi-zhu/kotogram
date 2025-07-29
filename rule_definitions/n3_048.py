"""Rule definition for 〜たばかりだ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the 〜たばかりだ grammar rule"""
    return GrammarRule(
        name="〜たばかりだ",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.VERB),
                    TokenPattern(value="た"),
                    TokenPattern(value="ばかり"),
                    TokenPattern(
                        value="だ",
                        alternatives=[
                            TokenPattern(value="です"),
                            TokenPattern(value="で"),
                        ],
                        optional=True,
                    ),
                ]
            ),
        ],
        description="動詞 + た + ばかり + だ/です",
        category="N3",
        index=48,
        examples=[
            "昨日、動物園に行ったら、先月生まれたばかりのライオンの赤ちゃんを見ることができました。",
            "A「遅くなってすみません。」B「いいえ、わたしも今来たばかりです。」",
            "さっき起きたばかりで、まだ眠いです。",
        ],
    )
