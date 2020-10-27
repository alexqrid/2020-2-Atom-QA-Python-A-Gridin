import pytest

from mysql_client.mysql_client import MysqlConnection


@pytest.fixture(scope='session')
def mysql_client():
    return MysqlConnection(user='root', password='pass', db_name='TEST_PYTHON')
