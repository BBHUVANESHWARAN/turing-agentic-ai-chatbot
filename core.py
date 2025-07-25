import os, json, datetime, textwrap
from typing import List
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
from .tools import TOOLS, ToolCallRequest

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class Message(BaseModel):
    role: str
    content: str
    timestamp: str = None

class TuringAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            tools=TOOLS,
            system_instruction=textwrap.dedent("""
                You are **Turing**, an agentic AI assistant.
                Always be concise, friendly, and helpful.
                Use the tools provided to answer accurately.
                Remember to store useful facts in memory.
            """)
        )
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def send(self, user_input: str, history: List[Message]) -> str:
        # Convert history to Gemini format
        messages = [
            {"role": m.role, "parts": [m.content]}
            for m in history[-10:]  # last 10 messages for context
        ]
        self.chat.history = messages
        response = self.chat.send_message(user_input)
        return response.text