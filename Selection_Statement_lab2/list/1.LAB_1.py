# Student Marks Analyzer

marks = [95, 102, 67, -5, 88, 76, 54, 120, 89, 45]

print("Original Marks:", marks)

# Remove invalid marks
valid_marks = []
for m in marks:
    if 0 <= m <= 100:
        valid_marks.append(m)

print("Valid Marks:", valid_marks)

# Calculate average
total = sum(valid_marks)
avg = total / len(valid_marks)
print("Average Marks:", avg)

# Find topper
topper = max(valid_marks)
print("Topper Marks:", topper)

# Display grades
print("Grades:")
for m in valid_marks:
    if m >= 90:
        print(m, "Grade A")
    elif m >= 75:
        print(m, "Grade B")
    elif m >= 50:
        print(m, "Grade C")
    else:
        print(m, "Grade D")


# Output:
# Original Marks: [95, 102, 67, -5, 88, 76, 54, 120, 89, 45]
# Valid Marks: [95, 67, 88, 76, 54, 89, 45]
# Average Marks: 73.43
# Topper Marks: 95
# Grades:
# 95 Grade A
# 67 Grade C
# 88 Grade B
# 76 Grade B
# 54 Grade C
# 89 Grade B
# 45 Grade D


