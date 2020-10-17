from mysql_client.mysql_client import MysqlConnection
from faker import Faker

fake = Faker(locale='ru_RU')


class MysqlBuilder:

    def __init__(self, connection: MysqlConnection):
        self.connection = connection
        self.create_prepods()
        self.create_students()

    def create_prepods(self):
        prepods_query = """
               CREATE TABLE if not exists `prepods` (
                 `id` smallint(6) NOT NULL AUTO_INCREMENT,
                 `name` char(20) NOT NULL,
                 `surname` char(50) NOT NULL,
                 `start_teaching` date NOT NULL DEFAULT '2020-01-01',
                 PRIMARY KEY (`id`)
               ) CHARSET=utf8

           """
        self.connection.execute_query(prepods_query)

    def create_students(self):
        students_query = """
               CREATE TABLE if not exists `students` (
                 `id` smallint(6) NOT NULL AUTO_INCREMENT,
                 `name` char(20) DEFAULT NULL,
                 `prepod_id` smallint(6) NOT NULL,
                 PRIMARY KEY (`id`),
                 KEY `prepod_id` (`prepod_id`),
                 CONSTRAINT `students_ibfk_1` FOREIGN KEY (`prepod_id`) REFERENCES `prepods` (`id`)
               ) CHARSET=utf8
            """
        self.connection.execute_query(students_query)

    def add_prepod(self):
        name = fake.first_name()
        surname = fake.last_name()
        start_teaching = fake.date()

        insert_prepod = f"""
               INSERT INTO prepods(name, surname, start_teaching) VALUES('{name}', '{surname}', '{start_teaching}')
           """
        self.connection.execute_query(insert_prepod)

    def add_students(self, prepod_id=None, count=10):
        for _ in range(count):
            name = fake.first_name()
            if prepod_id is None:
                self.add_prepod()
                prepod_id = self.connection.connection.insert_id()

            insert_student = f"""
                   INSERT INTO students(name, prepod_id) VALUES('{name}', '{prepod_id}')
               """
            self.connection.execute_query(insert_student)
