from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    ai_api_key: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()