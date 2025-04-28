# code goes here
file = open("Python/Lists/data.csv")
data = file.read().splitlines()

print(data)

# make every value a floating point number (decimal)
for i in range(len(data)):
    data [i] = float(data[i])

print(data)

# Find the smallest
smallestSoFar = data [0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
print("this is the smallest number")
print(smallestSoFar)

# Find the largest
largestSoFar = data [0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("this is the largest number")
print(largestSoFar)
# Find the sum
allnumsadded=0
for element in data:
    allnumsadded += element
print("The sum is:")
print(allnumsadded)
# What is an average
# An average is the sum of all the numbers divided by how many numbers there are
average = allnumsadded / (len(data))
print("The average is:")
print(average)