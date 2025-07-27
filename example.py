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
        matches = registry.match_all(tokens)

        if matches:
            print("🎯 Grammar patterns found:")
            for match in matches:
                matched_text = " ".join([t.surface for t in match.matched_tokens])
                print(
                    f"   • {match.rule_name}: '{matched_text}' "
                    f"(pos {match.start_pos}-{match.end_pos})"
                )
                if match.description:
                    print(f"     Description: {match.description}")
        else:
            print("❌ No grammar patterns matched")

        print()


if __name__ == "__main__":
    main()
