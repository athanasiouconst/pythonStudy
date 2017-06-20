#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector

#config database
conn = mysql.connector.connect(user = 'inep', password = 'inep', database = 'inep', use_unicode = True)

#open cursor
cursor = conn.cursor()
#query the database
cursor.execute('select * from users where age < 50 ')

#fetch data 
values = cursor.fetchall()
#print values 
print (values)

cursor.close()
conn.close()