from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

# SQLAlchemy model for the 'words' table
# Stores vocabulary words, their meanings, examples, and timestamps
class Word(Base):
    __tablename__ = "words"
    word_id = Column(Integer, primary_key=True, index=True)                            # word_id: SERIAL, PK, NOT NULL
    word = Column(String(200), nullable=False)                                         # word: VARCHAR(200), NOT NULL
    word_meaning = Column(String(300), nullable=False)                                 # word_meaning: VARCHAR(300), NOT NULL
    word_example = Column(String(500), nullable=True)                                  # word_example: VARCHAR(500), NULL
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False) # created_at: TIMESTAMP, NOT NULL, DEFAULT NOW()
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.now, nullable=True) # updated_at: TIMESTAMP, NULL