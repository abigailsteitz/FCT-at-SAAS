file = open('Python/lists/data.csv', 'r')
data = file.read().splitlines()

print(data)
 
# make every value a floating point number (decimal)
for i in range(len(data)):
  data[i] = float(data[i])

# Find the largest
largestSoFar = data[0]
for i in range(len(data)):
  if data[i] > largestSoFar:
    largestSoFar = data[i]
    
print("Largest: " + str(largestSoFar))

# The largest looks similar

# Find the sum
sumSoFar = 0
for i in range(len(data)):
  sumSoFar += data[i]
  
print("Sum: " + str(sumSoFar))

# Find the average looks similar
average = sumSoFar / len(data)
print("Average: " + str(average))