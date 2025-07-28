#!/usr/bin/env python3
"""Script to analyze a specific grammar rule by category and index"""

import argparse
import importlib
import sys
from typing import Optional

from kotogram import KotogramAnalyzer, RuleRegistry
from kotogram.grammar import GrammarRule


def load_specific_rule(category: str, index: int) -> Optional[GrammarRule]:
    """Load a specific rule from rule definition files"""
    # Convert category to uppercase for consistency
    category = category.upper()

    # Format the module name (e.g., "N3" -> "n3_001")
    module_name = f"{category.lower()}_{index:03d}"

    try:
        # Import the module
        module = importlib.import_module(f"rule_definitions.{module_name}")

        # Call the create_rule function
        if hasattr(module, "create_rule"):
            rule = module.create_rule()
            if isinstance(rule, GrammarRule):
                return rule
            else:
                print(
                    f"Error: {module_name}.create_rule() did not return a GrammarRule"
                )
                return None
        else:
            print(f"Error: {module_name} does not have create_rule function")
            return None

    except ImportError:
        print(f"Error: Could not import rule_definitions.{module_name}")
        return None
    except Exception as e:
        print(f"Error loading {module_name}: {e}")
        return None


def test_rule_examples(
    rule: GrammarRule, analyzer: KotogramAnalyzer, registry: RuleRegistry
):
    """Test each example for the given rule"""
    print(f"\n📋 Rule: {rule.name}")
    print(f"📝 Description: {rule.description}")

    for i, example in enumerate(rule.examples, 1):
        print(f"\nExample {i}:")

        # Parse the example into tokens
        tokens = analyzer.parse_text(example)

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
                for j, pattern_match in enumerate(match_result.pattern_matches):
                    matched_text = " ".join(
                        [t.surface for t in pattern_match.matched_tokens]
                    )
                    print(
                        f"      Match {j + 1}: '{matched_text}' "
                        f"(pos {pattern_match.start_pos}-{pattern_match.end_pos})"
                    )
        else:
            print("❌ No grammar patterns matched")


def main():
    parser = argparse.ArgumentParser(
        description="Test a specific grammar rule by category and index"
    )
    parser.add_argument("category", help="Rule category (e.g., N3, N2, N1)")
    parser.add_argument("index", type=int, help="Rule index (e.g., 1, 2, 3)")

    args = parser.parse_args()

    print(f"Category: {args.category.upper()}, Index: {args.index}")

    # Load the specific rule
    rule = load_specific_rule(args.category, args.index)
    if not rule:
        print(f"❌ Failed to load rule {args.category.upper()}_{args.index:03d}")
        sys.exit(1)

    # Initialize analyzer and registry
    analyzer = KotogramAnalyzer()
    registry = RuleRegistry()

    # Add only the specific rule to the registry
    registry.add_rule(rule)

    # Test the rule examples
    test_rule_examples(rule, analyzer, registry)


if __name__ == "__main__":
    main()
