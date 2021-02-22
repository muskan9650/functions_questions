#Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss parameter ko hume check karana 
#hai ki vo perfect number hain ya nahi. Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 
#tak sabhi perfect numbers ko print kare.[ hum ek aise integer number ko perfect number kahenge jo ki uske sabhi
#factors ( including 1 & excluding itself) ka sum uss number ke barabar hota hai.Example:- Expected 

 def perfect_num(n):
    sum=0
    for i in range(1, n):
        if n%i==0:
            sum+=i
    return sum==n
print(perfect_num(7))
