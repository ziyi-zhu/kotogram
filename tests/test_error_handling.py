"""Tests for error handling with intentionally unparsable types"""

from unittest.mock import Mock

import pytest

from kotogram import KotogramAnalyzer


class TestUnparsableTypes:
    """Test handling of intentionally unparsable types"""

    def setup_method(self):
        self.analyzer = KotogramAnalyzer()

    def test_unparsable_part_of_speech(self):
        """Test handling of unparsable part of speech"""
        # Create a mock Janome token with invalid part of speech
        mock_token = Mock()
        mock_token.surface = "テスト"
        mock_token.part_of_speech = "INVALID_POS,一般,*,*"
        mock_token.infl_type = "*"
        mock_token.infl_form = "*"
        mock_token.base_form = "テスト"
        mock_token.reading = "テスト"
        mock_token.phonetic = "テスト"

        with pytest.raises(ValueError, match="Unknown part of speech"):
            self.analyzer._parse_token(mock_token)

    def test_unparsable_detail_type(self):
        """Test handling of unparsable detail type"""
        # Create a mock Janome token with invalid detail type
        mock_token = Mock()
        mock_token.surface = "テスト"
        mock_token.part_of_speech = "名詞,INVALID_DETAIL,*,*"
        mock_token.infl_type = "*"
        mock_token.infl_form = "*"
        mock_token.base_form = "テスト"
        mock_token.reading = "テスト"
        mock_token.phonetic = "テスト"

        with pytest.raises(ValueError, match="Unknown detail type"):
            self.analyzer._parse_token(mock_token)

    def test_unparsable_verb_inflection(self):
        """Test handling of unparsable verb inflection"""
        # Create a mock Janome token with invalid verb inflection
        mock_token = Mock()
        mock_token.surface = "行く"
        mock_token.part_of_speech = "動詞,自立,*,*"
        mock_token.infl_type = "五段・ラ行"
        mock_token.infl_form = "INVALID_FORM"
        mock_token.base_form = "行く"
        mock_token.reading = "イク"
        mock_token.phonetic = "イク"

        with pytest.raises(ValueError, match="Unknown inflection form"):
            self.analyzer._parse_token(mock_token)

    def test_unparsable_verb_inflection_type(self):
        """Test handling of unparsable verb inflection type"""
        # Create a mock Janome token with invalid verb inflection type
        mock_token = Mock()
        mock_token.surface = "行く"
        mock_token.part_of_speech = "動詞,自立,*,*"
        mock_token.infl_type = "INVALID_CONJ"
        mock_token.infl_form = "基本形"
        mock_token.base_form = "行く"
        mock_token.reading = "イク"
        mock_token.phonetic = "イク"

        with pytest.raises(ValueError, match="Unknown inflection type"):
            self.analyzer._parse_token(mock_token)

    def test_unparsable_auxiliary_verb_type(self):
        """Test handling of unparsable auxiliary verb type"""
        # Create a mock Janome token with invalid auxiliary verb type
        mock_token = Mock()
        mock_token.surface = "た"
        mock_token.part_of_speech = "助動詞,*,*,*"
        mock_token.infl_type = "INVALID_AUX"
        mock_token.infl_form = "基本形"
        mock_token.base_form = "た"
        mock_token.reading = "タ"
        mock_token.phonetic = "タ"

        with pytest.raises(ValueError, match="Unknown inflection type"):
            self.analyzer._parse_token(mock_token)

    def test_multiple_unparsable_values(self):
        """Test handling of multiple unparsable values in one token"""
        # Create a mock Janome token with multiple invalid values
        mock_token = Mock()
        mock_token.surface = "テスト"
        mock_token.part_of_speech = "INVALID_POS,INVALID_DETAIL,*,*"
        mock_token.infl_type = "INVALID_CONJ"
        mock_token.infl_form = "INVALID_FORM"
        mock_token.base_form = "テスト"
        mock_token.reading = "テスト"
        mock_token.phonetic = "テスト"

        # Should raise error for the first unparsable value (part of speech)
        with pytest.raises(ValueError, match="Unknown part of speech"):
            self.analyzer._parse_token(mock_token)


if __name__ == "__main__":
    pytest.main([__file__])
