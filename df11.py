x = [3]
dc = {1:"one" , 2: "two" , 3 : "three" , 4: "four"}
def removekeys(mydict, keylist):
    for i in keylist:
        if i in  mydict.keys():
            mydict.pop(i)
    return mydict

print(removekeys(dc,x))


