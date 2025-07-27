#!/usr/bin/env python3
"""
FastAPI server for Kotogram Japanese morphological analysis and grammar matching
"""

from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from kotogram.analyzer import KotogramAnalyzer
from kotogram.grammar import GrammarMatchResult, RuleRegistry
from kotogram.token import KotogramToken

# Initialize FastAPI app
app = FastAPI(
    title="Kotogram API",
    description="Japanese morphological analysis and grammar matching API",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Initialize analyzer and rule registry
analyzer = KotogramAnalyzer()
rule_registry = RuleRegistry()

# Try to load rules from the rules directory if it exists
rules_dir = Path("rules")
if rules_dir.exists() and rules_dir.is_dir():
    try:
        rule_registry.load_rules_from_directory("rules")
        print(f"Loaded {len(rule_registry.rules)} grammar rules")
    except Exception as e:
        print(f"Warning: Could not load grammar rules: {e}")
else:
    print("Warning: No rules directory found. Grammar matching will not work.")


# Pydantic models for API requests and responses
class ParseRequest(BaseModel):
    text: str


class ParseResponse(BaseModel):
    text: str
    tokens: list[KotogramToken]


class MatchRequest(BaseModel):
    tokens: list[KotogramToken]


class MatchResponse(BaseModel):
    tokens: list[KotogramToken]
    matches: list[GrammarMatchResult]


class ParseAndMatchRequest(BaseModel):
    text: str


class ParseAndMatchResponse(BaseModel):
    text: str
    tokens: list[KotogramToken]
    matches: list[GrammarMatchResult]


class HealthResponse(BaseModel):
    status: str
    rules_loaded: int
    available_rules: list[str]


@app.post("/parse", response_model=ParseResponse)
async def parse_text(request: ParseRequest):
    """Parse Japanese text into tokens"""
    try:
        if not request.text or not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")

        # Parse the text
        tokens = analyzer.parse_text(request.text)

        return ParseResponse(text=request.text, tokens=tokens)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/match", response_model=MatchResponse)
async def match_grammar(request: MatchRequest):
    """Match tokens against grammar rules"""
    try:
        if not request.tokens:
            raise HTTPException(status_code=400, detail="Tokens list cannot be empty")

        # Match against grammar rules
        matches = rule_registry.find_all_matches(request.tokens)

        return MatchResponse(tokens=request.tokens, matches=matches)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/parse-and-match", response_model=ParseAndMatchResponse)
async def parse_and_match(request: ParseAndMatchRequest):
    """Parse Japanese text into tokens and match against grammar rules"""
    try:
        if not request.text or not request.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")

        # Parse the text
        tokens = analyzer.parse_text(request.text)

        # Match against grammar rules
        matches = rule_registry.find_all_matches(tokens)

        return ParseAndMatchResponse(text=request.text, tokens=tokens, matches=matches)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        rules_loaded=len(rule_registry.rules),
        available_rules=rule_registry.get_rule_names(),
    )


if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=8080)
