"""Token class for Japanese morphological analysis"""

from pydantic import BaseModel, Field

from .types import DetailType, InflectionForm, InflectionType, PartOfSpeech


class KotogramToken(BaseModel):
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

    # Inflection type (活用型)
    infl_type: InflectionType = Field(..., description="Inflection type")

    # Inflection form (活用形)
    infl_form: InflectionForm = Field(..., description="Inflection form")

    # Base form (原形)
    base_form: str = Field(..., description="Base form")

    # Reading (読み)
    reading: str = Field(..., description="Reading")

    # Pronunciation (発音)
    phonetic: str = Field(..., description="Pronunciation")

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
        if self.infl_type.value != "*":
            details.append(self.infl_type.value)
        if self.infl_form.value != "*":
            details.append(self.infl_form.value)

        # Build the string
        result = f"{self.surface}{base_part}【{self.part_of_speech.value}】"
        if not self.is_symbol:
            result += f"「{self.reading}・{self.phonetic}」"
        if details:
            result += "・".join(details)

        return result
