file = open('Python/Lists/data.csv', 'r')
data = file.read().splitlines()

print("Data is based on # of hours of sleep in the last night")
#make every value a floating point number (decimal)

for i in range(len(data)):
    data[i] = float(data[i])

print(data)

#find the smallest number in the list
smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element

print("Smallest: " + str(smallestSoFar))

#find the sum of the list
sumSoFar = 0
for element in data:
    sumSoFar += element

print("Sum: " + str(sumSoFar))

#find the average of the list
average = sumSoFar / len(data)
print("Average: " + str(average))

#find the largest number in the list
largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("Largest: " + str(largestSoFar))
