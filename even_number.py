#10. Write a Python program to print the even numbers from a given list. 
def even_list(n):
    a=[]
    for i in n:
        if i%2==0:
            a.append(i)
    return a
print(even_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))