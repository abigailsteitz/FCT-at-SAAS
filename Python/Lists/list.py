import math

file = open("Python/Lists/Data.csv", "r")
data = file.read().splitlines()

print("These are the favorite numbers of my classmates")

# Make every value a floating point number

for i in range(len(data)):
    data[i] = float(data[i])

print(data) 

# Find the smallest

smallest = data[7]
for element in data:
    if element < smallest:
        smallest = element
print("The smallest")
print(smallest)

# find the sum
sum = 0
for element in data:
    sum += element
print("The sum")
print (sum)



# find the average
# Add up all nummbers, divide by the number of numbers
average = sum / len(data)

print("The average")
print(average)

# find the largest

biggest = data[7]
for element in data:
    if element > biggest:
        biggest = element
        
print("The biggest")
print(biggest)

# The median

data.sort()
# if element % 2 == 0:
if len(data) % 2 == 0:
    # find middle two, add them together, divide by 2
    middleIndex1 = int(len(data) / 2)
    middleIndex2 = int((len(data) / 2 )-1)
    value1 = data[middleIndex1]
    value2 = data[middleIndex2]
    averageOfMiddle = (value1 + value2) / 2

    print("The median")
    print(averageOfMiddle)
else:
    # find the middle number
    middleIndex = math.floor(len(data) / 2)
    median = data[middleIndex]

    print("The median")
    print(median)