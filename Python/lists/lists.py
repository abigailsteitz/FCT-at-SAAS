file = open("Python/lists/data.csv")
data = file.read().splitlines()

print(data)

#make every value a floating point number(decimal)
for i in range(len(data)):
    data[i] = float(data[i])

print(data)

#find the smallest
smallestsofar = data[0]
for element in data:
    if element < smallestsofar:
        smallestsofar = element

print(smallestsofar)
#find the sum
allnumsadded=0
for element in data:
    allnumsadded += element
print("the sum is:")
print(allnumsadded)

# find the medium 
data.sort()
if len(data) % 2 == 0:
    medium = (data[len(data)//2] + data[len(data)//2 - 1]) / 2
else:
    medium = data[len(data)//2]
print("the medium is:")
print(medium)   
# find the average
average = allnumsadded / len(data)
print("the average is:")
print(average)
