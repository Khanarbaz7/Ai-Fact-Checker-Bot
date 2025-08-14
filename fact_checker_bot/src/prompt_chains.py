import re
import json
from fact_checker_bot.src.utils import get_gemini_llm
from fact_checker_bot.src.search_tools import search_web

llm = get_gemini_llm()

def initial_response(claim: str) -> str:
    return llm.invoke(f"Provide a brief factual answer to: {claim}").content

def extract_assumptions(answer: str) -> list:
    prompt = f"""
    Extract the key factual assumptions made in the following answer.
    Return them strictly as a JSON list of short strings.

    Answer:
    {answer}
    """
    raw_output = llm.invoke(prompt).content.strip()
    raw_output = re.sub(r"```(?:json)?", "", raw_output).strip()

    try:
        assumptions = json.loads(raw_output)
        if isinstance(assumptions, list) and assumptions:
            return [a.strip() for a in assumptions if a.strip()]
    except json.JSONDecodeError:
        pass

    return [answer.strip()]


def verify_assumption(assumption: str) -> dict:
    """Verify an assumption using web search and return clean verdict, explanation, and evidence."""
    search_results = search_web(assumption)

    prompt = f"""
    Based on the following search results, verify this assumption: "{assumption}".

    Return ONLY a JSON object with exactly the following keys:
    - "verdict": one of "True", "False", or "Uncertain"
    - "explanation": a short explanation (2–4 sentences)
    - "evidence_links": a list of URLs (from the search results) supporting your verdict

    Search Results:
    {search_results}
    """

    raw_output = llm.invoke(prompt).content.strip()

    raw_output = re.sub(r"```(?:json)?", "", raw_output).strip()

    try:
        parsed = json.loads(raw_output)
        verdict = parsed.get("verdict", "").strip()
        explanation = parsed.get("explanation", "").strip()
        evidence_links = parsed.get("evidence_links", [])
        if not isinstance(evidence_links, list):
            evidence_links = [str(evidence_links)]
    except json.JSONDecodeError:
        verdict = "Uncertain"
        explanation = raw_output
        evidence_links = []

    return {
        "assumption": assumption,
        "verdict": verdict,
        "explanation": explanation,
        "evidence_links": evidence_links
    }


def final_synthesis(claim: str, assumptions_results: list) -> str:
    return llm.invoke(
        f"Based on these verified assumptions:\n{assumptions_results}\nProvide a refined fact-check for: {claim}"
    ).content
