from fastapi import FastAPI
from .database import engine
from . import models
from .routers import words

# Create database tables based on the models defined
models.Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application with a custom title
app = FastAPI(title="Vocabulary Notebook API")

# Register the word router to include its endpoints in the app
app.include_router(words.router)

# Define a root endpoint for a simple welcome message
@app.get("/")
def root():
    # Return a JSON response for the home path
    return {"message": "Welcome to the Vocabulary Notebook API!"}
