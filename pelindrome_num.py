#12 Write a Python function that checks whether a passed string is palindrome or not.
def pelindrome_num(n):
    i=0
    j=len(n)-1
    while i<=j:
        if n[i]!=n[j]:
            return "no it is not pelindrome number"
        i=i+1
        j=j-1
        return "yes it is pelindrome number"
print(pelindrome_num("sagun"))
