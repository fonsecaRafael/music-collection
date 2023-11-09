import pytest
from django.urls import reverse


@pytest.fixture
def response(client):
    return client.get(reverse('artists:artist'), args=('15',))


def test_status_code(response):
    assert response.status_code == 200
