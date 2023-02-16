from typing import Any

import pytest
from app.theoffice_api.api_client import TheOfficeAPIClient


@pytest.fixture
def office_client() -> TheOfficeAPIClient:
    return TheOfficeAPIClient()


@pytest.mark.asyncio
async def test__get_characters(office_client):
    characters: dict[str, list[dict[str, Any]]] = await office_client.get_endpoint('characters')

    assert len(characters['data']) > 0
    assert characters['data'][0].keys() == {'__v', '_id', 'firstname', 'lastname'}


@pytest.mark.asyncio
async def test__get_character_by_id(office_client):

    michael_id = '5e93b4a43af44260882e33b0'

    character = await office_client.get_endpoint(
        endpoint='characters',
        item_id_or_random=michael_id
    )

    assert character['data']['firstname'] == 'Michael'
    assert character['data']['lastname'] == 'Scott'
    assert character['data']['_id'] == michael_id
