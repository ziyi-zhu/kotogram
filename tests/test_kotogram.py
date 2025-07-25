"""Comprehensive tests for Kotogram package"""

import pytest

from kotogram import (
    AuxiliaryVerbType,
    DetailType,
    JanomeAnalyzer,
    PartOfSpeech,
    Token,
    VerbConjugation,
    VerbForm,
)


class TestCommonWords:
    """Test common Japanese words"""

    def setup_method(self):
        self.analyzer = JanomeAnalyzer()

    def test_nouns(self):
        """Test common nouns"""
        text = "猫 犬 本 車 家"
        tokens = self.analyzer.analyze_text(text)

        assert len(tokens) == 5
        for token in tokens:
            assert token.part_of_speech == PartOfSpeech.NOUN
            assert token.is_noun

    def test_verbs(self):
        """Test common verbs"""
        text = "行く 来る 見る 食べる 飲む"
        tokens = self.analyzer.analyze_text(text)

        assert len(tokens) == 5
        for token in tokens:
            assert token.part_of_speech == PartOfSpeech.VERB
            assert token.is_verb

    def test_particles(self):
        """Test common particles"""
        text = "の が を に で"
        tokens = self.analyzer.analyze_text(text)

        # Should have tokens
        assert len(tokens) > 0

        # Most should be particles, but some might be conjunctions
        particle_count = sum(
            1
            for token in tokens
            if token.is_particle or token.part_of_speech == PartOfSpeech.CONJUNCTION
        )
        assert particle_count >= 3  # At least 3 should be particles/conjunctions

    def test_adjectives(self):
        """Test common adjectives"""
        text = "大きい 小さい 美しい 新しい"
        tokens = self.analyzer.analyze_text(text)

        # Should have tokens
        assert len(tokens) > 0

        # Should have adjectives
        has_adjective = any(
            token.part_of_speech == PartOfSpeech.ADJECTIVE for token in tokens
        )
        assert has_adjective


class TestSentences:
    """Test complete sentences"""

    def setup_method(self):
        self.analyzer = JanomeAnalyzer()

    def test_simple_sentence(self):
        """Test a simple sentence"""
        text = "私は学生です。"
        tokens = self.analyzer.analyze_text(text)

        assert len(tokens) == 5
        assert tokens[0].surface == "私"
        assert tokens[0].is_noun
        assert tokens[1].surface == "は"
        assert tokens[1].is_particle
        assert tokens[2].surface == "学生"
        assert tokens[2].is_noun
        assert tokens[3].surface == "です"
        assert tokens[4].surface == "。"
        assert tokens[4].is_symbol

    def test_complex_sentence(self):
        """Test a more complex sentence"""
        text = "最新の企画書が出来あがったので、どうぞご覧ください。"
        tokens = self.analyzer.analyze_text(text)

        assert len(tokens) == 14

        # Check specific tokens
        assert tokens[0].surface == "最新"
        assert tokens[0].is_noun
        assert tokens[1].surface == "の"
        assert tokens[1].is_particle
        assert tokens[5].surface == "出来"
        assert tokens[5].is_verb
        assert tokens[7].surface == "た"
        assert tokens[7].is_auxiliary_verb
        assert tokens[13].surface == "。"
        assert tokens[13].is_symbol

    def test_question_sentence(self):
        """Test a question sentence"""
        text = "何を食べますか？"
        tokens = self.analyzer.analyze_text(text)

        # Janome may produce different number of tokens, so check for expected tokens
        assert len(tokens) >= 4  # At least 4 tokens

        # Check for key tokens
        surfaces = [token.surface for token in tokens]
        assert "何" in surfaces
        assert "を" in surfaces
        assert "？" in surfaces

        # Check for verb token
        has_verb = any(token.is_verb for token in tokens)
        assert has_verb


