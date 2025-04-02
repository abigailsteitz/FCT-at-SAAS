file = open('Python/Lists/data.csv', 'r')
data = file.read().splitlines()

# make every value a floating point number (decimal)
for i in range(len(data)):
  data[i] = float(data[i])
  
print(data)

# Find the smallest
smallestSoFar = data[0]
for i in range(len(data)):
  if data[i] < smallestSoFar:
    smallestSoFar = data[i]
    
print("Smallest: " + str(smallestSoFar))

# The largest looks similar

# Find the sum
sumSoFar = 0
for i in range(len(data)):
  sumSoFar += data[i]
  
print("Sum: " + str(sumSoFar))

# Find the average looks similar