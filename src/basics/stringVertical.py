#! /usr/bin/env python
# -*- coding: utf-8 -*-

#input of chars
stringText=input("Παρακαλώ εισάγετε μια πρόταση : ")

#length of the string 
stringLength = len(stringText)

#use upper func for uppercasing characters
#and use loop for printing vertical them
for i in range(0, stringLength,1):
    print(stringText[i].upper())

