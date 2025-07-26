# Kotogram - Japanese Morphological Analysis Package

A comprehensive Python package for Japanese morphological analysis with robust enum-based parsing and error handling.

## Features

- **Enum-based Type Safety**: All morphological features are represented as proper enum types
- **Robust Error Handling**: Graceful handling of unknown or unparsable values with logging
- **Clean Token Representation**: Beautiful string representation using Japanese punctuation symbols
- **Comprehensive Testing**: Extensive test suite covering common words, sentences, and edge cases
- **Modular Design**: Clean separation of concerns with dedicated modules for types, tokens, and analyzers
- **English Documentation**: All code comments and docstrings are in English for international accessibility

## Installation

This project uses Poetry for dependency management. To get started:

```bash
# Run the Poetry setup script
./setup_poetry.sh

# Or manually install Poetry and dependencies
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```

## Development Setup

This project uses pre-commit hooks to ensure code quality. To set up the development environment:

```bash
# Install Poetry and project dependencies
poetry install

# Install pre-commit hooks
poetry run pre-commit install

# Or run the complete setup script
./setup_poetry.sh
```

### Pre-commit Hooks

The following hooks are configured to run automatically on commit:

- **Black**: Code formatting (line length: 88)
- **isort**: Import sorting (compatible with Black)
- **flake8**: Linting with Black-compatible settings
- **mypy**: Type checking
- **bandit**: Security linting
- **pre-commit-hooks**: Basic file checks (trailing whitespace, YAML validation, etc.)

### Running Hooks Manually

```bash
# Run all hooks on all files
poetry run pre-commit run --all-files

# Run hooks on staged files only
poetry run pre-commit run

# Run a specific hook
poetry run pre-commit run black
poetry run pre-commit run flake8
poetry run pre-commit run mypy
```

## Quick Start

```python
from kotogram import KotogramAnalyzer

# Initialize analyzer
analyzer = KotogramAnalyzer()

# Analyze text
text = "最新の企画書が出来あがったので、どうぞご覧ください。"
tokens = analyzer.analyze_text(text)

# Print results
analyzer.print_tokens(tokens)
```

## Project Structure

```
kotogram/
├── __init__.py          # Package initialization and exports
├── types.py            # Enum definitions for all morphological features
├── token.py            # Token class with properties and string representation
└── analyzers.py        # Morphological analysis classes

tests/
├── __init__.py
├── test_kotogram.py    # Main test suite
└── test_error_handling.py  # Error handling tests

example.py              # Usage example
requirements.txt        # Dependencies
```

## Token Representation

Tokens are displayed in a clean, informative format:

```
最新【名詞】一般「サイシン・サイシン」
の【助詞】連体化「ノ・ノ」
出来（出来る）【動詞】自立・一段・連用形「デキ・デキ」
```

Format: `表層形（原形）【品詞】詳細1・詳細2・詳細3「読み・発音」`

- **Base form in brackets**: Only shown when different from surface form
- **Unknown values**: Automatically filtered out for cleaner display
- **Japanese symbols**: Uses 【】「」：・ for natural organization

## API Reference

### Core Classes

#### `KotogramToken`
Represents a single morphological analysis result.

**Properties:**
- `surface`: Surface form (表層形)
- `part_of_speech`: Part of speech (品詞)
- `pos_detail1/2/3`: Detailed classifications (品詞細分類)
- `conjugation_type`: Verb inflection type (活用型)
- `conjugation_form`: Verb form (活用形)
- `base_form`: Base form (原形)
- `reading`: Reading (読み)
- `pronunciation`: Pronunciation (発音)

**Methods:**
- `is_noun`, `is_verb`, `is_particle`, `is_symbol`, `is_auxiliary_verb`: Type checking
- `__str__()`: Beautiful string representation

#### `KotogramAnalyzer`
Main analyzer class using Janome for tokenization.

**Methods:**
- `analyze_text(text)`: Analyze Japanese text and return KotogramToken list
- `print_tokens(tokens)`: Print tokens in formatted output
- `parse_line(line)`: Parse single line of analysis results
- `parse_text(text)`: Parse multi-line analysis results

### Enum Types

#### `PartOfSpeech`
- `NOUN`, `VERB`, `ADJECTIVE`, `ADVERB`, `PARTICLE`, `AUXILIARY_VERB`
- `SYMBOL`, `PREFIX`, `SUFFIX`, `CONJUNCTION`, `INTERJECTION`, `UNKNOWN`

#### `POSDetailType`
Comprehensive enum covering all detail classifications for nouns, verbs, particles, and symbols.

#### `InflectionForm`
Verb inflection forms: `BASIC`, `INFLECTED`, `IMPERATIVE`, `CONDITIONAL`, etc.

#### `InflectionType`
Inflection types (merged from previous inflection and auxiliary verb types): `GODAN`, `ICHIDAN`, `SAHEN`, `AUX_SPECIAL_TA`, `AUX_SPECIAL_DA`, etc.

## Error Handling

The package includes robust error handling:

- **Unknown values**: Automatically converted to `UNKNOWN` enum values
- **Logging**: Warnings logged for unparsable values using loguru
- **Graceful degradation**: Analysis continues even with problematic input
- **Type safety**: All fields remain enum types, never falling back to strings

## Testing

Run the comprehensive test suite:

```bash
poetry run pytest tests/ -v
```

### Test Coverage

- **Common Words**: Nouns, verbs, particles, adjectives
- **Sentences**: Simple, complex, and question sentences
- **Phrases**: Greetings, verb phrases
- **Part of Speech**: Detection and classification
- **Token Properties**: String representation, base forms, details
- **Error Handling**: Unknown values, malformed input, edge cases
- **Enum Values**: Validation of all enum definitions

### Error Handling Tests

The test suite includes intentional tests with unparsable values to ensure:
- Warnings are properly generated
- Unknown values are handled gracefully
- Analysis continues without crashes
- All fields remain proper enum types

## Dependencies

- `janome`: Japanese morphological analyzer
- `pydantic`: Data validation and settings management
- `loguru`: Advanced logging
- `pytest`: Testing framework

## Example Usage

```python
#!/usr/bin/env python3
"""Example usage of Kotogram Japanese morphological analysis package"""

from kotogram import JanomeAnalyzer

def main():
    # Initialize analyzer
    analyzer = JanomeAnalyzer()

    # Test text
    text = "最新の企画書が出来あがったので、どうぞご覧ください。"

    # Analyze text
    tokens = analyzer.analyze_text(text)

    # Print results
    print(f"=== Morphological Analysis Results ({len(tokens)} tokens) ===")
    analyzer.print_tokens(tokens)

    # Statistics
    print("\n=== Statistics ===")
    pos_counts = {}
    for token in tokens:
        pos = token.part_of_speech.value
        pos_counts[pos] = pos_counts.get(pos, 0) + 1

    for pos, count in sorted(pos_counts.items()):
        print(f"{pos}: {count} tokens")

if __name__ == "__main__":
    main()
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License.
