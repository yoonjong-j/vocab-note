from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

# Create the engine to connect to the PostgreSQL database
engine = create_engine(settings.database_url)

# Create a session factory for database operations
# `autocommit=False`: Changes are only saved when we call `commit()`
# `autoflush=False`: Do not send changes to DB until we are ready 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all database models to inherit from
Base = declarative_base()

# Dependency function to provide a database session to routes
def get_db():
    # Create a new session
    db = SessionLocal()
    try:
        # Give the session to the requester (ex: a FastAPI route)
        yield db
    finally:
        # Always close the session after the request is finished
        db.close()
