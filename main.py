from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI OPD running!"}
from fastapi import UploadFile, File
import shutil
import os

@app.post("/voice")
async def voice_opd(audio: UploadFile = File(...)):
    file_path = f"temp_{audio.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    return {
        "message": "Voice received successfully",
        "filename": audio.filename
    }
