# Read input
num = int(input("Enter the number: "))

sum_digits = 0

while num > 0:
    digit = num % 10        # Get last digit
    sum_digits += digit     # Add digit to sum
    num //= 10              # Remove last digit
#print output
print(sum_digits)

#output
#Enter the number: 56
# 11