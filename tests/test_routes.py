import pytest
from flask import url_for

from FlaskLogin import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


def test_app(client):
    assert client.get(url_for('auth.signup')).status_code == 200


def test_login(client):
    assert client.post(url_for('auth.login'), data={'email':'saikiran1298gmail.com', 'password':'sachej-5fivxo-rIwbod'}, follow_redirects=True).status_code == 200
