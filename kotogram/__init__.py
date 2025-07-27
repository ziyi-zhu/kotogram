"""Kotogram - Japanese Morphological Analysis Package"""

from .analyzer import KotogramAnalyzer
from .grammar import (
    GrammarMatchResult,
    GrammarRule,
    GrammarRulePattern,
    PatternMatchResult,
    RuleRegistry,
    TokenPattern,
)
from .patterns import CommonPatterns
from .token import KotogramToken
from .types import InflectionForm, InflectionType, PartOfSpeech, POSDetailType

__version__ = "0.1.0"
__all__ = [
    "PartOfSpeech",
    "POSDetailType",
    "InflectionForm",
    "InflectionType",
    "KotogramToken",
    "KotogramAnalyzer",
    "TokenPattern",
    "GrammarRule",
    "GrammarRulePattern",
    "PatternMatchResult",
    "GrammarMatchResult",
    "RuleRegistry",
    "CommonPatterns",
]
