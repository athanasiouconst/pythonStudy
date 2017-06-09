#! /usr/bin/env python
# -*- coding: utf-8 -*-

def find(item, list):
    if item in list:
        return True
    else:
        return False

def printResult(found):
    if found:
        print("Search item found")
    elif not found:
        print("Search item not found")
    else:
        print("problem")
    
a="test"
lista=["ena","dyo","tria","test","pente"]
result=find(a,lista)
printResult(result)


b="notexist"
lista=["ena","dyo","tria","test","pente"]
result=find(b,lista)
printResult(result)
