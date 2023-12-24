from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Annotated
from fastapi import Depends
import os

class Settings(BaseSettings):
    app_name: str = "ai-service"
    zylalabs_api_key: str = os.getenv("ZYLALABS_API_KEY")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# @lru_cache()
def get_settings():
    return Settings()

@lru_cache()
def env(settings: Annotated[Settings, Depends(get_settings)] = get_settings()):
    return {
        "APP_NAME": settings.app_name,
        "ZYLALABS_API_KEY": settings.zylalabs_api_key
    }

# @lru_cache()
# env: Annotated[Settings, Depends(get_settings)]
    # "APP_NAME": get_settings().app_name,
    # "ADMIN_EMAIL": get_settings().admin_email
