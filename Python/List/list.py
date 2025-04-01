file = open ("python/List/data.csv")
data = file.read().splitlines()

print(data)

for i in range (len(data)):
    data[i] = float(data[i])

print(data)

smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element
print("the smallest number is")
print(smallestSoFar)

largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("the largest number is")
print(largestSoFar)

#find the sum

allnumbsadded = 0
for element in data:
    allnumbsadded += element
print("the sum is")
print(allnumbsadded)

#find the average
average = allnumbsadded / len(data)
print("the average is")
print(average)

#find the median which is the middle value between the highest and lowest number
Median = (largestSoFar + smallestSoFar)/2
print("the median is")
print(Median)