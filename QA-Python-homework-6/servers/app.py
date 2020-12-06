import socket
import threading
from flask import Flask, jsonify, request, make_response
from settings import APP_HOST, APP_PORT, MOCK_HOST, MOCK_PORT
from client import Client, ClientSocketError
from json import JSONDecodeError

app = Flask(__name__)


def run_app():
    server = threading.Thread(target=app.run, kwargs={
        'host': APP_HOST,
        'port': APP_PORT,
    })
    server.start()
    return server


def shutdown_app():
    terminate = request.environ.get('werkzeug.server.shutdown')
    if terminate:
        terminate()


def client_connect(host, port):
    try:
        client = Client(host, port)
    except ClientSocketError:
        return None
    return client


@app.route("/", methods=["GET", "POST"])
def mock_index():
    client: Client = client_connect(MOCK_HOST, MOCK_PORT)
    if client:
        client.send("test", "data", request.method, request.headers)
        try:
            response = client.get_json()
        except JSONDecodeError:
            return jsonify(
                {"error": "something went wrong on mock server"}), 500
        return jsonify(response), 200
    else:
        return jsonify({"error": "Connection error"}), 500


@app.route("/mock_down")
def mock_is_down():
    client = client_connect(MOCK_HOST, MOCK_PORT + 100)
    if client:
        return jsonify({"status": 200})
    else:
        return jsonify({"error": "Connection error"}), 500


@app.route("/auth", methods=["POST", "PUT"])
def auth_mock():
    client = client_connect(MOCK_HOST, MOCK_PORT)
    if client:
        client.send("auth", request.get_json(), request.method,
                    request.headers)
        try:
            response = client.get_json()
            if response.get("ERROR", False):
                return jsonify(response), 401
        except JSONDecodeError:
            return jsonify(
                {"error": "something went wrong on mock server"}), 500

        return jsonify(response), 200
    else:
        return jsonify({"error": "Connection error"}), 500


@app.route("/put_data", methods=["POST", "PUT"])
def put_data_mock():
    client = client_connect(MOCK_HOST, MOCK_PORT)
    if client:
        client.send("update", request.get_json(), request.method,
                    request.headers)
        try:
            response = client.get_json()
            return jsonify(response), 200
        except JSONDecodeError:
            return jsonify(
                {"error": "something went wrong on mock server"}), 500

    else:
        return jsonify({"error": "Connection error"}), 500


@app.route("/mock_500")
def mock_500():
    client = client_connect(MOCK_HOST, MOCK_PORT)
    if client:
        client.send("/error", "data", "GET",
                    request.headers)
        try:
            response = client.get_raw_data()
            return jsonify({"response": response}), 500
        except Exception:
            return jsonify(
                {"error": "something went wrong on mock server"}), 500
    return jsonify({"ERROR": "Connection error"}), 500


@app.route("/shutdown")
def shutdown():
    print(request.url)
    shutdown_app()
    return "ok", 200


run_app()
