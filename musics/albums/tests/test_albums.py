import pytest
from django.urls import reverse


@pytest.fixture
def resp_albums_user_logged(logged_client):
    return logged_client.get(reverse('albums:albums'))


def test_status_code(resp_albums_user_logged):
    assert resp_albums_user_logged.status_code == 200
