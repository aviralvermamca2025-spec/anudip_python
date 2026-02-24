#take input
number = int(input("Enter a number : "))
orgNum = number

rev = 0
while number > 0:
    rem = number % 10 
    rev = rev * 10 + rem
    number = number // 10

print("Orignal Number is : ", orgNum)
print("Reverse of the Number is : ", rev)

# output
# Enter a number : 1234
# Orignal Number is :  1234
# Reverse of the Number is :  4321