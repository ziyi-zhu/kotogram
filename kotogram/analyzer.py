"""Analyzers for Japanese morphological analysis"""

from janome.tokenizer import Token, Tokenizer

from .token import KotogramToken
from .types import InflectionForm, InflectionType, PartOfSpeech, POSDetailType


class KotogramAnalyzer:
    """Japanese morphological analysis class using Janome"""

    def __init__(self):
        self.tokenizer = Tokenizer()

    @staticmethod
    def parse_detail_type(value: str) -> POSDetailType:
        """Convert string to POSDetailType"""
        try:
            return POSDetailType(value)
        except ValueError:
            raise ValueError(f"Unknown detail type: '{value}'")

    @staticmethod
    def parse_inflection_form(value: str) -> InflectionForm:
        """Convert string to InflectionForm"""
        try:
            return InflectionForm(value)
        except ValueError:
            raise ValueError(f"Unknown inflection form: '{value}'")

    @staticmethod
    def parse_inflection_type(value: str) -> InflectionType:
        """Convert string to InflectionType"""
        try:
            return InflectionType(value)
        except ValueError:
            raise ValueError(f"Unknown inflection type: '{value}'")

    @staticmethod
    def parse_part_of_speech(value: str) -> PartOfSpeech:
        """Convert string to PartOfSpeech"""
        try:
            return PartOfSpeech(value)
        except ValueError:
            raise ValueError(f"Unknown part of speech: '{value}'")

    def _parse_token(self, token: Token) -> KotogramToken:
        """Parse a Janome token directly into a KotogramToken"""
        # Parse part of speech and details from the comma-separated string
        pos_parts = token.part_of_speech.split(",")

        return KotogramToken(
            surface=token.surface,
            part_of_speech=self.parse_part_of_speech(pos_parts[0]),
            pos_detail1=self.parse_detail_type(pos_parts[1]),
            pos_detail2=self.parse_detail_type(pos_parts[2]),
            pos_detail3=self.parse_detail_type(pos_parts[3]),
            infl_type=self.parse_inflection_type(token.infl_type),
            infl_form=self.parse_inflection_form(token.infl_form),
            base_form=token.base_form,
            reading=token.reading,
            phonetic=token.phonetic,
        )

    def parse_text(self, text: str) -> list[KotogramToken]:
        """Analyze text and return list of tokens"""
        tokens = []
        for token in self.tokenizer.tokenize(text):
            # Skip whitespace tokens
            if token.surface.strip() == "":
                continue

            # Parse Janome token directly into KotogramToken
            parsed_token = self._parse_token(token)
            tokens.append(parsed_token)

        return tokens

    def print_tokens(self, tokens: list[KotogramToken]):
        """Print analysis results"""
        for i, token in enumerate(tokens, 1):
            print(f"{i:2d}. {token}")
