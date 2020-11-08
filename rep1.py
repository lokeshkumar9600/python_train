from re import match
teststr  = "abc"
res  = match("[abc]" ,teststr)
if res :
    print("valid")
else:
    print("invalid")