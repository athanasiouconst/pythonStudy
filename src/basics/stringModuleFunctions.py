#! /usr/bin/env python
# -*- coding: utf-8 -*-
string="I am learning Python"

print "Length of string  \""+string+"\" is ", len(string)

salute="welcome to the python course!"
name = raw_input('enter your name: ')
outputstr = "Hi {0}\n{1}".format(name, salute)

print(outputstr)

num = 3.12391
print("{0} rounded to 4 decimal digits: {0:.4f}".format(num))

num = 3.12399
print("{0} rounded to 4 decimal digits: {0:10.4f}".format(num))

num = 12
print("{0} printed with format specifier: {0:10d}".format(num))

text="Python is a programming language. Also, Python is a snake"
spot = text.find("Python",1 )
print("I found matching, starting from {0}".format(spot))