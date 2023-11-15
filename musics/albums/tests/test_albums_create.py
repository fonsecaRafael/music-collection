import pytest
from django.urls import reverse


@pytest.fixture
def response(logged_client):
    return logged_client.get(reverse('albums:create'))


def test_status_code(response):
    assert response.status_code == 200
