def Addition_Calculation(num1,num2):
    addition = num1 + num2

def Addition_Calculation(num1,num2):
    addition = num1 + num2
    return addition

def Product_of_two_number(num1,num2):
    Product = num1 * num2
    return Product

def Division_of_two_number(num1,num2):
    Division = num1 / num2
    return Division

num1 = float(input("Enter first number"))
num2 = float(input("Enter Second number"))

# sum_result, diff_result = Addition_Calculation(num1, num2)
sum_result =Addition_Calculation(num1,num2)
diff_result =Difference_Calculation(num1,num2)
product_result = Product_of_two_number(num1, num2)
Division_result = Division_of_two_number(num1,num2)


# Display results
print("Addition:", sum_result)
print("Difference:", diff_result)
print("Product:",product_result)
print("Division:",Division_result)

