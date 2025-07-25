# 🤖 Turing Chatbot – Agentic AI Companion

> **Your autonomous, memory-backed AI assistant using Google Gemini Api Key.**

---

## Purpose
Turing is a lightweight, open-source demonstration of **Agentic AI**:
- Accepts a single natural-language goal
- Plans, reasons and uses tools (web search, memory, code execution) without human micromanagement
- Learns from every interaction and improves over time

---


---

## 🚀 Quick Start

### 1. Clone & install
```bash
git clone https://github.com/your-org/turing-chatbot.git
cd turing-chatbot
python -m venv .venv && source .venv/bin/activate   # or .venv\Scripts\activate
pip install -r requirements.txt

---

2. Add keys
Create .env:
Copy
GOOGLE_API_KEY=your_gemini_key
WEAVIATE_URL=https://your-cluster.weaviate.network
WEAVIATE_API_KEY=optional_key_for_sandbox
SERPAPI_API_KEY=optional_web_search_key

---

3. Run
bash
Copy
streamlit run turing.py
# Browse to http://localhost:8501

---

🧠 Architecture
Text
Copy
┌─────────────┐    ┌──────────────┐    ┌──────────────┐
│   Streamlit │◄──►│ Gemini LLM   │◄──►│ Tools        │
│    (UI)     │    │ (reasoning)  │    │ • Memory     │
└─────────────┘    └──────────────┘    │ • Search     │
                                       │ • Code       │
                                       └──────────────┘
