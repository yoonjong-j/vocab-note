from pydantic_settings import BaseSettings, SettingsConfigDict

# Settings class to manage environment variables and configurations
class Settings(BaseSettings):
    database_url: str                                  # Variable to store the PostgreSQL connection string from .env
    model_config = SettingsConfigDict(env_file=".env") # Configuration to tell Pydantic to read from the ".env" file

# Create a global instance of settings to be used throughout the application
settings = Settings()
