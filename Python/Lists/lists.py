file = open('Python/Lists/data.csv', 'r')
data = file.read().splitlines()

# make every value a floating point number (decimal)

for i in range(len(data)):
    data[i] = float(data[i]) 


print(data)



# find the smallest 

smallestsofar = data[4]
for element in data:
    if element < smallestsofar: 
        smallestsofar = element

print("Smallest: " + str(smallestsofar))








# find the sum

sumSofar = 0
for element in data:
    sumSofar += element


print("Sum: " + str(sumSofar))

# find the largest 

smallestsofar = data[4]
for element in data:
    if element > smallestsofar: 
        smallestsofar = element

print("Largest: " + str(smallestsofar))


# find the average
average = sumSofar / len(data)
print("Average: " + str(average))

