#!/usr/bin/env python3
"""Example usage of Kotogram Japanese morphological analysis package"""

from kotogram import KotogramAnalyzer, create_default_rules


def main():
    analyzer = KotogramAnalyzer()
    registry = create_default_rules()

    examples = [
        "最新の企画書が出来あがったので、どうぞご覧ください。",
        "赤ちゃんが寝ている間に、洗濯をしました。",
        "山田先生の講演の間、皆熱心に話を聞いていた。",
        "田中さんは医科大学の教授である一方、小説家としても有名だ。",
        "戦争ぐらい残酷なものはない。",
        "この問題は、十分に検討した上での結論です。",
        "それぞれの説明をよく聞いた上で、旅行のコースを選びたいと思います。",
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
