file = open('Python/lists/data.csv', 'r')
data = file.read().splitlines()

for i in range(len(data)):
    data[i] = float(data[i])

print(data)

smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element

print("Smallest: " + str(smallestSoFar))

sumSofar = 0
for element in data:
    sumSofar += element  # Fixed the typo (sumSofar vs. sumSoFar)

print("Sum: " + str(sumSofar))

# Calculate average
average = sumSofar / len(data) if len(data) > 0 else 0

print("Average: " + str(average))

# Finding the largest number
largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element

print("Largest: " + str(largestSoFar))