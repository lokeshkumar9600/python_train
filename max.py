arr = [x for x in range(0,100)]
minarr = 0
for i in range(0,len(arr)):  
    if arr[i]>minarr:
        minarr = arr[i]
    else:
        continue

print(minarr)