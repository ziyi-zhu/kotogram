"""Rule definition for ～さえ"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～さえ grammar rule"""
    return GrammarRule(
        name="～さえ",
        patterns=[
            # Pattern for noun + さえ
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="さえ"),
                ]
            ),
            # Pattern for particle + さえ
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.PARTICLE),
                    TokenPattern(value="さえ"),
                ]
            ),
            # Pattern for person noun + で + さえ
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="で"),
                    TokenPattern(value="さえ"),
                ]
            ),
        ],
        description="名詞/助詞＋さえ\n人物名詞（＋で）＋さえ",
        category="N3",
        index=34,
        examples=[
            "最初は怖くてプールに入ることさえできなかったが、今では50メートルも泳げるようになった。",
            "中学生の君にその問題が解けたとはすごいことだ。あれは大学生にさえ難しいと言われている。",
            "日本人でさえ、敬語を間違える場合がある。",
        ],
    )
