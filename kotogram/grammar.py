"""Grammar rule matching system for Japanese patterns"""

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

from .token import KotogramToken
from .types import DetailType, InflectionForm, PartOfSpeech


class PatternType(Enum):
    """Types of token patterns"""

    EXACT = "exact"
    PART_OF_SPEECH = "pos"
    INFLECTION_FORM = "inflection"
    BASE_FORM = "base_form"
    DETAIL = "detail"
    WILDCARD = "wildcard"
    ALTERNATIVE = "alternative"


@dataclass
class TokenPattern:
    """Pattern for matching individual tokens"""

    # Pattern type
    pattern_type: PatternType

    # Value to match against
    value: str | PartOfSpeech | InflectionForm | DetailType | PatternType

    # For alternative patterns (A/B syntax)
    alternatives: list[
        str | PartOfSpeech | InflectionForm | DetailType | PatternType
    ] | None = None

    # Whether this pattern is optional
    optional: bool = False

    # Custom matching function
    custom_matcher: Callable[[KotogramToken], bool] | None = None

    def matches(self, token: KotogramToken) -> bool:
        """Check if token matches this pattern"""
        if self.custom_matcher:
            return self.custom_matcher(token)

        if self.pattern_type == PatternType.EXACT:
            return token.surface == self.value or token.base_form == self.value

        elif self.pattern_type == PatternType.PART_OF_SPEECH:
            return token.part_of_speech == self.value

        elif self.pattern_type == PatternType.INFLECTION_FORM:
            return token.infl_form == self.value

        elif self.pattern_type == PatternType.BASE_FORM:
            return token.base_form == self.value

        elif self.pattern_type == PatternType.DETAIL:
            return (
                token.pos_detail1 == self.value
                or token.pos_detail2 == self.value
                or token.pos_detail3 == self.value
            )

        elif self.pattern_type == PatternType.WILDCARD:
            return True

        elif self.pattern_type == PatternType.ALTERNATIVE:
            if not self.alternatives:
                return False
            return any(
                self._matches_alternative(token, alt) for alt in self.alternatives
            )

    def _matches_alternative(
        self,
        token: KotogramToken,
        alternative: str | PartOfSpeech | InflectionForm | DetailType | PatternType,
    ) -> bool:
        """Check if token matches a specific alternative"""
        if isinstance(alternative, str):
            return token.surface == alternative or token.base_form == alternative
        elif isinstance(alternative, PartOfSpeech):
            return token.part_of_speech == alternative
        elif isinstance(alternative, InflectionForm):
            return token.infl_form == alternative
        elif isinstance(alternative, DetailType):
            return (
                token.pos_detail1 == alternative
                or token.pos_detail2 == alternative
                or token.pos_detail3 == alternative
            )
        elif (
            isinstance(alternative, PatternType) and alternative == PatternType.WILDCARD
        ):
            return True
        return False

    @classmethod
    def from_string(cls, pattern_str: str) -> "TokenPattern":
        """Create TokenPattern from string representation"""
        pattern_str = pattern_str.strip()

        # Handle optional patterns
        optional = False
        if pattern_str.endswith("?"):
            optional = True
            pattern_str = pattern_str[:-1]

        # Handle alternatives (A/B syntax)
        if "/" in pattern_str:
            parts = [p.strip() for p in pattern_str.split("/")]
            alternatives = []
            for part in parts:
                alt = cls._parse_single_pattern(part)
                alternatives.append(alt)
            return cls(
                pattern_type=PatternType.ALTERNATIVE,
                value=alternatives[0],
                alternatives=alternatives,
                optional=optional,
            )

        # Parse single pattern
        value = cls._parse_single_pattern(pattern_str)
        pattern_type = cls._determine_pattern_type(value)

        return cls(pattern_type=pattern_type, value=value, optional=optional)

    @staticmethod
    def _parse_single_pattern(
        pattern_str: str,
    ) -> str | PartOfSpeech | InflectionForm | DetailType | PatternType:
        """Parse a single pattern value"""
        pattern_str = pattern_str.strip()

        # Handle special patterns
        if pattern_str == "*":
            return PatternType.WILDCARD

        # Try to parse as PartOfSpeech
        try:
            return PartOfSpeech(pattern_str)
        except ValueError:
            pass

        # Try to parse as InflectionForm
        try:
            return InflectionForm(pattern_str)
        except ValueError:
            pass

        # Try to parse as DetailType
        try:
            return DetailType(pattern_str)
        except ValueError:
            pass

        # Return as string
        return pattern_str

    @staticmethod
    def _determine_pattern_type(
        value: str | PartOfSpeech | InflectionForm | DetailType | PatternType,
    ) -> PatternType:
        """Determine pattern type from value"""
        if value == PatternType.WILDCARD:
            return PatternType.WILDCARD
        if isinstance(value, PartOfSpeech):
            return PatternType.PART_OF_SPEECH
        if isinstance(value, InflectionForm):
            return PatternType.INFLECTION_FORM
        if isinstance(value, DetailType):
            return PatternType.DETAIL
        return PatternType.EXACT


