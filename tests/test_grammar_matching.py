"""Tests for grammar matching system"""


from kotogram import (
    DetailType,
    GrammarRule,
    InflectionForm,
    InflectionType,
    KotogramAnalyzer,
    KotogramToken,
    PartOfSpeech,
    PatternType,
    RuleRegistry,
    TokenPattern,
    create_default_rules,
)


class TestTokenPattern:
    """Test TokenPattern class"""

    def test_exact_match(self):
        """Test exact surface form matching"""
        pattern = TokenPattern(pattern_type=PatternType.EXACT, value="赤ちゃん")
        token = KotogramToken(
            surface="赤ちゃん",
            part_of_speech=PartOfSpeech.NOUN,
            pos_detail1=DetailType.NOUN_GENERAL,
            pos_detail2=DetailType.UNKNOWN,
            pos_detail3=DetailType.UNKNOWN,
            infl_type=InflectionType.UNKNOWN,
            infl_form=InflectionForm.UNKNOWN,
            base_form="赤ちゃん",
            reading="あかちゃん",
            phonetic="アカチャン",
        )
        assert pattern.matches(token)

    def test_part_of_speech_match(self):
        """Test part of speech matching"""
        pattern = TokenPattern(
            pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN
        )
        token = KotogramToken(
            surface="本",
            part_of_speech=PartOfSpeech.NOUN,
            pos_detail1=DetailType.NOUN_GENERAL,
            pos_detail2=DetailType.UNKNOWN,
            pos_detail3=DetailType.UNKNOWN,
            infl_type=InflectionType.UNKNOWN,
            infl_form=InflectionForm.UNKNOWN,
            base_form="本",
            reading="ほん",
            phonetic="ホン",
        )
        assert pattern.matches(token)

    def test_inflection_form_match(self):
        """Test inflection form matching"""
        pattern = TokenPattern(
            pattern_type=PatternType.INFLECTION_FORM, value=InflectionForm.BASIC
        )
        token = KotogramToken(
            surface="読む",
            part_of_speech=PartOfSpeech.VERB,
            pos_detail1=DetailType.VERB_INDEPENDENT,
            pos_detail2=DetailType.UNKNOWN,
            pos_detail3=DetailType.UNKNOWN,
            infl_type=InflectionType.GODAN,
            infl_form=InflectionForm.BASIC,
            base_form="読む",
            reading="よむ",
            phonetic="ヨム",
        )
        assert pattern.matches(token)

    def test_wildcard_match(self):
        """Test wildcard matching"""
        pattern = TokenPattern(
            pattern_type=PatternType.WILDCARD, value=PatternType.WILDCARD
        )
        token = KotogramToken(
            surface="何でも",
            part_of_speech=PartOfSpeech.NOUN,
            pos_detail1=DetailType.NOUN_GENERAL,
            pos_detail2=DetailType.UNKNOWN,
            pos_detail3=DetailType.UNKNOWN,
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
            pattern_type=PatternType.ALTERNATIVE,
            value=PartOfSpeech.VERB,
            alternatives=[PartOfSpeech.VERB, PartOfSpeech.ADJECTIVE],
        )
        verb_token = KotogramToken(
            surface="読む",
            part_of_speech=PartOfSpeech.VERB,
            pos_detail1=DetailType.VERB_INDEPENDENT,
            pos_detail2=DetailType.UNKNOWN,
            pos_detail3=DetailType.UNKNOWN,
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
            pattern_type=PatternType.ALTERNATIVE,
            value=PartOfSpeech.VERB,
            alternatives=[PartOfSpeech.VERB, PartOfSpeech.ADJECTIVE],
        )
        adj_token = KotogramToken(
            surface="美しい",
            part_of_speech=PartOfSpeech.ADJECTIVE,
            pos_detail1=DetailType.UNKNOWN,
            pos_detail2=DetailType.UNKNOWN,
            pos_detail3=DetailType.UNKNOWN,
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
            TokenPattern(
                pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN
            ),
            TokenPattern(pattern_type=PatternType.EXACT, value="の"),
            TokenPattern(pattern_type=PatternType.EXACT, value="間"),
        ]
        rule = GrammarRule("test_rule", patterns, "Test rule")

        tokens = [
            KotogramToken(
                surface="講演",
                part_of_speech=PartOfSpeech.NOUN,
                pos_detail1=DetailType.NOUN_GENERAL,
                pos_detail2=DetailType.UNKNOWN,
                pos_detail3=DetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="講演",
                reading="こうえん",
                phonetic="コウエン",
            ),
            KotogramToken(
                surface="の",
                part_of_speech=PartOfSpeech.PARTICLE,
                pos_detail1=DetailType.PARTICLE_CASE,
                pos_detail2=DetailType.UNKNOWN,
                pos_detail3=DetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="の",
                reading="の",
                phonetic="ノ",
            ),
            KotogramToken(
                surface="間",
                part_of_speech=PartOfSpeech.NOUN,
                pos_detail1=DetailType.NOUN_GENERAL,
                pos_detail2=DetailType.UNKNOWN,
                pos_detail3=DetailType.UNKNOWN,
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
            TokenPattern(
                pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN
            ),
            TokenPattern(pattern_type=PatternType.EXACT, value="の"),
            TokenPattern(pattern_type=PatternType.EXACT, value="間"),
        ]
        rule = GrammarRule("test_rule", patterns, "Test rule")

        tokens = [
            KotogramToken(
                surface="動詞",
                part_of_speech=PartOfSpeech.VERB,
                pos_detail1=DetailType.VERB_INDEPENDENT,
                pos_detail2=DetailType.UNKNOWN,
                pos_detail3=DetailType.UNKNOWN,
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
            TokenPattern(
                pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN
            ),
            TokenPattern(pattern_type=PatternType.EXACT, value="の"),
            TokenPattern(pattern_type=PatternType.EXACT, value="間"),
        ]
        rule = GrammarRule("test_rule", patterns, "Test description")
        registry.add_rule(rule)

        tokens = [
            KotogramToken(
                surface="講演",
                part_of_speech=PartOfSpeech.NOUN,
                pos_detail1=DetailType.NOUN_GENERAL,
                pos_detail2=DetailType.UNKNOWN,
                pos_detail3=DetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="講演",
                reading="こうえん",
                phonetic="コウエン",
            ),
            KotogramToken(
                surface="の",
                part_of_speech=PartOfSpeech.PARTICLE,
                pos_detail1=DetailType.PARTICLE_CASE,
                pos_detail2=DetailType.UNKNOWN,
                pos_detail3=DetailType.UNKNOWN,
                infl_type=InflectionType.UNKNOWN,
                infl_form=InflectionForm.UNKNOWN,
                base_form="の",
                reading="の",
                phonetic="ノ",
            ),
            KotogramToken(
                surface="間",
                part_of_speech=PartOfSpeech.NOUN,
                pos_detail1=DetailType.NOUN_GENERAL,
                pos_detail2=DetailType.UNKNOWN,
                pos_detail3=DetailType.UNKNOWN,
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

    def test_default_rules(self):
        """Test that default rules are created correctly"""
        registry = create_default_rules()
        rule_names = registry.get_rule_names()

        expected_rules = [
            "～間に",
            "～間",
            "～あがる",
            "～一方（で）",
            "～上で（の）",
            "～ないうちに",
            "～おきに",
            "～から～にかけて",
            "～くらい／ぐらい",
        ]

        for expected_rule in expected_rules:
            assert expected_rule in rule_names


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
                    DetailType.NOUN_GENERAL
                    if pos == PartOfSpeech.NOUN
                    else DetailType.UNKNOWN
                ),
                pos_detail2=DetailType.UNKNOWN,
                pos_detail3=DetailType.UNKNOWN,
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
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.WILDCARD, value=None),
            TokenPattern(pattern_type=PatternType.EXACT, value="です"),
        ]
        rule = GrammarRule("test_wildcard", patterns)

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
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
            TokenPattern(pattern_type=PatternType.EXACT, value="です"),
        ]
        rule = GrammarRule("test_multi_wildcard_zero", patterns)

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
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
            TokenPattern(pattern_type=PatternType.EXACT, value="です"),
        ]
        rule = GrammarRule("test_multi_wildcard_multiple", patterns)

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
            TokenPattern(
                pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN
            ),
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
            TokenPattern(
                pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN
            ),
            TokenPattern(pattern_type=PatternType.EXACT, value="にかけて"),
        ]
        rule = GrammarRule("test_compound_noun_pattern", patterns)

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
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
            TokenPattern(
                pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN
            ),
            TokenPattern(pattern_type=PatternType.EXACT, value="です"),
        ]
        rule = GrammarRule("test_multi_wildcard_choice", patterns)

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
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
            TokenPattern(
                pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN
            ),
            TokenPattern(pattern_type=PatternType.EXACT, value="です"),
        ]
        rule = GrammarRule("test_multi_wildcard_no_match", patterns)

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
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
        ]
        rule = GrammarRule("test_multi_wildcard_end", patterns)

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
        """Test pattern with multiple multi-wildcards"""
        # Pattern: A + ** + B + ** + C
        patterns = [
            TokenPattern(pattern_type=PatternType.EXACT, value="A"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
            TokenPattern(pattern_type=PatternType.EXACT, value="B"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
            TokenPattern(pattern_type=PatternType.EXACT, value="C"),
        ]
        rule = GrammarRule("test_multiple_multi_wildcards", patterns)

        # Test tokens: A + X + Y + B + Z + C
        tokens = self._create_test_tokens(
            [
                ("A", PartOfSpeech.NOUN),
                ("X", PartOfSpeech.VERB),
                ("Y", PartOfSpeech.PARTICLE),
                ("B", PartOfSpeech.NOUN),
                ("Z", PartOfSpeech.VERB),
                ("C", PartOfSpeech.NOUN),
            ]
        )

        match = rule.match(tokens, 0)
        assert match is not None
        assert len(match.matched_tokens) == 6
        assert [t.surface for t in match.matched_tokens] == [
            "A",
            "X",
            "Y",
            "B",
            "Z",
            "C",
        ]

    def test_wildcard_vs_multi_wildcard_difference(self):
        """Test the difference between wildcard (*) and multi-wildcard (**)"""
        # Wildcard pattern: から + * + です (matches exactly one token)
        wildcard_patterns = [
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.WILDCARD, value=None),
            TokenPattern(pattern_type=PatternType.EXACT, value="です"),
        ]
        wildcard_rule = GrammarRule("test_wildcard", wildcard_patterns)

        # Multi-wildcard pattern: から + ** + です (matches any number of tokens)
        multi_wildcard_patterns = [
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
            TokenPattern(pattern_type=PatternType.EXACT, value="です"),
        ]
        multi_wildcard_rule = GrammarRule(
            "test_multi_wildcard", multi_wildcard_patterns
        )

        # Test with zero tokens between から and です
        tokens_zero = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        wildcard_match = wildcard_rule.match(tokens_zero, 0)
        multi_wildcard_match = multi_wildcard_rule.match(tokens_zero, 0)

        assert wildcard_match is None  # Wildcard requires exactly one token
        assert multi_wildcard_match is not None  # Multi-wildcard can match zero tokens

        # Test with one token between から and です
        tokens_one = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("何か", PartOfSpeech.NOUN),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        wildcard_match = wildcard_rule.match(tokens_one, 0)
        multi_wildcard_match = multi_wildcard_rule.match(tokens_one, 0)

        assert wildcard_match is not None  # Wildcard matches exactly one token
        assert multi_wildcard_match is not None  # Multi-wildcard can match one token

        # Test with multiple tokens between から and です
        tokens_multiple = self._create_test_tokens(
            [
                ("から", PartOfSpeech.PARTICLE),
                ("A", PartOfSpeech.NOUN),
                ("B", PartOfSpeech.VERB),
                ("です", PartOfSpeech.AUXILIARY_VERB),
            ]
        )

        wildcard_match = wildcard_rule.match(tokens_multiple, 0)
        multi_wildcard_match = multi_wildcard_rule.match(tokens_multiple, 0)

        assert wildcard_match is None  # Wildcard cannot match multiple tokens
        assert (
            multi_wildcard_match is not None
        )  # Multi-wildcard can match multiple tokens

    def test_real_world_integration_with_analyzer(self):
        """Test wildcard patterns with real Japanese text analysis"""
        # Create a rule that uses multi-wildcard to match flexible patterns
        patterns = [
            TokenPattern(
                pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN
            ),
            TokenPattern(pattern_type=PatternType.EXACT, value="から"),
            TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
            TokenPattern(pattern_type=PatternType.EXACT, value="まで"),
        ]
        rule = GrammarRule("test_real_world", patterns)

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
