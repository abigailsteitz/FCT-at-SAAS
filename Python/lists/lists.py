file = open('Python/lists/data.csv', 'r')
data = file.read().splitlines()

print(data)

for i in range(len(data)):
    data[i] = float(data[i])

print(data)

largestSoFar = data[0]
for element in data:
    if element > largestSoFar:
        largestSoFar = element


print("Largest: " + str(largestSoFar))

sumSoFar = 0
for i in range(len(data)):
    sumSoFar += data[i] 
    
print("Sum: " + str(sumSoFar))


average = sumSoFar / len(data)

print("Average:", average)
