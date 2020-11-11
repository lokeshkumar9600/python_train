x = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
y = [ x[i]  for i in range(0,len(x)) if sum(x[i])!= 3 ]
print(y)