import requests, subprocess, tempfile, os
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.embeddings import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
import google.generativeai as genai
from .memory import add_to_memory, recall_fact

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
if os.path.exists("faiss_index"):
    vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
else:
    vectorstore = FAISS.from_texts(["dummy"], embeddings)

search = SerpAPIWrapper()

def web_search(query: str) -> str:
    """Search the web using SerpAPI and return top 5 snippets."""
    return search.run(query)

def remember_fact(fact: str) -> str:
    """Store a fact into long-term memory."""
    vectorstore.add_texts([fact])
    vectorstore.save_local("faiss_index")
    return "Saved to memory."

def recall_fact(query: str) -> str:
    """Look up a fact from long-term memory."""
    docs = vectorstore.similarity_search(query, k=3)
    if not docs:
        return "I found no prior knowledge."
    return "\n".join([d.page_content for d in docs])

def run_python(code: str) -> str:
    """Execute Python code in a sandbox and return stdout/stderr."""
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
        f.write(code.encode())
        fname = f.name
    try:
        result = subprocess.run(
            ["python", fname], capture_output=True, text=True, timeout=10
        )
        return result.stdout or result.stderr
    finally:
        os.remove(fname)

def remember_fact(fact: str) -> str:
    add_to_memory(fact)
    return "Saved to long-term memory."

def recall_fact_tool(query: str) -> str:
    return recall_fact(query)

# Gemini requires `tools` as plain functions with descriptions
TOOLS = [web_search, remember_fact, recall_fact, run_python]