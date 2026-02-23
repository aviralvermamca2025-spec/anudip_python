# E-Commerce Cart System

prices = [1000, 2000, 3000, 2000, 1500, 500]

print("Original Prices:", prices)

# Remove duplicates
unique_prices = list(set(prices))
print("Unique Prices:", unique_prices)

# Calculate total
total = sum(unique_prices)
print("Total:", total)

# Apply discount
if total > 5000:
    discount = total * 0.10
else:
    discount = 0

total_after_discount = total - discount

# Add GST
gst = total_after_discount * 0.18
final_amount = total_after_discount + gst

print("Final Amount:", final_amount)


# Output:
# Original Prices: [1000, 2000, 3000, 2000, 1500, 500]
# Unique Prices: [1000, 2000, 3000, 1500, 500]
# Total: 8000
# Final Amount: 8496.0