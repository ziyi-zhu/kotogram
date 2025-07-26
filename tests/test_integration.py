"""Integration tests for Kotogram with real Japanese text"""

import pytest

from kotogram import KotogramAnalyzer, create_default_rules


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
            print(f"DEBUG: found_rules for '{rule_name}':", found_rules)
            assert (
                rule_name in found_rules
            ), f"Expected rule '{rule_name}' not found in matches: {found_rules}"

    def test_rule_1(self):
        """Test rule: ～間に"""
        expected_rule = "～間に"
        sentences = [
            "赤ちゃんが寝ている間に、洗濯をしました。",
            "日本に留学している間に富士山に登りたい。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_2(self):
        """Test rule: ～間"""
        expected_rule = "～間"
        sentences = [
            "山田先生の講演の間、皆熱心に話を聞いていた。",
            "私は夏休みの間、ずっと実家にいました。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_3(self):
        """Test rule: ～あがる"""
        expected_rule = "～あがる"
        sentences = [
            "最新の企画書が出来あがったので、どうぞご覧ください。",
            "彼氏へのマフラーが編みあがった。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_4(self):
        """Test rule: ～一方（で）"""
        expected_rule = "～一方（で）"
        sentences = [
            "田中さんは医科大学の教授である一方、小説家としても有名だ。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_5(self):
        """Test rule: ～上で（の）"""
        expected_rule = "～上で（の）"
        sentences = [
            "私が皆様のご意見を伺った上で、来週ご報告いたします。",
            "それぞれの説明をよく聞いた上で、旅行のコースを選びたいと思います。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_6(self):
        """Test rule: ～ないうちに"""
        expected_rule = "～ないうちに"
        sentences = [
            "弟と妹がいると集中できないから、今日は二人が帰ってこないうちに、宿題をやってしまう。",
            "昨日のパーティーは、友だちと話していたら、ほとんど何も食べないうちに終わってしまって、後でおなかがすいてしまった。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_7(self):
        """Test rule: ～おきに"""
        expected_rule = "～おきに"
        sentences = [
            "この道には5メートルおきに木が植えてある。",
            "新宿へ向かう電車は3分おきに出ている。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_8(self):
        """Test rule: ～から～にかけて"""
        expected_rule = "～から～にかけて"
        sentences = [
            "あの鳥が日本で見られるのは、11月から3月にかけてです。",
            "東北地方から北海道にかけて今夜は大雪になるでしょう。",
        ]
        self._test_rule_matches(expected_rule, sentences)

    def test_rule_9(self):
        """Test rule: ～くらい／ぐらい"""
        expected_rule = "～くらい／ぐらい"
        sentences = ["戦争ぐらい残酷なものはない。", "彼くらい努力する人はいない。"]
        self._test_rule_matches(expected_rule, sentences)
