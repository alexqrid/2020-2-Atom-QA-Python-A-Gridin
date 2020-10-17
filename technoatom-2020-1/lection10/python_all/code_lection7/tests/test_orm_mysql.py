from random import randint

import pytest

from models.models import Student
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection
from mysql_orm_client.orm_builder import MysqlOrmBuilder


class TestOrmMysql:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlOrmConnection = mysql_orm_client
        self.builder = MysqlOrmBuilder(mysql_orm_client)

    def test(self):
        for _ in range(10):
            self.builder.add_prepod()

    def test_students_delete(self):
        for _ in range(10):
            self.builder.add_students(count=randint(1, 10))

        res = self.mysql.session.query(Student).filter_by(id=10)
        res.delete()
        self.mysql.session.commit()

        self.mysql.session.query(Student).delete()
        self.mysql.session.commit()
