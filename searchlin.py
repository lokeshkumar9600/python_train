def linsearch(arr,item):
    for i in range(0,len(arr)):
        if arr[i] == item:
            ans = True
            return ans
        else:
            ans = False
    
    return ans


print(linsearch([2,3,5,7,8],21))