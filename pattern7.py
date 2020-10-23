"""
printing the hallow diamond pattern 
author: @lokesh

"""
c =0
sp = 7
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(" ",end="")
    c = c+1
    j = j-(i-c)
    for y in range(0,2*j-1):
        print("*", end="")
    for y in range(1,i+1):
        print(" ",end="")
    print()
for v in range(1,5):
    for b in range(0,v+1):
        print(" ",end="")
    for s in range(0,sp):
        print("*",end="")
    sp=sp-2
    for b in range(0,v+1):
        print(" ",end="")
    print()
    
