#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

def searchVariableFunction():    
    #O χρήστης πληκτρολογεί το αλφαριθμιτικό που επιθυμεί
    searchVariable = input("Παρακαλώ δώστε το αλφαριθμιτικό που επιθυμείτε να αναζητήσετε : ")
    return searchVariable

def startNumber():    
    #O χρήστης πληκτρολογεί τη σελίδα έναρξης
    while True:
        try:
            searchStartNumber = int(input("Παρακαλώ δώστε τον αριθμό της σελίδας έναρξης : "))
            break
        except ValueError:
            print("Παρακαλώ δώστε ένα ακέραιο αριθμό. Προσπαθήστε ξανά!")
            print("")
    return searchStartNumber

def finishNumber():    
    #O χρήστης πληκτρολογεί τη τελική σελίδα
    while True:
        try:
            searchFinishNumber = int(input("Παρακαλώ δώστε τον αριθμό της τελικής σελίδα : "))
            break
        except ValueError:
            print("Παρακαλώ δώστε ένα ακέραιο αριθμό. Προσπαθήστε ξανά!")
            print("")
    return searchFinishNumber


#εκκίνηση του προγράμματος
#ανάθεση τιμών
searchVariableIndex = searchVariableFunction()
startNumberIndex = startNumber()
finishNumberIndex = finishNumber()

print("")
print("Έχετε πληκτρολογήσει για αναζήτηση τη λέξη: {0} . ".format(searchVariableIndex))
print("")
print("Η σελίδα έναρξης είναι η {0} . ".format(startNumberIndex))
print("")
print("Η σελίδα λήξης είναι η {0} . ".format(finishNumberIndex))
print("")

#read request
response = urllib.request.urlopen('http://www.kathimerini.gr/')
html = response.read()


print("Έχουν δημιουργηθεί σελίδες html των παρακάτω διευθύνσεων: ")

for i in range (startNumberIndex, finishNumberIndex+1):
    url = "http://www.kathimerini.gr/search?q={0}&t={1}&page={2}".format(searchVariableIndex, startNumberIndex, i)
    #create file ekdd.html in binary mode
    fileout = open("page{0}.html".format(i),"wb")
    
    #write html from http://www.kathimerini.gr/ response
    fileout.write(html)
    fileout.close()
    print("Η σελίδα page{0}.html αντιστοιχεί στη διεύθυνση {1}".format(i, url))


