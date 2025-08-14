from fact_checker_bot.src.fact_checker import fact_check_claim

def fact_check(claim: str) -> dict:
    """Run fact check and return raw result dict."""
    return fact_check_claim(claim)
