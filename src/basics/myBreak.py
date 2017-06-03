correctPass = "letmein"
validUser = False

for i in range (1,4,1):
    check = input("add password : ")
    if check == correctPass:
        validUser = True
        break

if validUser:
    print("welcome ! ")
else:
    print("Try again!!")