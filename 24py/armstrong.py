def isarmstrong(num):
    num = str(num)
    sumar =  0 
    for i in num :
        i = int(i)
        sumar += int(i**3)
    if sumar == int(num):
        return True
    else:
        return False

print(isarmstrong(370))