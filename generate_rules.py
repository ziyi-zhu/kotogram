#!/usr/bin/env python3
"""Script to generate and save default grammar rules to files"""

import json
from pathlib import Path

from kotogram.grammar import GrammarRule, RuleRegistry, TokenPattern
from kotogram.types import PartOfSpeech


def create_default_rules() -> RuleRegistry:
    """Create default grammar rules for Japanese patterns"""
    registry = RuleRegistry()

    patterns_noun_no_aida = [
        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
        TokenPattern(value="の"),
        TokenPattern(value="間"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～間",
            patterns=patterns_noun_no_aida,
            description="名詞＋の＋間",
            tag="N3-1",
        )
    )

    patterns_verb_basic_maida = [
        TokenPattern(part_of_speech=PartOfSpeech.VERB),
        TokenPattern(value="間"),
        TokenPattern(value="に"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～間に",
            patterns=patterns_verb_basic_maida,
            description="動詞普通形＋間に",
            tag="N3-2",
        )
    )

    patterns_verb_masu_agaru = [
        TokenPattern(part_of_speech=PartOfSpeech.VERB),
        TokenPattern(value="あがる"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～あがる",
            patterns=patterns_verb_masu_agaru,
            description="動詞「ます形」＋あがる",
            tag="N3-3",
        )
    )

    patterns_noun_de_aru_ippou = [
        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
        TokenPattern(value="で"),
        TokenPattern(value="ある"),
        TokenPattern(value="一方"),
        TokenPattern(value="で", optional=True),
    ]
    registry.add_rule(
        GrammarRule(
            name="～一方（で）",
            patterns=patterns_noun_de_aru_ippou,
            description="名詞＋である＋一方（で）",
            tag="N3-5",
        )
    )

    patterns_noun_verb_ta_uede = [
        TokenPattern(part_of_speech=PartOfSpeech.VERB),
        TokenPattern(value="た"),
        TokenPattern(value="上"),
        TokenPattern(value="で"),
        TokenPattern(value="の", optional=True),
    ]
    registry.add_rule(
        GrammarRule(
            name="～上で（の）",
            patterns=patterns_noun_verb_ta_uede,
            description="名詞＋動詞「た形」＋上で（の）",
            tag="N3-7",
        )
    )

    patterns_verb_negative_uchini = [
        TokenPattern(part_of_speech=PartOfSpeech.VERB),
        TokenPattern(value="ない"),
        TokenPattern(value="うち"),
        TokenPattern(value="に"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～ないうちに",
            patterns=patterns_verb_negative_uchini,
            description="動詞「ない形」＋ない＋うちに",
            tag="N3-10",
        )
    )

    patterns_numeral_okini = [
        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
        TokenPattern(value="おき"),
        TokenPattern(value="に"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～おきに",
            patterns=patterns_numeral_okini,
            description="数量詞＋おきに",
            tag="N3-12",
        )
    )

    patterns_noun_kara_noun_nikakete = [
        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
        TokenPattern(value="から"),
        TokenPattern(),  # Multi-wildcard (all fields None)
        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
        TokenPattern(value="にかけて"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～から～にかけて",
            patterns=patterns_noun_kara_noun_nikakete,
            description="名詞＋から＋名詞＋にかけて",
            tag="N3-19",
        )
    )

    patterns_gurai_wa_nai = [
        TokenPattern(part_of_speech=PartOfSpeech.NOUN),
        TokenPattern(
            alternatives=[
                TokenPattern(value="ぐらい"),
                TokenPattern(value="くらい"),
            ]
        ),
        TokenPattern(),  # Multi-wildcard (all fields None)
        TokenPattern(value="は"),
        TokenPattern(value="い", optional=True),
        TokenPattern(value="ない"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～くらい／ぐらい",
            patterns=patterns_gurai_wa_nai,
            description="～ぐらい～はない",
            tag="N3-23",
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
