import os
import sys
import sqlite3
import json

def parse_log(filename):
    print(f"Started to parse {filename}")
    conn = sqlite3.connect("/tmp/logs.db")
    cursor = conn.cursor()
    table = f"{filename[:-4]}_{filename[-3:]}"
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    cursor.execute(f"""CREATE TABLE {table} (
        ip text,
        method text,
        url text,
        status INTEGER,
        size_of INTEGER);""")
    conn.commit()
    output = f"processed_{filename}.py.txt"
    parsed = []
    with open(filename, 'r') as fd:
        logs = fd.readlines()
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
                       "status": temp[8],
                       "size": size}
                      )

    cursor.executemany(
        f"""INSERT INTO {table} (ip,method,url,status,size_of)
     VALUES (:ip,:method,:url,:status,:size)""", parsed)
    conn.commit()
    cursor.execute(f"SELECT COUNT(1) FROM {table}")
    result = {"total_queries": cursor.fetchone()[0]}
    cursor.execute(f"""SELECT method, COUNT(1) FROM {table}
    GROUP BY method HAVING method IN ('GET','POST')""")
    result['method_stats'] = "\n".join(
        [f"{i[0]} - {i[1]}" for i in cursor.fetchall()])
    cursor.execute(f"""SELECT url, status, size_of  from {table}
                        group by size_of order by size_of desc limit 10""")
    result["biggest"] = "\n".join([f"{i[0]} {i[1]} {i[2]}"
                                   for i in cursor.fetchall()
                                   ])

    cursor.execute(f"""select ip, url, status,count(1) from {table}
                    group by ip,url having status>=400 and status<500
                    order by count(1) desc limit 10""")

    result["top_4xx"] = "\n".join([f"{i[0]} {i[1]} {i[2]}"
                                   for i in cursor.fetchall()])

    cursor.execute(f"""select ip, url, status,size_of from {table}
                        where status>=500 and status <600 order by size_of desc
                        limit 10;""")
    result["top_5xx"] = "\n".join([f"{i[0]} {i[1]} {i[2]} {i[3]}"
                                   for i in cursor.fetchall()])
    with open(os.path.join(os.getcwd(),filename[:-4]+".json"), 'w') as fd:
        json.dump(result, fd, indent=4)

    with open(os.path.join(os.getcwd(), output), 'w') as fd:
        fd.write(f"Result of processing {filename}\n")
        fd.write(
            f"Total queries amount: {result['total_queries']}\n{'=' * 20}")
        fd.write(f"\nStats on GET/POST methods: {result['method_stats']}\n")
        fd.write(
            f"{'=' * 20}\nTop 10 queries by size:\n {result['biggest']}\n")
        fd.write(f"{'=' * 20}\nTop 10 4xx queries by ip, location:\n"
                 f" {result['top_4xx']}\n{'=' * 20}")
        fd.write(f"\nTop 10 failed queries by size:\n{result['top_5xx']}\n")
    print(f"Processed {filename} and put results in {output}")
    cursor.execute(f"DROP TABLE {table}")
    conn.commit()
    conn.close()
    os.remove('/tmp/logs.db')


def parse(source):
    if os.path.isdir(source):
        files = [i for i in os.listdir(source) if i.endswith('.log')]
        for i in files:
            parse(i)
    elif os.path.isfile(source) and source.endswith(".log"):
        parse_log(source)
    else:
        print("Not a log file")
        return 1
    return 0


if __name__ == "__main__":
    parse(sys.argv[1])
