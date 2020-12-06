import socket
import time

import pytest

from client import Client
from settings import *
import requests
from servers.mock import SimpleHTTPServer
from servers.app import run_app


class TestServer:
    # мок и приложение запускаются 1 раз на все тесты
    # сессионная фикстура
    @pytest.fixture(scope="session", autouse=True)
    def get_mock(self):
        """
        собственный HTTP Mock реализует обработку POST/PUT запросов
        """
        mock = SimpleHTTPServer(MOCK_HOST, MOCK_PORT)
        mock.start()
        time.sleep(1)
        yield mock
        mock.stop()

    @pytest.fixture(scope="session", autouse=True)
    def get_app(self):
        app = run_app()
        time.sleep(1)
        yield app
        requests.get(APP_URL + "/shutdown")

    def test_client_sending_post(self):
        # Написать собственный HTTP клиент с использованием библиотеки socket
        # отправлять POST запросы
        req = requests.post(APP_URL)
        assert req.status_code == 200

    def test_client_put(self):
        # реализовать обработку PUT запросов
        data = {"test": 123}
        req = requests.put(APP_URL + "/put_data", json={"test": 123})
        assert req.status_code == 200
        assert req.json() == {"data": str(data)}

    def test_mock_down(self):
        # приложение поднято, а мок не поднят
        req = requests.get(APP_URL + "/mock_down")
        assert req.status_code == 500

    def test_mock_timeout(self):
        # приложение поднято, а мок не отвечает(timeout)
        with pytest.raises(TimeoutError):
            client = Client(MOCK_HOST, MOCK_PORT)
            client.send("wait", "data", "GET", {})
            client.get_raw_data()

    def test_mock_500(self):
        req = requests.get(APP_URL + "/mock_500")
        assert req.status_code == 500

    def test_auth(self):
        # отправка запроса в приложение отправляется с кастомным хэдэром
        data = {"user": "test"}
        req = requests.post(APP_URL + "/auth", json=data,
                            headers={"Authorization": "Bearer 123a"})
        assert req.status_code == 200
        assert req.json() == {"auth": str(data)}

    def test_auth_2(self):
        # неавторизованный запрос на защищенный локейшн
        data = {"user": "test"}
        req = requests.post(APP_URL + "/auth", json=data)
        assert req.status_code == 401
