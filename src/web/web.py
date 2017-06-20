#!/usr/bin/env python2.7
#-*-coding:utf8-*-

import urllib.request

response = urllib.request.urlopen('http://wikipedia.org/')

html = response.read()

print(html)