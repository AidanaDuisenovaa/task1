first = int(input("First number: "))
second = int(input("Second number: "))
third = int(input("Third number: "))

maximum = max(first,second,third)
minimum = min(first,second,third)
midium = first + second +third - minimum - maximum

print(minimum)
print(midium)
print(maximum)