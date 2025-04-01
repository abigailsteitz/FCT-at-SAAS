file = open("Python/Lists/data.csv")
data =file.read().splitlines()

print(data)

for i in range(len(data)):
    data[i] = float(data[i])

print(data)


smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
print(smallestSoFar)

allnumsadded=0
for element in data:
    allnumsadded += element
print("The sum is:")
print(allnumsadded)

# average: The sum of a list of numbers, divided by how many numbers there are
average=allnumsadded / len(data)

print("Average is:")
print(average)

largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("Largest number is:")
print(largestSoFar)



