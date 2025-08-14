from langchain_community.utilities import SerpAPIWrapper
from fact_checker_bot.config.settings import SERPAPI_KEY

def search_web(query: str, num_results: int = 5) -> str:
    """Search the web using SerpAPI and return condensed evidence."""
    search = SerpAPIWrapper(serpapi_api_key=SERPAPI_KEY)
    
    # Use SerpAPI structured results
    results = search.results(query)  # dict
    if "organic_results" not in results:
        return "No search results found."

    condensed = []
    for item in results["organic_results"][:num_results]:
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        condensed.append(f"{title} — {snippet} ({link})")

    return "\n".join(condensed)
