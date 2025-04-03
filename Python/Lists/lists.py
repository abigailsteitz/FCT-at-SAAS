file = open("Python/Lists/data.csv")
data = file.read().splitlines()

print(data)

for i in range(len(data)):
    data[i] = float(data[i])

print(data)

# Find the smallest
smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
print("The smallest number is:")
print(smallestSoFar)

# Find the largest
largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("The largest number is:")
print(largestSoFar)

# Find the sum
allnumbersadded=0
for element in data:
    allnumbersadded += element
print("The sum is:")
print(allnumbersadded)

# Find the average
average = allnumbersadded / len(data)
print("The average is:")
print(average)
