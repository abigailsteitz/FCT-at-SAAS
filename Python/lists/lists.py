file = open('Python/Lists/data.csv', 'r')
data = file.read().splitlines()

for i in range(len(data)):
   data[i] = float(data[i])

print(data)

smallestSoFar = data[0]
for i in range(len(data)):
   if data[i] < smallestSoFar:
     smallestSoFar = data [i]

print("Smallest: " + str(smallestSoFar))

largestSoFar = data[0]
for i in range(len(data)):
   if data[i] > largestSoFar:
     largestSoFar = data [i]
    
print("Largest: " + str(largestSoFar))

sumSoFar = 0
for i in range(len(data)):
   sumSoFar += data[i]

   print("Sum: " + str(sumSoFar))
   
average = sumSoFar / len(data)
print("Average: " + str(average))