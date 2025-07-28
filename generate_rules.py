#!/usr/bin/env python3
"""Script to generate and save grammar rules to files"""

import importlib
import json
import pkgutil
from pathlib import Path

from kotogram.grammar import RuleRegistry


def load_rules_from_files() -> RuleRegistry:
    """Load all grammar rules from individual rule definition files"""
    registry = RuleRegistry()

    # Import the rule_definitions package
    import rule_definitions

    # Get all modules in the rule_definitions package
    rule_modules = []
    for _, module_name, is_pkg in pkgutil.iter_modules(rule_definitions.__path__):
        if not is_pkg and (
            module_name.startswith("n3_") or module_name.startswith("n4_")
        ):
            rule_modules.append(module_name)

    # Sort modules to ensure consistent loading order
    rule_modules.sort()

    print(f"Found {len(rule_modules)} rule definition files:")

    for module_name in rule_modules:
        try:
            # Import the module
            module = importlib.import_module(f"rule_definitions.{module_name}")

            # Call the create_rule function
            if hasattr(module, "create_rule"):
                rule = module.create_rule()
                registry.add_rule(rule)
                print(f"  Loaded: {module_name} -> {rule.name}")
            else:
                print(f"  Warning: {module_name} does not have create_rule function")

        except Exception as e:
            print(f"  Error loading {module_name}: {e}")

    return registry


def save_rules_to_files():
    """Load all rules from definition files and save each to a separate JSON file"""
    # Create rules directory
    rules_dir = Path("rules")
    rules_dir.mkdir(exist_ok=True)

    # Load rules from definition files
    registry = load_rules_from_files()

    print(f"\nGenerating {len(registry.rules)} rules...")

    for rule in registry.rules:
        # Serialize rule
        rule_data = rule.model_dump(mode="json")

        # Use category_index as filename
        category = rule.category or "unknown"
        filename = f"{category.lower()}_{rule.index:03d}.json"
        filepath = rules_dir / filename

        # Save to file
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(rule_data, f, ensure_ascii=False, indent=2)

        print(f"  Saved: {filepath}")

    print(f"\nAll rules saved to {rules_dir}/ directory")


if __name__ == "__main__":
    save_rules_to_files()
