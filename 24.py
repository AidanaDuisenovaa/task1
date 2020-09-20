d = int(input("Days:"))
h = int(input("Hours:"))
m = int(input("minutes:"))
s = int(input("seconds:"))

day_in_second = d*86400
hour_in_second = h*3600
minute_in_second = m*60
result = day_in_second+hour_in_second+minute_in_second+s
print("the total number of seconds:",result)