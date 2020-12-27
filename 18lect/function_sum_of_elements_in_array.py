def sum_arr(arr):
    sumb = 0
    for i in arr:
        i = int(i)
        sumb += i
    return sumb
x = list((input().split(","))
print(sum_arr(x))
