from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sentiment Analyzer"
    version: str = "1.0"

    class Config:
        env_file = ".env"

settings = Settings()