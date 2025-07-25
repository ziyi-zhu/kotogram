"""Token class for Japanese morphological analysis"""

from typing import Union

from pydantic import BaseModel, Field

from .types import (
    AuxiliaryVerbType,
    DetailType,
    PartOfSpeech,
    VerbConjugation,
    VerbForm,
)


class Token(BaseModel):
    """Class to store Japanese morphological analysis results"""

    # Surface form (表層形)
    surface: str = Field(..., description="Surface form")

    # Part of speech (品詞)
    part_of_speech: PartOfSpeech = Field(..., description="Part of speech")

    # Detailed part of speech 1 (品詞細分類1)
    pos_detail1: DetailType = Field(..., description="Detailed part of speech 1")

    # Detailed part of speech 2 (品詞細分類2)
    pos_detail2: DetailType = Field(..., description="Detailed part of speech 2")

    # Detailed part of speech 3 (品詞細分類3)
    pos_detail3: DetailType = Field(..., description="Detailed part of speech 3")

    # Conjugation type (活用型)
    conjugation_type: Union[VerbConjugation, AuxiliaryVerbType] = Field(
        ..., description="Conjugation type"
    )

    # Conjugation form (活用形)
    conjugation_form: VerbForm = Field(..., description="Conjugation form")

    # Base form (原形)
    base_form: str = Field(..., description="Base form")

    # Reading (読み)
    reading: str = Field(..., description="Reading")

    # Pronunciation (発音)
    pronunciation: str = Field(..., description="Pronunciation")

    @property
    def is_noun(self) -> bool:
        """Check if token is a noun"""
        return self.part_of_speech == PartOfSpeech.NOUN

    @property
    def is_verb(self) -> bool:
        """Check if token is a verb"""
        return self.part_of_speech == PartOfSpeech.VERB

    @property
    def is_particle(self) -> bool:
        """Check if token is a particle"""
        return self.part_of_speech == PartOfSpeech.PARTICLE

    @property
    def is_symbol(self) -> bool:
        """Check if token is a symbol"""
        return self.part_of_speech == PartOfSpeech.SYMBOL

    @property
    def is_auxiliary_verb(self) -> bool:
        """Check if token is an auxiliary verb"""
        return self.part_of_speech == PartOfSpeech.AUXILIARY_VERB

    def __str__(self) -> str:
        """String representation of the token"""
        # Base form in brackets only if different from surface
        base_part = f"（{self.base_form}）" if self.base_form != self.surface else ""

        # Collect non-unknown values
        details = []
        if self.pos_detail1.value != "*":
            details.append(self.pos_detail1.value)
        if self.pos_detail2.value != "*":
            details.append(self.pos_detail2.value)
        if self.pos_detail3.value != "*":
            details.append(self.pos_detail3.value)
        if self.conjugation_type.value != "*":
            details.append(self.conjugation_type.value)
        if self.conjugation_form.value != "*":
            details.append(self.conjugation_form.value)

        # Build the string
        result = f"{self.surface}{base_part}【{self.part_of_speech.value}】"
        if not self.is_symbol:
            result += f"「{self.reading}・{self.pronunciation}」"
        if details:
            result += "・".join(details)

        return result
