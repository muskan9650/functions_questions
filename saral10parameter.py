#Apko students naam ka ek function define karna hai or uss function mai list of students
#name as a parameter pass karna hai(List ka use nahi karna hai)
def students(*name):
    for i in name :
        print("student name", i)
students("reena", "sheeta", "deepa", "geeta")



#Apko isGreaterThen20 naam ka function define karna hai jismai apko function mai do parameter pass karane hai 
#or first parameter by default 20 hi hona chahiye.
def isgreaterthen20(x, y=20):
    z=x+y
    print(z)
isgreaterthen20( x=4)


