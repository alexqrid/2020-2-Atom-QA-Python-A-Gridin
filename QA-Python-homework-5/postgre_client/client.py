import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import execute_batch

class PostgresqlConnection(object):

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = '127.0.0.1'
        self.port = 5432

        self.connection = self.connect()
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def get_connection(self, db_created=False):
        return psycopg2.connect(host=self.host, port=self.port,
                                user=self.user, password=self.password,
                                dbname=self.db_name if db_created
                                else 'postgres')

    def connect(self):
        connection = self.get_connection()
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute('DROP DATABASE IF EXISTS logs')
        cursor.execute('CREATE DATABASE logs')
        connection.close()

        return self.get_connection(db_created=True)

    def insert_many(self, query, data):
        execute_batch(self.cursor,query, data,page_size=5000)
