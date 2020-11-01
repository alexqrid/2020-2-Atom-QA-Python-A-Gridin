import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading


class StubHandleRequests(BaseHTTPRequestHandler):
    data = None

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self.data)


class SimpleHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.stop_server = False
        self.handler = StubHandleRequests
        self.handler.data = None
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()

    def set_data(self, data):
        self.handler.data = json.dumps(data).encode()
