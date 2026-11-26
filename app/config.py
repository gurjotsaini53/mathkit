from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "mathKit"
    version: str = "0.0.1"
    environment: str = "development"
    debug: bool = True

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
