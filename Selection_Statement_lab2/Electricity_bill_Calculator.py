# Electricity Bill Calculator

# Input
units = int(input("Enter electricity units consumed: "))
age = int(input("Enter age: "))

# Bill calculation
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7

else:
    bill = units * 10

# Senior citizen discount
if age >= 60:
    discount = bill * 0.10
    bill = bill - discount

# Output
print("Electricity Bill=", bill)
