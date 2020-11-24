def rfunc(n):
    if n == 1 :
        return 1
    else:
        return n + rfunc(n-1)

print(rfunc(4))