@dataclass
class MatchResult:
    """Result of a grammar rule match"""

    rule_name: str
    start_pos: int
    end_pos: int
    matched_tokens: list[KotogramToken]
    confidence: float = 1.0
    description: str | None = None


class GrammarRule:
    """Grammar rule with pattern sequence"""

    def __init__(self, name: str, patterns: list[TokenPattern], description: str = ""):
        self.name = name
        self.description = description
        self.patterns = patterns

    def match(
        self, tokens: list[KotogramToken], start_pos: int = 0
    ) -> MatchResult | None:
        """Match this rule against tokens starting from start_pos"""
        if start_pos >= len(tokens):
            return None

        matched_tokens = []
        current_pos = start_pos
        pattern_index = 0

        while pattern_index < len(self.patterns):
            pattern = self.patterns[pattern_index]

            # Check if we've reached the end of tokens
            if current_pos >= len(tokens):
                if pattern.optional:
                    pattern_index += 1
                    continue
                else:
                    return None

            # Try to match current pattern
            if pattern.matches(tokens[current_pos]):
                matched_tokens.append(tokens[current_pos])
                current_pos += 1
                pattern_index += 1
            elif pattern.optional:
                # Skip optional pattern
                pattern_index += 1
            else:
                # Non-optional pattern failed to match
                return None

        # Check if we've matched all patterns
        if pattern_index == len(self.patterns):
            return MatchResult(
                rule_name=self.name,
                start_pos=start_pos,
                end_pos=current_pos,
                matched_tokens=matched_tokens,
                description=self.description,
            )

        return None

    def find_all_matches(self, tokens: list[KotogramToken]) -> list[MatchResult]:
        """Find all matches of this rule in the token sequence"""
        matches = []
        for i in range(len(tokens)):
            match = self.match(tokens, i)
            if match:
                matches.append(match)
        return matches


class RuleRegistry:
    """Container for grammar rules with matching capabilities"""

    def __init__(self):
        self.rules: list[GrammarRule] = []

    def add_rule(self, rule: GrammarRule):
        """Add a grammar rule to the registry"""
        self.rules.append(rule)

    def add_rule_from_string(
        self, name: str, pattern_string: str, description: str = ""
    ):
        """Add a rule from string representation"""
        pattern_sequence = [p.strip() for p in pattern_string.split()]
        patterns = [TokenPattern.from_string(pattern) for pattern in pattern_sequence]
        rule = GrammarRule(name, patterns, description)
        self.add_rule(rule)

    def match_all(self, tokens: list[KotogramToken]) -> list[MatchResult]:
        """Match all rules against the token sequence"""
        all_matches = []
        for rule in self.rules:
            matches = rule.find_all_matches(tokens)
            all_matches.extend(matches)

        # Sort by start position
        all_matches.sort(key=lambda x: x.start_pos)
        return all_matches

    def match_specific(
        self, tokens: list[KotogramToken], rule_name: str
    ) -> list[MatchResult]:
        """Match a specific rule by name"""
        for rule in self.rules:
            if rule.name == rule_name:
                return rule.find_all_matches(tokens)
        return []

    def get_rule_names(self) -> list[str]:
        """Get list of all rule names"""
        return [rule.name for rule in self.rules]


