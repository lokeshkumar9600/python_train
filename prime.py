
x = int(input())
y = int(input())
for i in range(2,y+1):
     z = i //2
     while z>1:
          if i % z == 0:
            print(i , "not an prime")
            break
          z = z - 1
     else:
        print(i ,"is a prime")
    
