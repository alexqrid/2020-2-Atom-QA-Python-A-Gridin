from faker import Faker

from mysql_client.mysql_client import MysqlConnection

fake = Faker(locale='ru_RU')


class MysqlBuilder(object):
    def __init__(self, connection: MysqlConnection):
        self.connection = connection

        self.create_prepods()
        self.create_student()

    def create_prepods(self):
        preods_query = """
           CREATE TABLE IF NOT EXISTS `prepods` (
             `id` smallint(6) NOT NULL AUTO_INCREMENT,
             `name` char(20) NOT NULL,
             `surname` char(50) NOT NULL,
             `start_teaching` date NOT NULL DEFAULT '2020-01-01',
             PRIMARY KEY (`id`)
           ) CHARSET=utf8
           """

        self.connection.execute_query(preods_query)

    def create_student(self):
        students_query = """
           CREATE TABLE IF NOT EXISTS `students` (
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
        insert_query = f"INSERT INTO prepods(name, surname, start_teaching) " \
                       f"VALUES('{name}', '{surname}', '{start_teaching}')"

        self.connection.execute_query(insert_query)

    def add_students(self, prepod_id=None, count=10):
        """ Метод для добавления записей в таблицу students без ORM """
        for _ in range(count):
            name = fake.first_name()
            if prepod_id is None:
                # prepod_id не указан, генерируем нового препода, записываем в базу и получаем его id
                self.add_prepod()
                prepod_id = self.connection.connection.insert_id()

            insert_student = f"""
                   INSERT INTO students(name, prepod_id) VALUES('{name}', '{prepod_id}')
               """
            # Добавляем запись в таблицу students
            self.connection.execute_query(insert_student)