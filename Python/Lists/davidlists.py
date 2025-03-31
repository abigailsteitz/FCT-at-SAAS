file = open('Python/Lists/daviddata.csv', 'r')
data = file.read().splitlines()

# Make every value a floating point (decimal)

for i in range(len(data)):
  data[i] = float(data[i])



print(data)


smallestSoFar = data[0]
for element in data:
  if element < smallestSoFar:
    smallestSoFar = element

print("Smallest: " + str(smallestSoFar))




greatestSoFar = data[7]
for i in range(len(data)):
  if data[i] > greatestSoFar:
    greatestSoFar = data[i]
    
print("Greatest: " + str(greatestSoFar))

# Find the sum
sumSoFar = 0
for element in data:
  sumSoFar += element
  
print("Sum: " + str(sumSoFar))



averageSoFar = 0

averageSoFar = sumSoFar/len(data)

print("Average: " + str(averageSoFar))


