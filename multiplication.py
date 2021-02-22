#3. Write a Python function to multiply all the numbers in a list.
def product(numbers):
    multy=1
    for i in numbers:
        multy=multy*i
    return multy

print(product((8, 2, 3, -1, 7)))