import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pytest
from unittest.mock import patch

@patch("fact_checker_bot.src.search_tools.search_web", return_value="Mocked search result for Obama")
@patch("fact_checker_bot.src.prompt_chains.llm.invoke", side_effect=lambda prompt: type("obj", (object,), {"content": "Mocked LLM output"})())
def test_fact_check_claim(mock_llm, mock_search):
    from fact_checker_bot.src.fact_checker import fact_check_claim
    claim = "Barack Obama was the 44th president of the USA"
    result = fact_check_claim(claim)
    assert isinstance(result, dict)
    assert "claim" in result
    assert result["claim"] == claim
    assert "final_answer" in result
