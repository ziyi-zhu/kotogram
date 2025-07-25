"""Kotogram - Japanese Morphological Analysis Package"""

from .analyzers import JanomeAnalyzer, MorphologicalAnalyzer
from .token import Token
from .types import (
    AuxiliaryVerbType,
    DetailType,
    PartOfSpeech,
    VerbConjugation,
    VerbForm,
)

__version__ = "0.1.0"
__all__ = [
    "PartOfSpeech",
    "DetailType",
    "VerbForm",
    "VerbConjugation",
    "AuxiliaryVerbType",
    "Token",
    "MorphologicalAnalyzer",
    "JanomeAnalyzer",
]
