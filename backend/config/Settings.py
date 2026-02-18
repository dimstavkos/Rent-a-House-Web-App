from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_env: str
    app_name: str
    database_schema: str
    database_host: str
    database_port: str
    database_username: str
    database_password: str
    secret : str
    algorithm : str

    model_config = SettingsConfigDict(env_file=".env")