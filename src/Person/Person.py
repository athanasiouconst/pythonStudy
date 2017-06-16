#!/usr/bin/python
# -*- coding: utf-8 -*-


#class Person
class Person:        
    personCount = 0
    #init Person
    def __init__(self, lastName, firstName, age, address):
        self.lastName = lastName
        self.firstName = firstName
        self.age = age
        self.address = address
        Person.personCount += 1
    
    #showInfo method    
    def ShowInfo(self):
        print ( "  Επώνυμο : ", self.lastName,
                ", Όνομα: ", self.firstName,
                ", Ηλικία ", self.age,
                ", Διεύθυνση ", self.address)

#class Student
class Student(Person): 
    
    #init Student
    def __init__(self, lastName, firstName, age, address, graduateSchool):
        Person.__init__(self, lastName, firstName, age, address)
        self.graduateSchool = graduateSchool

    #showStudent method    
    def ShowStudent(self):
        print ( "  Επώνυμο : ", self.lastName,
                ", Όνομα: ", self.firstName,
                ", Ηλικία ", self.age,
                ", Διεύθυνση ", self.address,
                ", Σχολείο Αποφοίτησης ", self.graduateSchool)



#Person Class
"Δημιουργία object για κλάση Person "
person1 = Person("Αθανασίου", "Κωνσταντίνος", "32" ,"Δημητρίου Ανδρεά 109-111")
person2 = Person("Μιχαήλ", "Κωνσταντίνα", "30" ,"Μάρκου Μπότσαρη 109-111")

"Εκτύπωση δεδομένων για τη κλάση Person "
print("Εκτύπωση δεδομένων για τη κλάση Person :")
person1.ShowInfo()
person2.ShowInfo()
print("")

"Δημιουργία object για κλάση Student "
student1 = Student("Αθανασίου", "Κωνσταντίνος", "32" ,"Δημητρίου Ανδρεά 109-111","4ο Λύκειο")
student2 = Student("Μιχαήλ", "Κωνσταντίνα", "30" ,"Μάρκου Μπότσαρη 109-111","5ο Λύκειο")

print("Εκτύπωση δεδομένων για τη κλάση Student :")
student1.ShowStudent()
student2.ShowStudent()
print("")

print("Εκτύπωση δεδομένων για τη κλάση Student με μέθοδο της Person:")
student1.ShowInfo()
student2.ShowInfo()
print("")
