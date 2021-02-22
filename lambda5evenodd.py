#5. Write a Python program to filter a list of integers using Lambda. Go to the editor
#Original list of integers:
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even=list(filter(lambda x:x%2==0, x))
print(even)
odd=list(filter(lambda x:x%2!=0, x))
print(odd)
