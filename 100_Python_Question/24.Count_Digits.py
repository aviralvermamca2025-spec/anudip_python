number = int(input("Enter a number : "))
count = 0
while number > 0:
    number = number // 10
    count +=1
print("Count of digits in the number is : " , count)

#Output
#Enter a number : 12345
#Count of digits in the number is : 5