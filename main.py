from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class PatientRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "AI OPD running!"}

@app.post("/chat")
def chat(request: PatientRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": request.message}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
