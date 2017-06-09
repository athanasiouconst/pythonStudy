#! /usr/bin/env python
# -*- coding: utf-8 -*-

synolo1 =  {1,2,3,"Peter"}
synolo2=set()

synolo2.add(1)
synolo1.update({1,33,44},{2,55,66})
se3={}

print(type(synolo1),synolo1)

print(type(synolo2),synolo2)

print(type(se3),se3)

synolo3 = {1,2,3}
lista = {1,5,6}
synolo3.update("costas",lista)
print(synolo3)

synolo3.discard(1)
print(synolo3)

try:
    synolo3.remove(1)
except:
    pass

print(synolo3)


