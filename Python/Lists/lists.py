# code goes here
file = open("Python/Lists/data.csv",)
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
print(smallestSoFar)

# Find the sum
allnumsadded=0
for element in data:
    allnumsadded += element
print("The sum is:")
print(allnumsadded)