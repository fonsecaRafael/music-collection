import pytest
from model_mommy import mommy


@pytest.fixture()
def logged_user(db, django_user_model):
    user_model = mommy.make(django_user_model)
    user_model.is_staff = False
    return user_model


@pytest.fixture()
def logged_admin(db, django_user_model):
    user_model = mommy.make(django_user_model, is_staff=True)
    return user_model


@pytest.fixture()
def logged_client(logged_user, client):
    client.force_login(logged_user)
    return client


@pytest.fixture()
def admin_logged_client(logged_admin, client):
    client.force_login(logged_admin)
    return client
