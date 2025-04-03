file = open("Python/lists/data.csv")
data = file.read().splitlines()

print(data)

for i in range(len(data)):
    data[i] = float(data[i])

print(data) 

# FIND THE SMALLEST NUMBER IN THE LIST

smallestsofar = data[0]
for element in data:
    if element < smallestsofar:
        smallestsofar = element
print("The smallest number is", element)


allnumsadded=0
for element in data:
    allnumsadded += element
print("The sum of the numbers is", allnumsadded)

average = sum(data) / len(data)  # Divide the total sum by the number of elements
print("The average of the numbers is", average) 
#also can use
# find the sum of the list of numbers 
#total_sum = sum(data)  # Use the sum() function to calculate the total
#print("The sum of the numbers is", total_sum)