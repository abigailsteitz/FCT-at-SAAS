# code goes here
file = open("Python/lists/data.csv" , "r")
data = file.read().splitlines() 

print(data)

# make every value a floating point number (decimal)
for i in range(len(data)):
    data[i] = float(data[i])

print(data)

# find the smallest
smallestSoFar = data [0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
        print(smallestSoFar)

# find the sum
allnumsadded=0
for element in data:
    allnumsadded += element
    print ("the sum is:")
    print(allnumsadded)


# find the largest 
largestSoFar = data [0]
for element in data:
    if element < largestSoFar:
        largestSoFar = element
print("largestSoFar")
print(largestSoFar)

# find the largest
avrege = data [0]
for element in data:
    