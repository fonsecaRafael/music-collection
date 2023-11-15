import pytest
from django.urls import reverse


@pytest.fixture
def resp_users_admin_logged(admin_logged_client):
    response = admin_logged_client.get(reverse('base:users'))
    return response


def test_admin_status_code(resp_users_admin_logged):
    assert resp_users_admin_logged.status_code == 200


@pytest.fixture
def resp_users_no_admin_logged(logged_client):
    response = logged_client.get(reverse('base:users'))
    return response


def test_user_status_code(resp_users_no_admin_logged):
    assert resp_users_no_admin_logged.status_code == 302
    assert resp_users_no_admin_logged.url.startswith(reverse('login'))
