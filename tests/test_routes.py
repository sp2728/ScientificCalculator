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
    rv = client.post(url_for('auth.login'), data={'email':'va322@njit.edu', 'password':'va322@njit'})
    print(rv)
    assert rv.status_code == 302

'''
def test_login(client):
    d = client.get(url_for('auth.login'))
    response = client.post(d,
                           data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome', name='Pat'),
                           follow_redirects=True)
    assert response.status_code == 200
    assert b"Welcome, Pat!" in response.data
    assert b"Open Calculator" in response.data
    assert b"Home" in response.data
    assert b"Profile" in response.data
    assert b"Calculator" in response.data
    assert b"Logout" in response.data
    assert b"Login" not in response.data
    assert b"Register" not in response.data'''
