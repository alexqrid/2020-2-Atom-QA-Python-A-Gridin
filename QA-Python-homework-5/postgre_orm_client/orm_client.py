import sqlalchemy
from sqlalchemy.orm import sessionmaker


class PostgresqlORMConnection(object):
    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.port = 5432
        self.host = '127.0.0.1'
        self.connection = self.connect()
        self.session = sessionmaker(bind=self.connection)()
        self.session.connection().connection.set_isolation_level(0)

    def get_connection(self, db_created=False):
        engine = sqlalchemy.create_engine(
            'postgresql://{user}:{password}@{host}:{port}/{db}'.format(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                db=self.db_name if db_created else 'postgres'
            ),
            executemany_mode='batch', client_encoding='utf8',
            execution_options={
                "isolation_level": "AUTOCOMMIT"
            }
        )
        return engine.connect()

    def connect(self):
        connection = self.get_connection(db_created=False)

        connection.execute('DROP DATABASE IF EXISTS logs')
        connection.execute('CREATE DATABASE logs')
        connection.close()

        return self.get_connection(db_created=True)
