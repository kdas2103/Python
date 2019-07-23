weight=int(input("what is your weight? ")) # converting the input to intiger and storing it as variable
unit=input("(L)bs or (k)g: ")
if unit.upper()== "L":                      # converting the UNIT input to upper case 
    converted=weight*0.45
    print(f"Your weight in Kgs: {converted}")
else:
    converted=weight/0.45
    print(f"Your weight in lbs: {converted}")

