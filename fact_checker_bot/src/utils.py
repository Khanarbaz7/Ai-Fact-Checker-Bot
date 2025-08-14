from langchain_google_genai import ChatGoogleGenerativeAI
from fact_checker_bot.config.settings import GEMINI_API_KEY, DEFAULT_MODEL, DEFAULT_TEMPERATURE, MAX_TOKENS


def get_gemini_llm(model_name=DEFAULT_MODEL, temperature=DEFAULT_TEMPERATURE):
    """Return a configured Gemini LLM instance."""
    return ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=GEMINI_API_KEY,
        temperature=temperature,
        max_output_tokens=MAX_TOKENS
    )
