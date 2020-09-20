money = float(input("Your cost: "))

tax_rate = 0.08
tip_rate = 0.21

tax = money * tax_rate
tip = money * tip_rate
result = tax + money + tip

print("Your tax %.2f" % tax)
print("Your tip %.2f" % tip)
print("Your final cost %.2f" % result)