file = open('Python/lists/data.csv', 'r')
data = file.read().splitlines()

print("What time did you eat lunch yesterday?")

for i in range(len(data)):
    data[i] = float(data[i])

print(data)

smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
print("Earliest: " + str(smallestSoFar))

largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("Latest: " + str(largestSoFar))

sumSoFar = 0
for element in data:
    sumSoFar += element
print("Sum: " + str(sumSoFar))

averageSoFar = 0
for element in data:
    averageSoFar = sumSoFar / len(data)
print("Average: " + str(averageSoFar))



