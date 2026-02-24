# take three input principal, rate, time
principal = float(input("Enter the principal: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))

#alculate Simple Interest
Simple_int = (principal * rate * time ) / 100
#print result
print("Simple Interest is:", Simple_int)

#output
# Enter the principal:2000
# Enter the rate:5
# Enter the time:2
# Simple Interest is: 200.0