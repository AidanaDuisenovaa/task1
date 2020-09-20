from math import sqrt

height = float(input("Height in meter: "))
gravity = 9.8
vf = sqrt(gravity * 2 * height)
print("Hit the ground at %.2f m/s."%vf)