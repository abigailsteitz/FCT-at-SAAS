file = open ("Python/lists/Data.csv")
data=file.read().splitlines()

print(data)

#make every value a floating point number
for i in range(len(data)):
    data[i] = float(data[i])

print(data)

#find the smallest value
smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
print("The smallest value is: ", smallestSoFar)

#find the sum
allnumsadded = 0
for element in data:
    allnumsadded += element
print("The sum is: ", allnumsadded)


#find the average
allnumsadded = 0
for element in data:
    allnumsadded += element
print("The sum is: ", allnumsadded)
print("The average is: ", allnumsadded/len(data))

#find the largest value
largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("The largest value is: ", largestSoFar)

#find the median
median = 0
if len(data) % 2 == 0:
    median = (data[len(data)//2] + data[len(data)//2 - 1]) / 2
else:
    median = data[len(data)//2]
print("The median is: ", median)
#find the mode
from collections import Counter 
counter = Counter(data)
most_common = counter.most_common(1)
print("The mode is: ", most_common[0][0])
#find the standard deviation