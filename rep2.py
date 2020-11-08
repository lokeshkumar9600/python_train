from re import match
teststr  = "aerds"
res  = match("....." ,teststr) #using a period "."  // or can use to specify range [1-4], [a-z]
if res :
    print("valid")
else:
    print("invalid")