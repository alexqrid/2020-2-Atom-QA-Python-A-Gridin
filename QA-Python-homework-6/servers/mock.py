import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import time
from settings import TIMEOUT, MOCK_HOST, MOCK_PORT


class MockHandleRequests(BaseHTTPRequestHandler):
    data = None

    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        print(self.request)
        if self.path == '/wait':
            time.sleep(TIMEOUT)
            self._set_headers(code=504)
        elif self.path == '/error':
            self._set_headers(code=500)
        else:
            self._set_headers()
            self.wfile.write(json.dumps(self.data).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = post_data.decode()
        print(self.path)
        print(self.request)
        if self.path == '/auth':
            if not self.headers['Authorization']:
                self.send_response(401)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                data = {'ERROR': 'Authorization required'}
                self.wfile.write(json.dumps(data).encode())
            else:
                self._set_headers()
                self.wfile.write(json.dumps({"auth": post_data}).encode())
        elif self.path == '/test':
            print("Entered", self.path)
            self._set_headers()
            self.wfile.write(json.dumps({"auth": post_data}).encode())
        elif self.path == '/update':
            print("Entered ", self.path)
            self.send_response(405)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("<h1> Method not allowed</h1>".encode())
        else:
            print("Entered to 404 ", self.path)
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("<h1> Not found</h1>".encode())

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        if self.path == '/update':
            print("Entered ", self.path)
            self._set_headers()
            self.data = put_data.decode()
            self.wfile.write(json.dumps({"data": self.data}).encode())
        elif self.path == '/auth':
            print("Entered ", self.path)
            self.send_response(405)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("<h1> Method not allowed</h1>".encode())
        else:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write("<h1> Server ERROR</h1>".encode())


class SimpleHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = MockHandleRequests
        self.handler.data = {"user": "Hello world"}
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=False)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_data(self, data):
        self.handler.data = json.dumps(data).encode()
