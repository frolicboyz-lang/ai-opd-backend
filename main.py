from fastapi import FastAPI
import os
import uvicorn

app = FastAPI(title="AI OPD Backend")

@app.get("/")
def root():
    return "ai opd running"

# IMPORTANT: This is required for Replit / cloud platforms
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
