from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Base schema for shared word attributes
class WordBase(BaseModel):
    word: str = Field(..., max_length=200, description="The vocabulary word")                             # Required: The vocabulary word
    word_meaning: str = Field(..., max_length=300, description="Meaning of the word")                     # Required: Definition of the word
    word_example: Optional[str] = Field(None, max_length=500, description="Example sentence of the word") # Optional: Example sentence of the word

# Schema for creating a new word (inherits from base)
class WordCreate(WordBase):
    # Use fields from WordBase for validation
    pass

# Schema for updating a word (all fields optional)
class WordUpdate(BaseModel):
    word: Optional[str] = Field(None, max_length=200)
    word_meaning: Optional[str] = Field(None, max_length=300)
    word_example: Optional[str] = Field(None, max_length=500)

# Schema for API response (includes DB fields)
class Word(WordBase):
    word_id: int                             # Auto-incrementing primary key
    created_at: datetime                     # Record creation time
    updated_at: Optional[datetime] = None    # Record last update time

    model_config = {"from_attributes": True} # Config to allow mapping from SQLAlchemy models
