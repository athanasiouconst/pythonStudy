#!/usr/bin/python
# -*- coding: utf-8 -*-


#input of protosArithmos value
protosArithmos = ""
protosArithmosBoolean = False

#input of deyterosArithmos value
deyterosArithmos = ""
deyterosArithmosBoolean = False


while( type(protosArithmos)!=int ):
    protosArithmos = int(input("Παρακαλώ εισάγετε τον πρώτο ακέραιο αριθμό της επιθυμίας σας : "))
    if(type(protosArithmos)==int):
        protosArithmosBoolean = True
        break

while( type(deyterosArithmos)!=int ):
    deyterosArithmos = int(input("Παρακαλώ εισάγετε τον δεύτερο ακέραιο αριθμό της επιθυμίας σας : "))
    if(type(deyterosArithmos)==int):
        deyterosArithmosBoolean = True
        break

if(protosArithmosBoolean == False & deyterosArithmosBoolean == False):
    print("Try Again!")


if(protosArithmosBoolean == True & deyterosArithmosBoolean == True):
    if(deyterosArithmos < protosArithmos):
        temp = protosArithmos
        protosArithmos = deyterosArithmos
        deyterosArithmos=temp
    print("Οι πρώτοι αριθμοί στο διάστημα {0} - {1} είναι, όπως παρακάτω : ".format(protosArithmos,deyterosArithmos))

for protosArithmos in range(protosArithmos, deyterosArithmos):
    if protosArithmos%2 != 0:
        print(protosArithmos)
            

  