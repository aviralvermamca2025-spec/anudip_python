# Bank Transaction Analyzer
transactions = [5000, -2000, 15000, -500, 20000, -7000, 12000]

print("Transactions:", transactions)

# Total balance
balance = sum(transactions)

# Largest withdrawal
withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals)

# Deposits greater than 10000
count = 0
for t in transactions:
    if t > 10000:
        count += 1

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits greater than 10000:", count)


# Output:
# Transactions: [5000, -2000, 15000, -500, 20000, -7000, 12000]
# Total Balance: 42500
# Largest Withdrawal: -7000
# Deposits greater than 10000: 3