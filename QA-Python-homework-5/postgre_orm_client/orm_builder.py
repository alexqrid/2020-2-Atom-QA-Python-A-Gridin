import random

from models.models import Base, Log
from postgre_orm_client.orm_client import PostgresqlORMConnection


class PostgresqlOrmBuilder(object):
    def __init__(self, connection: PostgresqlORMConnection):
        self.db = connection
        self.engine = self.db.connection.engine
        self.create_log()

    def create_log(self):
        if self.engine.dialect.has_table(self.engine, 'error_log'):
            Base.metadata.tables['error_log'].drop(self.engine)
        Base.metadata.tables['error_log'].create(self.engine)

    def add_log(self):
        log = Log(ip="127.0.0.1",
                  method=random.choice(['GET', 'POST', 'HEAD', 'PUT']),
                  url="/index.html", status=random.randint(400, 600),
                  size=random.randint(0, 10 ** 8))

        self.db.session.add(log)
        self.db.session.commit()
        return log
