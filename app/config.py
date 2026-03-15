from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
