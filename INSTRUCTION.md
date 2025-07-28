You will be implementing Japanese grammar rules by analyzing images that contain rule definitions. Each rule must be implemented as a separate Python file following the established patterns and conventions.

## Step-by-Step Process

### 1. Image Analysis
- Carefully examine the provided image(s) for grammar rule information
- Extract the following for each rule:
  - **Category** (N3)
  - **Index** (numerical identifier)
  - **Rule name** (the grammar pattern name, usually in Japanese)
  - **Pattern description** (how the grammar is formed)
  - **All examples** provided in the image
  - **Usage notes** or **meaning** if provided

### 2. File Creation
For each rule, create a new Python file:
- **Filename format**: `{category}_{index:03d}.py` (e.g., `n3_001.py`, `n3_024.py`)
- **Location**: Place in the `rule_definitions/` directory
- **Structure**: Follow the template below

### 3. Rule Implementation Template
```python
from kotogram.grammar import GrammarRule, GrammarRulePattern, TokenPattern
from kotogram.patterns import CommonPatterns
from kotogram.types import PartOfSpeech

def create_rule() -> GrammarRule:
    return GrammarRule(
        name="[Rule name from image]",
        patterns=[
            GrammarRulePattern(
                patterns=[
                    # Use CommonPatterns when possible
                    # Make patterns flexible with optional=True, alternatives=[...]
                    # Example patterns:
                    *CommonPatterns.VERB_MASU,  # For ます形
                    TokenPattern(value="ながら"),
                    # Add more patterns as needed
                ]
            ),
        ],
        description="[Pattern description from image. Include ALL patterns for this rule, separated by \\n]",
        category="[Category from image]",
        index=[Index from image],
        examples=[
            # ALL examples from the image
            "[Example 1]",
            "[Example 2]",
            # Add at least one example for patterns missing examples
        ],
    )
```

### 4. Pattern Design Guidelines

#### Before Starting
- Look at 5 example rules in the `rule_definitions/` directory and patterns in `kotogram/patterns.py` to understand the established patterns and conventions

#### ⚠️ CRITICAL: Avoid Overly Broad Patterns
**NEVER create patterns that are too general and could match everything.** This is a common mistake that leads to false positives.

**❌ WRONG - These patterns are too broad:**
```python
TokenPattern(
    part_of_speech=PartOfSpeech.VERB,
    infl_form=InflectionForm.INFLECTED,
)
TokenPattern(
    part_of_speech=PartOfSpeech.VERB,
    infl_form=InflectionForm.BASIC,
)
TokenPattern(part_of_speech=PartOfSpeech.NOUN)
```

**Key Principle:** Patterns should be specific enough to only match the actual grammar forms you're trying to identify, not every possible instance of that part of speech or inflection form.

#### Rule Combination Guidelines
When a grammar rule has multiple meanings or usage patterns (e.g., hearsay vs. appearance for ~そうだ), combine them into a single comprehensive rule:
- **Combine all patterns** from different meanings into one rule
- **List all patterns** in the description field without differentiating meanings
- **Include all examples** from all meanings in the examples list
- **No need to mention or differentiate** different meanings in the description or code comments
- **Use a single file** with all patterns rather than creating separate rules

Example: For ~そうだ which has both hearsay (伝聞) and appearance (様態) meanings, combine all patterns into one rule with all examples.

#### Use CommonPatterns When Available
Available CommonPatterns for reference:

**Verb Patterns:**
- `CommonPatterns.VERB_MASU` - 動詞「ます形」
- `CommonPatterns.VERB_BASIC` - 動詞辞書形
- `CommonPatterns.VERB_TA` - 動詞 + た
- `CommonPatterns.VERB_NAI` - 動詞 + ない
- `CommonPatterns.VERB_OR_I_ADJ_PLAIN` - 動詞普通形/い形容詞普通形

