file = open("Python/Lists/data.csv")
data = file.read().splitlines()


print(data)

for i in range(len(data)):
    data[i] = float(data[i])

  
print(data)


#Find the smallets number in the list
smallestSoFar = data[0]
for element in data:
    if element < smallestSoFar:
        smallestSoFar = element

print("The smallest number is:")
print(smallestSoFar)

#find the sum
allnumadded=0
for element in data:
    allnumadded += element
print("The sum of all the numbers is:")
print(allnumadded)

#the largest number in the list
largestSoFar = data[0] 
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("The largest number is:") 
print(largestSoFar)

#the average of the numbers in the list
average = allnumadded / len(data)
print("The average of the numbers is:")
print(average)
#the median of the numbers in the list
median = 0 
if len(data) % 2 == 0:
    median = (data[len(data)//2] + data[len(data)//2 - 1]) / 2
else:
    median = data[len(data)//2]
print("The median of the numbers is:")
print(median)

