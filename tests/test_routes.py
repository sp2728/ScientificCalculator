import pytest
from flask import url_for

from FlaskLogin import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


def test_index(client):
    assert client.get(url_for('main.index')).status_code == 200


def test_getLogin(client):
    assert client.get(url_for('auth.login')).status_code == 200


def test_getSignup(client):
    assert client.get(url_for('auth.signup')).status_code == 200

def test_login(client):
    rv = client.post(url_for('auth.login'), data={'email':'va322@njit.edu', 'password':'va322@njit'}, follow_redirects=True)
    print(rv)
    assert rv.status_code == 200
    assert b"Welcome, varsha!" in rv.data
    assert b"Home" in rv.data
    assert b"Profile" in rv.data
    assert b"Calculator" in rv.data
    assert b"Logout" in rv.data



