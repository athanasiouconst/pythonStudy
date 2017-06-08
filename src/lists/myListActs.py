#! /usr/bin/env python
# -*- coding: utf-8 -*-

Lista1 = ["George","Maria"]
Lista2 = ["Nick","Maria"]

all= Lista1 +Lista2
print(all)

all=[Lista1,Lista2]
print(all)

Lista1 +=["1"]
print(Lista1)

Lista2 +=["1"]
print(Lista2)

Lista2 = Lista2*2
print(Lista2)

for i in range(len(Lista2)):
    print(Lista2[i])
    
List=["aa","bb","cc","c"]
search = input("enter element: ")
if search in List:
    print(List.index(search))
else:
    print("not found")