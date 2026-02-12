from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Use SQLite for portability in this demo, switch to MySQL for prod
DATABASE_URL = "sqlite:///./crm.db" 

Base = declarative_base()

class Interaction(Base):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String(255))
    interaction_type = Column(String(50))
    date = Column(DateTime, default=datetime.utcnow)
    topics_discussed = Column(Text)
    sentiment = Column(String(50))
    outcomes = Column(Text)
    next_steps = Column(Text)
    materials_shared = Column(JSON, default=list)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)