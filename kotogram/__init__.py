"""Kotogram - Japanese Morphological Analysis Package"""

from .analyzer import KotogramAnalyzer
from .grammar import GrammarRule, MatchResult, RuleRegistry, TokenPattern
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
    "RuleRegistry",
    "MatchResult",
]
