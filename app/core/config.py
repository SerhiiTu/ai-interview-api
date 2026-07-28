from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Interview API"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ai_interview"
    ai_api_key: str | None = None
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()