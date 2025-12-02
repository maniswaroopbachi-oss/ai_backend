from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# Configure Gemini API key
genai.configure(api_key="AIzaSyBMWGAmPAUWF32NFkvdyh0_Mjrs_fq5Gcc")

# Input model
class Question(BaseModel):
    question: str

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/ask")
def ask(data: Question):

    prompt = prompt = f"""
Explain the following term in a simple and clear way suitable for students.
Include:

1. Definition: Simple and clear (1–2 sentences)
2. Explanation: Easy to understand
3. Daily Life Example: One practical example
4. Summary: A short 2-line summary

Term: {data.question}
"""


    try:
        model = genai.GenerativeModel("gemini-3-pro-preview")
        response = model.generate_content(prompt)

        return {"answer": response.text}

    except Exception as e:
        return {"error": str(e)}




