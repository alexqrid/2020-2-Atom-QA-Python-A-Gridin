import pytest
import requests
import json
from urllib.parse import urljoin
from application import atom
from stub import flask_stub, simple_http_server
from mock_server import flask_mock
from tests.settings import APP_URL, APP_SHUTDOWN_URL, STUB_SHUTDOWN_URL, STUB2_URL, STUB2_HOST, STUB2_PORT, \
    MOCK_URL, MOCK_SHUTDOWN_URL, MOCK_SET_USERS


class StubData:
    data = {"valid": "True"}


class AppData:
    data = {"page": "base"}


class Stub2Data:
    data = {"ok": "ok"}


@pytest.fixture(scope='session')
def stub_server():
    server = simple_http_server.SimpleHTTPServer(STUB2_HOST, STUB2_PORT)
    server.start()
    yield server
    server.stop()


@pytest.fixture(scope='session')
def mock():
    flask_mock.run_mock()
    atom.run_app()
    yield
    requests.get(MOCK_SHUTDOWN_URL)
    requests.get(APP_SHUTDOWN_URL)


@pytest.mark.skip('no need')
def test_stub():
    atom.DATA = AppData.data
    flask_stub.DATA = StubData.data
    atom.run_app()
    flask_stub.run_stub()
    response = requests.get(APP_URL)
    requests.get(APP_SHUTDOWN_URL)
    requests.get(STUB_SHUTDOWN_URL)
    assert response.status_code == 200
    assert json.loads(response.content) == AppData.data


# @pytest.mark.skip('no need')
def test_stub2(stub_server):
    stub_server.set_data(Stub2Data.data)
    response = requests.get(STUB2_URL)
    assert response.status_code == 200
    assert json.loads(response.content) == Stub2Data.data


@pytest.mark.skip('no need')
def test_valid_user(mock):
    # кладём тестовые данные
    check_user = 'iliya'
    valid_users = 'kirill, iliya'
    mock_response = requests.put(MOCK_SET_USERS, data={'users': valid_users}, timeout=2)
    app_response = requests.get(urljoin(APP_URL, check_user))

    # Проверяем статус и данные из мока
    assert mock_response.status_code == 200
    assert mock_response.json() == {"users": f"Users {valid_users} was set"}

    # Проверяем статус и данные из приложения
    assert app_response.status_code == 200
    assert app_response.json() == f"User {check_user} has permissions"


@pytest.mark.skip('no need')
def test_invalid_user(mock):
    # кладём тестовые данные
    check_user = 'yar'
    valid_users = 'kirill, iliya'
    mock_response = requests.put(MOCK_SET_USERS, data={'users': valid_users}, timeout=2)
    app_response = requests.get(urljoin(APP_URL, check_user))

    # Проверяем статус и данные из мока
    assert mock_response.status_code == 200
    assert mock_response.json() == {"users": f"Users {valid_users} was set"}

    # Проверяем статус и данные из приложения
    assert app_response.status_code == 401
    assert app_response.json() == f"User {check_user} hasn't permissions"
