#Write a Python program to execute a string containing Python code.
my_code='print("hello world")'
code="""
def multiply (x,y):
    return x*y
print(multiply(3,2))
"""
exec(my_code)
exec(code)