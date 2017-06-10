#! /usr/bin/env python
# -*- coding: utf-8 -*-

filename = input("δωστε όνομα αρχείου για αναγνωση : ")
filein = open(filename,"r")

data = filein.read()
print(data)
filein.close()