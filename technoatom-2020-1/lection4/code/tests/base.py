import pytest
import os

from ui.pages.base import BasePage
from ui.pages.main import MainPage
from ui.pages.python_events import PythonEventsPage
from ui.pages.bad_ssl import BadSSLPage
from ui.pages.download import DownloadPage
from ui.pages.python_382 import PythonPage382

from ui.decorators import wait


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.bad_ssl_page: BadSSLPage = request.getfixturevalue('bad_ssl_page')
        self.download_page: DownloadPage = request.getfixturevalue('download_page')
        self.python382_page: PythonPage382 = request.getfixturevalue('python382_page')

    def wait_download(self, file_name, timeout=10):

        def _check_download():
            for f in os.listdir(self.config['download_dir']):
                if f.endswith('.crdownload'):
                    return False

            if file_name in os.listdir(self.config['download_dir']):
                return True

            return False

        wait(_check_download, timeout=timeout, check=True)
