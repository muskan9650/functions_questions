#8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def unique_list1(n):
    c=[]
    for i in n:
        if i not in c:
            c.append(i)
    return c

print(unique_list1([1,2,3,3,3,3,4,5]))

