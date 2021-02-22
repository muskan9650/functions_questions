#Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski length jyaada hogi use print karega aur
#agar dono strings ki length equal hui to dono ko line by line print karega 
def strings(str1, str2):
    if len(str1)>len(str2):
        print("hello world")
    elif len(str1)<len(str2):
        print("how are you")
    else:
        print("hello world")
        print("how are you")
str1=input("enter 1st string")
str2=input("enter 2nd string")
strings(str1, str2)