feet = int(input("Your number of feet:"))
inches = int(input("Your number of inches: "))


one_foot_in = 12
one_in_cent = 2.54
                 
cm = (feet*one_foot_in + inches)*one_in_cent
                 
print("Your height in cm:",cm)