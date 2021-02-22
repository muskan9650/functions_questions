#Ek function banaiye jo 3 numbers ka sum aur average print kare.Hum user se 3 number input karwayenge aur fir unn 3
#numbers ka sum aur average print karwayenge jaisa ki niche output diya hua hain.
def numbers(number1, number2, number3):
    sum=number1+number2+number3
    average=sum/3
    return sum, average
number1=int(input("enter a number"))
number2=int(input("enter a number"))
number3=int(input("enter a number"))
print(numbers(number1, number2, number3))