file = open('python/lists/data.csv','r')
data = file.read().splitlines()

print(data)

for i in range(len(data)):
    data[i] = float(data[i])


print(data)

SmallestSoFar = data[0]
for element in data:
    print(element)
    if element < SmallestSoFar:
        SmallestSoFar = element


print("Smallest:")
print(SmallestSoFar)

SumSoFar = 0
for element in data:
        SumSoFar += element

print("Sum:")
print(SumSoFar)

LargestSoFar = data[0]

for element in data:
     print(element)
     if element > LargestSoFar:
        LargestSoFar = element

print("Largest:")
print(LargestSoFar)

Average = SumSoFar / len(data)
print("Average:")
print(Average)

median = 0
if len(data) % 2 == 0:
    median = (data[len(data)//2] + data[len(data)//2 - 1]) / 2

print("Median:")
print(median)