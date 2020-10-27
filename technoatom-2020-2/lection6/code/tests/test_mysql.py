import pytest

from mysql_client.mysql_client import MysqlConnection
from tests.builder import MysqlBuilder


class TestMysql:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlConnection = mysql_client
        self.builder = MysqlBuilder(self.mysql)

    def test(self):
        for _ in range(10):
            self.builder.add_prepod()

        res = self.mysql.execute_query('SELECT * FROM prepods')
        print('\n ' + str(res))

    def test_students_delete(self):
        """ Удаление записей из базы без ORM """

        # Создаем 10 записей в базе
        self.builder.add_students(count=10)

        # Удаляем запись с id=5
        self.mysql.execute_query('DELETE FROM students WHERE id=5')

        # Удаляем все оставшиеся записи
        self.mysql.execute_query('DELETE FROM students')
