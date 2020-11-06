mat1 = input().split(",")
mat2 = input().split(",")
res = [0,0,0,0,0,0,0,0,0]
for i in range(0,len(mat1)):
    res[i] = str(int(mat1[i])+int(mat2[i]))

print(",".join(res))

