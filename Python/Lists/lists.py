# Open and read the file
file = open('Python/Lists/data.csv', 'r')
data = file.read().splitlines()
file.close()

# Convert string data to float
for i in range(len(data)):
    data[i] = float(data[i])

# Print the full list
print("Data:", data)

# Find smallest
smallest = data[0]
for value in data:
    if value < smallest:
        smallest = value
print("Smallest:", smallest)

# Find largest
largest = data[0]
for value in data:
    if value > largest:
        largest = value
print("Largest:", largest)

# Calculate sum
total = 0
for value in data:
    total += value
print("Sum:", total)

# Calculate average
average = total / len(data)
print("Average:", average)

# Calculate median (Level 4)
data.sort()
if len(data) % 2 == 0:
    mid1 = len(data) // 2
    mid2 = mid1 - 1
    median = (data[mid1] + data[mid2]) / 2
else:
    median = data[len(data) // 2]
print("Median:", median)