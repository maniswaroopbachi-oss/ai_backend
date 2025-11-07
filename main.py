from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai

app = FastAPI()

# Allow MIT App Inventor to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = "AIzaSyC01uOOXhd76dbIfrIBM6EmRew7pMP8t30"  # Replace with your key

@app.get("/")
def home():
    return {"message": "AI Backend Running Successfully"}

@app.get("/ask")
def ask_ai(question: str):
    prompt = f"Give a clear, detailed, and easy-to-understand answer to: {question}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
    