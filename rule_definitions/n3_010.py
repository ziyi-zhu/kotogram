"""Rule definition for ～ないうちに"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～ないうちに grammar rule"""
    return GrammarRule(
        name="～ないうちに",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_NAI,
                    TokenPattern(value="うち"),
                    TokenPattern(value="に"),
                ]
            ),
        ],
        description="動詞「ない形」＋ない＋うちに",
        category="N3",
        index=10,
        examples=[
            "弟と妹がいると集中できないから、今日は二人が帰ってこないうちに、宿題をやってしまう。",
            "昨日のパーティーは、友だちと話していたら、ほとんど何も食べないうちに終わってしまって、後でおなかがすいてしまった。",
        ],
    )
