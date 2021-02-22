#9. Write a Python function that takes a number as a parameter and check the number is prime or not. 
def prime_num(n):
    if n==1 or n==2:
        return "prime"
    else:
        for i in range(2,n):
            if n%i!=0:
                return "prime" 
            else:
                return "not prime"
print(prime_num(2))
    
