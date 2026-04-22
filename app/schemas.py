from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class WordBase(BaseModel):
    """Base schema for shared word attributes"""
    # Required: The vocabulary word
    word: str = Field(..., max_length=200, description="The vocabulary word")                     
    # Required: Definition of the word
    word_meaning: str = Field(..., max_length=300, description="Meaning of the word")
    

class WordCreate(WordBase):
    """Schema for creating a new word (inherits from base)"""
    # Optional: Example sentence of the word                
    word_example: Optional[str] = Field(None, max_length=500, description="Example sentence of the word")

class WordUpdate(BaseModel):
    """Schema for updating a word (all fields optional)"""
    word: Optional[str] = Field(None, max_length=200)
    word_meaning: Optional[str] = Field(None, max_length=300)
    word_example: Optional[str] = Field(None, max_length=500)

class Word(WordBase):
    """Schema for API response (includes DB fields)"""
    # Auto-incrementing primary key
    word_id: int
    # Record creation time
    created_at: datetime
    # Record last update time
    updated_at: Optional[datetime] = None
    # Optional: Example sentence of the word                
    word_example: Optional[str] = Field(None, max_length=500, description="Example sentence of the word")
    # Config to allow mapping from SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)
