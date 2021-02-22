def maximun_fun(n):
    max=n[0]
    for i in range(len(n)):
        if n[i]>max:
            max=n[i]
    return max
print(maximun_fun(n=[5, 10, 15, 8, 6])