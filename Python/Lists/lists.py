file = open('Python/Lists/data.csv', 'r')
data = file.read().splitlines()

#make every value a floating point number (deimal)
for i in range (len(data)):
    data[i] = float(data[i])   

print(data)

# Find the smallest
smallestSoFar = data[6]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element

print("Smallest: "+ str(smallestSoFar))


# find the sum
sumSoFar = 0
for element in data:
    sumSoFar += element

print("Sum: "+ str(sumSoFar))

# Find the largest number
largestSoFar = data[6]
for element in data:
    if element > largestSoFar:
        largestSoFar = element

print("Largest: "+ str(largestSoFar))

# find the average
average = sumSoFar / len(data)
print("Average: "+ str(average))

print("Average rounded to 2 decimal places: "+ str(round(average, 2)))