import pytest

from app.theoffice_api.url_builder import URLBuilder


def test__build_character_urls():
    url_builder = URLBuilder()

    url_simple = url_builder.create_url('characters')

    url_w_id = url_builder.create_url(
        endpoint='characters',
        item_id_or_random='f_id'
    )

    url_w_random = url_builder.create_url(
        endpoint='characters',
        item_id_or_random='random',
    )

    assert url_simple == 'https://www.officeapi.dev/api/characters'
    assert url_w_id == 'https://www.officeapi.dev/api/characters/f_id'
    assert url_w_random == 'https://www.officeapi.dev/api/characters/random'
    with pytest.raises(ValueError):
        url_builder.create_url(endpoint='f_endpoint')
