file = open('Python/Lists/data.csv', 'r')
data = file.read().splitlines()

print(data)

for i in range(len(data)):
    data[i] = float(data[i])


print(data)

smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element

print("Smallest:")
print(smallestSoFar)


sumSoFar = 0
for element in data:
    sumSoFar += element

print("sum")
print(sumSoFar)


largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element

print("Largest:")
print(largestSoFar)


sumSoFar = 0
for element in data:
    sumSoFar += element

average = sumSoFar / len(data)

print("Average:")
print(average)