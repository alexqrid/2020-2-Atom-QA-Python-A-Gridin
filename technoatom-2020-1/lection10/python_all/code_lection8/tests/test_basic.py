import requests
from mock.mock import users


def add_user(user_id: int, user_data: dict):
    users.update({str(user_id): user_data})


def test_valid(mock_server):
    server_host, server_port = mock_server

    user = {'name': 'Ilya', 'surname': 'Kirillov'}
    add_user(1, user)

    url = f'http://{server_host}:{server_port}/user/1'

    result = requests.get(url, user)
    assert result.json() == user


def test_invalid(mock_server):
    server_host, server_port = mock_server

    user = {'name': 'Yaroslav', 'surname': 'Cherednichenko'}
    add_user(2, user)

    url = f'http://{server_host}:{server_port}/user/3'
    result = requests.get(url)
    assert result.status_code == 404
