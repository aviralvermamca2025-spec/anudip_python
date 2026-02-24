# Online Exam Result Processor

scores = [25, 40, 30, 35, 20, 50, 45]

print("Original Scores:", scores)

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

print("After removing lowest 2:", scores)

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

print("After grace marks:", scores)

# Count passed students
passed = 0
for s in scores:
    if s >= 40:
        passed += 1

print("Number of students passed:", passed)


# Output:
# Original Scores: [25, 40, 30, 35, 20, 50, 45]
# After removing lowest 2: [30, 35, 40, 45, 50]
# After grace marks: [35, 40, 40, 45, 50]
# Number of students passed: 4