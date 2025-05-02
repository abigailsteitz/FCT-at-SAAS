file = open("Python/Lists/data.csv", "r")
data = file.read().splitlines()

#make every value a floating point number (decimal)
for i in range(len(data)):
    data[i] = float(data[i])




print(data)

#find the smallest
smallestSoFar = data[4]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
print("Smallest: " + str (smallestSoFar))

#find the largest
smallestSoFar = data[4]
for element in data:
    if element > smallestSoFar:
        smallestSoFar = element
print("Largest: " + str (smallestSoFar))

#find the sum
sumsofar = 0
for element in data:
    sumsofar += element
print("Sum: " + str (sumsofar))

#find the average
average = sumsofar / len(data)
print("Average: " + str (average))