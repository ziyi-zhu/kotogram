"""Tests for grammar matching system"""

import pytest

from kotogram import (
    GrammarRule,
    InflectionForm,
    InflectionType,
    KotogramAnalyzer,
    KotogramToken,
    PartOfSpeech,
    POSDetailType,
    RuleRegistry,
    TokenPattern,
)


class TestTokenPattern:
    """Test TokenPattern class"""

    def test_exact_match(self):
        """Test exact surface form matching"""
        pattern = TokenPattern(value="赤ちゃん")
        token = KotogramToken(
            surface="赤ちゃん",
            part_of_speech=PartOfSpeech.NOUN,
            pos_detail1=POSDetailType.NOUN_GENERAL,
            pos_detail2=POSDetailType.UNKNOWN,
            pos_detail3=POSDetailType.UNKNOWN,
            infl_type=InflectionType.UNKNOWN,
            infl_form=InflectionForm.UNKNOWN,
            base_form="赤ちゃん",
            reading="あかちゃん",
            phonetic="アカチャン",
        )
        assert pattern.matches(token)

    def test_part_of_speech_match(self):
        """Test part of speech matching"""
        pattern = TokenPattern(part_of_speech=PartOfSpeech.NOUN)
        token = KotogramToken(
            surface="本",
            part_of_speech=PartOfSpeech.NOUN,
            pos_detail1=POSDetailType.NOUN_GENERAL,
            pos_detail2=POSDetailType.UNKNOWN,
            pos_detail3=POSDetailType.UNKNOWN,
            infl_type=InflectionType.UNKNOWN,
            infl_form=InflectionForm.UNKNOWN,
            base_form="本",
            reading="ほん",
            phonetic="ホン",
        )
        assert pattern.matches(token)

    def test_inflection_form_match(self):
        """Test inflection form matching"""
        pattern = TokenPattern(infl_form=InflectionForm.BASIC)
        token = KotogramToken(
            surface="読む",
            part_of_speech=PartOfSpeech.VERB,
            pos_detail1=POSDetailType.VERB_INDEPENDENT,
            pos_detail2=POSDetailType.UNKNOWN,
            pos_detail3=POSDetailType.UNKNOWN,
            infl_type=InflectionType.GODAN,
            infl_form=InflectionForm.BASIC,
            base_form="読む",
            reading="よむ",
            phonetic="ヨム",
        )
        assert pattern.matches(token)

    def test_wildcard_match(self):
        """Test wildcard matching (multi-wildcard when all fields None)"""
        pattern = TokenPattern()  # Empty pattern = multi-wildcard
        token = KotogramToken(
            surface="何でも",
            part_of_speech=PartOfSpeech.NOUN,
            pos_detail1=POSDetailType.NOUN_GENERAL,
            pos_detail2=POSDetailType.UNKNOWN,
            pos_detail3=POSDetailType.UNKNOWN,
            infl_type=InflectionType.UNKNOWN,
            infl_form=InflectionForm.UNKNOWN,
            base_form="何でも",
            reading="なにでも",
            phonetic="ナニデモ",
        )
        assert pattern.matches(token)

    def test_alternative_match_verb(self):
        """Test alternative pattern matching with verb"""
        pattern = TokenPattern(
            alternatives=[
                TokenPattern(part_of_speech=PartOfSpeech.VERB),
                TokenPattern(part_of_speech=PartOfSpeech.ADJECTIVE),
            ]
        )
        verb_token = KotogramToken(
            surface="読む",
            part_of_speech=PartOfSpeech.VERB,
            pos_detail1=POSDetailType.VERB_INDEPENDENT,
            pos_detail2=POSDetailType.UNKNOWN,
            pos_detail3=POSDetailType.UNKNOWN,
            infl_type=InflectionType.GODAN,
            infl_form=InflectionForm.BASIC,
            base_form="読む",
            reading="よむ",
            phonetic="ヨム",
        )
        assert pattern.matches(verb_token)

    def test_alternative_match_adjective(self):
        """Test alternative pattern matching with adjective"""
        pattern = TokenPattern(
            alternatives=[
                TokenPattern(part_of_speech=PartOfSpeech.VERB),
                TokenPattern(part_of_speech=PartOfSpeech.ADJECTIVE),
            ]
        )
        adj_token = KotogramToken(
            surface="美しい",
            part_of_speech=PartOfSpeech.ADJECTIVE,
            pos_detail1=POSDetailType.UNKNOWN,
            pos_detail2=POSDetailType.UNKNOWN,
            pos_detail3=POSDetailType.UNKNOWN,
            infl_type=InflectionType.ADJECTIVE_ISTEM,
            infl_form=InflectionForm.BASIC,
            base_form="美しい",
            reading="うつくしい",
            phonetic="ウツクシイ",
        )
        assert pattern.matches(adj_token)


