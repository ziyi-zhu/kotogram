"""Rule definition for 〜ず(に)"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the 〜ず(に) grammar rule"""
    return GrammarRule(
        name="〜ず(に)",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(
                        part_of_speech=PartOfSpeech.VERB,
                        alternatives=[
                            TokenPattern(
                                value="せ",
                            ),
                        ],
                    ),
                    TokenPattern(
                        value="ず",
                    ),
                    TokenPattern(
                        value="に",
                    ),
                ]
            ),
        ],
        description="動詞「ない形」＋ず(に)\n特殊：する→せず(に)",
        category="N3",
        index=24,
        examples=[
            "昨日は忙しくて、夜10時まで何も食べずに働いた。",
            "辞書を使わずに日本語の新聞を読むことができますか。",
            "勉強せずにテストを受けた。",
        ],
    )
