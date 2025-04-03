file = open("python/lists/data.cvs", "r")
data = file.read().splitlines()

print(data)

for i in range(len(data)):
    data[i] = float(data[i])

print(data)

print(" ")

smallestsofar = data[0]
for element in data:
    if element < smallestsofar:
        smallestsofar = element

print("smallest so far = ", (smallestsofar))


sumofdata = data[0]
for element in data:
    sumofdata += element

print("total = ", sumofdata)


average = sumofdata / len(data)
print("average = ", (average))

bigsofar = data[0]
for element in data:
    if element > bigsofar:
        bigsofar = element
print("biggest so far = ", (bigsofar))

median = ((bigsofar) + (smallestsofar)) / 2
print("median = ", (median))

print(" ")
print(" ")
print(" ")
