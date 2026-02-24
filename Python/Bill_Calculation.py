books = int(input("Enter the number of books you buy: "))
pens = int(input("Enter the number of pens you buy: "))

bookPrice = 45
penPrice = 20

total_bill = (books * bookPrice) + (pens * penPrice)
amount_given = 500

remaining_balance = amount_given - total_bill

print("Total Bill Amount =", total_bill)
print("Remaining Balance =", remaining_balance)