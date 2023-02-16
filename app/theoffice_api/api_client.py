import httpx
import logging
from app.config.app import get_settings
from app.theoffice_api.url_builder import URLBuilder


settings = get_settings()
logger = logging.getLogger(f'{settings.APP_NAME}-log')


class TheOfficeAPIClient:

    @staticmethod
    async def get_endpoint(endpoint: str, item_id_or_random: str = None) -> dict:

        url_builder = URLBuilder()

        request = httpx.get(
            url=url_builder.create_url(endpoint, item_id_or_random),
        )

        logger.info(f'GET {request.url}')

        request.raise_for_status()

        return request.json()

