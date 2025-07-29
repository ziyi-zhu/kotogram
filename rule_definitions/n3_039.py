"""Rule definition for ～(は)する/(も)する"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～(は)する/(も)する grammar rule"""
    return GrammarRule(
        name="～(は)する/(も)する",
        patterns=[
            # Pattern for noun + は/も + する
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(
                        value="",
                        alternatives=[
                            TokenPattern(value="は"),
                            TokenPattern(value="も"),
                        ],
                    ),
                    TokenPattern(value="する"),
                ]
            ),
        ],
        description="名詞＋(は)する/(も)する",
        category="N3",
        index=39,
        examples=[
            "そのホテルは一泊10万円もするそうだ。",
            "入社して半年もしないうちに仕事をやめた。",
            "飛行機で行くなら3時間はするでしょう。",
        ],
    )
