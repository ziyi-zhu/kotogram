"""Analyzers for Japanese morphological analysis"""

from typing import List

from .token import Token
from .types import (
    AuxiliaryVerbType,
    DetailType,
    PartOfSpeech,
    VerbConjugation,
    VerbForm,
)


class MorphologicalAnalyzer:
    """Class to parse Japanese morphological analysis results"""

    @staticmethod
    def parse_detail_type(value: str) -> DetailType:
        """Convert string to DetailType"""
        if not value or value == "*":
            return DetailType.UNKNOWN
        try:
            return DetailType(value)
        except ValueError:
            raise ValueError(f"Unknown detail type: '{value}'")

    @staticmethod
    def parse_verb_form(value: str) -> VerbForm:
        """Convert string to VerbForm"""
        if not value or value == "*":
            return VerbForm.UNKNOWN
        try:
            return VerbForm(value)
        except ValueError:
            raise ValueError(f"Unknown verb form: '{value}'")

    @staticmethod
    def parse_verb_conjugation(value: str) -> VerbConjugation:
        """Convert string to VerbConjugation"""
        if not value or value == "*":
            return VerbConjugation.UNKNOWN
        try:
            return VerbConjugation(value)
        except ValueError:
            raise ValueError(f"Unknown verb conjugation: '{value}'")

    @staticmethod
    def parse_auxiliary_verb_type(value: str) -> AuxiliaryVerbType:
        """Convert string to AuxiliaryVerbType"""
        if not value or value == "*":
            return AuxiliaryVerbType.UNKNOWN
        try:
            return AuxiliaryVerbType(value)
        except ValueError:
            raise ValueError(f"Unknown auxiliary verb type: '{value}'")

    @classmethod
    def parse_line(cls, line: str) -> Token:
        """Parse a single line of analysis results"""
        # Split by tab
        parts = line.strip().split("\t")
        if len(parts) != 2:
            raise ValueError(f"Invalid format: {line}")

        surface = parts[0]
        features = parts[1].split(",")

        if len(features) < 9:
            # Pad with empty strings if insufficient
            features.extend([""] * (9 - len(features)))

        # Parse part of speech with error handling
        try:
            part_of_speech = PartOfSpeech(features[0])
        except ValueError:
            raise ValueError(
                f"Failed to parse part of speech: '{features[0]}' for token '{surface}'"
            )

        # Handle conjugation type - differs by part of speech
        if part_of_speech == PartOfSpeech.AUXILIARY_VERB:
            conjugation_type = cls.parse_auxiliary_verb_type(features[4])
        else:
            conjugation_type = cls.parse_verb_conjugation(features[4])

        return Token(
            surface=surface,
            part_of_speech=part_of_speech,
            pos_detail1=cls.parse_detail_type(features[1]),
            pos_detail2=cls.parse_detail_type(features[2]),
            pos_detail3=cls.parse_detail_type(features[3]),
            conjugation_type=conjugation_type,
            conjugation_form=cls.parse_verb_form(features[5]),
            base_form=features[6],
            reading=features[7],
            pronunciation=features[8],
        )

    @classmethod
    def parse_text(cls, text: str) -> List[Token]:
        """Parse multiple lines of analysis results"""
        tokens = []
        for line in text.strip().split("\n"):
            if line.strip():
                tokens.append(cls.parse_line(line))
        return tokens


class JanomeAnalyzer:
    """Japanese morphological analysis class using Janome"""

    def __init__(self):
        try:
            from janome.tokenizer import Tokenizer

            self.tokenizer = Tokenizer()
        except ImportError:
            raise ImportError(
                "Janome is not installed. Please install with: pip install janome"
            )

    def analyze_text(self, text: str) -> List[Token]:
        """Analyze text and return list of tokens"""
        tokens = []
        for token in self.tokenizer.tokenize(text):
            # Skip whitespace tokens
            if token.surface.strip() == "":
                continue

            # Convert Janome token to string format
            token_str = f"{token.surface}\t{token.part_of_speech},{token.infl_type},{token.infl_form},{token.base_form},{token.reading},{token.phonetic}"

            # Parse and convert to Token object
            parsed_token = MorphologicalAnalyzer.parse_line(token_str)
            tokens.append(parsed_token)

        return tokens

    def print_tokens(self, tokens: List[Token]):
        """Print analysis results"""
        for i, token in enumerate(tokens, 1):
            print(f"{i:2d}. {token}")
