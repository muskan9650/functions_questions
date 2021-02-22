#10 Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce
fibo = lambda a : reduce(lambda x,_: x+[x[-1]+x[-2]], range(a-2),[0,1])
print(fibo(2))
print(fibo(5))

