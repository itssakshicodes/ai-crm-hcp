# AI-First CRM: HCP Interaction Module

This repository contains a prototype for a Life Sciences CRM module focused on logging HCP interactions. It features a hybrid interface (Structured Form + AI Chat) powered by LangGraph and Groq LLM.

## Features
- **Hybrid Interface**: Users can type "Met Dr. Smith regarding X" and the AI fills the form/db.
- **LangGraph Agent**: Orchestrates tools for logging, editing, and compliance checking.
- **Tech Stack**: React (Frontend), FastAPI (Backend), Groq/Gemma2 (LLM).

## Setup Instructions

### Backend
1. Navigate to `backend/`.
2. Create a `.env` file and add your Groq API Key: `GROQ_API_KEY=your_key_here`.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt