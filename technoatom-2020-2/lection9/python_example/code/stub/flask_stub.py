import threading
from flask import Flask, jsonify, request
from tests import settings

app = Flask(__name__)
DATA = {}


def run_stub():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.STUB_HOST,
        'port': settings.STUB_PORT
    })

    server.start()
    return server


# Добавляем точку завершения приложения, чтобы мы могли его при необходимостм правильно закрыть
def shutdown_stub():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_stub()


@app.route('/valid/<user>')
def valid(user):
    return jsonify(DATA)


if __name__ == '__main__':
    run_stub()
