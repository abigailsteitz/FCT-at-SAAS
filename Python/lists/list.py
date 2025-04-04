file = open('Python/lists/Data.csv', 'r')
data = file.read().splitlines()

# make evrey value a floating point number (decimal)
for i in range(len(data)):
   data[i] = float(data[i])
print(data)

smallestSOFar = data[0]
for element in data:
    if element < smallestSOFar:
        smallestSOFar = element

print("smallest " + str(smallestSOFar))

# find the largest number in the list
largestSoFar = data[0]      
for element in data:
    if element > largestSoFar:
        largestSoFar = element
print("largest " + str(largestSoFar))  

# find the average of the numbers in the list
sum = 0         
for element in data:
    sum += element
average = sum / len(data)       
print("average " + str(average))

#find sum of all numbers in the list
sum = 0
for element in data:
    sum += element 
print("sum " + str(sum))
#find median of the numbers in the list
median = 0
if len(data) % 2 == 0:
    median = (data[len(data)//2] + data[len(data)//2 - 1]) / 2
else:
    median = data[len(data)//2]     
print("median " + str(median))