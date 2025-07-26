#!/usr/bin/env python3
"""Example usage of Kotogram Japanese morphological analysis package"""

from kotogram import JanomeAnalyzer


def main():
    analyzer = JanomeAnalyzer()

    examples = [
        "最新の企画書が出来あがったので、どうぞご覧ください。",
        "赤ちゃんが寝ている間に、洗濯をしました。",
        "山田先生の講演の間、皆熱心に話を聞いていた。",
    ]

    for text in examples:
        print(f"=== {text} ===")
        tokens = analyzer.analyze_text(text)
        analyzer.print_tokens(tokens)
        print(tokens)


if __name__ == "__main__":
    main()
