# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75
a=lambda x,y=15:x*y
print(a(4))
print(a(5))
print(a(2))