def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1] = temp
    return arr

print(bubblesort([3,4,5,2,1]))