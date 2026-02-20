
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request schema
class ChatRequest(BaseModel):
    user_id: str
    message: str

# Simple chat endpoint (just echoes the message)
@app.post("/chat")
def chat(request: ChatRequest):
    user_id = request.user_id
    user_message = request.message
    response = f"Echo: {user_message}"
    return {"response": response}

@app.get("/")
def root():
    return {"message": "StudyBot is running!"}
