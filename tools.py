from langchain_core.tools import tool
from models import SessionLocal, Interaction
from datetime import datetime
import json

@tool
def log_interaction_tool(hcp_name: str, topics: str, sentiment: str, outcomes: str):
    """Logs a new interaction with an HCP into the database. Use this when the user provides meeting details."""
    db = SessionLocal()
    try:
        new_interaction = Interaction(
            hcp_name=hcp_name,
            topics_discussed=topics,
            sentiment=sentiment,
            outcomes=outcomes,
            date=datetime.now()
        )
        db.add(new_interaction)
        db.commit()
        return f"Successfully logged interaction with {hcp_name}. ID: {new_interaction.id}"
    except Exception as e:
        return f"Error logging interaction: {str(e)}"
    finally:
        db.close()

@tool
def edit_interaction_tool(interaction_id: int, field: str, new_value: str):
    """Edits a specific field of a logged interaction. Fields: sentiment, topics_discussed, outcomes."""
    db = SessionLocal()
    interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()
    if interaction:
        setattr(interaction, field, new_value)
        db.commit()
        return f"Updated {field} for interaction {interaction_id}."
    return "Interaction not found."

@tool
def schedule_followup_tool(hcp_name: str, task: str, due_date: str):
    """Schedules a follow-up task. Use when user says 'remind me to...' or 'schedule next'."""
    # Simulation of calendar API integration
    return f"Scheduled follow-up for {hcp_name}: '{task}' on {due_date}."

@tool
def compliance_check_tool(material_name: str):
    """Checks if a material is approved for distribution."""
    # Mock compliance DB
    restricted = ["Phase 1 Data", "Off-label Slide Deck"]
    if material_name in restricted:
        return f"WARNING: {material_name} is restricted. Do not distribute."
    return f"Compliance Check: {material_name} is approved."

@tool
def sentiment_analysis_tool(text: str):
    """Analyzes text to determine sentiment if not explicitly provided."""
    # In a real app, this might call another lightweight model
    keywords = ["angry", "upset", "complained"]
    if any(k in text.lower() for k in keywords):
        return "Negative"
    return "Neutral/Positive"