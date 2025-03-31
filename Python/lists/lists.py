file = open('Python/Lists/data.csv','r')
data = file.read().splitlines()

print(data)

for i in range(len(data)):
  data[i] = float(data[i])
  
print(data)

# Find the smallest
smallestSoFar = data[0]
for i in range(len(data)):
  if data[i] < smallestSoFar:
    smallestSoFar = data[i]
    
print("Smallest")
print(smallestSoFar)

# The largest looks similar
# Find the smallest
biggestSoFar = data[0]
for i in range(len(data)):
  if data[i] > biggestSoFar:
    biggestSoFar = data[i]
    

print("biggest")
print(biggestSoFar)

# Find the sum
sumSoFar = 0
for element in data:
  sumSoFar += element 
  
print("Sum")
print(sumSoFar)

# Find the average looks similar
# add all the numbers, divided by how many nums
average = sumSoFar / len(data)
print(average)