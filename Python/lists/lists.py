file = open ('Python/lists/data.csv', 'r')
data = file.read().splitlines()

# make every value a floating point number (decimal)
for i in range(len(data)):
    data[i] = float(data[i])

print(data)

# Find the smallest
smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element

print("smallest:" + str(smallestSoFar))

# find the sum
sumSOFar = 0
for element in data:
    sumSOFar += element

print("sum: " + str(sumSOFar))


# Find the largest
largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("largest:" + str(largestSoFar))