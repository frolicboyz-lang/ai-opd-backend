from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PatientRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "AI OPD running!"}

@app.post("/chat")
def chat(request: PatientRequest):
    return {
        "response": f"You said: {request.message}"
    }
        return {"error": str(e)}
