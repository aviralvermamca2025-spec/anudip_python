# Attendance Tracker

attendance = [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]

print("Attendance List:", attendance)

# Calculate percentage
present = attendance.count(1)
total = len(attendance)

percentage = (present / total) * 100
print("Attendance Percentage:", percentage)

# Check below 75%
if percentage < 75:
    print("Warning: Attendance below 75%")

# Replace consecutive absences
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"
        attendance[i+1] = "Warning"

print("Updated Attendance:", attendance)


# Output:
# Attendance List: [1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
# Attendance Percentage: 60.0
# Warning: Attendance below 75%
# Updated Attendance: [1, 1, 0, 1, 'Warning', 'Warning', 1, 1, 0, 1]