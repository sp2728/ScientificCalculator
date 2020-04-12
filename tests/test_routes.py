import pytest
from flask import url_for
from FlaskLogin import db
from FlaskLogin.models import User
from flask_login import login_required, current_user
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
    rv = client.post(url_for('auth.login'), data={'email': 'va123@gmail.com', 'password': 'va123@gmail'},
                     follow_redirects=True)
    assert rv.status_code == 200
    assert b"Welcome, varsha!" in rv.data
    assert b"Home" in rv.data
    assert b"Profile" in rv.data
    assert b"Calculator" in rv.data
    assert b"Logout" in rv.data
    return rv


def test_logout(client):
    rv = test_login(client)
    rv1 = client.get(url_for('auth.logout'), follow_redirects=True)
    assert rv1.status_code == 200
    assert b"Home" in rv1.data
    assert b"Calculator" not in rv1.data


def test_user_creation(client):
    # dummy data creation
    data = {'email': 'pat@gmail.com', 'password': 'pat@gmail', 'name': 'Pat'}
    rv = client.post(url_for('auth.signup'), data=data,
                     follow_redirects=True)
    assert rv.status_code == 200
    # dummy data login
    rv1 = client.post(url_for('auth.login'), data=data,
                      follow_redirects=True)
    assert rv1.status_code == 200
 # dummy data deletion
    all_data = User.query.filter(User.email == current_user.email).delete()
    print(current_user.email)
    db.session.commit()



