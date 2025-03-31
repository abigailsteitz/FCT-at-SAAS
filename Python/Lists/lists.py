file = open('Python/Lists/data.csv', 'r')
data = file.read().splitlines()
for i in range(len(data)):
    data[i] = float(data[i]) 
 
print(data)

#find the smallest
smallestSoFar = data[1]
for element in data: 
    if element < smallestSoFar:
        smallestSoFar  = element
print("smallest: " + str(smallestSoFar))
    
#find the largest
largestSoFar = data[1]
for element in data: 
    if element > largestSoFar:
        largestSoFar  = element
print("largest: " + str(largestSoFar))
    
#find the sum
sumSoFar = 0
for element in data: 
    sumSoFar += element
print("Sum: " + str(sumSoFar))

#find the average
averageSoFar = sumSoFar / len(data)
print("Average: " + str(averageSoFar))

#find the median. will need myListNameHere.sort
# Find the median
data.sort()  # Ensure the data is sorted
medianSoFar = 0
mid = len(data) // 2  # Integer division

if len(data) % 2 == 0:
    medianSoFar = (data[mid] + data[mid - 1]) / 2  # Average of middle two numbers
else:
    medianSoFar = data[mid]  # Middle element for odd-length lists

print("Median:", medianSoFar)
    

