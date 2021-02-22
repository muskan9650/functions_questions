#check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" 
#agar dono numbers even (2 se divide hote hain) nahi toh print kare 
#"Dono numbers even nahi hai"
def check_numbers(x,y):
    if x%2==0 and y%2==0:
        print("both are even")
    else:
        print("both are not even")
check_numbers(8,10)

#Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments ki tarah le aur fir check kare
#  ki same index waale dono integers even hain ya nahi. Yeh check karne ke liye pichle Part 1 mein 
# likhe check_numbers function ka use karo. Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur [6, 19, 24, 12, 3, 87] 
# Toh usko yeh output deni chaiye:
def check_numbers(x,y):
    for i in range(len(x)):
        if x[i]%2==0 and y[i]%2==0:
            print(x[i], y[i], "both are even")
        else:
            print("both are not even")
check_numbers(x=[2, 6, 18, 10, 3, 75], y=[6, 19, 24, 12, 3, 87])
