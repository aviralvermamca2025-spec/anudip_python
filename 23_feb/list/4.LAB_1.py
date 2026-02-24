# Salary Processing System
salaries = [25000, 60000, 45000, 80000, 30000, 55000]

print("Original Salaries:", salaries)

# Remove below minimum wage (30000)
valid = []
for s in salaries:
    if s >= 30000:
        valid.append(s)

# Add 5% bonus to salary > 50000
for i in range(len(valid)):
    if valid[i] > 50000:
        valid[i] = valid[i] + valid[i]*0.05

# Sort descending
valid.sort(reverse=True)

print("Processed Salaries:", valid)

# Top 3 salaries
print("Top 3 Salaries:", valid[:3])


# Output:
# Original Salaries: [25000, 60000, 45000, 80000, 30000, 55000]
# Processed Salaries: [84000.0, 63000.0, 57750.0, 45000, 30000]
# Top 3 Salaries: [84000.0, 63000.0, 57750.0]