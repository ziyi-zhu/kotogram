"""Kotogram - Japanese Morphological Analysis Package"""

from .analyzer import KotogramAnalyzer
from .grammar import (
    GrammarRule,
    MatchResult,
    PatternType,
    RuleRegistry,
    TokenPattern,
    create_default_rules,
)
from .token import KotogramToken
from .types import DetailType, InflectionForm, InflectionType, PartOfSpeech

__version__ = "0.1.0"
__all__ = [
    "PartOfSpeech",
    "DetailType",
    "InflectionForm",
    "InflectionType",
    "KotogramToken",
    "KotogramAnalyzer",
    "TokenPattern",
    "GrammarRule",
    "RuleRegistry",
    "MatchResult",
    "PatternType",
    "create_default_rules",
]
