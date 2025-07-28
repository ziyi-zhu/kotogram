You will be implementing Japanese grammar rules by analyzing images that contain rule definitions. Each rule must be implemented as a separate Python file following the established patterns and conventions.

## Step-by-Step Process

### 1. Image Analysis
- Carefully examine the provided image(s) for grammar rule information
- Extract the following for each rule:
  - **Category** (e.g., N3, N2, N1)
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
        description="[Pattern description from image]",
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

#### Use CommonPatterns When Available
- `CommonPatterns.VERB_MASU` for 動詞「ます形」
- `CommonPatterns.I_ADJECTIVE_PLAIN` for い形容詞普通形
- `CommonPatterns.NA_ADJECTIVE_STEM_NA` for な形容詞語幹＋な
- `CommonPatterns.NOUN_WO` for 名詞＋を
- Check existing CommonPatterns before creating new patterns

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
