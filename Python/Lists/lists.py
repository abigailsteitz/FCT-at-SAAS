file = open('Python/Lists/data.csv', 'r')
data = file.read().splitlines()

# Convert each line in the data to a floating point number
data = [float(line) for line in data]
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
largestSoFar = data[0]
for i in range(len(data)):
  if data[i] > largestSoFar:
    largestSoFar = data[i]

print("largest: " + str(largestSoFar))

# Find the sum
sumSoFar = 0
for i in range(len(data)):
  sumSoFar += data[i]
  
print("Sum: " + str(sumSoFar))

# Find the average looks similar

averageSoFar = 0
if len(data) > 0: # To avoid division by zero
  averageSoFar = sumSoFar / len(data)

  print("Average: " + str(averageSoFar))