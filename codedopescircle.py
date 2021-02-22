#Write a function to calculate area and circumference of a circle.
def circle(r):
    area = 3.14*(r**2) 
    circumference = 2 * 3.14 * r
    return area, circumference
print(circle(4))

