import pytest
from models.models import Log
from postgre_orm_client.orm_builder import PostgresqlOrmBuilder


class TestPostgresOrm(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, postgres_orm_client):
        self.builder = PostgresqlOrmBuilder(connection=postgres_orm_client)

    def test(self):
        log = self.builder.add_log()
        db_entry = self.builder.db.session\
            .query(Log).filter_by(ip='127.0.0.1')
        assert log == db_entry.first()
