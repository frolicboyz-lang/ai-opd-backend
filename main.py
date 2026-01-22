
from fastapi import FastAPI
from pydantic import BaseModel
import os
import openai

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

class PatientRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "AI OPD running!"}

@app.post("/chat")
def chat(request: PatientRequest):
    user_message = request.message
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content": user_message}]
        )
        answer = response.choices[0].message.content
        return {"response": answer}
    except Exception as e:
        return {"error": str(e)}
