#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Η countList είναι συνάρτηση υπολογισμού του μήκους των λέξεων 
#Δέχεται ένα όρισμα το οποίο είνα η λίστα λέξων σύφμωνα με το αρχείο που έχει επιλεγεί
#Το μήκος προσθίθεται σε μια μεταβλητή count, η οποία στο τέλος των επαναλήψεων θα έχει το συνολικό μήκοςτων λέξεων
#Στη συνάρτηση countList καλείτε η συνάρτηση countListAVG, η οποία δέχεται δύο ορίσματα
#Το πρώτο όρισμα είναι το σύνολο του μήκου των λέξεων και το δεύτερο η λίστα με τις λέξεις

#συνάρτηση υπολογισμού του μήκους των λέξεων
def countList(listItem):
    count = 0
    for i in range(len(listItem)):
        count +=len(listItem[i])
    print("Το συνολικό μήκος των λέξεων του αρχείου που επιλέξατε είναι : {0} ".format(count))
    countListAVG(count,listItem)   
    
#συνάρτηση υπολογισμού του μεσου όρους των λέξεων
def countListAVG(count, listItem):
    #υπολογισμός μέσου όρους (χωρίς δεκαδικά στοιχεία)
    listAvg = round(count / len(listItem),0)
    print("Ο μέσος όρος των λέξεων του αρχείου που επιλέξατε είναι : {0} ".format(listAvg))  


#εκκίνηση του προγράμματος, όπου ο χρήστης πληκτρολογεί το αρχείο που επιθυμεί
fileName = input("Παρακαλώ δώστε το όνομα του αρχείου που επιθυμείτε να αναγνώσεται : ")

try:
    #διάβασμα του αρχείου που έχει επιλεγεί
    fileIn = open(fileName,"r")
    text=fileIn.read()
    
    #τοποθέτηση όλων των λέξεων του αρχείου σε μια λίστα
    listItem = text.split()
    
    #κλήση συνάρτησης countList με όρισμα τη λίστα 
    countList(listItem)
    
    fileIn.close()
except IOError:
    print("Παρουσιάστηκε πρόβλημα κατά την ανάγνωση του αρχείου")
    

