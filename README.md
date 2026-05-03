# 🔬 ResearchAI Pipeline

An end-to-end **multi-agent research system** that automates the entire workflow:

**Search → Scrape → Write → Critique**

Built using **LangChain + Groq (LLMs) + Streamlit**, this app performs real-time research and generates structured reports with AI-driven evaluation.

***

## 🚀 Features

- 🔍 **Search Agent** – Finds relevant, recent web data using Tavily
- 📄 **Reader Agent** – Scrapes and extracts clean content from URLs
- ✍️ **Writer Chain** – Generates structured research reports
- 🧐 **Critic Chain** – Evaluates report quality with scoring and feedback
- ⚡ **Fast LLM inference** via Groq (LLaMA 3.1)
- 🎨 **Modern Streamlit UI** with live pipeline tracking

***

## 🧠 Architecture

The system follows a **4-step AI pipeline**:

### 1. Search Agent

- Uses `web_search` tool
- Retrieves top results (titles, URLs, snippets)

### 2. Reader Agent

- Uses `scrape_url` tool
- Extracts detailed content from the best source

### 3. Writer Chain

- Combines search + scraped data
- Produces a structured report with:
  - Introduction
  - Key Findings
  - Conclusion
  - Sources

### 4. Critic Chain

- Reviews the generated report
- Outputs:
  - Score (X/10)
  - Strengths
  - Areas to Improve
  - Final verdict

***

## 🛠️ Tech Stack

- **LLM**: Groq (LLaMA 3.1 8B Instant)
- **Framework**: LangChain
- **Frontend**: Streamlit
- **Search API**: Tavily
- **Web Scraping**: BeautifulSoup + Requests
- **Environment**: Python + dotenv

***

## 📁 Project Structure

```bash
.
├── app.py          # Streamlit UI + pipeline execution
├── agents.py       # Agent and chain definitions
├── tools.py        # Web search and scraping tools
├── .env            # API keys (not committed)
```

***

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone (https://github.com/Mehta-Kartik/Multi_Agent_Researcher.git)
cd research-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

> ⚠️ **Important:** Do not hardcode API keys in source code.

***

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at:

```text
http://localhost:8501
```

***

## 🧪 Example Workflow

**Input:**

```text
Latest advances in multimodal LLMs
```

**Pipeline Output:**

- Search results from the web
- Scraped article content
- Structured research report
- Critic evaluation (for example, Score: 8/10)

***

## 🔧 Key Components

### `agents.py`

- `build_search_agent()` → Uses the web search tool
- `build_reader_agent()` → Uses the scraping tool
- `writer_chain` → Generates the research report
- `critic_chain` → Evaluates the generated report

### `tools.py`

- `web_search(query)` → Tavily-powered search
- `scrape_url(url)` → Clean text extraction from webpages

### `app.py`

- Interactive pipeline execution
- Live progress tracking across 4 steps
- Tab-based results view:
  - Full Report
  - Source Data
  - Critic Review
- Downloadable report output

***

## ⚠️ Notes

- A stable internet connection is required for search and scraping
- Some websites may block scraping requests
- Output quality depends on the relevance of search results
- API rate limits may affect usage

***

## 📌 Future Improvements

- Multi-source scraping instead of a single URL
- RAG-based memory with a vector database
- Citation verification
- Async pipeline for faster execution
- Agent orchestration with LangGraph
