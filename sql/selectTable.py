import sqlite3


def select_data(table):
    dbname = 'example.sqlite3'
    # connect database
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    try:
        # do SQL
        data = c.execute("select * from %s" % table)
        data = data.fetchall()
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    # save DATABASE
    conn.commit()
    # close DATABASE
    conn.close()

    return data


def insert_data(table, data):
    dbname = 'example.sqlite3'
    # connect database
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    insert_data: tuple = data
    try:
        # do SQL
        c.execute("insert into %s values (?,?,?,?,?)" % table, insert_data)
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    # save DATABASE
    conn.commit()
    # close DATABASE
    conn.close()


def update_data(data1, data2):
    dbname = 'example.sqlite3'
    # connect database
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    try:
        # do SQL
        c.execute("update cute set rest = ? where getdate = ?", (data1, data2))
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    # save DATABASE
    conn.commit()
    # close DATABASE
    conn.close()


def delete_data(data1):
    dbname = 'example.sqlite3'
    # connect database
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    try:
        # do SQL
        c.execute("delete from cute where getdate = ?", (data1))
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])
    # save DATABASE
    conn.commit()
    # close DATABASE
    conn.close()


# insert_data("cute", ("test", 2, 2, 2, 2))
# print(select_data("cute"))
# update_data("cute", 3, "test")
