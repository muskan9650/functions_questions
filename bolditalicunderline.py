#17. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.
def make_bold(fn):
    def write():
        return "<b>" + fn + "</b>"
    return write
def make_underline(fn):
    def write():
        return "<u>" + fn + "</u>"
    return write
def make_italic():
    def write():
        return "<i>" + fn + "</i>"
    return write
def hello():
    return "hello world"
print(hello())