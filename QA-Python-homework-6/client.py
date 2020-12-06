import json
import socket
from settings import TIMEOUT


class ClientSocketError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=TIMEOUT):
        self.host = host
        self.port = port
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientSocketError("Error while creating connection", err)

    def _read(self):
        result = ""
        while True:
            try:
                data = self.connection.recv(1024)
                if data:
                    result += data.decode()
                else:
                    break
            except socket.timeout:
                raise TimeoutError("timeoute exceeded")
        return result

    def send(self, path, data, method, headers):
        req = f"{method.upper()} /{path} HTTP/1.1\r\n Host: {self.host} \r\n"
        for k, v in headers.items():
            req += f"{k}:{v}\r\n"
        req += f"Content-length: {len(str(data))}\r\n"
        req += "\r\n" + str(data)
        print(req)
        self.connection.sendall(req.encode())

    def get_json(self):
        data = self._read()
        data = data.splitlines()
        if len(data):
            data = data[-1]
        else:
            data = ""
        return json.loads(data)

    def get_raw_data(self):
        data = self._read()
        return data
