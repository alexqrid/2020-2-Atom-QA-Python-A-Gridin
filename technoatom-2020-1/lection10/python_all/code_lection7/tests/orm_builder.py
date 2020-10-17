from faker import Faker

from models.models import Base, Prepod, Student
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection

fake = Faker(locale='ru_RU')


class MysqlOrmBuilder:

    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = connection.connection.engine
        self.create_prepods()
        self.create_students()

    def create_prepods(self):
        if not self.engine.dialect.has_table(self.engine, 'prepods'):
            Base.metadata.tables['prepods'].create(self.engine)

    def create_students(self):
        if not self.engine.dialect.has_table(self.engine, 'students'):
            Base.metadata.tables['students'].create(self.engine)

    def add_prepod(self):
        prepod = Prepod(
            name=fake.first_name(),
            surname=fake.last_name(),
            start_teaching=fake.date()
        )

        self.connection.session.add(prepod)
        self.connection.session.commit()

        return prepod

    def add_students(self, prepod_id=None, count=10):
        for _ in range(count):
            student = Student(name=fake.first_name())

            if prepod_id is None:
                prepod_id = self.add_prepod().id

            student.prepod_id = prepod_id

            self.connection.session.add(student)
            self.connection.session.commit()
