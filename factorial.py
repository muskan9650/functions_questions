#5. Write a Python function to calculate the factorial of a number (a non-negative integer). 
#The function accepts the number as an argument.
def factorial_num(n):
    product=1
    i=n
    while i>0:
        product=product*i
        i=i-1
    return product
print(factorial_num(4))
