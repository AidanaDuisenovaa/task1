ss = int(input("Seconds"))
D = 0
H = 0
M = 0


minutes = 60
hours = 3600
days = 24 * 3600

if ss // days != 0:
    D = ss // days
    ss %= days

if ss // hours != 0:
    H = ss // hours 
    ss %= hours 

if ss // minutes != 0:
    M = ss // minutes 
    ss %= minutes

print("%i:%02i:%02I:%02I" % (D, H , M, ss))

