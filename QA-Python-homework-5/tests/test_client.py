import os

import pytest

from postgre_client.builder import PostgresqlBuilder


class TestPostgresql:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, postgres_client):
        self.builder = PostgresqlBuilder(postgres_client)

    # @pytest.mark.skip(reason="passed")
    def test_parse_logs(self):
        log_file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "access.log")
        count = self.builder.parse_log(log_file_path)
        assert count

    def test_add_log(self):
        """ Удаление записей из базы без ORM """
        table = "error_log"
        self.builder.create_log_table(table)
        # Создаем 10 записей в базе
        self.builder.add_log(10)
        self.builder.db.cursor.execute(f"SELECT COUNT(1) FROM {table} ")
        assert self.builder.db.cursor.fetchone()[0] == 10
        # Удаляем записи
        self.builder.db.cursor.execute(f"DELETE FROM {table} WHERE"
                                       f" ip='127.0.0.1' and method='GET'")
        self.builder.db.connection.commit()
        # Удаляем все оставшиеся записи
        self.builder.db.cursor.execute(f'TRUNCATE {table}')
        self.builder.db.connection.commit()
        self.builder.db.cursor.execute(f"SELECT COUNT(1) FROM {table} ")
        assert self.builder.db.cursor.fetchone()[0] == 0
