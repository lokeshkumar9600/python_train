a = int(input())
b = int(input())
c = int(input())
n = int(input())
arr = [a,b,c]
d1 = arr[1]-arr[0]
d2 = arr[2]-arr[1]
for x in range(4,n+1):
    if x%2 == 0 :
        arr.append(arr[-1]+d1)
    else:
        arr.append(arr[-1]+d2)

print(arr[-1])

    
