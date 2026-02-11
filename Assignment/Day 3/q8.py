qty = int(input("Enter quantity: "))
unit_price = 5

total_price = qty * unit_price

if qty > 50:
    discount = total_price * 0.15
elif qty > 30:
    discount = total_price * 0.10
else:
    discount = 0

final_price = total_price - discount

print("Total price:", total_price)
print("Discount:", discount)
print("Final price to pay:", final_price)