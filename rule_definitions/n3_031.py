"""Rule definition for ～ことになる"""

from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_rule() -> GrammarRule:
    """Create the ～ことになる grammar rule"""
    return GrammarRule(
        name="～ことになる",
        patterns=[
            # Pattern for verb dictionary form + ことになる (Usage 1: decision by others)
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(value="なる"),
                ]
            ),
            # Pattern for verb nai-form + ことになる (Usage 1: decision by others)
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_NAI,
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(value="なる"),
                ]
            ),
            # Pattern for verb plain form + (という)ことになる (Usage 2: "in other words")
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(value="なる"),
                ]
            ),
            # Pattern for noun + ということになる (Usage 2: "in other words")
            GrammarRulePattern(
                patterns=[
                    TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                    TokenPattern(value="という"),
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(value="なる"),
                ]
            ),
            # Pattern for verb + ということになる (Usage 2: "in other words")
            GrammarRulePattern(
                patterns=[
                    *CommonPatterns.VERB_BASIC,
                    TokenPattern(value="という"),
                    TokenPattern(value="こと"),
                    TokenPattern(value="に"),
                    TokenPattern(value="なる"),
                ]
            ),
        ],
        description="動詞辞書形＋ことになる\n動詞「ない形」＋ことになる\n動詞普通形＋ことになる\n名詞＋ということになる\n動詞＋ということになる",
        category="N3",
        index=31,
        examples=[
            "新しい支店を開くことになった。",
            "来月から授業は8時から始まることになりました。",
            "家賃は一か月5万円だから、1年で60万円も払うことになる。",
            "彼女はおじの娘だから、わたしと彼女はいとこ同士ということになる。",
            "毎日8時間働くんだから、一週間40時間働くということになるね。",
        ],
    )
