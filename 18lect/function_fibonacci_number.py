def func_fibo(pos):
    x = int(pos)
    arr = [0,1]
    if pos == 1 : 
        arr = [0]
        return arr
    elif pos == 2 : 
         arr = [0,1]
         return arr
    else:
        for i in range(2,x):
            temp = arr[i-2]+arr[i-1]
            arr.append(temp)
        return arr
            
x = input("enter the number of terms in fibonacci series : ")   
x = func_fibo(x)
for y in x :
    print(y,end=" ")
