moredeposit = 0.25
lessdeposit = 0.10

more = int(input("Do you have more than one liter?: "))
less = int(input("Do you have one liter or less?: "))

refund = moredeposit*more + lessdeposit*less
print("Your total refund is $%.2f. " % refund)