from pydantic import BaseSettings, Field, PostgresDsn


class Settings(BaseSettings):
    db_url: PostgresDsn = Field(
        env="DB_URL", default="postgresql://user:password@localhost:5432/fast_tmi"
    )


settings = Settings()
