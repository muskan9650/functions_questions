#16.Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
def output():
    i=1
    list1=[]
    for i in range(1,31):
        j=i**2
        list1.append(j)
    print(list1)
output()