s = input().lower()
arr = [i for i in s]
dct = {}
for u in range(0,len(arr)):
    counter  = 0 
    for num in arr:
        if arr[u] == num:
            counter += 1
            dct[arr[u]] = counter

print(sorted(dct.keys()))
