import pytest

from postgre_client.client import PostgresqlConnection
from postgre_orm_client.orm_client import PostgresqlORMConnection


@pytest.fixture(scope="session", autouse=True)
def credentials():
    try:
        from local_config import credentials
    except ImportError:
        import os
        credentials = {"DB_USER": os.getenv("DB_USER"),
                       "DB_PASS": os.getenv("DB_PASS")}
    return credentials


@pytest.fixture(scope='session')
def postgres_client(credentials):
    return PostgresqlConnection(user=credentials['DB_USER'],
                                password=credentials['DB_PASS'],
                                db_name='postgres')


@pytest.fixture(scope='session')
def postgres_orm_client(credentials):
    return PostgresqlORMConnection(user=credentials['DB_USER'],
                                   password=credentials['DB_PASS'],
                                   db_name='postgres')
