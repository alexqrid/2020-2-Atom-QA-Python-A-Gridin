import pytest

from mysql_client.mysql_client import MysqlConnection
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection


@pytest.fixture(scope='session')
def mysql_client():
    return MysqlConnection('root', 'pass', 'TEST_PYTHON')


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection('root', 'pass', 'TEST_PYTHON_ORM')
