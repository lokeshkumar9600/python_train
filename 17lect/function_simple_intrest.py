def simple_int(P,N,R=10.5):
    ans = P*(1+(R/100)*N)
    return ans

print(simple_int(10000,10.5,5))
