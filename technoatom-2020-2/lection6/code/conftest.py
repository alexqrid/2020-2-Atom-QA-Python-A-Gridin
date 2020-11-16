import pytest
import numpy

from mysql_client.mysql_client import MysqlConnection
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection


@pytest.fixture(scope='session')
def mysql_client():
    return MysqlConnection(user='root', password='pass', db_name='TEST_PYTHON')


@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection(user='root', password='pass', db_name='TEST_PYTHON_ORM')
