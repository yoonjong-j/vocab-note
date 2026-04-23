from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from .. import models, schemas
from ..database import get_db

# Initialize the router for word-related endpoints
router = APIRouter(
    prefix="/words",
    tags=["words"]
)

@router.post(
        "/", 
        response_model=schemas.WordResponse,
        status_code=status.HTTP_201_CREATED
)
def create_word(word: schemas.WordCreate, db: Session = Depends(get_db)):
    """Create a new vocabulary entry"""
    # Map incoming schema data to the SQLAlchemy model
    db_word = models.Word(**word.model_dump())

    # Persist the record to the database
    db.add(db_word)
    db.commit()

    # Refresh to retrieve database-generated fields (ex: created_at)
    db.refresh(db_word)

    return db_word
