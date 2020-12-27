"""
printing the fibonacci series
"""

x  = int(input("enter the number :"))
temp = [0,1,1]
if(x == 1):
    print(str(0))
elif(x==2):
    print(str(1))
else:
    
    if(x==3):
        print(str(1))
    else:
        for i in range(3,x):
            temp.append(temp[i-2]+temp[i-1])
        print(temp)