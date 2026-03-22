from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

model = genai.GenerativeModel("gemini-pro")

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_ai(data: Question):
    try:
        response = model.generate_content(data.question)
        return {"answer": response.text}
    except Exception as e:
        return {"error": str(e)}