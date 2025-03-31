file = open('Python/lists/data.csv', 'r')
data = file.read().splitlines()


for i in range(len(data)):
    data[i] = float(data[i])

print(data)
smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
print("")
print("Smallest")
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
print("Largest")
print(largestSoFar)

Average = 0
for element in data:
    Average += element /10
print("Average")
print(Average)
