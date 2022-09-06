#convert weight in kg to pounds or pounds to kg 



weight =int(input("Enter your weight:"))

pound_or_kg = input("(L)bs or (k)g:")


#pounds to kg
if pound_or_kg.upper() == "L":
    converted = weight*0.45
    print(f"you are {converted} kilos") 
#kg to pounds
elif pound_or_kg.upper() == "K":
    converted = weight/0.45
    print(f"you are {converted} pounds")

else:
    print("Enter correctly i.e k or l")