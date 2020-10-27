from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Prepod(Base):
    # В __tablename__ указывается имя таблицы, которую мы хотим создать
    __tablename__ = 'prepods'
    # __table_args__ используется для установки кодировки в базе на utf8, т. к. мы записываем в нее кириллицу.
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(50), nullable=False)
    start_teaching = Column(Date, nullable=False, default='2020-01-01')

    # Метод __repr__ используется для того, чтобы можно было сделать красивый вывод полей нашей модели
    # при обращении к ней из дебага или просто печати ее содердимого.
    # Сравните вывод print(PrepodInstance):
    # без __repr__ : <models.models.Prepod object at 0x7fe25dc9eac0>
    # с __repr__   : <Prepod(id='2',name='Clarence', surname='Wright', start_teaching='2002-11-30')>
    def __repr__(self):
        return f"<Prepod(" \
               f"id='{self.id}'," \
               f"name='{self.name}', " \
               f"surname='{self.surname}', " \
               f"start_teaching='{self.start_teaching}'" \
               f")>"


class Student(Base):
    __tablename__ = 'students'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    # Помимо остальных полей, устанавливаем ForeignKey для  `prepod_id` на поле `id` из модели Prepod
    prepod_id = Column(Integer, ForeignKey(f'{Prepod.__tablename__}.{Prepod.id.name}'), nullable=False)

    def __repr__(self):
        return f"<Student(" \
               f"id='{self.id}'," \
               f"name='{self.name}', " \
               f"prepod_id='{self.prepod_id}'" \
               f")>"
