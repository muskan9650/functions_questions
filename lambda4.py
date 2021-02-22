#4. Write a Python program to sort a list of dictionaries using Lambda.
#Original list of dictionaries :
x=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
y=sorted(x,key=lambda a:a['color'])
print(y)
 
