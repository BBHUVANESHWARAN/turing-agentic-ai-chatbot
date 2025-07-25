# 🤖 Turing Chatbot – Agentic AI Assistant

> One command. Zero micromanagement.  
> An open-source, memory-backed AI agent powered by **Google Gemini** that **plans, searches, codes, and remembers** so you don’t have to.

## 🚀 Quick Start

```bash
git clone git@github.com:BBHUVANESHWARAN/turing-agentic-ai-chatbot.git
cd turing-chatbot
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
echo "GOOGLE_API_KEY=YOUR_KEY" > .env
streamlit run turing.py'''



🔑 Environment Variables
Create .env (never commit):
GOOGLE_API_KEY=YOUR_GEMINI_KEY
WEAVIATE_URL=https://edu-demo.weaviate.network
WEAVIATE_API_KEY=optional
