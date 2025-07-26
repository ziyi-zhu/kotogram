"""Tests for grammar matching system"""

import pytest

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
            "動詞普通形＋間に",
            "名詞＋の＋間",
            "動詞「ます形」＋あがる",
            "名詞＋である＋一方",
            "名詞＋動詞「た形」＋上で",
            "動詞「ない形」＋ない＋うちに",
            "数量詞＋おきに",
            "名詞＋から＋名詞＋にかけて",
            "～ぐらい～はない",
        ]

        for expected_rule in expected_rules:
            assert expected_rule in rule_names


class TestIntegration:
    """Integration tests with real Japanese text"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Set up analyzer and registry"""
        self.analyzer = KotogramAnalyzer()
        self.registry = create_default_rules()

    def _test_rule_matches(self, rule_name, sentences):
        """Helper method to test if a rule matches in given sentences"""
        for sentence in sentences:
            tokens = self.analyzer.parse_text(sentence)
            matches = self.registry.match_all(tokens)

            # Check if expected rule is found
            found_rules = [m.rule_name for m in matches]
            assert (
                rule_name in found_rules
            ), f"Expected rule '{rule_name}' not found in matches: {found_rules}"

    def test_rule_1(self):
        """Test rule: 動詞普通形＋間に"""
        expected_rule = "動詞普通形＋間に"
        sentences = [
            "赤ちゃんが寝ている間に、洗濯をしました。",
            "日本に留学している間に富士山に登りたい。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_2(self):
        """Test rule: 名詞＋の＋間"""
        expected_rule = "名詞＋の＋間"
        sentences = [
            "山田先生の講演の間、皆熱心に話を聞いていた。",
            "私は夏休みの間、ずっと実家にいました。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_3(self):
        """Test rule: 動詞「ます形」＋あがる"""
        expected_rule = "動詞「ます形」＋あがる"
        sentences = [
            "最新の企画書が出来あがったので、どうぞご覧ください。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_4(self):
        """Test rule: 名詞＋である＋一方"""
        expected_rule = "名詞＋である＋一方"
        sentences = [
            "田中さんは医科大学の教授である一方、小説家としても有名だ。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_5(self):
        """Test rule: 名詞＋動詞「た形」＋上で"""
        expected_rule = "名詞＋動詞「た形」＋上で"
        sentences = [
            "私が皆様のご意見を伺った上で、来週ご報告いたします。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_6(self):
        """Test rule: 動詞「ない形」＋ない＋うちに"""
        expected_rule = "動詞「ない形」＋ない＋うちに"
        sentences = [
            "弟と妹がいると集中できないから、今日は二人が帰ってこないうちに、宿題をやってしまう。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_7(self):
        """Test rule: 数量詞＋おきに"""
        expected_rule = "数量詞＋おきに"
        sentences = [
            "この道には5メートルおきに木が植えてある。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_8(self):
        """Test rule: 名詞＋から＋名詞＋にかけて"""
        expected_rule = "名詞＋から＋名詞＋にかけて"
        sentences = [
            "あの鳥が日本で見られるのは、11月から3月にかけてです。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_9(self):
        """Test rule: ～ぐらい～はない"""
        expected_rule = "～ぐらい～はない"
        sentences = [
            "戦争ぐらい残酷なものはない。",
        ]
        self._test_rule_matches(expected_rule, sentences)
