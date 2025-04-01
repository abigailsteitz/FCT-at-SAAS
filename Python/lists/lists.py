file = open ("Python/Lists/data.csv", "r")
data = file.read().splitlines()

print(data)

for i in range(len(data)):
    data[i] = float(data[i])

print(data)

smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
print("the smallest number is:")
print(smallestSoFar)

largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("the largest number is:")
print(largestSoFar)

allnumsadded = 0
for element in data:
    allnumsadded += element
print("the sum is:")
print(allnumsadded)

average = allnumsadded / len(data)
print("the average is:")
print(average)