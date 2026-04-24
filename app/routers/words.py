from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
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

    # Return the created word entry
    return db_word

@router.get(
    "/",
    response_model=List[schemas.WordResponse],
    status_code=status.HTTP_200_OK
)
def get_words(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve a list of vocabulary entries with pagination support"""
    
    # Database query with pagination
    words = db.query(models.Word).offset(skip).limit(limit).all()

    # Return the retrieved word list
    return words

@router.get(
    "/random",
    response_model=schemas.WordResponse,
    status_code=status.HTTP_200_OK
)
def get_random_word(db: Session = Depends(get_db)):
    """Retrieve a random vocabulary entry from the database"""

    # Randomly shuffle the words and pick the first one
    word = db.query(models.Word).order_by(text("RANDOM()")).first()

    # If no words exist, raise a `404 Not Found` error
    if word is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No words found in the database"
        )
    
    # Return the randomly selected word
    return word

@router.get(
    "/{word_id}",
    response_model=schemas.WordResponse,
    status_code=status.HTTP_200_OK
)
def get_word(word_id: int, db: Session = Depends(get_db)):
    """Retrieve a single vocabulary entry by its ID"""

    # Query the database for a word that matches the given word_id
    word = db.query(models.Word).filter(models.Word.word_id == word_id).first()

    # Check if the word exists; if not, raise a `404 Not Found` error
    if word is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id {word_id} not found"
        )
    
    # Return the found word object
    return word

@router.patch(
    "/{word_id}",
    response_model=schemas.WordResponse,
    status_code=status.HTTP_200_OK
)
def update_word(word_id: int, updated_word: schemas.WordUpdate, db: Session = Depends(get_db)):
    """Update an existing vocabulary entry"""

    # Prepare a query to find the word by its ID
    word_query = db.query(models.Word).filter(models.Word.word_id == word_id)
    # Execute the query to get the existing word
    db_word = word_query.first()

    # Raise a `404 Not Found` error if the word does not exist
    if db_word is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id {word_id} not found"
        )
    
    # Extract only the fields provided in the request
    update_data = updated_word.model_dump(exclude_unset=True)
    # Perform the update in the database
    word_query.update(update_data, synchronize_session=False)

    # Save changes to the database
    db.commit()
    # Reload the word object with updated data
    db.refresh(db_word)

    # Return the updated word entry
    return db_word

@router.delete(
    "/{word_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_word(word_id: int, db: Session = Depends(get_db)):
    """Remove a vocabulary entry"""

    # Search for the word in the database by its ID
    word = db.query(models.Word).filter(models.Word.word_id == word_id).first()

    # Raise a `404 Not Found` error if the word does not exist
    if word is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Word with id {word_id} not found"
        )
    
    # Mark the word object for deletion
    db.delete(word)
    # Commit the change to permanently remove the word
    db.commit()

    # Return None as 204 status code requires no response body
    return None