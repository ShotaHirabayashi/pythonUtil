# -*- coding: utf-8 -*-

import sqlite3

dbname = 'example.sqlite3'
# connect database
conn = sqlite3.connect(dbname)
c = conn.cursor()
c.execute('create table cute(getdate text, rest int, stay int,empty int, reserve int)')
# save DATABASE
conn.commit()
# close DATABASE
conn.close()
