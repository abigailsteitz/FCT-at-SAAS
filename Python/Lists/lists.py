file = open("Python/Lists/data.csv")
data = file.read().splitlines()
print(data)

#make every value in the list an integer
for i in range(len(data)):
    data[i] = float(data[i])

print(data)

#find the smallest 
smallestSoFar = data[0]
for element in data:
    print("evaluating", element)
    if element < smallestSoFar:
        smallestSoFar = element
print("the smallest is", smallestSoFar)
#find the sum 
total = 0
for element in data:
    total += element

print ("the sum is",total)

#find the average
average = total / len(data)
print("the average is", average)

#find the largest
largestSoFar = data[0]
for element in data:
    print("evaluating", element)
    if element > largestSoFar:
        largestSoFar = element
print("the largest number is", largestSoFar)