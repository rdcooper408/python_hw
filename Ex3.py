#EX.3)
R_DNA = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
R_DNAcut = R_DNA.find('AATTC')
R_DNA1 = R_DNA[0:R_DNAcut]
R_DNA2 = R_DNA[R_DNAcut:100]
print(R_DNA1)
print("Fragment 1 Length = " + str(len(R_DNA1)))
print(R_DNA2)
print("Fragment 2 Length = " + str(len(R_DNA2)))
