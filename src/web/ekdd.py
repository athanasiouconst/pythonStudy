#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

#read request
response = urllib.request.urlopen('http://www.ekdd.gr/')
html = response.read()

#create file ekdd.html in binary mode
fileout = open("ekdd.html","wb")

#text variable with the html response from the website
text = html

#write html into ekdd.html file
fileout.write(text)
fileout.close()
