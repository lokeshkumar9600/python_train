x = [[1,2,3],[4,5,6],[7,8,9]]
trans =[]
for row in range(0,len(x[0])):
    ans = []
    for i in x:
        ans.append(i[row])
    trans.append(ans)
        

print(trans)


