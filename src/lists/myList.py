#! /usr/bin/env python
# -*- coding: utf-8 -*-

List1 = ['eggs', 'spam', 'onions',2,3,2.4]

List2 = [List1,'more eggss',1200]

print(List1)
print(List2)

str = "good morning my dear friend"
t = str.split()
print(t)


str = "goodXXmorningXXmyXXdearXXfriend"
t = str.split("XX")
print(t)


Lista1 = ["costas", "maria", "constantina"]
Lista2 = ["maria", "costas", "constantina"]
Lista3 = ["ntina", "costas", "constantina"]


if Lista1 == Lista2:
    print("equal")
else:
    print("unequal")
    
    
    name="abcdefghijklmnop"

print(name[-6:-3])

str = '<a href="http://www.ekdd.gr/ekdda/custom/seminars/pdf/10319_2_2013.pdf" target="_blank" title="Σχετική Εγκύκλιος">ΗΛΕΚΤΡΟΝΙΚΗ ΓΡΑΜΜΑΤΕΙΑΚΗ ΥΠΟΣΤΗΡΙΞΗ</a>'
text = str.split('</a>')
splitText = text[0].split('">')
print(splitText[1])