"""Integration tests for Kotogram with real Japanese text"""

import pytest

from kotogram import KotogramAnalyzer, RuleRegistry


class TestIntegration:
    """Integration tests with real Japanese text"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up analyzer and registry"""
        self.analyzer = KotogramAnalyzer()
        self.registry = RuleRegistry()
        self.registry.load_rules_from_directory("rules")

    def test_all_rule_examples(self):
        """Test all examples for each rule"""
        for rule in self.registry.rules:
            print(f"Testing rule: {rule.name}")

            # Skip rules without examples
            if not rule.examples:
                print(f"  No examples for rule '{rule.name}', skipping")
                continue

            for example in rule.examples:
                print(f"  Testing example: {example}")
                tokens = self.analyzer.parse_text(example)
                matches = self.registry.find_all_matches(tokens)

                # Check if the rule is found in matches
                found_rules = [m.rule_name for m in matches]
                assert rule.name in found_rules, (
                    f"Expected rule '{rule.name}' not found in matches for example '{example}'. "
                    f"Found rules: {found_rules}"
                )
                print(f"    ✓ Rule '{rule.name}' matched successfully")
