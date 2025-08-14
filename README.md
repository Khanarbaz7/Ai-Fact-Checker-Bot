# AI Fact-Checker Bot

An intelligent fact-checking bot built with **LangChain**, **web search integration**, and **prompt chaining** to verify claims and provide accurate, evidence-backed answers.  
The bot uses advanced reasoning steps to identify assumptions, validate them with online sources, and synthesize a final verified response.

---

## 📌 Features

- **LangChain Integration** – Uses chat models like OpenAI GPT, Anthropic Claude, or open-source LLMs.
- **Prompt Chaining** – Breaks down claims into assumptions, verifies them, and refines answers.
- **Web Search** – Retrieves real-time information via DuckDuckGo or SerpAPI.
- **Multiple Interfaces** – Works with Streamlit, Gradio, or CLI.
- **Source Credibility Assessment** – Evaluates reliability based on domain authority & recency.
- **Claim Classification** – Categorizes claims as factual, opinion, mixed, or unverifiable.
- **Error Handling & Caching** – Graceful fallbacks for API errors and optimized repeated queries.

---

## 🛠️ Tech Stack

- **Python 3.11+**
- [LangChain](https://python.langchain.com/)
- [Streamlit](https://docs.streamlit.io/) / [Gradio](https://gradio.app/docs/)
-  `requests` / `beautifulsoup4`
- `python-dotenv` for API key management

## 📂 Project Structure
```
fact_checker_bot/
├── .env
├── .env.example
├── .gitignore
├── app.py
├── main.py
├── runner.py
├── requirements.txt
├── README.md
├── assets/
│ ├── streamlit_home_placeholder.png
│ ├── fact_check_example_placeholder.png
│ ├── evidence_view_placeholder.png
├── fact_checker_bot/
│ ├── config/ # Config files (prompts, settings)
│ ├── examples/ # Example queries & notebooks
│ ├── src/ # Main bot logic, search tools, prompt chains, utils
│ ├── tests/ # Unit tests
├── logs/
│ ├── fact_checks.log
```
---

## ⚙️ Installation

# Clone the repository
git clone https://github.com/your-username/ai-fact-checker-bot.git
cd ai-fact-checker-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys inside .env
---
#Usage 
streamlit run src/ui/streamlit_app.py

📸 Screenshots
## 📸 Screenshots

**Home Interface (Streamlit)**  
![Streamlit Home](assets/streamlit_home_placeholder.png)

**Fact Verification Example**  
![Fact Check Example](assets/fact_check_example_placeholder.png)

**Search Results Evidence View**  
![Evidence View](assets/evidence_view_placeholder.png)

##Future Improvements:

Multi-language support

Voice input/output

Batch fact-checking from uploaded documents

Integration with social media APIs for real-time claim detection

##  Acknowledgments

- [Nikhil Sharma](https://www.linkedin.com/in/-nikhil/) – Project concept and guidance  
- [LangChain Documentation](https://python.langchain.com/) – Framework reference  
- [Prompt Engineering Guide](https://www.promptingguide.ai/) – Prompt design best practices  
- [SerpAPI](https://serpapi.com/) – Web search integration
  


