"""Rule definition for ～から言うと/から言えば/から言って"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～から言うと/から言えば/から言って grammar rule"""
    return GrammarRule(
        name="～から言うと/から言えば/から言って",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="から"),
                    TokenPattern(
                        value="言う",
                        alternatives=[
                            TokenPattern(value="言え"),
                            TokenPattern(value="言っ"),
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
        description="名詞＋から言うと/から言えば/から言って",
        category="N3",
        index=17,
        examples=[
            "記者「ところで、社員に望むことは何でしょうか。」社長「そうですね。経営者の立場から言うと、何でも率直に言ってほしいです。」",
            "今の販売状況から言えば、今年の目標達成は厳しいだろう。",
            "実務経験から言って、田中さんがこの仕事に一番ふさわしいと思う。",
        ],
    )
