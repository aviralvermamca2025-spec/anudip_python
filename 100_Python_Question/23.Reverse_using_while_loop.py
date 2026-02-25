number = int(input("Enter a number : "))
reverse = 0
while number > 0:
    digits = number % 10
    reverse = reverse * 10 + digits
    number = number // 10
print("Reverse of the number is : ", reverse)

#Output
#Enter a number : 1234
#Reverse of the number is : 4321