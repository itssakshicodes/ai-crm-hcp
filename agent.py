import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from tools import log_interaction_tool, edit_interaction_tool, schedule_followup_tool, compliance_check_tool, sentiment_analysis_tool

load_dotenv()

# Setup Groq LLM
# Ensure GROQ_API_KEY is in your .env file
llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY") # Add your key in .env
)

# Define tools list
tools = [
    log_interaction_tool, 
    edit_interaction_tool, 
    schedule_followup_tool, 
    compliance_check_tool,
    sentiment_analysis_tool
]

# Create the graph
agent_executor = create_react_agent(llm, tools)

def run_agent(user_input: str):
    """Entry point for the API to call the agent"""
    response = agent_executor.invoke({"messages": [("human", user_input)]})
    return response["messages"][-1].content