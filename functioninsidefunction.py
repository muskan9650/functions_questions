#19. Write a Python program to access a function inside a function.
def disp():
    def show():
        print("show function")
    print("disp function")
    show()
disp()

def add (x,y):
    def sub(x,y):
        print(x-y)
    print(x+y)
    sub(5,3)
add(5,3)