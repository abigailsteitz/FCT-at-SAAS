file = open("Python/Lists/Data.csv", "r")
data = file.read().splitlines()

# make every value a floating point number(Decimal)
for i in range(len(data)):
    data[i] = float(data[i])
print(data)

# find the smallest
smallestSoFar = data[6]
for element in data: 
    if element < smallestSoFar:
        smallestSoFar = element

print("Smallest: " + str(smallestSoFar))


# find the sum
sumSoFar = 0
for element in data:
    sumSoFar += element

print("Sum: " + str(sumSoFar))

# Find the largest number
largestSoFar = data[6]
for element in data: 
    if element > largestSoFar:
        largestSoFar = element
print("largestSoFar: " + str(largestSoFar))


# Find the average
average = sumSoFar / len(data)
print("Average: " + str(average))

print("Average rounded to 2 decimal place:" + str(round(average, 2)))

