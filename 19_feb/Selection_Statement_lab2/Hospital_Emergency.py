age = int(input("Enter patient age: "))
heart_rate = int(input("Enter heart rate: "))
severe_injury = input("Does the patient have a severe injury? (yes/no): ").strip().lower()
moderate_condition = input("Is the condition moderate? (yes/no): ").strip().lower()

# Check if heart rate is abnormal (normal range: 60–100)
heart_abnormal = heart_rate < 60 or heart_rate > 100

# Determine initial category
if heart_abnormal or severe_injury == "yes":
    category = "Critical"
elif moderate_condition == "yes":
    category = "Moderate"
else:
    category = "Normal"

# Upgrade rule for elderly patients
if age > 65 and category == "Moderate":
    category = "Critical"

# Output
print("Triage Category:", category)
