import random

from postgre_client.client import PostgresqlConnection


class PostgresqlBuilder(object):
    def __init__(self, connection: PostgresqlConnection):
        self.db = connection
        self.table = None
        self.sql = None

    def create_log_table(self, tablename):
        self.db.cursor.execute(f"DROP TABLE IF EXISTS {tablename}")
        self.db.connection.commit()
        query = f"""CREATE TABLE IF NOT EXISTS {tablename}(
            status smallint ,
            size bigint,
            method varchar(6),
            ip varchar(15),
            url varchar(2048)
            )"""
        self.db.cursor.execute(query)
        self.db.connection.commit()
        self.sql = f"""INSERT INTO {tablename} (ip,method,url,status,size)
          VALUES (%(ip)s,%(method)s,%(url)s,%(status)s,%(size)s)"""
        self.table = tablename

    def parse_log(self, filename):
        table = filename.split("/")[-1]
        table = table.replace(".", "_")
        self.create_log_table(table)
        with open(filename, 'r') as fd:
            logs = fd.readlines()
        parsed = []
        for i in logs:
            temp = i.split(" ")
            try:
                size = int(temp[9])
            except ValueError:
                size = 0
            if len(temp[5]) <= 10:
                method = temp[5][1:]  # "POST or "GET
            else:
                method = temp[5][-3:]  # был запрос схлопнутый с querystring
            parsed.append({"ip": temp[0],
                           "method": method,
                           "url": temp[6],
                           "status": int(temp[8]),
                           "size": size}
                          )

        self.db.insert_many(self.sql, parsed)
        self.db.cursor.execute(f"SELECT COUNT(1) FROM {self.table}")
        count = self.db.cursor.fetchone()[0]
        with open("/tmp/res.txt", 'w') as fd:
            fd.write(f'{count}  {len(parsed)}')
        return count == len(parsed)

    def add_log(self, count=5):
        test = []
        for i in range(count):
            test.append({"ip": "127.0.0.1",
                         "method": random.choice(
                             ['GET', 'POST', 'HEAD', 'PUT']),
                         "url": "/index.html",
                         "status": random.randint(400, 600),
                         "size": random.randint(0, 10 ** 8)
                         })
        self.db.insert_many(self.sql, test)
