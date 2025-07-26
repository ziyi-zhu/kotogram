#!/usr/bin/env python3
"""Example usage of Kotogram Japanese morphological analysis package"""

from kotogram import KotogramAnalyzer, RuleRegistry


def main():
    analyzer = KotogramAnalyzer()
    registry = RuleRegistry()
    registry.load_rules_from_directory("rules")

    examples = [
        "最新の企画書が出来あがったので、どうぞご覧ください。",
        "赤ちゃんが寝ている間に、洗濯をしました。",
        "山田先生の講演の間、皆熱心に話を聞いていた。",
        "田中さんは医科大学の教授である一方、小説家としても有名だ。",
        "それぞれの説明をよく聞いた上で、旅行のコースを選びたいと思います。",
        "戦争ぐらい残酷なものはない。この問題は、十分に検討した上での結論です。",
        "新宿へ向かう電車は3分おきに出ている。",
        "あの鳥が日本で見られるのは、11月から3月にかけてです。",
        "東北地方から北海道にかけて今夜は大雪になるでしょう。",
        "この道には5メートルおきに木が植えてある。",
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
