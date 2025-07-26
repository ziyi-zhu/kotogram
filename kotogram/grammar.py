"""Grammar rule matching system for Japanese patterns"""

import json
from pathlib import Path

from pydantic import BaseModel, Field

from .token import KotogramToken
from .types import InflectionForm, InflectionType, PartOfSpeech, POSDetailType


class TokenPattern(BaseModel):
    """Pattern for matching individual tokens using Pydantic"""

    # Value that matches either surface form or base form
    value: str | None = Field(
        None, description="Value to match against surface or base form"
    )

    # Part of speech (品詞)
    part_of_speech: PartOfSpeech | None = Field(
        None, description="Part of speech to match"
    )

    # Single detailed part of speech (instead of three)
    pos_detail: POSDetailType | None = Field(
        None, description="Detailed part of speech to match"
    )

    # Inflection type (活用型)
    infl_type: InflectionType | None = Field(
        None, description="Inflection type to match"
    )

    # Inflection form (活用形)
    infl_form: InflectionForm | None = Field(
        None, description="Inflection form to match"
    )

    # Alternative patterns (list of TokenPattern objects)
    alternatives: list["TokenPattern"] | None = Field(
        None, description="Alternative patterns"
    )

    # Whether this pattern is optional
    optional: bool = Field(False, description="Whether this pattern is optional")

    def matches(self, token: KotogramToken) -> bool:
        """Check if token matches this pattern"""
        # Check if pattern is optional (always matches)
        if self.optional and self._is_empty_pattern():
            return True

        # Check if this is a multi-wildcard (all fields are None)
        if self._is_multi_wildcard():
            return True

        # Check alternatives first
        if self.alternatives:
            for alt in self.alternatives:
                if alt.matches(token):
                    return True

        # Check main pattern - all non-None fields must match
        return self._matches_main_pattern(token)

    def _is_empty_pattern(self) -> bool:
        """Check if this is an empty pattern (only used with optional=True)"""
        return (
            self.value is None
            and self.part_of_speech is None
            and self.pos_detail is None
            and self.infl_type is None
            and self.infl_form is None
            and not self.alternatives
        )

    def _is_multi_wildcard(self) -> bool:
        """Check if this is a multi-wildcard pattern (all fields are None)"""
        return (
            self.value is None
            and self.part_of_speech is None
            and self.pos_detail is None
            and self.infl_type is None
            and self.infl_form is None
            and not self.alternatives
            and not self.optional
        )

    def _matches_main_pattern(self, token: KotogramToken) -> bool:
        """Check if token matches the main pattern (all non-None fields must match)"""
        # Check value (matches either surface or base form)
        if self.value is not None:
            if token.surface != self.value and token.base_form != self.value:
                return False

        # Check part of speech
        if self.part_of_speech is not None:
            if token.part_of_speech != self.part_of_speech:
                return False

        # Check detailed part of speech (matches any of the three)
        if self.pos_detail is not None:
            if (
                token.pos_detail1 != self.pos_detail
                and token.pos_detail2 != self.pos_detail
                and token.pos_detail3 != self.pos_detail
            ):
                return False

        # Check inflection type
        if self.infl_type is not None:
            if token.infl_type != self.infl_type:
                return False

        # Check inflection form
        if self.infl_form is not None:
            if token.infl_form != self.infl_form:
                return False

        return True


# Enable forward references for alternatives field
TokenPattern.model_rebuild()


class MatchResult(BaseModel):
    """Result of a grammar rule match"""

    rule: "GrammarRule" = Field(..., description="The matched grammar rule")
    start_pos: int = Field(..., description="Start position in token sequence")
    end_pos: int = Field(..., description="End position in token sequence")
    matched_tokens: list[KotogramToken] = Field(
        ..., description="List of matched tokens"
    )

    @property
    def rule_name(self) -> str:
        """Get the rule name for backward compatibility"""
        return self.rule.name

    @property
    def description(self) -> str:
        """Get the rule description for backward compatibility"""
        return self.rule.description


class GrammarRule(BaseModel):
    """Grammar rule with pattern sequence using Pydantic"""

    name: str = Field(..., description="Name of the grammar rule")
    patterns: list[TokenPattern] = Field(
        ..., description="List of token patterns to match"
    )
    description: str = Field("", description="Description of the grammar rule")
    tag: str | None = Field(None, description="Optional tag for the rule")

    def model_post_init(self, __context) -> None:
        """Validate patterns after model initialization"""
        self._validate_patterns()

    def _validate_patterns(self):
        """Validate that there is at most one multi-wildcard per rule"""
        multi_wildcard_count = sum(
            1 for pattern in self.patterns if pattern._is_multi_wildcard()
        )
        if multi_wildcard_count > 1:
            raise ValueError(
                f"Rule '{self.name}' has {multi_wildcard_count} multi-wildcards. Only one multi-wildcard per rule is allowed."
            )

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
            if pattern._is_multi_wildcard():
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
                        temp_rule = GrammarRule(
                            name="temp", patterns=remaining_patterns
                        )
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
                                rule=self,
                                start_pos=start_pos,
                                end_pos=temp_match.end_pos,
                                matched_tokens=matched_tokens,
                            )
                    else:
                        # No remaining patterns, so we match everything
                        matched_tokens.extend(tokens[current_pos:])
                        return MatchResult(
                            rule=self,
                            start_pos=start_pos,
                            end_pos=len(tokens),
                            matched_tokens=matched_tokens,
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
                rule=self,
                start_pos=start_pos,
                end_pos=current_pos,
                matched_tokens=matched_tokens,
            )

        return None

    def find_all_matches(self, tokens: list[KotogramToken]) -> list[MatchResult]:
        """Find all matches of this rule in the token sequence"""
        matches: list[MatchResult] = []
        for i in range(len(tokens)):
            match = self.match(tokens, i)
            if match:
                # Check if this match overlaps with any existing match
                overlaps = False
                for existing_match in matches:
                    if (
                        match.start_pos < existing_match.end_pos
                        and match.end_pos > existing_match.start_pos
                    ):
                        overlaps = True
                        # Keep the longer match
                        if len(match.matched_tokens) > len(
                            existing_match.matched_tokens
                        ):
                            matches.remove(existing_match)
                            matches.append(match)
                        break

                if not overlaps:
                    matches.append(match)
        return matches


class RuleRegistry:
    """Container for grammar rules with matching capabilities"""

    def __init__(self):
        self.rules: list[GrammarRule] = []

    def add_rule(self, rule: GrammarRule):
        """Add a grammar rule to the registry"""
        self.rules.append(rule)

    def load_rules_from_directory(self, directory_path: str) -> None:
        """Load rules from JSON files in a directory"""
        rules_dir = Path(directory_path)
        if not rules_dir.exists():
            raise FileNotFoundError(f"Rules directory not found: {directory_path}")

        if not rules_dir.is_dir():
            raise NotADirectoryError(f"Path is not a directory: {directory_path}")

        rule_files = list(rules_dir.glob("*.json"))
        if not rule_files:
            raise FileNotFoundError(f"No JSON rule files found in: {directory_path}")

        for rule_file in rule_files:
            try:
                with open(rule_file, "r", encoding="utf-8") as f:
                    rule_data = json.load(f)

                # Create rule directly from JSON data using Pydantic
                rule = GrammarRule(**rule_data)
                self.add_rule(rule)

            except Exception as e:
                raise ValueError(f"Error loading rule from {rule_file}: {e}")

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
