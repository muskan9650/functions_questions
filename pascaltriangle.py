#13. Write a Python function that prints out the first n rows of Pascal's triangle.
def pascal_triangle(n):
   i = [1]
   y = [0]
   for x in range(max(n,0)):
      print(i)
      i=[l+r for l,r in zip(i+y, y+i)]
   return n>=1
pascal_triangle(7) 
