# 🤖 Turing Chatbot – Agentic AI Assistant

> One command. Zero micromanagement.  
> An open-source, memory-backed AI agent powered by **Google Gemini** that **plans, searches, codes, and remembers** so you don’t have to.






2. README.md (copy-paste ready)
────────────────────────────────────────
markdown
Copy
# 🤖 Turing Chatbot – Agentic AI Companion

> **Your autonomous, memory-backed AI assistant powered by Google Gemini.**

---

## Purpose
Turing is a lightweight, open-source demonstration of **Agentic AI**:
- Accepts a single natural-language goal
- Plans, reasons and uses tools (web search, memory, code execution) without human micromanagement
- Learns from every interaction and improves over time

---

## ✨ Key Capabilities
| Capability        | Tool Used                     | Example |
|-------------------|------------------------------|---------|
| Long-term memory  | Weaviate cloud vector DB      | “What did I ask you last week about Python async?” |
| Web search        | SerpAPI                       | “Find today’s EUR/USD rate and plot it” |
| Code execution    | Local Python sandbox          | “Write and run a script that scrapes Hacker News top 10” |
| Multi-turn chat   | Streamlit UI                  | Keep context across dozens of turns |

---

## 🚀 Quick Start

### 1. Clone & install
'''bash
copy
git clone https://github.com/your-org/turing-chatbot.git
cd turing-chatbot
python -m venv .venv && source .venv/bin/activate   # or .venv\Scripts\activate
pip install -r requirements.txt


2. Add keys
Create .env:
bash
copy
GOOGLE_API_KEY=your_gemini_key
WEAVIATE_URL=https://your-cluster.weaviate.network
WEAVIATE_API_KEY=optional_key_for_sandbox
SERPAPI_API_KEY=optional_web_search_key



4. Run
bash
Copy
streamlit run turing.py


# Browse to http://localhost:8501
🧠 Architecture
Text
Copy
┌─────────────┐    ┌──────────────┐    ┌──────────────┐
│   Streamlit │◄──►│ Gemini LLM   │◄──►│ Tools        │
│    (UI)     │    │ (reasoning)  │    │ • Memory     │
└─────────────┘    └──────────────┘    │ • Search     │
                                       │ • Code       │
                                       └──────────────┘
