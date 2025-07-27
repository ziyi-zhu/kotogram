#!/usr/bin/env python3
"""Script to generate and save default grammar rules to files"""

import json
from pathlib import Path

from kotogram.grammar import GrammarRule, GrammarRulePattern, RuleRegistry, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech


def create_default_rules() -> RuleRegistry:
    """Create default grammar rules for Japanese patterns"""
    registry = RuleRegistry()

    registry.add_rule(
        GrammarRule(
            name="～間（に）",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                        TokenPattern(value="間"),
                        TokenPattern(value="に", optional=True),
                    ]
                ),
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.NA_ADJ_STEM_NA,
                        TokenPattern(value="間"),
                        TokenPattern(value="に", optional=True),
                    ]
                ),
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.NOUN_NO,
                        TokenPattern(value="間"),
                        TokenPattern(value="に", optional=True),
                    ]
                ),
            ],
            description="動詞普通形/い形容詞普通形＋間（に）\nな形容詞語幹＋な＋間（に）\n名詞＋の＋間（に）",
            category="N3",
            index=1,
            examples=[
                "赤ちゃんが寝ている間に、洗濯をしました。",
                "日本に留学している間に富士山に登りたい。",
                "この機械は新しい間、使い方が難しい。",
                "山田先生の講演の間、皆熱心に話を聞いていた。",
                "私は夏休みの間、ずっと実家にいました。",
                "便利な間にやっておきましょう。",
                "静かな間に勉強を終わらせたい。",
            ],
        )
    )

    registry.add_rule(
        GrammarRule(
            name="～あがる",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.VERB_MASU,
                        TokenPattern(
                            value="あがる",
                            alternatives=[
                                TokenPattern(value="上がる"),
                            ],
                        ),
                    ]
                ),
            ],
            description="動詞「ます形」＋あがる",
            category="N3",
            index=3,
            examples=[
                "最新の企画書が出来あがったので、どうぞご覧ください。",
                "彼氏へのマフラーが編みあがった。",
            ],
        )
    )

    registry.add_rule(
        GrammarRule(
            name="～いい/よい",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.VERB_MASU,
                        TokenPattern(
                            value="いい",
                            alternatives=[
                                TokenPattern(value="よい"),
                            ],
                        ),
                    ]
                ),
            ],
            description="動詞「ます形」＋いい/よい",
            category="N3",
            index=4,
            examples=[
                "この町は住みよいです。",
                "この薬は飲みいいです。",
                "この本はわかりよいです。",
            ],
        )
    )

    registry.add_rule(
        GrammarRule(
            name="～一方（で）",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                        TokenPattern(value="一方"),
                        TokenPattern(value="で", optional=True),
                    ]
                ),
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.NA_ADJ_STEM_NA_OR_DEARU,
                        TokenPattern(value="一方"),
                        TokenPattern(value="で", optional=True),
                    ]
                ),
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.NOUN_NO_OR_DEARU,
                        TokenPattern(value="一方"),
                        TokenPattern(value="で", optional=True),
                    ]
                ),
            ],
            description="動詞普通形/い形容詞辞書形＋一方（で）\nな形容詞語幹＋な/である＋一方（で）\n名詞＋である＋一方（で）",
            category="N3",
            index=5,
            examples=[
                "彼は自分は何もしていない一方で、他人のすることによく文句を言う。",
                "田中さんは医科大学の教授である一方、小説家としても有名だ。",
                "娘ならきっと合格できるだろうと信じる一方で、ちょっと不安なところもある。",
                "この機械は新しい一方で、使い方が難しい。",
                "収入が減る一方で、教育費などの支出は増えていくのだから、節約するしかない。",
                "姉は明るい一方で、妹は無口だ。",
                "彼は真面目な一方で、冗談もよく言う。",
                "この部屋は静かな一方で、少し暗いです。",
                "彼女は有名である一方、謙虚な人です。",
                "田中さんは医科大学の教授である一方、小説家としても有名だ。",
                "この制度は学生のための一方、教員にもメリットがある。",
            ],
        )
    )

    registry.add_rule(
        GrammarRule(
            name="～一方だ",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.VERB_BASIC,
                        TokenPattern(value="一方"),
                        TokenPattern(value="だ"),
                    ]
                ),
            ],
            description="動詞辞書形＋一方だ",
            category="N3",
            index=6,
            examples=[
                "ここ数年、この町の人口は減る一方だ。",
                "わが社の業績はよくなる一方だ。",
            ],
        )
    )

    registry.add_rule(
        GrammarRule(
            name="～上で（の）",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.VERB_TA,
                        TokenPattern(value="上"),
                        TokenPattern(value="で"),
                        TokenPattern(value="の", optional=True),
                    ]
                ),
            ],
            description="動詞「た形」＋上で（の）",
            category="N3",
            index=7,
            examples=[
                "私が皆様のご意見を伺った上で、来週ご報告いたします。",
                "それぞれの説明をよく聞いた上で、旅行のコースを選びたいと思います。",
            ],
        )
    )

    registry.add_rule(
        GrammarRule(
            name="～上に",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.VERB_OR_I_ADJ_PLAIN,
                        TokenPattern(value="上"),
                        TokenPattern(value="に"),
                    ]
                ),
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.NA_ADJ_STEM_NA_OR_DEARU,
                        TokenPattern(value="上"),
                        TokenPattern(value="に"),
                    ]
                ),
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.NOUN_NO_OR_DEARU,
                        TokenPattern(value="上"),
                        TokenPattern(value="に"),
                    ]
                ),
            ],
            description="動詞普通形/い形容詞辞書形＋上に\nな形容詞語幹＋な/である＋上に\n名詞＋の/である＋上に",
            category="N3",
            index=9,
            examples=[
                "そのスポーツクラブは入会金が要らない上に、わが家から近い。",
                "台風が近づいてきて、風が強い上に、雨も激しく降っている。",
                "この商品はデザインがユニークな上に、色もカラフルだ。",
                "彼は学生の上に、アルバイトもしている。",
            ],
        )
    )

    registry.add_rule(
        GrammarRule(
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
    )

    registry.add_rule(
        GrammarRule(
            name="～おきに",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        *CommonPatterns.QUANTIFIER,
                        TokenPattern(value="おき"),
                        TokenPattern(value="に"),
                    ]
                ),
            ],
            description="数量詞＋おきに",
            category="N3",
            index=12,
            examples=[
                "この道には5メートルおきに木が植えてある。",
                "新宿へ向かう電車は3分おきに出ている。",
            ],
        )
    )

    registry.add_rule(
        GrammarRule(
            name="～から～にかけて",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                        TokenPattern(value="から"),
                        TokenPattern(),
                        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                        TokenPattern(value="にかけて"),
                    ]
                ),
            ],
            description="名詞＋から＋名詞＋にかけて",
            category="N3",
            index=19,
            examples=[
                "あの鳥が日本で見られるのは、11月から3月にかけてです。",
                "東北地方から北海道にかけて今夜は大雪になるでしょう。",
            ],
        )
    )

    registry.add_rule(
        GrammarRule(
            name="～くらい／ぐらい",
            patterns=[
                GrammarRulePattern(
                    patterns=[
                        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
                        TokenPattern(
                            value="ぐらい",
                            alternatives=[
                                TokenPattern(value="くらい"),
                            ],
                        ),
                        TokenPattern(),
                        TokenPattern(value="は"),
                        TokenPattern(value="い", optional=True),
                        TokenPattern(value="ない"),
                    ]
                ),
            ],
            description="～ぐらい～はない",
            category="N3",
            index=23,
            examples=[
                "戦争ぐらい残酷なものはない。",
                "彼くらい努力する人はいない。",
            ],
        )
    )

    return registry


def save_rules_to_files():
    """Generate default rules and save each to a separate file"""
    # Create rules directory
    rules_dir = Path("rules")
    rules_dir.mkdir(exist_ok=True)

    # Generate default rules
    registry = create_default_rules()

    print(f"Generating {len(registry.rules)} default rules...")

    for idx, rule in enumerate(registry.rules):
        # Serialize rule
        rule_data = rule.model_dump(mode="json")

        # Use index as filename
        filename = f"{idx:03d}.json"
        filepath = rules_dir / filename

        # Save to file
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(rule_data, f, ensure_ascii=False, indent=2)

        print(f"  Saved: {filepath}")

    print(f"\nAll rules saved to {rules_dir}/ directory")


if __name__ == "__main__":
    save_rules_to_files()
