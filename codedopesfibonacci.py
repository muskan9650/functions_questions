#Write a function to find factorial of a number but also store the factorials calculated in a dictionary as done in
#the Fibonacci series example.
def fibonacci(n):
    i=0
    j=1
    z=1
    while i<=n:
        i=j
        j=z
        z= i+j
        print( i, j, z," ", end="")
        i=i+1
fibonacci(5)