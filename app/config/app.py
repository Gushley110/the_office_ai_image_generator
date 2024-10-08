from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'the_office_ai'


@lru_cache()
def get_settings():
    return Settings()
