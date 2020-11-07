x = [[1,2,3],[4,5,6],[7,8,9]]
arr = []
for i in range(0,len(x[0])):
    temp =[]
    for y in x:
        temp.append(y[i])
    arr.append(temp)

print(arr)
