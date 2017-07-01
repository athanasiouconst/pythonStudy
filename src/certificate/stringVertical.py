#! /usr/bin/env python
# -*- coding: utf-8 -*-

#input of chars
stringText=input("Παρακαλώ εισάγετε μια πρόταση : ")
i=0

for i in range (len(stringText)):
    reverc = stringText[:-len(stringText)]

print(reverc)