# Inventory Management System
stock = [0, 5, 20, 8, 15, 0, 3, 50, 9]

print("Original Stock:", stock)

# Remove items with 0 stock
stock = [item for item in stock if item != 0]

# Add restock to items below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

# Find total inventory
total = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory:", total)


# Output:
# Original Stock: [0, 5, 20, 8, 15, 0, 3, 50, 9]
# Updated Stock: [55, 20, 58, 15, 53, 50, 59]
# Total Inventory: 310