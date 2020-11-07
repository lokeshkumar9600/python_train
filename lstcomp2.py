x = [[1,2,3], [4,5,6], [7,8,9]]
trans = [[row[i] for row in x] for i in range(0,len(x[0]))]
print(trans)