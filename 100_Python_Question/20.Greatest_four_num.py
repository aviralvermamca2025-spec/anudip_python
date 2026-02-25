num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
num3 = float(input("Enter the third number : "))
num4 = float(input("Enter the fourth number : "))

if(num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("The greatest number is : ", num1)
elif(num2 >= num1 and num2 >= num3 and num2 >= num4):
    print("The greatest number is : ", num2)
elif(num3 >= num1 and num3 >= num2 and num3 >= num4):
    print("The greatest number is : ", num3)
elif(num4 >= num1 and num4 >= num2 and num4 >= num3):
    print("The greatest number is : ", num4)

#Output
#Enter the first number : 21
#Enter the second number : 34
#Enter the third number : 60
#Enter the fourth number : 24
#The greatest number is : 60.0