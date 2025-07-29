"""Rule definition for ～さえ～ば"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～さえ～ば grammar rule"""
    return GrammarRule(
        name="～さえ～ば",
        patterns=[
            # Pattern for verb masu-form + さえ + すれば/しなければ
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(value="さえ"),
                    TokenPattern(value="すれ"),
                    TokenPattern(value="ば"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_MASU,
                    TokenPattern(value="さえ"),
                    TokenPattern(value="しなければ"),
                ]
            ),
            # Pattern for i-adjective stem + く + さえ + あれば/なければ
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.ADJECTIVE),
                    TokenPattern(value="く"),
                    TokenPattern(value="さえ"),
                    TokenPattern(value="あれ"),
                    TokenPattern(value="ば"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.ADJECTIVE),
                    TokenPattern(value="く"),
                    TokenPattern(value="さえ"),
                    TokenPattern(value="なけれ"),
                    TokenPattern(value="ば"),
                ]
            ),
            # Pattern for na-adjective stem + で + さえ + あれば/なければ
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="で"),
                    TokenPattern(value="さえ"),
                    TokenPattern(value="あれ"),
                    TokenPattern(value="ば"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="で"),
                    TokenPattern(value="さえ"),
                    TokenPattern(value="なければ"),
                ]
            ),
            # Pattern for noun + さえ + various ba-forms
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="さえ"),
                    TokenPattern(value="よけれ"),
                    TokenPattern(value="ば"),
                ]
            ),
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="さえ"),
                    TokenPattern(value="よくなければ"),
                ]
            ),
            # Additional pattern for i-adjective + さえ + なければ (for 忙しくさえなければ)
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.ADJECTIVE),
                    TokenPattern(value="さえ"),
                    TokenPattern(value="なけれ"),
                    TokenPattern(value="ば"),
                ]
            ),
        ],
        description="動詞「ます形」＋さえ＋すれば/しなければ\nい形容詞語幹＋く＋さえ＋あれば/なければ\nな形容詞語幹＋で＋さえ＋あれば/なければ\n名詞＋さえ＋各詞類「ば形」",
        category="N3",
        index=35,
        examples=[
            "最近、自分さえよければいいという考えの人が増えている。",
            "この薬を飲みさえすれば、すぐ治るというわけではない。",
            "仕事が忙しくさえなければ、英語の勉強を続けたい。",
            "静かでさえあれば、狭くてもいい。",
        ],
    )
