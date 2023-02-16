from pydantic import BaseSettings, BaseModel
from app.config.app import get_settings


class LogConfig(BaseModel):
    LOGGER_NAME = f"{get_settings().APP_NAME}-log"
    LOG_FORMAT = "%(levelprefix)s %(asctime)s |%(filename)s|%(funcName)s| %(message)s"
    LOG_LEVEL = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    }
    loggers = {
        f"{get_settings().APP_NAME}-log": {"handlers": ["default"], "level": LOG_LEVEL},
    }
