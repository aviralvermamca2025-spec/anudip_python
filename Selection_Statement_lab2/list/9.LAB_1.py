# Movie Rating System

ratings = [5, 4, 3, 6, 2, 5, 1, 0, 5, 4]

print("Original Ratings:", ratings)

# Remove invalid ratings
valid = []
for r in ratings:
    if 1 <= r <= 5:
        valid.append(r)

# Average rating
avg = sum(valid) / len(valid)

# Count 5-star ratings
count_5 = valid.count(5)

# Sort ascending
valid.sort()

print("Valid Ratings:", valid)
print("Average Rating:", avg)
print("Number of 5-star ratings:", count_5)


# Output:
# Original Ratings: [5, 4, 3, 6, 2, 5, 1, 0, 5, 4]
# Valid Ratings: [1, 2, 3, 4, 4, 5, 5, 5]
# Average Rating: 3.625
# Number of 5-star ratings: 3