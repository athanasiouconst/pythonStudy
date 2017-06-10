#! /usr/bin/env python
# -*- coding: utf-8 -*-

filename = input("δωστε όνομα αρχείου για αναγνωση : ")
fileout = open(filename,"a")

text = input("πληκτρολογήστε το περιεχόμενο που θα προσθεσω και πατήστε enter : ")

fileout.write(text)
fileout.close()