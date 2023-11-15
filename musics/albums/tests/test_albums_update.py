import pytest
from django.urls import reverse
from model_mommy import mommy

from musics.albums.models import Album
from musics.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def create_albums(db):
    """Model-mommy library makes <3> instances of Album with random values each time it runs."""
    return mommy.make(Album, 3)


@pytest.fixture
def resp_album_user_logged(logged_client, create_albums):
    return logged_client.get(reverse('albums:album', args=[1]))


@pytest.fixture
def resp_album_admin_logged(admin_logged_client, create_albums):
    return admin_logged_client.get(reverse('albums:album', args=[1]))


def test_user_logged_delete_unavailable(resp_album_user_logged):
    assert_not_contains(resp_album_user_logged, reverse('albums:delete', args=[1]))


def test_admin_logged_delete_available(resp_album_admin_logged):
    assert_contains(resp_album_admin_logged, reverse('albums:delete', args=[1]))
