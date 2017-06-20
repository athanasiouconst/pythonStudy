#!/usr/bin/python
# -*- coding: utf-8 -*-


import sqlite3

def connectDB(filename):
    conn=sqlite3.connect(filename)
    c = conn.cursor()


def inputdata():
    print("insert Data: ")
    onoma = input("Name: ")
    if onoma == '':
        return None,None
    parent = input("foreas:")
    dief=input("post office address:")
    str_emails = input("email address:")
    emails = str_emails.split()
    ypiresia_tuple = (onoma, parent, dief)
    return ypiresia_tuple, emails

def insertDB(record, mails, connection, cursor):
    cursor.execute(''' insert into ypiresia(yp_name, yp_parent, yp_dief  values (?, ?, ?) ''', record)
    connection.commit()
    fkey = cursor.lastrowid
    
    for mail in mails:
        eml_record = (fkey, mail)
        cursor.execute()
    connection.commit()


cursor, connection = connectDB("C://sqlite3//paraliptes.db")
record, emails = inputdata()
while record != None :
    insertDB(record, emails, connection, cursor)
    record, emails = inputdata()
    
connection.close()

print("data entered!!")