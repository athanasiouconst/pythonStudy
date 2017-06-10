#! /usr/bin/env python
# -*- coding: utf-8 -*-

filename = input("δωστε όνομα αρχείου για αναγνωση : ")
try:
    
    filein = open(filename,"r")
    text=filein.read()
    print(text)
    filein.close()
except IOError:
    print("problem with file")