import sqlite3


def db_create():
    con = sqlite3.connect("demo.db")
    cur = con.cursor()
    sql = "create table if not exists todo(id integer, message text);"
    cur.execute(sql)
    cur.close()
    con.close()


def db_insert():
    con = sqlite3.connect("demo.db")
    cur = con.cursor()
    data = [
        "1,'hello,world1'",
        "2,'hello,world2'",
        "3,'hello,world3'",
        "4,'hello,world4'",
        "5,'hello,world5'",
    ]
    for i in data:
        cur.execute('INSERT INTO todo VALUES (%s)' % i)
        con.commit()
    cur.close()
    con.close()


def db_query():
    con = sqlite3.connect("demo.db")
    cur = con.cursor()
    data = cur.execute('select * from todo')
    print(data.fetchall())
    cur.close()
    con.close()


if __name__ == '__main__':
    db_create()
    db_insert()
    db_query()
