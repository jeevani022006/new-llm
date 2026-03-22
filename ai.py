import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Updated model
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 500
    }
)

chat = model.start_chat(history=[])

SYSTEM_PROMPT = """
You are a smart AI assistant.
Explain clearly and simply.
"""

def get_ai_response(user_input):
    try:
        prompt = SYSTEM_PROMPT + "\nUser: " + user_input
        
        response = chat.send_message(prompt)
        
        return response.text

    except Exception as e:
        print("ERROR:", e)
        return f"Error: {str(e)}"