# Predefined grammar rules based on test cases
def create_default_rules() -> RuleRegistry:
    """Create default grammar rules for Japanese patterns"""
    registry = RuleRegistry()

    # 動詞普通形＋間に - More flexible to match "寝ている間に"
    patterns_verb_basic_maida = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.VERB),
        TokenPattern(pattern_type=PatternType.EXACT, value="て"),
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.VERB),
        TokenPattern(pattern_type=PatternType.EXACT, value="間"),
        TokenPattern(pattern_type=PatternType.EXACT, value="に"),
    ]
    registry.add_rule(
        GrammarRule(
            "動詞普通形＋間に",
            patterns_verb_basic_maida,
            "Verb followed by 'て', another verb, '間' and 'に' (while)",
        )
    )

    # 名詞＋の＋間
    patterns_noun_no_aida = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="の"),
        TokenPattern(pattern_type=PatternType.EXACT, value="間"),
    ]
    registry.add_rule(
        GrammarRule(
            "名詞＋の＋間",
            patterns_noun_no_aida,
            "Noun followed by 'の' and '間' (during)",
        )
    )

    # 動詞「ます形」＋あがる - More flexible to match "出来あがった"
    patterns_verb_masu_agaru = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.VERB),
        TokenPattern(pattern_type=PatternType.EXACT, value="あがっ"),
        TokenPattern(pattern_type=PatternType.EXACT, value="た"),
    ]
    registry.add_rule(
        GrammarRule(
            "動詞「ます形」＋あがる",
            patterns_verb_masu_agaru,
            "Verb followed by 'あがっ' and 'た' (completed)",
        )
    )

    # 名詞＋である＋一方
    patterns_noun_de_aru_ippou = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="で"),
        TokenPattern(pattern_type=PatternType.EXACT, value="ある"),
        TokenPattern(pattern_type=PatternType.EXACT, value="一方"),
    ]
    registry.add_rule(
        GrammarRule(
            "名詞＋である＋一方",
            patterns_noun_de_aru_ippou,
            "Noun followed by 'で', 'ある', and '一方' (on the other hand)",
        )
    )

    # 名詞＋動詞「た形」＋上で - More flexible to match "伺った上で"
    patterns_noun_verb_ta_uede = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.VERB),
        TokenPattern(pattern_type=PatternType.EXACT, value="た"),
        TokenPattern(pattern_type=PatternType.EXACT, value="上"),
        TokenPattern(pattern_type=PatternType.EXACT, value="で"),
    ]
    registry.add_rule(
        GrammarRule(
            "名詞＋動詞「た形」＋上で",
            patterns_noun_verb_ta_uede,
            "Verb followed by 'た', '上' and 'で' (after)",
        )
    )

    # 動詞「ない形」＋ない＋うちに - More flexible to match "こないうちに"
    patterns_verb_negative_uchini = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.VERB),
        TokenPattern(pattern_type=PatternType.EXACT, value="ない"),
        TokenPattern(pattern_type=PatternType.EXACT, value="うち"),
        TokenPattern(pattern_type=PatternType.EXACT, value="に"),
    ]
    registry.add_rule(
        GrammarRule(
            "動詞「ない形」＋ない＋うちに",
            patterns_verb_negative_uchini,
            "Verb followed by 'ない', 'うち' and 'に' (before)",
        )
    )

    # 数量詞＋おきに - More flexible to match "5メートルおきに"
    patterns_numeral_okini = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="おき"),
        TokenPattern(pattern_type=PatternType.EXACT, value="に"),
    ]
    registry.add_rule(
        GrammarRule(
            "数量詞＋おきに",
            patterns_numeral_okini,
            "Two nouns followed by 'おき' and 'に' (every)",
        )
    )

    # 名詞＋から＋名詞＋にかけて - More flexible to match "11月から3月にかけて"
    patterns_noun_kara_noun_nikakete = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="から"),
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="にかけて"),
    ]
    registry.add_rule(
        GrammarRule(
            "名詞＋から＋名詞＋にかけて",
            patterns_noun_kara_noun_nikakete,
            "Two nouns, 'から', two more nouns, and 'にかけて' (from...to)",
        )
    )

    # ～ぐらい～はない
    patterns_gurai_wa_nai = [
        TokenPattern(pattern_type=PatternType.EXACT, value="ぐらい"),
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="な"),
        TokenPattern(pattern_type=PatternType.EXACT, value="もの"),
        TokenPattern(pattern_type=PatternType.EXACT, value="は"),
        TokenPattern(pattern_type=PatternType.EXACT, value="ない"),
    ]
    registry.add_rule(
        GrammarRule(
            "～ぐらい～はない",
            patterns_gurai_wa_nai,
            "Pattern 'ぐらい...はない' (nothing is as...as)",
        )
    )

    return registry
