import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pytest
from unittest.mock import patch

@patch("fact_checker_bot.src.search_tools.SerpAPIWrapper.run", return_value="Mocked search result about USA president")
def test_search_web_returns_results(mock_search):
    from fact_checker_bot.src.search_tools import search_web
    query = "current president of USA"
    results = search_web(query)
    assert results == "Mocked search result about USA president"
