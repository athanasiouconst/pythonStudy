#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math

#input of aktina value
aktina = float(input("Παρακαλώ πληκτρολογήστε την ακτίνα του κώνου : "))

#input of ypsos value
ypsos = float(input("Παρακαλώ πληκτρολογήστε το ύψος του κώνου : "))

#calculate embado value
embado  = (math.pi * aktina * (math.sqrt(aktina**2 + ypsos**2)+aktina) )

#print msg 
print("Το εμβαδό του κώνου με ακτίνα {0} και ύψος {1} είναι : {2} ".format(aktina,ypsos, embado))
