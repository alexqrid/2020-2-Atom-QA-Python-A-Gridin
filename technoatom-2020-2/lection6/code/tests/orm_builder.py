from faker import Faker

from models.models import Base, Prepod, Student
from mysql_orm_client.mysql_orm_client import MysqlOrmConnection

fake = Faker(locale='ru_RU')


class MysqlOrmBuilder(object):
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine

        self.create_prepods()
        self.create_students()

    def create_prepods(self):
        if not self.engine.dialect.has_table(self.engine, 'prepods'):
            Base.metadata.tables['prepods'].create(self.engine)

    def create_students(self):
        if not self.engine.dialect.has_table(self.engine, 'students'):
            Base.metadata.tables['students'].create(self.engine)

    def add_prepod(self):
        # Создаем запись в таблице 'prepods' через класс Prepod
        prepod = Prepod(
            name=fake.first_name(),
            surname=fake.last_name(),
            start_teaching=fake.date()
        )

        # Сохраняем объект в сесси, открытой в connection
        self.connection.session.add(prepod)
        # Записываем созданную запись в базу
        self.connection.session.commit()
        # Возвращаем объект для работы из тестов
        return prepod

    def add_students(self, prepod_id=None, count=10):
        for _ in range(count):
            # Создаем нового студента
            student = Student(name=fake.first_name())

            if prepod_id is None:
                # Генерируем случайного препода, запоминаем его id
                prepod_id = self.add_prepod().id

            # Указываем преподавателя для студента
            student.prepod_id = prepod_id

            # Записываем созданную модуль в базу
            self.connection.session.add(student)
            self.connection.session.commit()
