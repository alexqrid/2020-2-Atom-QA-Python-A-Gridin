import threading
import requests
from urllib.parse import urljoin
from flask import Flask, request, jsonify
from tests import settings

app = Flask(__name__)
DATA = {}


# Напишем функцию, которая будет отвечать за запуск нашего приложения
def run_app():
    # Используем треды, чтобы была общая память с pytest
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.APP_HOST,
        'port': settings.APP_PORT
    })

    server.start()
    return server


# Добавляем точку завершения приложения, чтобы мы могли его при необходимостм правильно закрыть
def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/check_socket/<user>')
def check_socket(user):
    return jsonify({'user': user})


@app.route('/shutdown')
def shutdown():
    shutdown_app()


@app.route('/<user>')
def index(user):
    mock_response = requests.get(f'{settings.MOCK_VALID_URL}/{user}')

    if mock_response.status_code == 401:
        return jsonify(f"User {user} hasn't permissions"), 401
    elif mock_response.status_code == 200:
        return jsonify(f"User {user} has permissions"), 200


if __name__ == '__main__':
    run_app()
