#add_numbers naam ka function likhiye jo do numbers ko arguments ke tarah le aur fir unka sum print karta hai.
#Arguments ka naam number1 aur number2 hona chaiye.
def argument(x,y):
    z=x+y
    print(z)
argument(30,40)


#add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho aur fir same position wale integers ka sum print karta ho.
# Same position waale 2 integers ka sum karne ke liye Part 1 mein di gayi add_numbers waale function ka use karo. 
# Jaise agar hum iss function ko [50, 60, 10] aur [10, 20, 13] denge ko woh yeh print karega
def add_number(x,y):
    z=0
    for i in range(len(x)):
        z = x[i]+ y[i]
        print(z)
add_number(x=[2, 3, 4], y=[6, 7, 8])
        