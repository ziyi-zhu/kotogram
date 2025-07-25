#!/usr/bin/env python3
"""Example usage of Kotogram Japanese morphological analysis package"""

from kotogram import JanomeAnalyzer


def main():
    """Main example function"""
    # Initialize Janome analyzer
    analyzer = JanomeAnalyzer()

    # Test text
    text = "最新の企画書が出来あがったので、どうぞご覧ください。"

    # Analyze text
    tokens = analyzer.analyze_text(text)

    # Display results
    analyzer.print_tokens(tokens)


if __name__ == "__main__":
    main()
