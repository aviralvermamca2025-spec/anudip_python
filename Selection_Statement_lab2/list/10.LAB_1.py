# Sports Tournament Points Table

# List of team points
points = [45, 60, -10, 30, 75, 50, -5, 65]

print("Original Points:", points)

# Replace negative points with 0
for i in range(len(points)):
    if points[i] < 0:
        points[i] = 0

print("After replacing negative points:", points)

# Sort leaderboard in descending order
points.sort(reverse=True)

print("Sorted Leaderboard:", points)

# Find winner and runner-up
winner = points[0]
runner_up = points[1]

print("Winner Points:", winner)
print("Runner-up Points:", runner_up)


# Output:
# Original Points: [45, 60, -10, 30, 75, 50, -5, 65]
# After replacing negative points: [45, 60, 0, 30, 75, 50, 0, 65]
# Sorted Leaderboard: [75, 65, 60, 50, 45, 30, 0, 0]
# Winner Points: 75
# Runner-up Points: 65