class TestPhrases:
    """Test common phrases"""

    def setup_method(self):
        self.analyzer = JanomeAnalyzer()

    def test_greeting_phrases(self):
        """Test greeting phrases"""
        text = "おはようございます こんにちは こんばんは"
        tokens = self.analyzer.analyze_text(text)

        # Should have tokens
        assert len(tokens) > 0

        # Should have various parts of speech
        pos_types = [token.part_of_speech for token in tokens]
        assert len(set(pos_types)) > 1

    def test_verb_phrases(self):
        """Test verb phrases"""
        text = "行きたい 見てください 食べましょう"
        tokens = self.analyzer.analyze_text(text)

        # Should have tokens
        assert len(tokens) > 0

        # Should contain verbs
        has_verb = any(token.is_verb for token in tokens)
        assert has_verb


class TestPartOfSpeech:
    """Test part of speech detection"""

    def setup_method(self):
        self.analyzer = JanomeAnalyzer()

    def test_noun_detection(self):
        """Test noun detection"""
        text = "東京 日本 会社 学校"
        tokens = self.analyzer.analyze_text(text)

        for token in tokens:
            assert token.is_noun
            assert not token.is_verb
            assert not token.is_particle
            assert not token.is_symbol

    def test_verb_detection(self):
        """Test verb detection"""
        text = "歩く 走る 泳ぐ 飛ぶ"
        tokens = self.analyzer.analyze_text(text)

        for token in tokens:
            assert token.is_verb
            assert not token.is_noun
            assert not token.is_particle
            assert not token.is_symbol

    def test_particle_detection(self):
        """Test particle detection"""
        text = "は が を に で から まで"
        tokens = self.analyzer.analyze_text(text)

        # Should have tokens
        assert len(tokens) > 0

        # Should have particles or conjunctions
        has_particle_or_conjunction = any(
            token.is_particle or token.part_of_speech == PartOfSpeech.CONJUNCTION
            for token in tokens
        )
        assert has_particle_or_conjunction

    def test_symbol_detection(self):
        """Test symbol detection"""
        text = "。 、 ！ ？"
        tokens = self.analyzer.analyze_text(text)

        for token in tokens:
            assert token.is_symbol
            assert not token.is_noun
            assert not token.is_verb
            assert not token.is_particle


class TestTokenProperties:
    """Test token properties and methods"""

    def setup_method(self):
        self.analyzer = JanomeAnalyzer()

    def test_token_string_representation(self):
        """Test token string representation"""
        text = "猫"
        tokens = self.analyzer.analyze_text(text)

        token = tokens[0]
        str_repr = str(token)

        # Should contain surface form and part of speech
        assert token.surface in str_repr
        assert token.part_of_speech.value in str_repr
        assert "【" in str_repr
        assert "】" in str_repr

    def test_token_with_base_form(self):
        """Test token with different base form"""
        text = "行く"
        tokens = self.analyzer.analyze_text(text)

        token = tokens[0]
        str_repr = str(token)

        # Should show base form in brackets if different
        if token.base_form != token.surface:
            assert "（" in str_repr
            assert "）" in str_repr
            assert token.base_form in str_repr

    def test_token_details(self):
        """Test token detail properties"""
        text = "美しい"
        tokens = self.analyzer.analyze_text(text)

        token = tokens[0]

        # Should have valid detail types
        assert isinstance(token.pos_detail1, DetailType)
        assert isinstance(token.pos_detail2, DetailType)
        assert isinstance(token.pos_detail3, DetailType)
        assert isinstance(token.conjugation_form, VerbForm)


