import os
from fixtures.fixtures import *

os.environ['WDM_LOG_LEVEL'] = '0'


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=None)
    parser.addoption('--headless', default=None)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')
    headless = request.config.getoption('--headless')

    return {'browser': browser, 'version': version, 'url': url,
            'download_dir': '/tmp', 'selenoid': selenoid, 'headless': headless}
