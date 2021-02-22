# # calculator
# def calculator(number1, number2, operation):
#     if operation=="add":
#         return number1+number2
#     elif operation=="sub":
#         return number1-number2
#     elif operation=="multi":
#         return number1 * number2
#     else:
#         return number1/number2
# number1=int(input("enter a number"))
# number2=int(input("enter a number"))
# print(calculator(number1, number2, "add"))
# print(calculator(number1,number2, "sub"))
# print(calculator(number1,number2, "multi"))
# print(calculator(number1,number2, "devide"))


#second type
def calculator(number1, number2):
    c=[]
    for i in range(len(number1)):
        z= number1[i]*number2[i]
        c.append(z)
    print(c)
calculator(number1=[5, 10, 50, 20], number2=[2, 20, 3, 5])




        

