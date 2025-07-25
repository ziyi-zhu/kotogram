"""Tests for error handling with intentionally unparsable types"""

import pytest

from kotogram import (
    DetailType,
    MorphologicalAnalyzer,
    PartOfSpeech,
)


class TestUnparsableTypes:
    """Test handling of intentionally unparsable types"""

    def setup_method(self):
        self.analyzer = MorphologicalAnalyzer()

    def test_unparsable_part_of_speech(self):
        """Test handling of unparsable part of speech"""
        # Create a line with invalid part of speech
        line = "テスト\tINVALID_POS,一般,*,*,*,*,テスト,テスト,テスト"

        with pytest.raises(ValueError, match="Failed to parse part of speech"):
            self.analyzer.parse_line(line)

    def test_unparsable_detail_type(self):
        """Test handling of unparsable detail type"""
        # Create a line with invalid detail type
        line = "テスト\t名詞,INVALID_DETAIL,*,*,*,*,テスト,テスト,テスト"

        with pytest.raises(ValueError, match="Unknown detail type"):
            self.analyzer.parse_line(line)

    def test_unparsable_verb_form(self):
        """Test handling of unparsable verb form"""
        # Create a line with invalid verb form
        line = "行く\t動詞,自立,*,*,五段・ラ行,INVALID_FORM,行く,イク,イク"

        with pytest.raises(ValueError, match="Unknown verb form"):
            self.analyzer.parse_line(line)

    def test_unparsable_verb_conjugation(self):
        """Test handling of unparsable verb conjugation"""
        # Create a line with invalid verb conjugation
        line = "行く\t動詞,自立,*,*,INVALID_CONJ,基本形,行く,イク,イク"

        with pytest.raises(ValueError, match="Unknown verb conjugation"):
            self.analyzer.parse_line(line)

    def test_unparsable_auxiliary_verb_type(self):
        """Test handling of unparsable auxiliary verb type"""
        # Create a line with invalid auxiliary verb type
        line = "た\t助動詞,*,*,*,INVALID_AUX,基本形,た,タ,タ"

        with pytest.raises(ValueError, match="Unknown auxiliary verb type"):
            self.analyzer.parse_line(line)

    def test_multiple_unparsable_values(self):
        """Test handling of multiple unparsable values in one token"""
        # Create a line with multiple invalid values
        line = "テスト\tINVALID_POS,INVALID_DETAIL,*,*,INVALID_CONJ,INVALID_FORM,テスト,テスト,テスト"

        # Should raise error for the first unparsable value (part of speech)
        with pytest.raises(ValueError, match="Failed to parse part of speech"):
            self.analyzer.parse_line(line)

    def test_malformed_line(self):
        """Test handling of malformed input line"""
        # Line with wrong format
        line = "テスト,名詞,一般,*,*,*,*,テスト,テスト,テスト"

        with pytest.raises(ValueError, match="Invalid format"):
            self.analyzer.parse_line(line)

    def test_insufficient_features(self):
        """Test handling of line with insufficient features"""
        # Line with too few features
        line = "テスト\t名詞,一般"
        token = self.analyzer.parse_line(line)

        # Should handle gracefully by padding with empty strings
        assert token.surface == "テスト"
        assert token.part_of_speech == PartOfSpeech.NOUN
        assert token.pos_detail1 == DetailType.NOUN_GENERAL
        # Remaining fields should be UNKNOWN or empty
        assert token.pos_detail2 == DetailType.UNKNOWN
        assert token.pos_detail3 == DetailType.UNKNOWN


class TestErrorMessages:
    """Test that error messages are properly formatted"""

    def setup_method(self):
        self.analyzer = MorphologicalAnalyzer()

    def test_detail_type_error_message(self):
        """Test that detail type error message is clear"""
        line = "テスト\t名詞,INVALID_DETAIL,*,*,*,*,テスト,テスト,テスト"

        with pytest.raises(ValueError) as exc_info:
            self.analyzer.parse_line(line)

        assert "Unknown detail type" in str(exc_info.value)
        assert "INVALID_DETAIL" in str(exc_info.value)

    def test_verb_form_error_message(self):
        """Test that verb form error message is clear"""
        line = "行く\t動詞,自立,*,*,五段・ラ行,INVALID_FORM,行く,イク,イク"

        with pytest.raises(ValueError) as exc_info:
            self.analyzer.parse_line(line)

        assert "Unknown verb form" in str(exc_info.value)
        assert "INVALID_FORM" in str(exc_info.value)

    def test_part_of_speech_error_message(self):
        """Test that part of speech error message is clear"""
        line = "テスト\tINVALID_POS,一般,*,*,*,*,テスト,テスト,テスト"

        with pytest.raises(ValueError) as exc_info:
            self.analyzer.parse_line(line)

        assert "Failed to parse part of speech" in str(exc_info.value)
        assert "INVALID_POS" in str(exc_info.value)
        assert "テスト" in str(exc_info.value)


if __name__ == "__main__":
    pytest.main([__file__])
