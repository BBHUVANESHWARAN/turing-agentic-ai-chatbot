import os, uuid, datetime
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from memory import save_memory, recall_memory

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ------------- Gemini model with tools -------------
tools = [
    {
        "function_declarations": [
            {
                "name": "search_memory",
                "description": "Recall previously stored facts.",
                "parameters": {
                    "type": "object",
                    "properties": {"query": {"type": "string"}},
                    "required": ["query"],
                },
            },
            {
                "name": "store_memory",
                "description": "Store new facts for later recall.",
                "parameters": {
                    "type": "object",
                    "properties": {"text": {"type": "string"}},
                    "required": ["text"],
                },
            },
        ]
    }
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=tools,
    system_instruction="You are Turing, an agentic AI assistant. "
                       "Use the provided functions to store and recall knowledge.",
)

# ------------- Streamlit UI -------------
st.set_page_config(page_title="Turing Chatbot", page_icon="🤖")
st.title("🤖 Turing Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# display history
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Ask me anything…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    chat = model.start_chat(history=[
        {"role": m["role"], "parts": [m["content"]]}
        for m in st.session_state.messages
    ])
    response = chat.send_message(prompt)

    # handle function calls
    for part in response.parts:
        if fn := part.function_call:
            args = {k: v for k, v in fn.args.items()}
            if fn.name == "search_memory":
                result = recall_memory(args["query"])
            elif fn.name == "store_memory":
                save_memory(args["text"])
                result = "Stored."
            else:
                result = "Unknown tool."
            st.session_state.messages.append(
                {"role": "function", "content": result}
            )

    text = response.text or "🤔"
    st.session_state.messages.append({"role": "model", "content": text})

    with st.chat_message("model"):
        st.markdown(text)