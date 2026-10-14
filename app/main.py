from fastapi import FastAPI

app = FastAPI(title="AI Follow-up Assistant", description="This is a simple AI follow-up assistant.")

@app.get("/")
def home():
    return {"message": "Welcome to the AI Follow-up Assistant!"}