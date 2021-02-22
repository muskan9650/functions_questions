#1. Write a Python function to find the Max of three number
def max_of_two(x,y):
    if x>y:
        return x
    return y
def max_of_three(x,y,z):
    return(max_of_two(x,(max_of_two(y,z))))
print(max_of_three(4,5,6))