class TestGrammarRule:
    """Test GrammarRule class"""

    def test_simple_rule_match(self):
        """Test simple grammar rule matching"""
        patterns = [
            TokenPattern(part_of_speech=PartOfSpeech.NOUN),
            TokenPattern(value="の"),
            TokenPattern(value="間"),
        ]
        rule = GrammarRule(name="test_rule", patterns=patterns, description="Test rule")

        tokens = [
            KotogramToken(
                surface="講演",
                part_of_speech=PartOfSpeech.NOUN,
                pos_detail1=POSDetailType.NOUN_GENERAL,
                pos_detail2=POSDetailType.UNKNOWN,
                pos_detail3=POSDetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="講演",
                reading="こうえん",
                phonetic="コウエン",
            ),
            KotogramToken(
                surface="の",
                part_of_speech=PartOfSpeech.PARTICLE,
                pos_detail1=POSDetailType.PARTICLE_CASE,
                pos_detail2=POSDetailType.UNKNOWN,
                pos_detail3=POSDetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="の",
                reading="の",
                phonetic="ノ",
            ),
            KotogramToken(
                surface="間",
                part_of_speech=PartOfSpeech.NOUN,
                pos_detail1=POSDetailType.NOUN_GENERAL,
                pos_detail2=POSDetailType.UNKNOWN,
                pos_detail3=POSDetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="間",
                reading="あいだ",
                phonetic="アイダ",
            ),
        ]

        match = rule.match(tokens, 0)
        assert match is not None
        assert match.rule_name == "test_rule"
        assert match.start_pos == 0
        assert match.end_pos == 3

    def test_rule_no_match(self):
        """Test grammar rule when no match is found"""
        patterns = [
            TokenPattern(part_of_speech=PartOfSpeech.NOUN),
            TokenPattern(value="の"),
            TokenPattern(value="間"),
        ]
        rule = GrammarRule(name="test_rule", patterns=patterns, description="Test rule")

        tokens = [
            KotogramToken(
                surface="動詞",
                part_of_speech=PartOfSpeech.VERB,
                pos_detail1=POSDetailType.VERB_INDEPENDENT,
                pos_detail2=POSDetailType.UNKNOWN,
                pos_detail3=POSDetailType.UNKNOWN,
                infl_type=InflectionType.GODAN,
                infl_form=InflectionForm.BASIC,
                base_form="動詞",
                reading="どうし",
                phonetic="ドウシ",
            ),
        ]

        match = rule.match(tokens, 0)
        assert match is None


class TestRuleRegistry:
    """Test RuleRegistry class"""

    def test_add_and_match_rule(self):
        """Test adding and matching rules"""
        registry = RuleRegistry()
        patterns = [
            TokenPattern(part_of_speech=PartOfSpeech.NOUN),
            TokenPattern(value="の"),
            TokenPattern(value="間"),
        ]
        rule = GrammarRule(
            name="test_rule", patterns=patterns, description="Test description"
        )
        registry.add_rule(rule)

        tokens = [
            KotogramToken(
                surface="講演",
                part_of_speech=PartOfSpeech.NOUN,
                pos_detail1=POSDetailType.NOUN_GENERAL,
                pos_detail2=POSDetailType.UNKNOWN,
                pos_detail3=POSDetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="講演",
                reading="こうえん",
                phonetic="コウエン",
            ),
            KotogramToken(
                surface="の",
                part_of_speech=PartOfSpeech.PARTICLE,
                pos_detail1=POSDetailType.PARTICLE_CASE,
                pos_detail2=POSDetailType.UNKNOWN,
                pos_detail3=POSDetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="の",
                reading="の",
                phonetic="ノ",
            ),
            KotogramToken(
                surface="間",
                part_of_speech=PartOfSpeech.NOUN,
                pos_detail1=POSDetailType.NOUN_GENERAL,
                pos_detail2=POSDetailType.UNKNOWN,
                pos_detail3=POSDetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="間",
                reading="あいだ",
                phonetic="アイダ",
            ),
        ]

        matches = registry.match_all(tokens)
        assert len(matches) == 1
        assert matches[0].rule_name == "test_rule"


