import os
from dataclasses import dataclass

import allure
import pytest
import logging
from api.client import ApiClient


@dataclass
class Settings:
    URL: str = None


@pytest.fixture(scope='session')
def config() -> Settings:
    settings = Settings(URL='https://jsonplaceholder.typicode.com')

    return settings


@pytest.fixture(scope='function')
def api_client(config, logger):
    return ApiClient(config.URL, logger)


@pytest.fixture(scope='function')
def logger(request):
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file = request.node.location[-1]

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    log = logging.getLogger('api_log')
    log.propogate = False
    log.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    failed_count = request.session.testsfailed
    yield log
    if request.session.testsfailed > failed_count:
        with open(log_file, 'r') as f:
            allure.attach(f.read(), name=log.name, attachment_type=allure.attachment_type.TEXT)

    os.remove(log_file)