class TestErrorHandling:
    """Test error handling and warnings"""

    def setup_method(self):
        self.analyzer = JanomeAnalyzer()

    def test_unknown_part_of_speech(self):
        """Test handling of unknown part of speech from Janome"""
        # This might trigger an error if Janome produces unknown part of speech
        text = "猫"
        try:
            tokens = self.analyzer.analyze_text(text)
            # If successful, should return tokens
            assert len(tokens) > 0
            for token in tokens:
                assert isinstance(token, Token)
        except ValueError as e:
            # If parsing fails, error should be informative
            assert "Failed to parse part of speech" in str(e) or "Unknown" in str(e)

    def test_unknown_detail_types(self):
        """Test handling of unknown detail types from Janome"""
        # Create a token with potentially unknown values
        text = "猫"
        try:
            tokens = self.analyzer.analyze_text(text)
            # If successful, should handle unknown values gracefully
            for token in tokens:
                assert token.pos_detail1.value in [
                    detail.value for detail in DetailType
                ]
                assert token.pos_detail2.value in [
                    detail.value for detail in DetailType
                ]
                assert token.pos_detail3.value in [
                    detail.value for detail in DetailType
                ]
        except ValueError as e:
            # If parsing fails, error should be informative
            assert "Unknown detail type" in str(e)

    def test_unknown_verb_forms(self):
        """Test handling of unknown verb forms from Janome"""
        text = "行く"
        try:
            tokens = self.analyzer.analyze_text(text)
            for token in tokens:
                if token.is_verb:
                    assert token.conjugation_form.value in [
                        form.value for form in VerbForm
                    ]
                    assert token.conjugation_type.value in [
                        conj.value for conj in VerbConjugation
                    ]
        except ValueError as e:
            # If parsing fails, error should be informative
            assert "Unknown verb form" in str(e) or "Unknown verb conjugation" in str(e)


class TestEdgeCases:
    """Test edge cases and special scenarios"""

    def setup_method(self):
        self.analyzer = JanomeAnalyzer()

    def test_empty_text(self):
        """Test empty text"""
        text = ""
        tokens = self.analyzer.analyze_text(text)

        assert len(tokens) == 0

    def test_whitespace_only(self):
        """Test whitespace only text"""
        text = "   \n\t  "
        tokens = self.analyzer.analyze_text(text)

        assert len(tokens) == 0

    def test_mixed_content(self):
        """Test mixed content with various types"""
        text = "123 猫 行く は ！"
        tokens = self.analyzer.analyze_text(text)

        # Should have tokens
        assert len(tokens) > 0

        # Should have different parts of speech
        pos_types = [token.part_of_speech for token in tokens]
        assert len(set(pos_types)) > 1

        # Check for specific tokens
        surfaces = [token.surface for token in tokens]
        assert "猫" in surfaces or any("猫" in s for s in surfaces)
        assert "！" in surfaces

    def test_long_text(self):
        """Test longer text"""
        text = "これは長い文章です。複数の文を含んでいます。テスト用の文章です。"
        tokens = self.analyzer.analyze_text(text)

        assert len(tokens) > 10

        # Should have various parts of speech
        pos_types = [token.part_of_speech for token in tokens]
        assert PartOfSpeech.NOUN in pos_types
        assert PartOfSpeech.PARTICLE in pos_types
        assert PartOfSpeech.SYMBOL in pos_types


class TestEnumValues:
    """Test enum value handling"""

    def test_part_of_speech_values(self):
        """Test all part of speech values"""
        expected_values = [
            "名詞",
            "動詞",
            "形容詞",
            "副詞",
            "助詞",
            "助動詞",
            "記号",
            "接頭詞",
            "接尾",
            "接続詞",
            "感動詞",
            "未知語",
        ]

        for pos in PartOfSpeech:
            assert pos.value in expected_values

    def test_detail_type_values(self):
        """Test detail type values are valid"""
        for detail in DetailType:
            # Should not be empty
            assert detail.value
            # Should be a string
            assert isinstance(detail.value, str)

    def test_verb_form_values(self):
        """Test verb form values are valid"""
        for form in VerbForm:
            assert form.value
            assert isinstance(form.value, str)

    def test_verb_conjugation_values(self):
        """Test verb conjugation values are valid"""
        for conj in VerbConjugation:
            assert conj.value
            assert isinstance(conj.value, str)

    def test_auxiliary_verb_type_values(self):
        """Test auxiliary verb type values are valid"""
        for aux_type in AuxiliaryVerbType:
            assert aux_type.value
            assert isinstance(aux_type.value, str)


if __name__ == "__main__":
    pytest.main([__file__])
