from urllib.parse import urljoin

APP_HOST, APP_PORT = '127.0.0.1', 1050
APP_URL = f'http://{APP_HOST}:{APP_PORT}'

STUB_HOST, STUB_PORT = '127.0.0.1', 1052
STUB_URL = f'http://{STUB_HOST}:{STUB_PORT}'

STUB2_HOST, STUB2_PORT = '127.0.0.1', 1053
STUB2_URL = f'http://{STUB2_HOST}:{STUB2_PORT}'

MOCK_HOST, MOCK_PORT = '127.0.0.1', 1054
MOCK_URL = f'http://{MOCK_HOST}:{MOCK_PORT}'

VALID_URL = urljoin(STUB_URL, 'valid')
MOCK_VALID_URL = urljoin(MOCK_URL, 'valid')
APP_SHUTDOWN_URL = urljoin(APP_URL, 'shutdown')
STUB_SHUTDOWN_URL = urljoin(STUB_URL, 'shutdown')
MOCK_SHUTDOWN_URL = urljoin(MOCK_URL, 'shutdown')
MOCK_SET_USERS = urljoin(MOCK_URL, 'set_valid_users')
