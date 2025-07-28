# Rule Definitions

This directory contains individual Python files for each grammar rule. Each file defines a single grammar rule and makes it easy to add, modify, or remove rules.

## File Structure

- Each rule is defined in its own Python file
- Files are named with the pattern: `{category}_{index}.py` (e.g., `n3_001.py`)
- Each file must contain a `create_rule()` function that returns a `GrammarRule` object
- The filename must match the rule's category and index (e.g., `n3_001.py` for a rule with category="N3" and index=1)

## Adding a New Rule

To add a new rule:

1. Create a new Python file in this directory with the naming convention `{category}_{index}.py`
2. Import the necessary classes:
   ```python
   from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
   from kotogram.patterns import CommonPatterns
   from kotogram.types import PartOfSpeech  # if needed
   ```

3. Define a `create_rule()` function that returns a `GrammarRule`:
   ```python
   def create_rule() -> GrammarRule:
       return GrammarRule(
           name="～ながら",
           patterns=[
               GrammarRulePattern(
                   patterns=[
                       *CommonPatterns.VERB_MASU,
                       TokenPattern(value="ながら"),
                   ]
               ),
           ],
           description="動詞「ます形」＋ながら",
           category="N3",
           index=24,
           examples=[
               "音楽を聞きながら、勉強します。",
               "テレビを見ながら、食事をします。",
           ],
       )
   ```

4. Run `python generate_rules.py` to regenerate the JSON files

## File Naming Convention

- `n3_001.py` - N3 category, rule index 1
- `n3_003.py` - N3 category, rule index 3
- `n3_004.py` - N3 category, rule index 4
- `n4_001.py` - N4 category, rule index 1 (for future use)
- etc.

**Important**: The filename must exactly match the rule's category and index values.

## Benefits

- **Easy to add new rules**: Just create a new file with the correct naming convention
- **Easy to modify rules**: Edit individual files without affecting others
- **Easy to remove rules**: Simply delete the file
- **Version control friendly**: Each rule change is a separate commit
- **Collaborative development**: Multiple people can work on different rules simultaneously
- **Clear organization**: Each rule is self-contained and documented

## Running the Generator

To generate JSON files from all rule definitions:

```bash
python generate_rules.py
```

This will:
1. Scan all rule definition files in this directory
2. Load each rule using the `create_rule()` function
3. Save all rules as JSON files in the `rules/` directory
4. Display progress and any errors

## Example Rule File

See `n3_001.py` for a complete example of how to define a new rule.
