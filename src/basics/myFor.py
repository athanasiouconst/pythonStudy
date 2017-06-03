basi = int(input("add an bash:"))
ekthetis = int(input("add ektheti:"))
i = 1
dynami = 1

for i in range (0,ekthetis,1):
    dynami = dynami * basi
    
print("i basi {0} pros ton ektheti {1} einai {2}: ".format(basi,ekthetis,dynami))
