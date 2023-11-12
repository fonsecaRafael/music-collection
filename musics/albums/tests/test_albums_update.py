import pytest
from django.urls import reverse
from model_mommy import mommy

from musics.albums.models import Album


@pytest.fixture
def create_albums(db):
    """Model-mommy library makes <3> instances of Album with random values each time it runs."""
    return mommy.make(Album, 3)


@pytest.fixture
def response(client, create_album):
    return client.get(reverse('albums:album', args=('1',)))


def test_status_code(response):
    assert response.status_code == 200
