#! /usr/bin/env python
# -*- coding: utf-8 -*-

myVar = 10

def fun():
    myVar = 1 
    for i in range(10):
        myVar +=10

fun()
print(myVar)

name= "Εθνικο Κεντρο Δημοσιας Διοικησης και Αυτοδιοικησης"
a=name.islower()
b=name.lower()

print(a)
print(b)

print(8%3)


x=6.8
y=2
print(x//y)

mydata = {}
mydata[1]=1
mydata[8]=3
mydata[1]+=1
mydata['1']=2
sum=0
for i in mydata:
    sum+=mydata[i]
print(sum)
