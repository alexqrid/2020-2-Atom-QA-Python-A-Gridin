from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Log(Base):
    __tablename__ = 'error_log'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    ip = Column('ip', VARCHAR(15))
    method = Column(VARCHAR)
    url = Column(VARCHAR)
    status = Column(Integer)
    size = Column(Integer)

    def __repr__(self):
        return f"<Log({self.ip},{self.status},{self.size}," \
               f"{self.method},{self.url}"
