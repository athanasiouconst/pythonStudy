#!/usr/bin/python
# -*- coding: utf-8 -*-


import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect("C://sqlite3//paraliptes.db")

c = conn.cursor()

c.execute(''' create table ypiresia (yp_id integer primary key, yp_name text not null, yp_parent text, yp_dief text)''')

c.execute(''' create table email (email text not null, yp_id integer not null references ypiresia(yp_id))''')

c.close()
print("Data base created")