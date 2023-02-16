from fastapi import FastAPI, HTTPException
from app.theoffice_api.api_client import TheOfficeAPIClient
import logging
from logging.config import dictConfig
from app.config.log import LogConfig
from app.config.app import get_settings

dictConfig(LogConfig().dict())

settings = get_settings()
logger = logging.getLogger(f'{settings.APP_NAME}-log')

app = FastAPI()


@app.get("/characters")
async def get_characters():
    office_client = TheOfficeAPIClient()
    characters = await office_client.get_endpoint('characters')

    return characters


@app.get("/characters/{character_id}")
async def get_characters(character_id: str):
    try:
        office_client = TheOfficeAPIClient()
        characters = await office_client.get_endpoint('quotes', character_id)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    return characters


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
