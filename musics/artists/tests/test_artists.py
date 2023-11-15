import pytest
from django.urls import reverse


@pytest.fixture
def resp_artists(logged_client):
    return logged_client.get(reverse('artists:artists'))


def test_status_code(resp_artists):
    assert resp_artists.status_code == 200
