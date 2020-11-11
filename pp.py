#oneliner using list comprehension
x = [[1,2,3],[4,5,6],[7,8,9]]
print( [ [row[i] for row in x] for i in range(0,len(x[0]))])



#regular using multiple loops
ans =[]
for i in range(0,len(x[0])):
    temp =[]
    for row in x :
        temp.append(row[i])
    ans.append(temp)
print(ans)

row = int(input())
for i in range(0,row+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

