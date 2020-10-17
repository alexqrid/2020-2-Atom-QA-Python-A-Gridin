from random import randint

import pytest

from mysql_client.mysql_client import MysqlConnection
from tests.builder import MysqlBuilder


class TestMysql:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlConnection = mysql_client
        self.builder = MysqlBuilder(mysql_client)

    def test(self):
        for _ in range(10):
            self.builder.add_prepod()

    def test_students(self):
        for _ in range(10):
            self.builder.add_students(count=randint(1, 10))

        res = self.mysql.execute_query('SELECT * from prepods')
        print(res)

        self.mysql.execute_query('DELETE FROM students')
