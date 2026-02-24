# Temperature Monitoring System

temps = [35, 42, 38, 46, 40, 39, 47, 41, 36]

print("Temperatures:", temps)

# Hottest and coldest
hottest = max(temps)
coldest = min(temps)

# Replace above 45 with Heat Alert
for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

# Count extreme days (>40)
count = 0
for t in temps:
    if t != "Heat Alert" and t > 40:
        count += 1

print("Hottest Day:", hottest)
print("Coldest Day:", coldest)
print("Updated Temps:", temps)
print("Extreme Days:", count)


# Output:
# Temperatures: [35, 42, 38, 46, 40, 39, 47, 41, 36]
# Hottest Day: 47
# Coldest Day: 35
# Updated Temps: [35, 42, 38, 'Heat Alert', 40, 39, 'Heat Alert', 41, 36]
# Extreme Days: 2