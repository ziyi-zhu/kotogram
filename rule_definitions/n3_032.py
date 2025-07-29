"""Rule definition for ～ことはない/こともない"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns


def create_rule() -> GrammarRule:
    """Create the ～ことはない/こともない grammar rule"""
    return GrammarRule(
        name="～ことはない/こともない",
        patterns=[
            # Pattern for verb dictionary form + ことはない
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="こと"),
                    TokenPattern(value="は"),
                    TokenPattern(value="ない"),
                ]
            ),
            # Pattern for verb dictionary form + こともない
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="こと"),
                    TokenPattern(value="も"),
                    TokenPattern(value="ない"),
                ]
            ),
        ],
        description="動詞辞書形＋ことはない/こともない",
        category="N3",
        index=32,
        examples=[
            "君が一人で責任を感じることはない。そんなに悩んでいたら体を壊してしまうよ。",
            "その器具は確かに便利そうだが、なくても困らないのだから、わざわざ買うことはない。",
        ],
    )
