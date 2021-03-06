import os
import uuid
from dataclasses import dataclass

import allure
import pytest
import logging
from api.mytarget_client import MytargetClient


@pytest.fixture(scope="session", autouse=True)
def credentials():
    try:
        from local_config import credentials
    except ImportError:
        import os
        credentials = {"email": os.getenv("LOGIN_EMAIL"),
                       "password": os.getenv("LOGIN_PASS")}
    return credentials


@pytest.fixture
def unique():
    temp = uuid.uuid1()
    return temp.hex


@pytest.fixture(scope='function')
def api_client(credentials, logger):
    return MytargetClient(logger=logger, credentials=credentials)


@pytest.fixture(scope='function')
def logger(request):
    """
        Фикстура для логирования.
    """

    log_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file = request.node.location[-1]

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    log = logging.getLogger('api_log')
    log.propogate = False
    log.setLevel(logging.DEBUG)
    log.addHandler(file_handler)

    # Для того чтобы аттачить логи в случае пофейленных тестов
    failed_count = request.session.testsfailed
    yield log
    if request.session.testsfailed > failed_count:
        with open(log_file, 'r') as f:
            allure.attach(f.read(), name=log.name,
                          attachment_type=allure.attachment_type.TEXT)

    os.remove(log_file)
