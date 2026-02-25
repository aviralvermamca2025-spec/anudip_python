bmi = float(input("Enter BMI value: "))

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")

# Output:
# Enter BMI value: 22.5
# Normal weight