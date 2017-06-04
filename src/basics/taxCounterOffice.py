#! /usr/bin/env python
# -*- coding: utf-8 -*-

#eisodima = 4500
#foros= ((1000 * 0) + 1000* 5/100 + 1000 *10/100 + 1500* 14/100)
#print(foros)

elaxistoEisodima = 1000
mediumEisodima = 2000
goodEisodima = 3000
elaxistoForos = 0
telikosForos = 0
#variable which is used for the subtraction
diaforaEisodimatos = 0
diaforaEisodimatosMedium=0
diaforaEisodimatosGood=0
diaforaEisodimatosVeryGood=0

#input of eisodima value
eisodima = float(input("Παρακαλώ πληκτρολογήστε το εισόδημα σας σε ευρώ : "))

if eisodima <= elaxistoEisodima:
    print("Ο φόρος που αναλογεί σε εισόδημα {0} είναι : {1} ευρώ".format(elaxistoEisodima,elaxistoForos))
    
elif (eisodima <= mediumEisodima) :
    diaforaEisodimatos =  eisodima - elaxistoEisodima
    telikosForos = diaforaEisodimatos * 5 /100
    print("Ο φόρος που αναλογεί σε εισόδημα {0} είναι : {1} ευρώ".format(eisodima,telikosForos))

elif (eisodima <= goodEisodima) :
    diaforaEisodimatosMedium =  eisodima - mediumEisodima
    telikosForos = elaxistoEisodima * 5 /100 + diaforaEisodimatosMedium* 10 / 100
    print("Ο φόρος που αναλογεί σε εισόδημα {0} είναι : {1} ευρώ".format(eisodima,telikosForos))

elif (eisodima > goodEisodima) :
    diaforaEisodimatosMedium =  eisodima - mediumEisodima 
    diaforaEisodimatosGood = goodEisodima - mediumEisodima
    diaforaEisodimatosVeryGood = eisodima - goodEisodima
    telikosForos = elaxistoEisodima * 5 /100 + diaforaEisodimatosGood* 10 / 100 + diaforaEisodimatosVeryGood * 14 / 100   
    print("Ο φόρος που αναλογεί σε εισόδημα {0} είναι : {1} ευρώ".format(eisodima,telikosForos))
    
    