class TestWildcardPatterns:
    """Test wildcard and multi-wildcard pattern matching"""

    def setup_method(self):
        """Set up test fixtures"""
        self.analyzer = KotogramAnalyzer()

    def _create_test_tokens(self, surfaces_and_pos):
        """Helper to create tokens from surface forms and parts of speech"""
        tokens = []
        for surface, pos in surfaces_and_pos:
            token = KotogramToken(
                surface=surface,
                part_of_speech=pos,
                pos_detail1=(
                    POSDetailType.NOUN_GENERAL
                    if pos == PartOfSpeech.NOUN
                    else POSDetailType.UNKNOWN
                ),
                pos_detail2=POSDetailType.UNKNOWN,
                pos_detail3=POSDetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form=surface,
                reading=surface,
                phonetic=surface,
            )
            tokens.append(token)
        return tokens

    def test_simple_wildcard(self):
        """Test basic wildcard matching"""
        # Pattern: から + * + です
        patterns = [
            TokenPattern(value="から"),
            TokenPattern(),
            TokenPattern(value="です"),
        ]
        rule = GrammarRule(name="test_wildcard", patterns=patterns)

        # Test tokens: から + 何か + です
        tokens = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("何か", PartOfSpeech.NOUN),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        match = rule.match(tokens, 0)
        assert match is not None
        assert len(match.matched_tokens) == 3
        assert [t.surface for t in match.matched_tokens] == ["から", "何か", "です"]

    def test_multi_wildcard_zero_tokens(self):
        """Test multi-wildcard matching zero tokens"""
        # Pattern: から + ** + です (should match "から です")
        patterns = [
            TokenPattern(value="から"),
            TokenPattern(),
            TokenPattern(value="です"),
        ]
        rule = GrammarRule(name="test_multi_wildcard_zero", patterns=patterns)

        # Test tokens: から + です (no tokens in between)
        tokens = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        match = rule.match(tokens, 0)
        assert match is not None
        assert len(match.matched_tokens) == 2
        assert [t.surface for t in match.matched_tokens] == ["から", "です"]

    def test_multi_wildcard_multiple_tokens(self):
        """Test multi-wildcard matching multiple tokens"""
        # Pattern: から + ** + です (should match "から A B C です")
        patterns = [
            TokenPattern(value="から"),
            TokenPattern(),
            TokenPattern(value="です"),
        ]
        rule = GrammarRule(name="test_multi_wildcard_multiple", patterns=patterns)

        # Test tokens: から + A + B + C + です
        tokens = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("A", PartOfSpeech.NOUN),
                ("B", PartOfSpeech.VERB),
                ("C", PartOfSpeech.PARTICLE),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        match = rule.match(tokens, 0)
        assert match is not None
        assert len(match.matched_tokens) == 5
        assert [t.surface for t in match.matched_tokens] == [
            "から",
            "A",
            "B",
            "C",
            "です",
        ]

    def test_multi_wildcard_with_specific_pattern_after(self):
        """Test multi-wildcard followed by specific pattern (like the bug we fixed)"""
        # Pattern: NOUN + から + ** + NOUN + にかけて
        patterns = [
            TokenPattern(part_of_speech=PartOfSpeech.NOUN),
            TokenPattern(value="から"),
            TokenPattern(),
            TokenPattern(part_of_speech=PartOfSpeech.NOUN),
            TokenPattern(value="にかけて"),
        ]
        rule = GrammarRule(name="test_compound_noun_pattern", patterns=patterns)

        # Test tokens: 月 + から + 3 + 月 + にかけて (compound noun case)
        tokens = self._create_test_tokens(
            [
                ("月", PartOfSpeech.NOUN),
                ("から", PartOfSpeech.PARTICLE),
                ("3", PartOfSpeech.NOUN),
                ("月", PartOfSpeech.NOUN),
                ("にかけて", PartOfSpeech.PARTICLE),
            ]
        )

        match = rule.match(tokens, 0)
        assert match is not None
        assert len(match.matched_tokens) == 5
        assert [t.surface for t in match.matched_tokens] == [
            "月",
            "から",
            "3",
            "月",
            "にかけて",
        ]

    def test_multi_wildcard_chooses_correct_match(self):
        """Test that multi-wildcard chooses the correct match when multiple candidates exist"""
        # Pattern: から + ** + NOUN + です
        patterns = [
            TokenPattern(value="から"),
            TokenPattern(),
            TokenPattern(part_of_speech=PartOfSpeech.NOUN),
            TokenPattern(value="です"),
        ]
        rule = GrammarRule(name="test_multi_wildcard_choice", patterns=patterns)

        # Test tokens: から + NOUN1 + VERB + NOUN2 + です
        # Should match NOUN2, not NOUN1, because NOUN2 is followed by です
        tokens = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("名詞1", PartOfSpeech.NOUN),
                ("動詞", PartOfSpeech.VERB),
                ("名詞2", PartOfSpeech.NOUN),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        match = rule.match(tokens, 0)
        assert match is not None
        assert len(match.matched_tokens) == 5
        assert [t.surface for t in match.matched_tokens] == [
            "から",
            "名詞1",
            "動詞",
            "名詞2",
            "です",
        ]

    def test_multi_wildcard_no_match_when_pattern_incomplete(self):
        """Test that multi-wildcard fails when remaining pattern cannot be completed"""
        # Pattern: から + ** + NOUN + です
        patterns = [
            TokenPattern(value="から"),
            TokenPattern(),
            TokenPattern(part_of_speech=PartOfSpeech.NOUN),
            TokenPattern(value="です"),
        ]
        rule = GrammarRule(name="test_multi_wildcard_no_match", patterns=patterns)

        # Test tokens: から + NOUN + VERB (missing です)
        tokens = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("名詞", PartOfSpeech.NOUN),
                ("動詞", PartOfSpeech.VERB),
            ]
        )

        match = rule.match(tokens, 0)
        assert match is None

    def test_multi_wildcard_at_end(self):
        """Test multi-wildcard at the end of pattern"""
        # Pattern: から + **
        patterns = [
            TokenPattern(value="から"),
            TokenPattern(),
        ]
        rule = GrammarRule(name="test_multi_wildcard_end", patterns=patterns)

        # Test tokens: から + A + B + C (should consume all remaining)
        tokens = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("A", PartOfSpeech.NOUN),
                ("B", PartOfSpeech.VERB),
                ("C", PartOfSpeech.PARTICLE),
            ]
        )

        match = rule.match(tokens, 0)
        assert match is not None
        assert len(match.matched_tokens) == 4
        assert [t.surface for t in match.matched_tokens] == ["から", "A", "B", "C"]

    def test_multiple_multi_wildcards(self):
        """Test that multiple multi-wildcards are not allowed"""
        # Pattern: A + ** + B + ** + C (should raise ValueError)
        patterns = [
            TokenPattern(value="A"),
            TokenPattern(),
            TokenPattern(value="B"),
            TokenPattern(),
            TokenPattern(value="C"),
        ]

        # Should raise ValueError for multiple multi-wildcards
        with pytest.raises(
            ValueError, match="Only one multi-wildcard per rule is allowed"
        ):
            GrammarRule(name="test_multiple_multi_wildcards", patterns=patterns)

    def test_multi_wildcard_behavior(self):
        """Test multi-wildcard behavior (all empty patterns are now multi-wildcards)"""
        # Multi-wildcard pattern: から + ** + です (matches any number of tokens)
        multi_wildcard_patterns = [
            TokenPattern(value="から"),
            TokenPattern(),  # Multi-wildcard (empty pattern)
            TokenPattern(value="です"),
        ]
        multi_wildcard_rule = GrammarRule(
            name="test_multi_wildcard", patterns=multi_wildcard_patterns
        )

        # Test with zero tokens between から and です
        tokens_zero = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        match_zero = multi_wildcard_rule.match(tokens_zero, 0)
        assert match_zero is not None  # Multi-wildcard can match zero tokens

        # Test with one token between から and です
        tokens_one = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("何か", PartOfSpeech.NOUN),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        match_one = multi_wildcard_rule.match(tokens_one, 0)
        assert match_one is not None  # Multi-wildcard can match one token

        # Test with multiple tokens between から and です
        tokens_multiple = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("A", PartOfSpeech.NOUN),
                ("B", PartOfSpeech.VERB),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        match_multiple = multi_wildcard_rule.match(tokens_multiple, 0)
        assert match_multiple is not None  # Multi-wildcard can match multiple tokens

    def test_real_world_integration_with_analyzer(self):
        """Test wildcard patterns with real Japanese text analysis"""
        # Create a rule that uses multi-wildcard to match flexible patterns
        patterns = [
            TokenPattern(part_of_speech=PartOfSpeech.NOUN),
            TokenPattern(value="から"),
            TokenPattern(),
            TokenPattern(value="まで"),
        ]
        rule = GrammarRule(name="test_real_world", patterns=patterns)

        # Test with real Japanese text
        text = "東京から大阪まで"
        tokens = self.analyzer.parse_text(text)

        match = rule.match(tokens, 0)
        assert match is not None
        assert len(match.matched_tokens) >= 3  # At least NOUN + から + まで

        # Verify the match includes から and まで
        surfaces = [t.surface for t in match.matched_tokens]
        assert "から" in surfaces
        assert "まで" in surfaces
