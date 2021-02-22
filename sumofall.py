#2. Write a Python function to sum all the numbers in a list:
#Sample List : (8, 2, 3, 0, 7)
def sum(numbers):
    add=0
    for i in numbers:
        add=add+i
    return add

print(sum((8,2,3,0,7)))

