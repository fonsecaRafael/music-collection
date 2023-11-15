import pytest
from django.urls import reverse

from musics.django_assertions import assert_contains


@pytest.fixture
def resp_artist(logged_client):
    return logged_client.get(reverse('artists:artist', args=('15',)))


def test_status_code(resp_artist):
    assert resp_artist.status_code == 200


def test_title(resp_artist):
    assert_contains(resp_artist, f'<title>MC - Details</title>')
