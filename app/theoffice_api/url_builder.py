import logging
from app.config.app import get_settings

settings = get_settings()
logger = logging.getLogger(f'{settings.APP_NAME}-log')


class URLBuilder:
    _BASE_URL: str = 'https://www.officeapi.dev/api'
    _ENDPOINTS: list = [
        'characters',
        'quotes',
        'episodes',
    ]

    def create_url(self, endpoint: str, item_id_or_random: str = None) -> str:
        if endpoint not in self._ENDPOINTS:
            msg = f'Endpoint {endpoint} not available'
            logger.error(f'Endpoint {endpoint} not available')
            raise ValueError(msg)

        url = f'{self._BASE_URL}/{endpoint}'
        logger.info(f'Request -> {url}')

        if item_id_or_random:
            return f'{url}/{item_id_or_random}'

        return url
