import pytest
from django.urls import reverse

from musics.albums.models import Album


@pytest.fixture
def create_album(db):
    album = Album(artist='Rihanna', name='Loud', year='2010-01-01')
    album.save()
    return album


@pytest.fixture
def response(client, create_album):
    return client.get(reverse('albums:album', args=('1',)))


def test_status_code(response):
    assert response.status_code == 200
