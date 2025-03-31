file = open('Python/lists/data.csv', 'r')
data = file.read().splitlines()

print("what was your GPA in winter tri '24-'25?")
print("answers:")

for i in range(len(data)):
    data[i] = float(data[i])

print(data)

#find smallest number
smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element

print("smallest / lowest GPA:")
print(smallestSoFar)

#find sum
sumSoFar = 0
for element in data:
    sumSoFar += element

print("sum:")
print(sumSoFar)

#find largest
largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element

print("largest / highest GPA:")
print(largestSoFar)

#find average
averageSoFar = sumSoFar/len(data)

print("average (GPA):")
print(averageSoFar)