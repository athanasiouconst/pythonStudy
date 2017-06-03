#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math
#a without matho.pi value

#input of pi value
pi = 3.14159

#input of aktina value
aktina = float(input("Παρακαλώ πληκτρολογήστε την ακτίνα της σφαίρας (με τιμή π=3,14159) : "))

#calculate ogkos value
ogkos  = (4/3) * (pi) * (aktina**3)

#print msg 
print("Ο όγκος της σφαίρα με ακτίνα {0} είναι {1} ".format(aktina,ogkos))

#b with matho.pi value

#input of aktina value
aktina = float(input("Παρακαλώ πληκτρολογήστε την ακτίνα της σφαίρας (με τιμή π=math.pi) : "))

#calculate ogkos value
ogkos  = (4/3) * (math.pi) * (aktina**3)

#print msg 
print("Ο όγκος της σφαίρα με ακτίνα {0} είναι {1} ".format(aktina,ogkos))
