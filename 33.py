num_of_loaves = int(input("The number of loaves: "))

price_bread = 3.49
discount = 0.60

regular_price = num_of_loaves * price_bread 
discount_d = regular_price * discount
final = regular_price - discount_d

print("Regular price is: %5.2f"%regular_price)
print("Discount is: %5.2f"%discount_d)
print("Final result is: %5.2f"%final)