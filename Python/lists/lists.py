file = open('Python/lists/data.csv', 'r')
data = file.read().splitlines()

for i in range(len(data)):
    data[i] = float(data[i])

print(data)

smallestsofar = data[0]
for element in data:
    print(element)
    if element < smallestsofar:
        smallestsofar = element

print("Smallest so far is", smallestsofar)

largestsofar = data[0]
for element in data:
    print(element)
    if element > largestsofar:
        largestsofar = element
print("Largest so far is", largestsofar)

sum = 0
for element in data:
    sum += element
print("Sum is", sum)

sum = 0
for element in data:
    sum += element
average = sum / len(data)
print("Average is", average)

def find_median(data):
    data.sort()
    n = len(data)
    if n % 2 == 0:
        median = (data[n//2 - 1] + data[n//2]) / 2
    else:
        median = data[n//2]
    return median
median = find_median(data)
print("Median is", median)