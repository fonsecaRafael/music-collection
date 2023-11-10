import pytest
from django.urls import reverse

from musics.django_assertions import assert_contains


@pytest.fixture
def response(client):
    return client.get(reverse('artists:artist', args=('15',)))


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, f'<title>MC - Detais</title>')


def test_artist_name(response):
    assert_contains(response, f'Aqui irá aparecer o nome do artista')
