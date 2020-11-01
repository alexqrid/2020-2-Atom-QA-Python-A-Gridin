import threading
from flask import Flask, jsonify, request
from tests import settings

app = Flask(__name__)
DATA = {}


class ValidUsers:
    users = None


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })

    server.start()
    return server


# Добавляем точку завершения приложения, чтобы мы могли его при необходимостм правильно закрыть
def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify('method not allowed'), 405


@app.route('/set_valid_users', methods=['PUT'])
def set_valid_users():
    if request.method == 'PUT':
        users = request.form['users']
        ValidUsers.users = [u.strip() for u in users.split(',')]
        return {'users': f'Users {users} was set'}


@app.route('/get_valid_users')
def get_valid_users():
    return jsonify({"users": ValidUsers.users})


@app.route('/valid/<user>')
def valid(user):
    if user not in ValidUsers.users:
        return jsonify({"bad_user": user}), 401
    else:
        return jsonify({"valid_user": user}), 200


if __name__ == '__main__':
    run_mock()
