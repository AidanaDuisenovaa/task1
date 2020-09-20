s1 = float(input("First side:"))
s2 = float(input("Second side:"))
s3 = float(input("Third side:"))

s = s1 + s2 + s3
area = (s * (s - s1)*(s - s2)*(s - s3))**0.5
print("Area is: %.2f" % area)