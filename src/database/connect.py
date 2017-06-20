#!/usr/bin/env python2.7
#-*-coding:utf8-*-

import mysql.connector

conn = mysql.connector.connect(user = 'inep', password = 'inep', database = 'inep', use_unicode = True)

#cursor = conn.cursor()    
#cursor.execute('create table users (id varchar(20) primary key, name varchar(20))')

#cursor.execute('insert into user(id, name) values (%s, %s)', ['1', 'Mary'])
#print (cursor.rowcount)

#conn.commit()
#cursor.close()

cursor = conn.cursor()
cursor.execute('select * from users')

values = cursor.fetchall()
print (values)

cursor.close()
conn.close()