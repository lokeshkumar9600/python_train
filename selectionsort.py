def selectionsort(arr):
    for i in range(0,len(arr)-1):
        minval = i
        for j in range(i,len(arr)):
            if arr[j] < arr[minval]:
                minval = j

        temp = arr[i]
        arr[i] = arr[minval]
        arr[minval] = temp
        print(arr)
    
    return arr

print(selectionsort([5,4,3,2,1]))