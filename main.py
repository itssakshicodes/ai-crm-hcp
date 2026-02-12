from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent
from models import init_db, SessionLocal, Interaction
from sqlalchemy.orm import Session
from fastapi import Depends

app = FastAPI(title="AI CRM HCP Module")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Init DB
init_db()

class ChatRequest(BaseModel):
    message: str

class InteractionLog(BaseModel):
    hcp_name: str
    interaction_type: str
    date: str
    time: str
    topics: str
    sentiment: str
    outcomes: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    """Endpoint for the AI Assistant Chat"""
    try:
        response = run_agent(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/log_interaction")
async def manual_log(data: InteractionLog, db: Session = Depends(get_db)):
    """Endpoint for manually submitting the form"""
    # Logic to save to DB manually if not using chat
    return {"status": "success", "message": "Interaction logged manually"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)