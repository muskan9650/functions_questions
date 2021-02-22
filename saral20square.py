#Ek function likho jo ki ek argument le jo number ho or dictionary return karega jisme keys 1 se lekar argument
# ke number tak hogi aur values unke squares honge.jaisa ki niche dikhaya gaya hai.
def output():
    i=1
    dict1={}
    for i in range(1,31):
        j=i**2
        dict1[i]=j
    print(dict1)
output()