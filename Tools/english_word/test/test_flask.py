import app
import pytest
import os
import tempfile
import sys

path = "\\".join(__file__.split("\\")[:-1]) + "/../"
sys.path.append(path)


@pytest.fixture
def client():
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    with app.app.app_context():
        app.db.create_all()

    yield client

    os.close(db_fd)
    os.unlink(app.app.config['DATABASE'])


def test_index(client):
    rv = client.get('/')
    assert '词神' in rv.data.decode(encoding="utf-8")


def test_add_new_word(client):
    rv = client.post("/add-new-word", data=dict(
        data="book n. 书"
    ), follow_redirects=True)
    assert 'book' in rv.data.decode(encoding="utf-8")
    assert 'n.' in rv.data.decode(encoding="utf-8")
    assert '书' in rv.data.decode(encoding="utf-8")


def test_recite_word(client):
    rv = client.post("/recite-words", data=dict(
        data="book"
    ), follow_redirects=True)
    assert '答对咯！' in rv.data.decode(encoding="utf-8")
