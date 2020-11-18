def fun_fact(num):
    x = int(num)
    ans = 1
    for i in range(1,x+1):
        ans *= i
    
    return ans

print(fun_fact(3))

    
