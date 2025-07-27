#!/usr/bin/env python3
"""Example usage of Kotogram Japanese morphological analysis package"""

from kotogram import KotogramAnalyzer, RuleRegistry


def main():
    analyzer = KotogramAnalyzer()
    registry = RuleRegistry()
    registry.load_rules_from_directory("rules")

    examples = [
        "最新の企画書が出来あがったので、どうぞご覧ください。",
        "彼は自分は何もしていない一方で、他人のすることによく文句を言う。",
        "この町は住みよいです。",
        "山田先生の講演の間、皆熱心に話を聞いていた。私は夏休みの間、ずっと実家にいました。",
        "ここ数年、この町の人口は減る一方だ。私が皆様のご意見を伺った上で、来週ご報告いたします。",
    ]

    print("=== Japanese Grammar Pattern Matching Demo ===\n")

    for text in examples:
        print(f"📝 Sentence: {text}")

        # Analyze the sentence
        tokens = analyzer.parse_text(text)

        # Print tokens
        print("🔎 Tokens:")
        analyzer.print_tokens(tokens)

        # Find grammar patterns
        matches = registry.find_all_matches(tokens)

        if matches:
            print("🎯 Grammar patterns found:")
            for match_result in matches:
                print(f"   📋 Rule: {match_result.rule_name}")
                if match_result.description:
                    print(f"      Description: {match_result.description}")

                # Print each pattern match separately
                for i, pattern_match in enumerate(match_result.pattern_matches):
                    matched_text = " ".join(
                        [t.surface for t in pattern_match.matched_tokens]
                    )
                    print(
                        f"      Match {i + 1}: '{matched_text}' "
                        f"(pos {pattern_match.start_pos}-{pattern_match.end_pos})"
                    )

                    # Print individual tokens for this match
                    print(
                        f"         Tokens: {[t.surface for t in pattern_match.matched_tokens]}"
                    )
                print()
        else:
            print("❌ No grammar patterns matched")

        print()


if __name__ == "__main__":
    main()
