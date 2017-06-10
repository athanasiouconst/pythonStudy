#! /usr/bin/env python
# -*- coding: utf-8 -*-

filename = input("δωστε όνομα αρχείου για δημιουργία : ")
fileout = open(filename,"w")

text = input("πληκτρολογήστε το περιεχόμενο και πατήστε enter : ")

fileout.write(text)
fileout.close()
