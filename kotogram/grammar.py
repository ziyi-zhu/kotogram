"""Grammar rule matching system for Japanese patterns"""

from dataclasses import dataclass
from enum import Enum

from .token import KotogramToken
from .types import InflectionForm, PartOfSpeech, POSDetailType


class PatternType(Enum):
    """Types of token patterns"""

    EXACT = "exact"
    PART_OF_SPEECH = "pos"
    INFLECTION_FORM = "inflection"
    BASE_FORM = "base_form"
    DETAIL = "detail"
    WILDCARD = "wildcard"
    MULTI_WILDCARD = "multi_wildcard"
    ALTERNATIVE = "alternative"


@dataclass
class TokenPattern:
    """Pattern for matching individual tokens"""

    # Pattern type
    pattern_type: PatternType

    # Value to match against
    value: str | PartOfSpeech | InflectionForm | POSDetailType | PatternType | None

    # For alternative patterns (A/B syntax)
    alternatives: (
        list[str | PartOfSpeech | InflectionForm | POSDetailType | PatternType] | None
    ) = None

    # Whether this pattern is optional
    optional: bool = False

    def matches(self, token: KotogramToken) -> bool:
        """Check if token matches this pattern"""
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

        elif self.pattern_type == PatternType.MULTI_WILDCARD:
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
        alternative: str | PartOfSpeech | InflectionForm | POSDetailType | PatternType,
    ) -> bool:
        """Check if token matches a specific alternative"""
        if isinstance(alternative, str):
            return token.surface == alternative or token.base_form == alternative
        elif isinstance(alternative, PartOfSpeech):
            return token.part_of_speech == alternative
        elif isinstance(alternative, InflectionForm):
            return token.infl_form == alternative
        elif isinstance(alternative, POSDetailType):
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

    def __init__(
        self,
        name: str,
        patterns: list[TokenPattern],
        description: str = "",
        tag: str | None = None,
    ):
        self.name = name
        self.patterns = patterns
        self.description = description
        self.tag = tag

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

            # MULTI_WILDCARD: match any number of tokens (including zero) until next pattern matches
            if pattern.pattern_type == PatternType.MULTI_WILDCARD:
                next_index = pattern_index + 1
                if next_index == len(self.patterns):
                    # If MULTI_WILDCARD is last, consume all remaining tokens
                    matched_tokens.extend(tokens[current_pos:])
                    current_pos = len(tokens)
                    pattern_index += 1
                    continue
                # Try to find a match for the remaining pattern sequence
                for skip in range(0, len(tokens) - current_pos + 1):
                    if current_pos + skip >= len(tokens):
                        break

                    # Create a sub-rule with remaining patterns and test it
                    remaining_patterns = self.patterns[next_index:]
                    if remaining_patterns:
                        temp_rule = GrammarRule("temp", remaining_patterns)
                        temp_match = temp_rule.match(tokens, current_pos + skip)
                        if temp_match:
                            # We found a valid match for the remaining patterns
                            # Add skipped tokens as matched
                            matched_tokens.extend(
                                tokens[current_pos : current_pos + skip]
                            )
                            # Add the remaining matched tokens
                            matched_tokens.extend(temp_match.matched_tokens)
                            return MatchResult(
                                rule_name=self.name,
                                start_pos=start_pos,
                                end_pos=temp_match.end_pos,
                                matched_tokens=matched_tokens,
                                description=self.description,
                            )
                    else:
                        # No remaining patterns, so we match everything
                        matched_tokens.extend(tokens[current_pos:])
                        return MatchResult(
                            rule_name=self.name,
                            start_pos=start_pos,
                            end_pos=len(tokens),
                            matched_tokens=matched_tokens,
                            description=self.description,
                        )

                return None

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

    patterns_noun_no_aida = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="の"),
        TokenPattern(pattern_type=PatternType.EXACT, value="間"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～間",
            patterns=patterns_noun_no_aida,
            description="名詞＋の＋間",
            tag="N3-1",
        )
    )

    patterns_verb_basic_maida = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.VERB),
        TokenPattern(pattern_type=PatternType.EXACT, value="間"),
        TokenPattern(pattern_type=PatternType.EXACT, value="に"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～間に",
            patterns=patterns_verb_basic_maida,
            description="動詞普通形＋間に",
            tag="N3-2",
        )
    )

    patterns_verb_masu_agaru = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.VERB),
        TokenPattern(pattern_type=PatternType.EXACT, value="あがる"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～あがる",
            patterns=patterns_verb_masu_agaru,
            description="動詞「ます形」＋あがる",
            tag="N3-3",
        )
    )

    patterns_noun_de_aru_ippou = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="で"),
        TokenPattern(pattern_type=PatternType.EXACT, value="ある"),
        TokenPattern(pattern_type=PatternType.EXACT, value="一方"),
        TokenPattern(pattern_type=PatternType.EXACT, value="で", optional=True),
    ]
    registry.add_rule(
        GrammarRule(
            name="～一方（で）",
            patterns=patterns_noun_de_aru_ippou,
            description="名詞＋である＋一方（で）",
            tag="N3-5",
        )
    )

    patterns_noun_verb_ta_uede = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.VERB),
        TokenPattern(pattern_type=PatternType.EXACT, value="た"),
        TokenPattern(pattern_type=PatternType.EXACT, value="上"),
        TokenPattern(pattern_type=PatternType.EXACT, value="で"),
        TokenPattern(pattern_type=PatternType.EXACT, value="の", optional=True),
    ]
    registry.add_rule(
        GrammarRule(
            name="～上で（の）",
            patterns=patterns_noun_verb_ta_uede,
            description="名詞＋動詞「た形」＋上で（の）",
            tag="N3-7",
        )
    )

    patterns_verb_negative_uchini = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.VERB),
        TokenPattern(pattern_type=PatternType.EXACT, value="ない"),
        TokenPattern(pattern_type=PatternType.EXACT, value="うち"),
        TokenPattern(pattern_type=PatternType.EXACT, value="に"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～ないうちに",
            patterns=patterns_verb_negative_uchini,
            description="動詞「ない形」＋ない＋うちに",
            tag="N3-10",
        )
    )

    patterns_numeral_okini = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="おき"),
        TokenPattern(pattern_type=PatternType.EXACT, value="に"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～おきに",
            patterns=patterns_numeral_okini,
            description="数量詞＋おきに",
            tag="N3-12",
        )
    )

    patterns_noun_kara_noun_nikakete = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="から"),
        TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(pattern_type=PatternType.EXACT, value="にかけて"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～から～にかけて",
            patterns=patterns_noun_kara_noun_nikakete,
            description="名詞＋から＋名詞＋にかけて",
            tag="N3-19",
        )
    )

    patterns_gurai_wa_nai = [
        TokenPattern(pattern_type=PatternType.PART_OF_SPEECH, value=PartOfSpeech.NOUN),
        TokenPattern(
            pattern_type=PatternType.ALTERNATIVE,
            value="ぐらい",
            alternatives=["ぐらい", "くらい"],
        ),
        TokenPattern(pattern_type=PatternType.MULTI_WILDCARD, value=None),
        TokenPattern(pattern_type=PatternType.EXACT, value="は"),
        TokenPattern(pattern_type=PatternType.EXACT, value="い", optional=True),
        TokenPattern(pattern_type=PatternType.EXACT, value="ない"),
    ]
    registry.add_rule(
        GrammarRule(
            name="～くらい／ぐらい",
            patterns=patterns_gurai_wa_nai,
            description="～ぐらい～はない",
            tag="N3-23",
        )
    )

    return registry
