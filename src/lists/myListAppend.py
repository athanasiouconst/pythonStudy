#! /usr/bin/env python
# -*- coding: utf-8 -*-

Lista1 = ["aa","bb"]
Lista2 = ["c", "d","c"]

Lista1.append(Lista2)

print(Lista1)

Lista1 = ["aa","bb"]
Lista2 = ["c", "d","c"]

Lista1.extend(Lista2)
print(Lista1)
