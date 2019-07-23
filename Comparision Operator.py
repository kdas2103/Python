name=input("what is your name? " ) # varable stored through input for name
name_length=int(len(name))          # calculate the lenght of input, coverted to intiger nad stored as variable
if name_length>3 and name_length<50: # applied conditional operator
    print("Name looks good")
else:
    print("Name must be more than 3 and less than 50 characters")
