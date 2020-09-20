from math import tan,pi
s = float(input("The length is: "))
n = int(input("The number of side: "))

area = (n * s **2)/(tan(pi/n)*4)
print("The area of polygon: %.2f"%area)