🔬 ResearchAI Pipeline
An end-to-end multi-agent research system that automates the entire workflow:

Search → Scrape → Write → Critique

Built using LangChain + Groq (LLMs) + Streamlit, this app performs real-time research and generates structured reports with AI-driven evaluation.

🚀 Features
🔍 Search Agent – Finds relevant, recent web data using Tavily

📄 Reader Agent – Scrapes and extracts clean content from URLs

✍️ Writer Chain – Generates structured research reports

🧐 Critic Chain – Evaluates report quality with scoring and feedback

⚡ Fast LLM inference via Groq (LLaMA 3.1)

🎨 Modern Streamlit UI with live pipeline tracking

🧠 Architecture
The system follows a 4-step AI pipeline:

Search Agent

Uses web_search tool

Retrieves top results (titles, URLs, snippets)

Reader Agent

Uses scrape_url tool

Extracts detailed content from best source

Writer Chain

Combines search + scraped data

Produces structured report:

Introduction

Key Findings

Conclusion

Sources

Critic Chain

Reviews report

Outputs:

Score (X/10)

Strengths

Areas to Improve

Final verdict

🛠️ Tech Stack
LLM: Groq (LLaMA 3.1 8B Instant)

Framework: LangChain

Frontend: Streamlit

Search API: Tavily

Web Scraping: BeautifulSoup + Requests

Environment: Python + dotenv

📁 Project Structure
text
.
├── app.py          # Streamlit UI + pipeline execution
├── agents.py       # Agent + chain definitions
├── tools.py        # Web search and scraping tools
├── .env            # API keys (not committed)
⚙️ Setup
1. Clone Repository
text
git clone <repo-url>
cd research-ai
2. Install Dependencies
text
pip install -r requirements.txt
3. Add Environment Variables
Create a .env file:

text
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
⚠️ Important: Do NOT hardcode API keys in code (security risk)

▶️ Run the App
text
streamlit run app.py
Then open in browser:

text
http://localhost:8501
🧪 Example Workflow
Input:

text
"Latest advances in multimodal LLMs"
Pipeline Output:

Search results from web

Scraped article content

Structured research report

Critic evaluation (e.g., Score: 8/10)

🔧 Key Components
Agents (agents.py)
build_search_agent() → Uses web search tool

build_reader_agent() → Uses scraping tool

writer_chain → Report generation

critic_chain → Report evaluation

Tools (tools.py)
web_search(query) → Tavily-powered search

scrape_url(url) → Clean text extraction from webpages

UI (app.py)
Interactive pipeline execution

Progress tracking (4 steps)

Tabs:

Full Report

Source Data

Critic Review

Downloadable report

⚠️ Notes
Ensure stable internet (required for search + scraping)

Some websites may block scraping

Output quality depends on search results

API rate limits may apply

📌 Future Improvements
Multi-source scraping instead of single URL

RAG-based memory (vector DB)

Citation verification

Async pipeline for faster execution

Agent orchestration (LangGraph)
