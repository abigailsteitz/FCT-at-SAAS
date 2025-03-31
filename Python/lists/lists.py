file = open("Python/lists/data.csv", "r")
data = file.read().splitlines()

print(data)

for i in range(len(data)):
    data[i] = float(data[i])
print(data)

print("The smallest number is:")
# Find the smallest number in a list
smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element

print(smallestSoFar)

sumSoFar = 0
for element in data:
    sumSoFar += element
print("The sum is:")
print(sumSoFar)


print("The average is:")
print(sumSoFar / len(data))


print("The largest number is:")
# Find the largest number in a list
largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print(largestSoFar)

