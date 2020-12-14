def bsorting(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j] > x[j+1]:
                temp = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
    return x 

print(bsorting([4,5,2,6,3]))