from pydantic_settings import BaseSettings, SettingsConfigDict

# Settings class to manage environment variables and configurations
class Settings(BaseSettings):
    # Variable to store the PostgreSQL connection string from .env
    database_url: str

    # Configuration to tell Pydantic to read from the ".env" file
    model_config = SettingsConfigDict(env_file=".env")

# Create a global instance of settings to be used throughout the application
settings = Settings()
