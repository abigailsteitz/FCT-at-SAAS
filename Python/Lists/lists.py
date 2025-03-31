file = open("Python/Lists/data.csv", "r")
data = file.read().splitlines()

# make every value a floating point number (decimal)
for i in range(len(data)):
    data[i] = float(data[i])

print(data)

# Find the smallest
smallestSoFar = data[7]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element

print("smallest:" + str(smallestSoFar))

# Find the largest
largestSoFar = data[3]
for element in data:
    if element > largestSoFar:
        largestSoFar = element

print("largest:" + str(largestSoFar))

# Find the sum
sumSoFar = 0
for element in data:
    sumSoFar += element

print("sum:" + str(sumSoFar))

# Find the average
averageSoFar = 0
for element in data:
    sumSoFar/len(data)

print("average:" + str(sumSoFar / len(data)))  

# find the median
# Sort the data first
data.sort()  # Sort the data in ascending order

print("sorted data: " + str(data))