**Adjective Patterns:**
- `CommonPatterns.NA_ADJ_STEM_NA` - な形容詞語幹 + な
- `CommonPatterns.NA_ADJ_STEM_NA_OR_DEARU` - な形容詞語幹 + な/である

**Noun Patterns:**
- `CommonPatterns.NOUN_NO` - 名詞 + の
- `CommonPatterns.NOUN_NO_OR_DEARU` - 名詞 + の/である
- `CommonPatterns.QUANTIFIER` - 数量詞

**Description Format:**
Always include ALL patterns for the rule in the description field, separated by `\n`. For example:
```
description="動詞普通形/い形容詞普通形＋間（に）\nな形容詞語幹＋な＋間（に）\n名詞＋の＋間（に）"
```

Check existing CommonPatterns before creating new patterns. Add new pattern if it does not exist.

#### Pattern Matching Guidelines

**TokenPattern Usage:**
When a `value` is specified for a TokenPattern, no need to add other information like `part_of_speech` or `pos_detail`. The value alone is sufficient for matching.

**For Explicit Patterns:**
When you see patterns like `～から～にかけて`, use:
```python
TokenPattern(value="から"),
TokenPattern(),  # Multi wildcard that matches any number of any token
TokenPattern(value="にかけて"),
```

**For Specific Forms:**
- For 動詞辞書形: Use `TokenPattern(part_of_speech=PartOfSpeech.VERB, infl_form=InflectionForm.BASIC)` or directly use `CommonPatterns.VERB_BASIC`
- For other specific forms, use the appropriate CommonPatterns or create specific TokenPatterns with the correct parameters

**For Optional Elements:**
- Use `optional=True` for things in parentheses like `(で)`
- Example: `TokenPattern(value="で", optional=True)`

#### Create New CommonPatterns When Needed
If a pattern appears commonly across rules but doesn't exist in CommonPatterns:
1. Add it to the CommonPatterns class
2. Use descriptive names (e.g., `VERB_TE_FORM`, `ADJECTIVE_STEM`)
3. Don't create patterns for single TokenPatterns like just `NOUN`

#### Make Patterns Flexible
- Use `optional=True` for optional elements
- Use `alternatives=[...]` for variations
- For です endings, consider adding な or だ as alternatives based on common usage
- Example:
```python
TokenPattern(
    value="ぐらい",
    alternatives=[
        TokenPattern(value="くらい"),
    ],
),
# ...
TokenPattern(value="は"),
TokenPattern(value="い", optional=True),
TokenPattern(value="ない"),
```

### 5. Testing Process

#### Initial Testing
Run the test for your specific rule:
```bash
# Activate virtual environment
source .venv/bin/activate

python test_rule.py [CATEGORY] [INDEX]
# Example: python test_rule.py N3 24
```

#### Verification Checklist
- [ ] **All examples match**: Every example from the image passes the test
- [ ] **Correct token matching**: Verify tokens match the intended pattern, not just individual words
- [ ] **Pattern accuracy**: Ensure the matched portion represents the actual grammar rule
- [ ] **No false positives**: The pattern shouldn't match unrelated text

#### Iteration Process
1. Run the test and examine the output carefully
2. Check which examples fail and why
3. Analyze the tokenization and matching process
4. Modify patterns to fix issues:
   - Adjust TokenPattern values
   - Add alternatives or make elements optional
   - Use different CommonPatterns if needed
5. Repeat until all examples pass

#### Handle Impossible Examples
If an example cannot pass due to parsing limitations:
- Replace it with a similar, parseable example
- Ensure the new example still demonstrates the grammar rule correctly
- Document the change in comments if necessary

### 6. Final Validation

#### Run Full Test Suite
```bash
# Generate updated rules
python generate_rules.py

# Run all tests
pytest
```

#### Ensure Everything Passes
- [ ] All existing tests still pass
- [ ] New rule tests pass
- [ ] No regressions introduced
- [ ] JSON generation successful
