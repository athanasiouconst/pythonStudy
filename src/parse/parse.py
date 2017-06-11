#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

def subText(data):
    
    #Διάβασμα του κώδικα html 
    html = data
    
    #έυρεση των συνδέσμων με πρότυπο "http://www.ekdd.gr/ekdda/custom/seminars/pdf/"
    strLink = re.findall('http://www.ekdd.gr/ekdda/custom/seminars/pdf/.*', html)
    #δομή επάνάληψης, όπου και θα πραγματοποιηθούν τρια διαδοχικά split για το τελικό αποτέλεσμα
    
    for i in range (len(strLink)):
        #πρώτο split ώστε να βρεθεί το link
        httpSplit = strLink[i].split('" target="_blank" ')
        #εκτύπωση link
        print(httpSplit[0])
        #δεύτερο spli με το κλείσιμο του συνδέσμου
        strSplit = strLink[i].split('</a>') 
        
        #τρίτο split για τον τίτλο του συνδέσμου
        splitText = strSplit[0].split('">')
        #εκτύπωση τίτλου συνδέσμου
        print(splitText[1])
        
        #εκτύπωση κενής γραμμής
        print("")

            
#εκκίνηση του προγράμματος, όπου ο χρήστης πληκτρολογεί το αρχείο που επιθυμεί
fileName = input("Παρακαλώ δώστε το όνομα του αρχείου που επιθυμείτε να αναγνώσετε : ")

try:
    #διάβασμα του αρχείου που έχει επιλεγεί
    fileIn = open(fileName, "r", encoding="utf-8")
    data = fileIn.read()
    #κλήση της συνάρτησης subText με όρισμα το αρχείο ως κείμενο data
    subText(data)
    fileIn.close()
except IOError:
    print("Παρουσιάστηκε πρόβλημα κατά την ανάγνωση του αρχείου")
    

